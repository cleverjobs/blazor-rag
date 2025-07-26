# How can I decrease the whitespace between nodes?

## Question

**Dav** asked on 15 Jun 2021

I have a treeview. And there is too much white space between the nodes. How can I control this? I have included a screenshot so you see what I mean.

## Answer

**Marin Bratanov** answered on 15 Jun 2021

Hello David, You can use CSS to target the treeview nodes and decrease the default paddings they have in our stylesheet (or rules coming from site-specific stylesheets, because the screenshot feels a bit too large for our built-in designs). You can see where those rules come from by inspecting the rendered HTML and its CSS rules (see here for an example). Here's also one code snippet I made for you with that approach that showcases the concept: <style>.small-spacing.k-treeview.k-in { padding: 0; /*note that in your case the CSS rule may be different and may have to target a different element*/ }
</style> <TelerikTreeView Data=" @FlatData " Class="small-spacing">
<TreeViewBindings>
<TreeViewBinding IdField="Id" ParentIdField="ParentIdValue" ExpandedField="Expanded" TextField="Text" HasChildrenField="HasChildren" IconField="Icon" />
</TreeViewBindings>
</TelerikTreeView>

@code { public class TreeItem {
public int Id { get; set; } public string Text { get; set; } public int? ParentIdValue { get; set; } public bool HasChildren { get; set; } public string Icon { get; set; } public bool Expanded { get; set; }
} public IEnumerable <TreeItem> FlatData { get; set; } protected override void OnInitialized ()
{
LoadFlatData();
} private void LoadFlatData ()
{
List<TreeItem> items=new List<TreeItem>();

items.Add(new TreeItem()
{
Id=1,
Text="Project",
ParentIdValue=null,
HasChildren=true,
Icon="folder",
Expanded=true
}); items.Add ( new TreeItem ()
{
Id=2,
Text="Design",
ParentIdValue=1,
HasChildren=true,
Icon="brush",
Expanded=true
}); items.Add ( new TreeItem ()
{
Id=3,
Text="Implementation",
ParentIdValue=1,
HasChildren=true,
Icon="folder",
Expanded=true
}); items.Add ( new TreeItem ()
{
Id=4,
Text="site.psd",
ParentIdValue=2,
HasChildren=false,
Icon="psd",
Expanded=true
}); items.Add ( new TreeItem ()
{
Id=5,
Text="index.js",
ParentIdValue=3,
HasChildren=false,
Icon="js"
}); items.Add ( new TreeItem ()
{
Id=6,
Text="index.html",
ParentIdValue=3,
HasChildren=false,
Icon="html"
}); items.Add ( new TreeItem ()
{
Id=7,
Text="styles.css",
ParentIdValue=3,
HasChildren=false,
Icon="css"
}); FlatData=items;
}
} Regards, Marin Bratanov
