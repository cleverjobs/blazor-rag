# Menu dropdown list hover color

## Question

**Mik** asked on 08 Feb 2022

Hi, I am using the TelerikMenu Blazor component and I am trying to change the background color of the submenu items when being hovered over. I can successfully change the hover colors for the top-level menus but not the submenus. When I am running the app, I can go into developer tools and write the css to change the submenu background when being hovered over, but when I try that same css in my page css file, only the top-level menu items are affected (meaning the hover affect only happens to the top-level menu), I have attached a picture of the submenu with a background color change on hover via Developer Tools. I am probably missing a hierarchy level in the css - any assistance is appreciated. Thanks, Mike Menu creation tag: <nav class="navbar navbar-dark navbar py-md-0" id="navbar-custom-style"> <span class=" k-link k-menu-link"> <TelerikMenu Data="MenuItems" UrlField="@nameof(MenuItem.Page)" Orientation="MenuOrientation.Horizontal" Class="centered-menu"> </TelerikMenu> </span> </nav> Menu creation code: public List<MenuItem> MenuItems { get; set; } protected override async Task OnInitializedAsync() { List<MenuItem> menuItems=new List<MenuItem>() { new MenuItem { Text="Home", Page="/", IconClass="oi oi-home" }, new MenuItem { Text="Application Health", Items=new List<MenuItem>() { new MenuItem { Text="Counter", Page="/counter" }, new MenuItem { Text="Batch Review", Page="/batchreview", IconClass="oi oi-bar-chart" }, new MenuItem { Text="Closed Items", Page="" }, }, IconClass="oi oi-heart" }, new MenuItem { Text="Fetch Data", Page="/fetchdata", IconClass="oi oi-rich" }, }; MenuItems=menuItems; } Menu CSS (only affects top level menus): ::deep .centered-menu.k-menu .k-item { color: white; font-weight: bold; background: #007DBC; padding: 0; } ::deep .k-item.k-menu-item:hover { color: whitesmoke; background-color: #0b6fa4; } When I add this to my page css from the dev tools (which only affected the sub-menus), only the top menu items are affected:::deep li.k-item.k-menu-item:hover { color: darkblue; background-color: hotpink; }

## Answer

**Matthias** answered on 08 Feb 2022

Hello Mike, for me it works without any problems.. even if "!important" should be avoided... for my needs it works well. .k-menu-link { background-color: #0b6fa4!important; color: white!important;
}.k-menu-link:hover { color: darkblue!important; background-color: hotpink!important;
} regards Matthias

### Response

**Mike** commented on 08 Feb 2022

Thanks for looking into this Matthias! Unfortunately it still does not work for me (which leads me to believe I have something wrong somewhere). Using your css still only affects the top menu items (not the sub menus). Thanks, Mike

### Response

**Mike** answered on 10 Feb 2022

Figured it out. I needed to, as far as I know :-), put the styling inside the razor page. Once there, embedded between the style tags, the sub-menus now carry the styling the top-level menus have. When inside the page.razor.css file the styles would not work for the sub-menus (only the top-level menus - even using ::deep), So again, thanks Mathias, I put your css script in the right place and all is good. Mike
