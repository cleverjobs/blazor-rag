# .net8 webserver project Navmenu draweritem Hint not displaying, why?

## Question

**Dea** asked on 05 Aug 2024

See that popup hint when the user has eht emouse over the draweritem, [Products], had this working fine in the net6 version of the app. But on converting to .net8 it appears to have stopped working. Do I need to do somethign different? I cant find any simple examples of gettign this to work. Code I have: @inject NavigationManager NavigationManager <TelerikTooltip TargetSelector=".k-drawer-items span.k-icon[title]" /> <div class="drawer-container"> <div class="custom-toolbar"> <TelerikButton OnClick="@ToggleDrawer" Icon="@FontIcon.Menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"> </TelerikButton> <span class="mail-box">@strAppName</span> </div> <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="true" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> <ul> @foreach (var item in context) { var selectedClass=item==SelectedItem ? "k-selected" : string.Empty; <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass k-level-@(item.Level)"> <TelerikSvgIcon Icon="@item.Icon"></TelerikSvgIcon> <span class="k-item-text">@item.Text</span> <span class="k-icon k-font-icon k-i-@item.Icon" title="@item.Title"></span> @if (item.Expanded && (item.Children?.Any() ?? false)) { <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronDown" /> } else if (!item.Expanded && (item.Children?.Any() ?? false)) { <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronRight" /> } </li> } </ul> </div> </Template> </TelerikDrawer> </div> <style> .sidebar { background-image: none !important; } .drawer-container { /* margin: 30px auto;*/ width: 100% !important; /*100%*/ } .k-drawer-container { position: relative; width: 100%; } .custom-toolbar { width: @strAppNameWidth; background-color: #f6f6f6; line-height: 49px; border-bottom: inset; border-bottom-width: 1px; padding: 3px 8px; color: #656565; } .mail-box { margin-left: 20px; font-weight: bold; font-size: 17px; } .page ul { list-style: none; margin: 0; padding: 0; } .page li:last-child { border: 0; } .page li h6 { border-bottom: none; padding-bottom: 8px; } .k-drawer-content { padding: 25px; font-size: 18px; } .k-d-level { display: flex; } .drawer-chevron-icon { position: absolute; right: 0; line-height: inherit; margin: 0 8px } </style> As far as I can tell this line: <span class="k-icon k-font-icon k-i-@item.Icon" title="@item.Title"></span> Should be doing the work of showing the Hint whcih I am putting in title in code behind. example: new List<DrawerItem> { new DrawerItem { Title="Home", Text="Home", Icon=SvgIcon.Home, Url="./" }, new DrawerItem { Title="Management", Text="Management", Icon=SvgIcon.DataSds, Url="Management" }, new DrawerItem { Title="Products", Text="Products", Icon=SvgIcon.BuildingBlocks, Url="Products" }, Any suggestions pointers as to what I am doing incorrectly? Thanks Deasun.

### Response

**Deasun** commented on 06 Aug 2024

Found the fix for above: @* wrap this span around this to get the popup tooltip for each item in the menu *@<span class="icon-container" title="@item.Title"> <TelerikSvgIcon Icon="@item.Icon"></TelerikSvgIcon> </span>

## Answer

**Deasun** answered on 06 Aug 2024

see comment above

### Response

**Hristian Stefanov** commented on 07 Aug 2024

Hi Deasun, I'm glad to see that you have quickly resolved the matter on your own. Thank you for sharing the fix here, so other developers with the same scenario can benefit from it. Kind Regards, Hristian
