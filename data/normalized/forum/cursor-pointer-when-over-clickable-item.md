# Cursor pointer when over clickable item

## Question

**Dea** asked on 25 Jan 2021

Is there a way to get the cursor to look like a pointer when over an item, short of using the template?

## Answer

**Nadezhda Tacheva** answered on 26 Jan 2021

Hello Dean, The TreeeView items are wrapped in divs with classes .k-item and .k-treeview-item. You can use that to add some CSS styling and set the cursor to pointer. As of release 2.21.0 the TreeView has a Class parameter which will allow you to add custom CSS class to it and style only the desired instance, not all instances of TreeView on the page/app. To better illustrate how to achieve the desired behavior I've created the following example of a TreeView with a pointer cursor (no functionality included, only styling to demonstrate how to show pointer). <style>
.my-treeview .k-item.k-treeview-item {
cursor: pointer;
}
</style> <TelerikTreeView Class="my-treeview" Data="@FlatData">
<TreeViewBindings>
<TreeViewBinding IdField="Id" ParentIdField="ParentIdValue" ExpandedField="Expanded" TextField="Text" HasChildrenField="HasChildren" IconField="Icon" />
</TreeViewBindings>
</TelerikTreeView>

@code { public class TreeItem { public int Id { get; set; } public string Text { get; set; } public int? ParentIdValue { get; set; } public bool HasChildren { get; set; } public string Icon { get; set; } public bool Expanded { get; set; }
} public IEnumerable<TreeItem> FlatData { get; set; } protected override void OnInitialized ( ) {
LoadFlatData();
} private void LoadFlatData ( ) {
List<TreeItem> items=new List<TreeItem>();

items.Add( new TreeItem()
{
Id=1,
Text="Project",
ParentIdValue=null,
HasChildren=true,
Icon="folder",
Expanded=true });

items.Add( new TreeItem()
{
Id=2,
Text="Design",
ParentIdValue=1,
HasChildren=true,
Icon="brush",
Expanded=true });
items.Add( new TreeItem()
{
Id=3,
Text="Implementation",
ParentIdValue=1,
HasChildren=true,
Icon="folder",
Expanded=true });

items.Add( new TreeItem()
{
Id=4,
Text="site.psd",
ParentIdValue=2,
HasChildren=false,
Icon="psd",
Expanded=true });
items.Add( new TreeItem()
{
Id=5,
Text="index.js",
ParentIdValue=3,
HasChildren=false,
Icon="js" });

FlatData=items;
}
} Regards, Nadezhda

### Response

**Dean** answered on 02 Feb 2021

Thank you for this, works great
