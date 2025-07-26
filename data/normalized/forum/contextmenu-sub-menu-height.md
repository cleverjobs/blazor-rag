# ContextMenu sub menu height

## Question

**Rob** asked on 25 Apr 2023

Hi, I've got a pretty simple Context menu: <TelerikContextMenu @ref="@TheContextMenu" Data="@MenuItems" OnClick="@( (ContextMenuItem itm)=> ClickHandler(itm) )" DisabledField="Disabled" /> It contains one item that is a submenu of project names: var mnuProjects=Projects.Select(x=> new ContextMenuItem() { Text=x.Name, CommandName="Project", Id=x.ID }).ToList();

MenuItems=new List<ContextMenuItem>()
{
... other items new ContextMenuItem
{
Text="Projects",
HasChildren=true,
Items=mnuProjects
},

... other items
}; The number of projects has now grown too long to display without going off the bottom of the page. Is there a quick way to set the height of the list that appears?

## Answer

**Dimo** answered on 28 Apr 2023

Hello Robert, You can limit the height of child menu groups, according to the example below. This will work reliably, but only if the ContextMenu target is at the top of the browser viewport, which may not always be the case. So until we implement screen boundary detection and sub-menu opening direction, a more robust solution will be to switch from a ContextMenu to some other UI for project selection - for example, a Window or a DropDownList. Using long scrollable context menus is not very user friendly anyway, because finding items may not be easy (there is no searching / filtering, etc.) <div class="context-menu-target" style="width:200px; height: 100px; background: #fc9;">
Show Context Menu.
</div> <TelerikContextMenu Data="@MenuItems" Selector=".context-menu-target"> </TelerikContextMenu> <style>.k-animation-container.k-context-menu,.k-animation-container.k-menu-popup { max-height: 30vh; /* 90vh / number of menu levels */ overflow: auto;
}.k-animation-container.k-context-menu.k-menu-link-text,.k-animation-container.k-menu-popup.k-menu-link-text { padding-right: 20px;
} </style> @code { public List<MenuItem> MenuItems { get; set; } public class MenuItem { public int Id { get; set; } public int? ParentId { get; set; } public string Text { get; set; }=string.Empty;
} protected override void OnInitialized ( ) {
MenuItems=new List<MenuItem>(); for (int i=1; i <=30; i++)
{
MenuItems.Add( new MenuItem ( ) { Id=i, ParentId=null, Text=$ "Level 1 Item {i}" });
} for (int j=101; j <=130; j++)
{
MenuItems.Add( new MenuItem ( ) { Id=j, ParentId=1, Text=$ "Level 2 Item {j}" });
MenuItems.Add( new MenuItem ( ) { Id=j * 2, ParentId=30, Text=$ "Level 2 Item {j * 2}" });
} for (int k=1001; k <=1030; k++)
{
MenuItems.Add( new MenuItem ( ) { Id=k, ParentId=101, Text=$ "Level 3 Item {k}" });
MenuItems.Add( new MenuItem ( ) { Id=k * 2, ParentId=130, Text=$ "Level 3 Item {k * 2}" });
MenuItems.Add( new MenuItem ( ) { Id=k * 3, ParentId=101 * 2, Text=$ "Level 3 Item {k * 3}" });
MenuItems.Add( new MenuItem ( ) { Id=k * 4, ParentId=130 * 2, Text=$ "Level 3 Item {k * 4}" });
}

base.OnInitialized();
}
} Regards, Dimo Progress Telerik
