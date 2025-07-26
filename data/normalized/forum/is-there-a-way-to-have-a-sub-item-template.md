# Is there a way to have a sub item template

## Question

**Chr** asked on 06 Jun 2020

I'm looking to do some a type of "mega menu" where a given top level menu item has a number of sub items, I'd like to have a different layout, or even a list view for the sub menu template. I thought maybe using the HasChildrenField set to false would allow me to do something but have not had luck so far. An example of the type of thing I am talking about can be found here ([https://freefrontend.com/css-menu/)](https://freefrontend.com/css-menu/)) in CSS

## Answer

**Chris** answered on 06 Jun 2020

Sorry this is a better link to what I am trying to produce: [https://freefrontend.com/css-menu/#mega-menu](https://freefrontend.com/css-menu/#mega-menu)

### Response

**Marin Bratanov** answered on 08 Jun 2020

Hi Chris, Something like the snippet below would be the general approach at the moment. Make sure to check out the comments for a feature that must be implemented before this is viable. <style> /* this first rule will affect ALL animation containers on the page and they are used in many places
this would let you have a more specific selector:
[https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance)
*/.k-animation-container.k-animation-container-shown,
.k-animation-container .k-menu-item, .k-animation-container .k-menu-link {
width: 100 % !important;
}
.k-animation-container .mega-menu-item {
width: 100 %;
height: 20 vh;
border: 2 px solid black;
background: gray;
}
.k-animation-container .mega-menu-item li {
height: 200 px;
background: yellow;
}
</style>

<TelerikMenu Data="@MenuItems" ItemsField="SubSectionList">
<ItemTemplate Context="item">
@{ //the mega menu comes from child items and we choose what HTML to render //in this example - from separate components for brevity if (item.Section.ToLowerInvariant()=="companymegamenu" )
{
<CompanyMenu />
} else if (item.Section.ToLowerInvariant()=="servicesmegamenu" )
{
<ServicesMenu />
} else {
<text>@item.Section</text>
}
}
</ItemTemplate>
</TelerikMenu>

@code { public List<MenuItem> MenuItems { get; set; } public class MenuItem { public string Section { get; set; } public string Page { get; set; } public List<MenuItem> SubSectionList { get; set; }
} protected override void OnInitialized ( ) {
MenuItems=new List<MenuItem>()
{ new MenuItem()
{
Section="Company",
SubSectionList=new List<MenuItem>()
{ new MenuItem()
{
Section="companymegamenu" }
}
}, new MenuItem()
{
Section="Services",
SubSectionList=new List<MenuItem>()
{ new MenuItem()
{
Section="servicesmegamenu",
},
}
}
}; base.OnInitialized();
}
} and the very basic content of the child components that you'd replace with your desired HTML: <div class="mega-menu-item"> the company mega menu <ul> <li> Overview </li> <li> Events </li> <li> Careers </li> </ul> </div> and <div class="mega-menu-item"> the SERVICES mega menu <ul> <li> Consulting </li> <li> Training </li> </ul> </div> Regards, Marin Bratanov
