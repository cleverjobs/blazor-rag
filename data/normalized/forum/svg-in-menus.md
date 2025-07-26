# SVG in Menus

## Question

**Mar** asked on 18 Mar 2022

Hi I would like to build a dark mode toggle like the one on use on Dark Mode - Tailwind CSS Have been looking at the documentation for the content menu and the "normal" menu. I can see that you can use a template but can I build a template that's accept svg? Any plans on implementing headless-ui for blazor? I really like the concept. Could use Bootstrap dropdown, but again why use another framework? Dropdowns · Bootstrap v5.1 (getbootstrap.com)

## Answer

**Svetoslav Dimitrov** answered on 23 Mar 2022

Hello Martin, The templates of the Menu should accept SVG as they are standard RenderFragments. Below, I have added an example of a Menu that uses the item template to insert an SVG: <TelerikMenu Data="@MenuItems" ItemsField="@nameof(MenuItem.SubSectionList)"> <ItemTemplate Context="item"> @{
var shouldNavigate=!string.IsNullOrEmpty(item.Page);
if (shouldNavigate)
{ <NavLink href="@item.Page"> @item.Section </NavLink> }
else
{ <svg version="1.1" baseProfile="full" width="300" height="200" xmlns="[http://www.w3.org/2000/svg">](http://www.w3.org/2000/svg">) <rect width="100%" height="100%" fill="black" /> <circle cx="150" cy="100" r="90" fill="blue" /> </svg> <span style="font-weight: bold;"> See more about our @item.Section.ToLowerInvariant() </span> }
} </ItemTemplate> </TelerikMenu> @code {
public List <MenuItem> MenuItems { get; set; }

public class MenuItem
{
public string Section { get; set; }
public string Page { get; set; }
public List <MenuItem> SubSectionList { get; set; }
}

protected override void OnInitialized()
{
MenuItems=new List <MenuItem> ()
{
new MenuItem()
{
Section="Company",
SubSectionList=new List <MenuItem> ()
{
new MenuItem()
{
Section="Overview",
Page="company/overview"
},
new MenuItem()
{
Section="Events",
Page="company/events"
},
new MenuItem()
{
Section="Careers",
Page="company/careers"
}
}
},
new MenuItem()
{
Section="Services",
SubSectionList=new List <MenuItem> ()
{
new MenuItem()
{
Section="Consulting",
Page="consultingservices"
},
new MenuItem()
{
Section="Education",
Page="education"
}
}
}
};

base.OnInitialized();
}
} Regarding the toggling of the Dark Mode dynamically, this would be possible once the Nouvelle theme is available. Currently, it is in an experimental stage and you can track the development from this GitHub issue. On the topic of the Headless UI for Blazor, I should say that we are not currently developing such an option. While it looks interesting option to explore I would say that the biggest benefit of using a UI product suite like ours is the built-in themes that come with the components, hence the developer should not spend time learning CSS and applying custom styles to the components from scratch. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Martin Herløv** commented on 23 Mar 2022

Thanks 👍 What if I want to use a svg for each menu items? Headless UI is great when the default components don't fit in. Also you can style them to look anyway you want

### Response

**Svetoslav Dimitrov** commented on 28 Mar 2022

The <ItemTemplate> renders for each item in the menu, so if you want for each and every item you can remove the conditional block (if and else) and an SVG will be rendered for each item. You can read more information on the template available for the Menu from the Template article.
