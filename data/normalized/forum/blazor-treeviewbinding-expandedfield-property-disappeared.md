# Blazor TreeViewBinding ExpandedField property disappeared

## Question

**EdEd** asked on 26 Jan 2022

What happened to it? Don't know if it affected the code below. In either case the code is not working. Seems like it should I am trying to write code to expand/collapse nodes when they are clicked on regardless if I click on the expand arrow or text. Getting nowhere. private void OnTvItemClick(object e, TreeItem tvItem)
{
if(tvItem.HasChildren)
{
tvItem.Expanded=!tvItem.Expanded;
}
} Can you help? Thanks ... Ed

## Answer

**Apostolos** answered on 28 Jan 2022

Hello Ed, We already discussed this case in a separate thread, so I will just repeat the solution here for community visibility.===There are breaking changes in our 3.0 release related to the TreeView. To programmatically expand/collapse TreeView items, add or remove item objects in the ExpandedItems property: @using System.Collections.ObjectModel <TelerikTreeView Data="@AuthTreeData" @ref="@tv" @bind-ExpandedItems="@ExpandedItems" SelectionMode="@TreeViewSelectionMode.Single" SelectedItems="@SelectedItems"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentIdValue"> <ItemTemplate Context="ct"> @{
var tvItem=ct as TreeItem; <label class="p-2" @key=@tvItem.Id @onclick=@((e)=> OnTvItemClick(e, tvItem))>
@tvItem.Text </label> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code {

public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentIdValue { get; set; }
public TreeItem Parent { get; set; }
public bool HasChildren { get; set; }
public string Icon { get; set; }
public bool Expanded { get; set; }
public string Page { get; set; }
}

public TelerikTreeView tv { get; set; }

public IEnumerable <object> SelectedItems { get; set; }=new List <object> ();
public IEnumerable <object> ExpandedItems { get; set; }=new List <TreeItem> ();
public ObservableCollection <TreeItem> AuthTreeData { get; set; }=new
ObservableCollection <TreeItem> {

new TreeItem()
{
Id=1,
Text="Project",
ParentIdValue=null,
HasChildren=true,
Icon="folder",
},
new TreeItem()
{
Id=2,
Text="Design",
ParentIdValue=1,
HasChildren=true,
Icon="brush",
},
new TreeItem()
{
Id=3,
Text="Implementation",
ParentIdValue=1,
HasChildren=true,
Icon="folder",
},
new TreeItem()
{
Id=4,
Text="site.psd",
ParentIdValue=2,
HasChildren=false,
Icon="psd",
},
new TreeItem()
{
Id=5,
Text="index.js",
ParentIdValue=3,
HasChildren=false,
Icon="js"
},
new TreeItem()
{
Id=6,
Text="index.html",
ParentIdValue=3,
HasChildren=false,
Icon="html"
},
};

private void OnTvItemClick(object e, TreeItem tvItem)
{ if (ExpandedItems.FirstOrDefault(x=> (x as TreeItem).Id==tvItem.Id)==null)
{
ExpandedItems=ExpandedItems.Append(tvItem);
}
else
{
ExpandedItems=ExpandedItems.Where(x=> (x as TreeItem).Id !=tvItem.Id).ToList();
} }
} Regards, Apostolos
