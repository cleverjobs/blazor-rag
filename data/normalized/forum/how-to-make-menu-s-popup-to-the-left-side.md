# How to make Menu's popup to the left side

## Question

**Ind** asked on 11 Sep 2021

Hi I'm having a cascading menu on the right side of the page, So it is natural to make the popup direction to the left. like bootstrap dropdown dropleft [https://getbootstrap.com/docs/4.5/components/dropdowns/#dropleft](https://getbootstrap.com/docs/4.5/components/dropdowns/#dropleft) Does anyone know whats the solution for this common layout? Thanks in advance. This is the current behaviour when the menu is on the right side of the page. This is my code, taken and modified from [https://docs.telerik.com/blazor-ui/components/menu/overview](https://docs.telerik.com/blazor-ui/components/menu/overview) <h3> menu on Right side </h3> <div class="toolbar-buttons"> <TelerikMenu Data="@MenuItems" Orientation="MenuOrientation.Horizontal" UrlField="@nameof(MenuItem.Page)" ItemsField="@nameof(MenuItem.SubSectionList)" TextField="@nameof(MenuItem.Section)"> </TelerikMenu> </div> @code {

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
Section="Right aligned menu", // items that don't have a URL will not render links
SubSectionList=new List <MenuItem> ()
{
new MenuItem()
{
Section="menuItem1",
SubSectionList=new List <MenuItem> ()
{
new MenuItem()
{
Section="menuItem-subMenu1",
Page="consultingservices"
},
new MenuItem()
{
Section="menuItem-subMenu1",
Page="education"
}
}
},
new MenuItem()
{
Section="MenuItem2",
Page="company/events"
}

}
},
};

base.OnInitialized();
}
} <style type="text/css">.toolbar-buttons { display: flex; flex-direction: row; justify-content: end;
} </style>

## Answer

**Marin Bratanov** answered on 12 Sep 2021

Hello Indra, We tend to implement automatic viewport boundary detection in our components to have all menu items and sub-items remain visible, and you can Follow the implementation of that for Blazor here: [https://feedback.telerik.com/blazor/1460102-built-in-boundary-detection-or-property-to-set-the-expand-direction-of-sub-menus.](https://feedback.telerik.com/blazor/1460102-built-in-boundary-detection-or-property-to-set-the-expand-direction-of-sub-menus.) I've also added your Vote on your behalf (our management monitors the popularity of items like that, and takes it into account for planning). On a similar note, you may want to Vote for and Follow a similar feature for the dropdowns here: [https://feedback.telerik.com/blazor/1468216-built-in-boundary-detection](https://feedback.telerik.com/blazor/1468216-built-in-boundary-detection) Regards, Marin Bratanov Progress Telerik
