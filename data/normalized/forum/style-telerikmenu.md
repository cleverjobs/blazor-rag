# Style TelerikMenu

## Question

**Hen** asked on 28 Aug 2024

I am still struggeling with CSS. I want to set the Backgroundcolor and the Link/Text-Color of a specific Menu-Component. I know who to style the Menu generally for the whole Application but I need it just for one Page. The Menu-Component has no explicit Style Attribut to set in inline just for the specific object. This is the way I style the Link-Color but it sets the color for all my Menus... .k-menu-link { color: red; } Any help ?

## Answer

**Hristian Stefanov** answered on 29 Aug 2024

Hi Hendrik, To customize the background color and text color of a specific Menu component instance, you can use the OnItemRender event to assign a unique CSS class to each item. This approach ensures that only the targeted menu is styled, while other menus on the page remain unaffected by these custom styles. Here's an example I've prepared for you: <TelerikMenu Data="@MenuItems" ParentIdField="@nameof(MenuItem.SectionId)" IdField="@nameof(MenuItem.Id)" TextField="@nameof(MenuItem.Section)" OnItemRender="@OnMenuItemRender"> </TelerikMenu> <style>.custom-item,.popup-item { background-color: #bbb; color: green!important;
} </style> <TelerikMenu Data="@MenuItems" ParentIdField="@nameof(MenuItem.SectionId)" IdField="@nameof(MenuItem.Id)" TextField="@nameof(MenuItem.Section)"> </TelerikMenu> @code {
private List <MenuItem> MenuItems { get; set; } private void OnMenuItemRender(MenuItemRenderEventArgs args)
{
var item=args.Item as MenuItem;

if (item.SectionId==null)
{
args.Class="custom-item";
}
else
{
args.Class="popup-item";
}
} protected override void OnInitialized()
{
MenuItems=new List <MenuItem> ()
{
new MenuItem()
{
Id=1,
Section="Overview"
},
new MenuItem()
{
Id=2,
Section="Demos"
},
new MenuItem()
{
Id=3,
Section="Roadmap"
},
new MenuItem()
{
Id=4,
SectionId=3,
Section="What's new"
},
new MenuItem()
{
Id=5,
SectionId=3,
Section="Roadmap"
},
new MenuItem()
{
Id=6,
SectionId=3,
Section="Release History"
},
new MenuItem()
{
Id=7,
SectionId=2,
Section="Grid"
},
new MenuItem()
{
Id=8,
SectionId=2,
Section="Charts"
}
};

base.OnInitialized();
}

public class MenuItem
{
public int Id { get; set; }
public int? SectionId { get; set; }
public string Section { get; set; }
}
} Regards, Hristian Stefanov

### Response

**Hendrik** commented on 30 Aug 2024

Thank you for your support. You got my question wrong but I do not blame you for that. My description was maybe bad or misleading. In the meantime I solved my problem myself (it was just a selector issue) but you gave me a whole new opportunity to style the menu I did not even think about. So your effort was finally very helpful.

### Response

**Dusty** commented on 22 Mar 2025

Is there a way to dynamically change the CSS classes of the menu items after the menu has been rendered, perhaps based on user interactions or other events?
