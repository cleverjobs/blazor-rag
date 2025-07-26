# How to Change the treenode Text, font size and color at runtime in Blazor?

## Question

**** asked on 05 Aug 2022

Hi, How to change the treenode Text, font size and color at runtime in Blazor? I am trying following code. I changed text in both data structures i.e. FlatData and ExpandedItems. Text is being changed in data structure but change is not reflecting on UI. <TelerikTreeView OnItemClick="@OnItemClickHandler" Data="@FlatData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentIdValue"> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code{

public ObservableCollection <TreeItem> FlatData { get; set; }
public IEnumerable <object> ExpandedItems { get; set; }

protected override async Task OnInitializedAsync()
{
LoadFlatData();
timer=new System.Threading.Timer(async _=> // async void
{
FlatData[0].Text="Net";

ExpandedItems=FlatData;

// we need StateHasChanged() because this is an async void handler
// we need to Invoke it because we could be on the wrong Thread
await InvokeAsync(StateHasChanged);
}, null, 0, 5000);
}
}

## Answer

**Hristian Stefanov** answered on 09 Aug 2022

Hi Developer, I confirm the desired result is achievable by using the TreeView ItemTemplate. Here is an example I have prepared to demonstrate: <TelerikTreeView Data="@FlatData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding> <ItemTemplate> @{
TreeItem itm=context as TreeItem; <strong style="color: @itm.Color; font-size: @itm.FontSize"> @itm.Text </strong> } </ItemTemplate> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> @code {
IEnumerable <TreeItem> FlatData { get; set; }
IEnumerable <object> ExpandedItems { get; set; }=new List <TreeItem> ();

protected override void OnInitialized()
{
FlatData=GetFlatData(); FlatData.ToList()[0].Text="TEST";
FlatData.ToList()[0].FontSize="15px";
FlatData.ToList()[0].Color="red"; ExpandedItems=FlatData.Where(x=> x.HasChildren==true).ToList();
}

List <TreeItem> GetFlatData()
{
List <TreeItem> items=new List <TreeItem> ();

items.Add(new TreeItem()
{
Id=1,
Text="wwwroot",
ParentId=null,
HasChildren=true,
Icon="folder",
});
items.Add(new TreeItem()
{
Id=2,
Text="css",
ParentId=1,
HasChildren=true,
});
items.Add(new TreeItem()
{
Id=3,
Text="js",
ParentId=1,
HasChildren=true,
Icon="folder",
});
items.Add(new TreeItem()
{
Id=4,
Text="site.css",
ParentId=2,
Icon="css"
});
items.Add(new TreeItem()
{
Id=5,
Text="scripts.js",
ParentId=3,
Icon="js"
});

return items;
}

public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentId { get; set; }
public bool HasChildren { get; set; }
public string Icon { get; set; }
public string FontSize { get; set; }
public string Color { get; set; }
}
} You can extend the above approach on your own in the actual project to cover the scenario needs. Regards, Hristian Stefanov
