# Can't display FontIcon in Menu Item

## Question

**Chr** asked on 19 Jun 2023

I feel like I'm missing something really simple here. I want to display an icon with a menu item. I'm following this example [https://docs.telerik.com/blazor-ui/components/menu/icons](https://docs.telerik.com/blazor-ui/components/menu/icons) and want to add the FontIcon.Menu. In the code below, I added the icon to the top level menu item. @layout TelerikLayout
@inherits LayoutComponentBase
@using Telerik.FontIcons; <PageTitle> HR Taxonomy Change Management </PageTitle> <div class="container"> <div class="border"> <div class="title"> Taxonomy Change Management </div> <div class="login"> <LoginDisplay /> </div> <div style="height: 80px;"> <TelerikMenu IconField="@(nameof(MenuItem.Icon))" Data="MenuItems" Orientation=@MenuOrientation.Horizontal> </TelerikMenu> </div> </div> <div> <article class="content px-4"> @Body </article> </div> </div> @code{
public List <MenuItem> MenuItems { get; set; }=new List <MenuItem> ();

public class MenuItem
{
public string Text { get; set; }
public bool Disabled { get; set; }
public object Icon { get; set; }
public IEnumerable <MenuItem> Items { get; set; }
}

protected override void OnInitialized()
{
MenuItems=new List <MenuItem> ()
{
new MenuItem()
{
Text="None",
Icon="@FontIcon.Menu",
Items=new List <MenuItem> ()
{
new MenuItem {Text="Home" },
new MenuItem {Text="New Request"},
new MenuItem {Text="Admin"}
}
}
};

base.OnInitialized();
}
} <style> #demo-runner { height: 400px;
} </style>

## Answer

**Hristian Stefanov** answered on 20 Jun 2023

Hi Chris, Thank you for sharing your configuration. This greatly aids the investigation process. Upon careful review of the provided code, I have found the root cause for the incorrect display of the icon. The issue stems from a typo in the line responsible for setting the "Icon" property of the MenuItem. To rectify this typo, remove the double quotation marks surrounding the @FontIcon.Menu. I have modified the sample for your convenience, and the revised section is highlighted for clarity: @using Telerik.FontIcons; <TelerikMenu IconField="@(nameof(MenuItem.Icon))" Data="MenuItems" Orientation=@MenuOrientation.Horizontal> </TelerikMenu> @code {
public List <MenuItem> MenuItems { get; set; }=new List <MenuItem> ();

protected override void OnInitialized()
{
List <MenuItem> menuItems=new List <MenuItem> {
new MenuItem { Text="Home" },
new MenuItem { Text="New Request" },
new MenuItem { Text="Admin" }
};

MenuItems=new List <MenuItem> ()
{
new MenuItem()
{
Text="None", Icon=@FontIcon.Menu,
Items=menuItems
}
};
}

public class MenuItem
{
public string Text { get; set; }
public bool Disabled { get; set; }
public object Icon { get; set; }
public IEnumerable <MenuItem> Items { get; set; }
}
} If you encounter any further difficulties or encounter any obstacles during the testing phase, please do not hesitate to reach out. I am here to provide any additional assistance you may require. Regards, Hristian Stefanov
