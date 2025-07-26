# TreeView margin.left problem

## Question

**wuwu** asked on 01 Jun 2020

I test the TreeView control,using the style: .sidebar { position: fixed; top: 40px; left: 0; bottom: 0; width: 240px; overflow-y: auto; border-right: 1px solid #e4e6e9; background-color:mediumaquamarine; padding:0px 0px 0px 0px; } in MainLayout.razor: <body> <div class="header"> <a href="[http://blazor.net">About</a>](http://blazor.net">About</a>) </div> <div class="sidebar"> <NavMenu/> </div> <div class="content"> @Body </div> </body> and in NavMenu.razor: @inject NavigateTreesService NavigateTrees <TelerikTreeView Data="@NavigateTrees.TreeData"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentIdValue" IconField="Icon" UrlField="Page"> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> Then run,look this picture attachment,There's always a spare part on the left. and I found the treeview control's properties is too few,i can't set the sytle.

## Answer

**Svetoslav Dimitrov** answered on 01 Jun 2020

Hello Wu, For sidebar navigation menu you could use the Drawer component ( [https://docs.telerik.com/blazor-ui/components/drawer/overview](https://docs.telerik.com/blazor-ui/components/drawer/overview) ) as it is more fit for the purpose. You can explore it live from our demos page here: [https://demos.telerik.com/blazor-ui/drawer/overview.](https://demos.telerik.com/blazor-ui/drawer/overview.) I noticed you would like to create a menu with Hierarchical data, if so, our Hierarchical Drawer demo would be useful: [https://demos.telerik.com/blazor-ui/drawer/hierarchical-drawer.](https://demos.telerik.com/blazor-ui/drawer/hierarchical-drawer.) It utilizes the Template of the component and you can read more on that in our documentation: [https://docs.telerik.com/blazor-ui/components/drawer/templates#template.](https://docs.telerik.com/blazor-ui/components/drawer/templates#template.) Also, you can find the Navigation article for the Drawer useful: [https://docs.telerik.com/blazor-ui/components/drawer/navigation,](https://docs.telerik.com/blazor-ui/components/drawer/navigation,) where we have explained how to use the Drawer in the MainLayout. As of the TreeView, you can wrap the component in a div with a class (for example mySidebarNavigation) and target the k-treeview-lines ul and set the padding to 0px - the 40px padding comes from the browser (screenshot attached). Below, you can see a code sample. <style>.mySidebarNavigation.k-treeview-lines { padding: 0px;
} </style> <div class="mySidebarNavigation"> <TelerikTreeView Data="@FlatData"> <TreeViewBindings> <TreeViewBinding ParentIdField="ParentIdValue"> </TreeViewBinding> </TreeViewBindings> </TelerikTreeView> </div> @code {
public class TreeItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentIdValue { get; set; }
public bool HasChildren { get; set; }
public string Icon { get; set; }
public bool Expanded { get; set; }
}

public IEnumerable <TreeItem> FlatData { get; set; }

protected override void OnInitialized()
{
LoadFlatData();
}

private void LoadFlatData()
{
List <TreeItem> items=new List <TreeItem> ();
items.Add(new TreeItem()
{
Id=1,
Text="Project",
ParentIdValue=null,
HasChildren=true,
Icon="folder",
Expanded=true
});
items.Add(new TreeItem()
{
Id=2,
Text="Design",
ParentIdValue=1,
HasChildren=true,
Icon="brush",
Expanded=true
});
items.Add(new TreeItem()
{
Id=3,
Text="Implementation",
ParentIdValue=1,
HasChildren=true,
Icon="folder",
Expanded=true
});

items.Add(new TreeItem()
{
Id=4,
Text="site.psd",
ParentIdValue=2,
HasChildren=false,
Icon="psd",
Expanded=true
});

items.Add(new TreeItem()
{
Id=5,
Text="index.js",
ParentIdValue=3,
HasChildren=false,
Icon="js"
});
items.Add(new TreeItem()
{
Id=6,
Text="index.html",
ParentIdValue=3,
HasChildren=false,
Icon="html"
});

items.Add(new TreeItem()
{
Id=7,
Text="styles.css",
ParentIdValue=3,
HasChildren=false,
Icon="css"
});

FlatData=items;
}
} Regards, Svetoslav Dimitrov

### Response

**wu** answered on 01 Jun 2020

thank your answer! I used the above code in the NavMenu.razor,But it didn't work. I want to realize independent scrolling on the left menu and right content,but your drawer is in a layout,I think the menu and the content area share a scroll bar.

### Response

**wu** answered on 01 Jun 2020

Ok,It is work. Can you provide examples of custom styles,for example modify the alternate line background color for the grid control. Or provide examples of style modifications in demo in future!

### Response

**wu** answered on 01 Jun 2020

There's another problem there. look the attachment,When I adjust the browser window,two scroll bars appear. But the lower part of the scroll bar on the left is cropped,the right scroll bar is good.

### Response

**Marin Bratanov** answered on 02 Jun 2020

Hi Wu, The following KB article shows how you can implement custom and conditional styling on the grid rows: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background) You may also find this blog post useful on reviewing what is rendered so you can devise your own rules that provide the styling you need: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) This can also help you investigate the issues with your project layout CSS rules. Regards, Marin Bratanov
