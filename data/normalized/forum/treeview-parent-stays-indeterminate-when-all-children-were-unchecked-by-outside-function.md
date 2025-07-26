# TreeView parent stays indeterminate when all children were unchecked by outside function

## Question

**Jac** asked on 15 Nov 2022

Here is the sample that shows what is the issue. Just check any child and click "clear" button. The "full checks" are removed correctly, but indeterminate ones stays. @* Enable the CheckParents parameter and observe the behavior of this setting. *@<TelerikTreeView Data="@FlatData" @bind-ExpandedItems="@ExpandedItems" CheckParents="true" CheckBoxMode="@TreeViewCheckBoxMode.Multiple" @bind-CheckedItems="@checkedItems">
<TreeViewBindings>
<TreeViewBinding IdField="Id" ParentIdField="ParentIdValue" TextField="Text" HasChildrenField="HasChildren" IconField="Icon" />
</TreeViewBindings>
</TelerikTreeView>

<div>
Checked items:
<ul>
@if (checkedItems.Any())
{ foreach ( var item in checkedItems)
{ var checkedItem=item as TreeItem;
<li>
<span>
<TelerikIcon Icon="@checkedItem.Icon"></TelerikIcon>
</span>
<span>
@(checkedItem.Text)
</span>
</li>
}
}
</ul>
<button @onclick="Clear">clear</button>
</div>

@code { public IEnumerable <object> checkedItems { get; set; }=new List<object>(); public class TreeItem { public int Id { get; set; } public string Text { get; set; } public int? ParentIdValue { get; set; } public bool HasChildren { get; set; } public string Icon { get; set; }
} public IEnumerable<TreeItem> FlatData { get; set; } public IEnumerable <object> ExpandedItems { get; set; }=new List<TreeItem>(); protected override void OnInitialized ( ) {
LoadFlatData();
ExpandedItems=FlatData.Where(x=> x.HasChildren==true ).ToList();
} private void Clear ( ) {
checkedItems=new List<object>();
StateHasChanged();
} private void LoadFlatData ( ) {
List<TreeItem> items=new List<TreeItem>();

items.Add( new TreeItem()
{
Id=1,
Text="Project",
ParentIdValue=null,
HasChildren=true,
Icon="folder" });

items.Add( new TreeItem()
{
Id=2,
Text="Design",
ParentIdValue=1,
HasChildren=true,
Icon="brush" });
items.Add( new TreeItem()
{
Id=3,
Text="Implementation",
ParentIdValue=1,
HasChildren=true,
Icon="folder" });

items.Add( new TreeItem()
{
Id=4,
Text="site.psd",
ParentIdValue=2,
HasChildren=false,
Icon="psd" });
items.Add( new TreeItem()
{
Id=5,
Text="index.js",
ParentIdValue=3,
HasChildren=false,
Icon="js" });
items.Add( new TreeItem()
{
Id=6,
Text="index.html",
ParentIdValue=3,
HasChildren=false,
Icon="html" });
items.Add( new TreeItem()
{
Id=7,
Text="styles.css",
ParentIdValue=3,
HasChildren=false,
Icon="css" });

FlatData=items;
}
} Am I doing something wrong?

## Answer

**Dimo** answered on 18 Nov 2022

Hi Jacek, Indeed, this is a known issue with the TreeView checkboxes. The linked page contains a workaround - I hope it works for you. I also voted on your behalf to bump the item's priority. Regards, Dimo Progress Telerik
