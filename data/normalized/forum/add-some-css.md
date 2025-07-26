# add some css?

## Question

**Ran** asked on 14 Oct 2019

Hi, How do I add css to Telerik blazor widget markup? Specifically, I am interested in changing the back and fore color of the treeview. Thanks ... Ed

## Answer

**Marin Bratanov** answered on 14 Oct 2019

Hi Ed, The general approach is to examine the rendered HTML and add CSS rules that target the elements you want to alter, and override our default values with the results you desire. The following blog post could help you in this regard: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) You may also want to Follow and Vote on this feature that would make this easier for the suite in general: [https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.) That said, here's an example I made to help you get started: <style> div.k-widget.k-treeview { background-color: red;

}.k-item.k-treeview-item { color: yellow; background-color: blue;
} span.k-in { background-color: green;
} div.k-treeview span.k-in:hover { background-color: cyan; color: purple;
}
</style>

<TelerikTreeView Data="@FlatData ">
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
