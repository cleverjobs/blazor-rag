# After upgrade no nav menu icons or blanks!

## Question

**Dea** asked on 14 Nov 2023

My app showed no icons after upgrading to 4.6.0. :( I tried the KB suggestions to fix it. Went from no icons to getting the hamburger back and blank boxes! See: In _Host.cshtml I added: <link href="_content/Telerik.UI.for.Blazor/css/kendo-font-icons/font-icons.css" rel="stylesheet" /> In _Imports.razor I added: @using Telerik.FontIcons In codebehind page I have: public TelerikDrawer<DrawerItem> Drawer { get; set; } public DrawerItem SelectedItem { get; set; } public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem> { new DrawerItem { Title="Home", Text="Home", Icon="home", Url="./" }, new DrawerItem { Separator=true}, new DrawerItem { Title="CostTN Search", Text="CostTN Search", Icon="eye", Url="TNSearch" }, new DrawerItem { Title="RevIOTN Search", Text="RevIOTN Search", Icon="search", Url="RevIOTNSearch" }, new DrawerItem { Title="TN Mapping", Text="TN Mapping", Icon="subreport", Url="TNMapping" }, new DrawerItem { Title="Load Stats", Text="Load Stats", Icon="subreport", Url="LoadStats" }, new DrawerItem { Title="UnMapped Lines", Text="UnMapped Lines", Icon="subreport", Url="UnMappedLines" }, new DrawerItem { Separator=true}, // new DrawerItem //{ // Title="Crtls Demo", // Text="Crtls Demo", // Icon="subreport", // Url="ControlsDemo" //}, }; I am not sure what I am missing.

### Response

**Deasun** commented on 14 Nov 2023

tried teleriks example code: <TelerikDrawer Data="@Data" IconField="@nameof(DrawerItem.Icon)" MiniMode="true" @bind -Expanded="@DrawerExpanded" Mode="DrawerMode.Push" @ref="@DrawerRef" @bind -SelectedItem="@SelectedItem"> <DrawerContent> <TelerikButton OnClick="@(()=> DrawerRef.ToggleAsync())" Icon="@FontIcon.Menu"> Toggle drawer </TelerikButton> <div class="m-5"> Selected Item: @SelectedItem?.Text </div> </DrawerContent> </TelerikDrawer> <style> /* Third-party icon libraries should provide these styles out-of-the-box. */ /* base styles for all custom icons */ .my-icon { /* Define size, position and font styles here. */ width: 1em; height: auto; font-size: 16px; } /* styles for specific custom icons */ .my-icon-purple { /* define a background image or a font icon glyph here */ background: purple; flex-shrink: 0; } </style> @code { private TelerikDrawer <DrawerItem> DrawerRef { get; set; } private bool DrawerExpanded { get; set; }=true; private DrawerItem SelectedItem { get; set; } private IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> () { new DrawerItem { Text="Current Location", Icon=FontIcon.Pin }, new DrawerItem { Text="Navigation", Icon=FontIcon.Home }, new DrawerItem { Text="Favorites", Icon="my-icon my-icon-purple" }, }; public class DrawerItem { public string Text { get; set; } public object Icon { get; set; } } } Only thinkg that works is the purple! No home or pin show up!! Any one any ideas?

## Answer

**Dimo** answered on 15 Nov 2023

Hello Deasun, Font icons require 3 things: NuGet package, that is installed automatically as a dependency of Telerik.UI.for.Blazor package @using Telerik.FontIcons The font-icons.css stylesheet If you have all these three (and the Telerik UI for Blazor version is 4.6.0 ), then the only remaining reason is CSS code in the app, which overrides the icon font, and that's why you see the squares. In general, if you see squares in whatever content, this indicates a missing font. You can check the browser's network console if the font-icons.css file is loaded successfully. If you get 404, then perhaps the components version is not 4.6.0 (but in this case the icon font should be part of the main component CSS theme). I am attaching a working project here. The Home and Counter pages contain two Drawers that match the code snippets from this thread. Please compare with your app and let me know if you have additional questions. Regards, Dimo Progress Telerik

### Response

**Deasun** commented on 16 Nov 2023

the example doesnt seem to be using a TelerikDrawer object? in my Navmenu.razor I am using: <div class="drawer-container"> <div class="custom-toolbar"> <TelerikButton OnClick="@ToggleDrawer" Icon="@FontIcon.Menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"></TelerikButton> <span class="mail-box">@strAppName</span> </div> <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="true" Mode="@DrawerMode.Push" SelectedItem="@SelectedItem" SelectedItemChanged="((DrawerItem item)=> SelectedItemChangedHandler(item))"> <DrawerContent> @{ var additionalData=SelectedItem?.AdditionalData; if (additionalData !=null && additionalData.Any()) { <div class="page"> <ul> @foreach (var dataItem in additionalData) { <li> @if (!string.IsNullOrWhiteSpace(dataItem.Item1)) { <h6>@dataItem.Item1</h6> } <p>@dataItem.Item2</p> </li> } </ul> </div> } } </DrawerContent> <ItemTemplate Context="item"> <span class="k-icon k-i-@item.Icon" title="@item.Title"></span> <span class="k-item-text">@item.Text</span> </ItemTemplate> </TelerikDrawer> </div> codebehind looks like: public TelerikDrawer<DrawerItem> Drawer { get; set; } public DrawerItem SelectedItem { get; set; } public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem> { new DrawerItem { Title="Home", Text="Home", Icon="home", Url="./" }, new DrawerItem { Separator=true}, new DrawerItem { Title="CostTN Search", Text="CostTN Search", Icon="accessibility", Url="TNSearch" }, new DrawerItem { Title="RevIOTN Search", Text="RevIOTN Search", Icon="accessibility", Url="RevIOTNSearch" }, new DrawerItem { Title="TN Mapping", Text="TN Mapping", Icon="accessibility", Url="TNMapping" }, new DrawerItem { Title="Load Stats", Text="Load Stats", Icon="accessibility", Url="LoadStats" }, new DrawerItem { Title="UnMapped Lines", Text="UnMapped Lines", Icon="accessibility", Url="UnMappedLines" }, new DrawerItem { Separator=true}, new DrawerItem { Title="Maintenance", Text="Maintenance", Icon="gears", Url="Maintenance" }, new DrawerItem { Title="IT Stats", Text="IT Stats", Icon="chart-rose", Url="ITStats" }, }; The minute I add that into the page I lose the icons.

### Response

**Dimo** commented on 17 Nov 2023

The Drawer placement doesn't matter. The attached project contains Drawers in Index.razor and Counter.razor. Please check this REPL example, which shows three different ways to render font icons. Assuming that you have the font-icons.css file, then what you need to change is: Make the Icon property of type FontIcon, and use a TelerikFontIcon component in the ItemTemplate. <TelerikFontIcon Icon="@item.Icon" /> OR Add a k-font-icon class to the <span>. Generally, the <span> approach exists mainly for historical reasons. We recommend using FontIcon objects instead. <span class="k-icon k-font-icon k-i-@item.Icon" title="@item.Title"> </span> I see that you have also tried a mixture of the two options above - use a FontIcon item property and a <span>. I don't see a reason to do that. It can also work, but you need to fix the CSS class casing, because the font icon Enum strings are Uppercase: <span class="k-icon k-font-icon k-i-@item.Icon.ToString().ToLower() " title="@item.Title"> </span> Finally, I should clarify that the REPL playground doesn't register the font-icons.css file automatically, so the linked example registers it explicitly in the left vertical toolbar.

### Response

**Deasun** commented on 17 Nov 2023

those REPL example links never seem to work for me. All browsers come up with the following:

### Response

**Dimo** commented on 17 Nov 2023

Try clearing the browser cache. The last REPL example code is below: <link href="[https://blazor.cdn.telerik.com/blazor/5.0.0/kendo-font-icons/font-icons.css"](https://blazor.cdn.telerik.com/blazor/5.0.0/kendo-font-icons/font-icons.css") rel="stylesheet" type="text/css" /> <div class="drawer-container"> <div class="custom-toolbar"> <TelerikButton OnClick="@( async ()=> await Drawer.ToggleAsync() )" Icon="@FontIcon.Menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"> </TelerikButton> </div> <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="true" Mode="@DrawerMode.Push" @bind-SelectedItem="@SelectedItem"> <DrawerContent> Drawer Content </DrawerContent> <ItemTemplate Context="item"> <span class="k-icon k-font-icon k-i-@item.Icon" title="@item.Title"> </span> <TelerikFontIcon Icon="@item.FIcon" /> <span class="k-icon k-font-icon k-i-@item.FIcon.ToString().ToLower()" title="@item.Title"> </span> <span class="k-item-text"> @item.Text </span> </ItemTemplate> </TelerikDrawer> </div>

@code {
public TelerikDrawer<DrawerItem> Drawer { get; set; }
public DrawerItem SelectedItem { get; set; }
public IEnumerable<DrawerItem> Data { get; set; }=new List<DrawerItem>() { new DrawerItem ( ) {
Title="Home",
Text="Home",
FIcon=FontIcon.Home,
Icon="home",
Url="./" }, new DrawerItem ( ) { Separator=true }, new DrawerItem ( ) {
Title="CostTN Search",
Text="CostTN Search",
FIcon=FontIcon.Accessibility,
Icon="accessibility",
Url="TNSearch" }, new DrawerItem ( ) { Separator=true }, new DrawerItem ( ) {
Title="Maintenance",
Text="Maintenance",
FIcon=FontIcon.Gears,
Icon="gears",
Url="Maintenance" }, new DrawerItem ( ) {
Title="IT Stats",
Text="IT Stats",
FIcon=FontIcon.ChartRose,
Icon="chart-rose",
Url="ITStats" }
};

public class DrawerItem {
public string Text { get; set; }
public string Title { get; set; }
public FontIcon FIcon { get; set; }
public string Icon { get; set; }
public string Url { get; set; }
public bool Separator { get; set; }
}
}

### Response

**Deasun** commented on 27 Nov 2023

Appears to be working now. Thanks for all the help.
