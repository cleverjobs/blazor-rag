# treeview item hot area

## Question

**Ran** asked on 29 Nov 2019

Hi, Right now, when I click on a highlighted treeview item it only fires the onClick if I click directly on the text. How can I add some css to make the highlighted area clickable. By highlighted I mean: div.k-treeview span.k-in:hover { background-color: pink; color: black; }

## Answer

**Marin Bratanov** answered on 29 Nov 2019

Hi Randy, At the moment, the treeview does not have a built-in click handler and you need to implement one yourself in a template: [https://feedback.telerik.com/blazor/1418731-node-click-event.](https://feedback.telerik.com/blazor/1418731-node-click-event.) Thus, you need to ensure that it is attached to the proper element and that child elements don't stop its propagation. As usual with templates and customizations, you may have to tweak the CSS a little to match your preferences. Here's an example I made for you: <style>
div.k-treeview span.k- in:hover {
background-color: pink;
color: black;
} /* to make the entire colored area "clickable", move the padding from the Telerik theme to your own element */ div.k-treeview span.k- in {
padding: 0;
}

.MyNode {
padding: 6 px 8 px;
}

</style>

<TelerikTreeView Data="@FlatData">
<TreeViewBindings>
<TreeViewBinding ParentIdField="ParentIdValue">
<ItemTemplate>
<div class="MyNode" @onclick="@MyClick">@( (context as TreeItem).Text )</div>
</ItemTemplate>
</TreeViewBinding>
</TreeViewBindings>
</TelerikTreeView>

@result

@code {
MarkupString result { get; set; } void MyClick ( ) {
result=new MarkupString(result.ToString() + "<br />" + DateTime.Now.Millisecond);
} public class TreeItem { public int Id { get; set; } public string Text { get; set; } public int? ParentIdValue { get; set; } public bool HasChildren { get; set; } public string Icon { get; set; } public bool Expanded { get; set; }
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
} Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 29 Nov 2019

Love it! All I was missing was: /* to make the entire colored area "clickable", move the padding from the Telerik theme to your own element */ div.k-treeview span.k- in { padding: 0; } Once again, thanks!

### Response

**Randy Hompesch** answered on 29 Nov 2019

Love it! All I was missing was: /* to make the entire colored area "clickable", move the padding from the Telerik theme to your own element */ div.k-treeview span.k-in { padding: 0; } Once again ... Thanks!
