# how to get tooltips on drawer items

## Question

**Dea** asked on 18 Apr 2024

I have the below code that I was hoping would show the hint above the {getting Started] drawer item when user puts mouse over it. But to no hope. :( didnt work. What am I doing wrong? <TelerikTooltip TargetSelector=".k-drawer-items span.icon-container[title]" /> <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="false" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind -Expanded="@Expanded"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> <ul> @foreach (var item in context) { var selectedClass=item==SelectedItem ? "k-selected" : string.Empty; <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass k-level-@(item.Level)"> <TelerikSvgIcon Icon="@item.Icon"></TelerikSvgIcon> <span class="icon-container" title="@item.Title"></span> <span class="k-item-text"> @item.Text </span> @if (item.Expanded && (item.Children?.Any() ?? false)) { <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronDown" /> } else if (!item.Expanded && (item.Children?.Any() ?? false)) { <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronRight" /> } </li> } </ul> </div> </Template> <DrawerContent> @SelectedItem?.Description </DrawerContent> </TelerikDrawer> @code { public TelerikDrawer <DrawerItem> Drawer { get; set; } public DrawerItem SelectedItem { get; set; } public bool Expanded { get; set; }=true; public IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> { new DrawerItem { Title="Well hello there!", Text="Getting Started", Icon=SvgIcon.QuestionCircle, Description="The Blazor framework by Microsoft allows you to create web applications with .NET and C# to create front-end. The Telerik® UI for Blazor components facilitate the front-end development by providing you with ready made UI components." }, new DrawerItem { Text="Components", Icon=SvgIcon.Categorize, Description="Blazor is still a new technology and the component suite is young. We are constantly working on adding new features and components. Tell us which components you want implemented and how you intend to use them, and Blazor, at our feedback portal.", Children=new List <DrawerItem> () { new DrawerItem { Text="Grid", Icon=SvgIcon.Grid, Level=1, Description="The Telerik Blazor Data Grid provides a comprehensive set of ready-to-use features covering everything from paging, sorting, filtering, editing, and grouping to row virtualization, optimized data reading, keyboard navigation and accessibility support." }, new DrawerItem { Text="Calendar", Icon=SvgIcon.CalendarDate, Level=1, Description="The Calendar component allows the user to scroll through a calendar and select one or more dates. " }, new DrawerItem { Text="Menu", Icon=SvgIcon.Menu, Level=1, Description="The Menu component displays data (flat or hierarchical) in a traditional menu-like structure." }, } }, new DrawerItem { Text="Browser Support", Icon=SvgIcon.Calendar, Description="Browsers supported by Telerik UI for Blazor: Chrome (including Android and iOS), Edge, Firefox, Safari (including iOS)" } }; public async Task ToggleDrawer()=> await Drawer.ToggleAsync(); protected override void OnInitialized() { SelectedItem=Data.First(); } public void OnItemSelect(DrawerItem selectedItem) { SelectedItem=selectedItem; selectedItem.Expanded=!selectedItem.Expanded; var newData=new List <DrawerItem> (); foreach (var item in Data.Where(x=> x.Level <=selectedItem.Level)) { newData.Add(item); if (item==selectedItem && selectedItem.Expanded && (item.Children?.Any() ?? false)) { foreach (var child in item.Children) { newData.Add(child); } } if (item !=selectedItem && !(item.Children?.Contains(selectedItem) ?? false)) { item.Expanded=false; } } Data=newData; } public class DrawerItem { public string Title { get; set; } public string Text { get; set; } public ISvgIcon Icon { get; set; } public bool Expanded { get; set; } public int Level { get; set; } public string Description { get; set; } public IEnumerable <DrawerItem> Children { get; set; } } }

## Answer

**Hristian Stefanov** answered on 19 Apr 2024

Hi Deasun, The reason for the problem here is that the " <span class="icon-container" title="@item.Title"> " has no content inside and zero dimensions. Therefore, to achieve the desired result, make sure that the span element wraps the content inside the " <li>. " Here is a modified version of your code (see the highlighted parts): <TelerikTooltip TargetSelector=".k-drawer-items span.icon-container[title]" /> <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="false" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> <ul> @foreach (var item in context)
{
var selectedClass=item==SelectedItem ? "k-selected" : string.Empty; <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass k-level-@(item.Level)"> <TelerikSvgIcon Icon="@item.Icon"> </TelerikSvgIcon> <span class="icon-container" style="width: 100%;" title="@item.Title"> <span class="k-item-text"> @item.Text </span> @if (item.Expanded && (item.Children?.Any() ?? false))
{ <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronDown" /> }
else if (!item.Expanded && (item.Children?.Any() ?? false))
{ <TelerikSvgIcon Class="drawer-chevron-icon" Icon="@SvgIcon.ChevronRight" /> } </span> </li> } </ul> </div> </Template> <DrawerContent> @SelectedItem?.Description </DrawerContent> </TelerikDrawer> @code {
public TelerikDrawer <DrawerItem> Drawer { get; set; }
public DrawerItem SelectedItem { get; set; }
public bool Expanded { get; set; }=true;
public IEnumerable <DrawerItem> Data { get; set; }=new List <DrawerItem> {
new DrawerItem
{
Title="Well hello there!",
Text="Getting Started",
Icon=SvgIcon.QuestionCircle,
Description="The Blazor framework by Microsoft allows you to create web applications with .NET and C# to create front-end. The Telerik® UI for Blazor components facilitate the front-end development by providing you with ready made UI components."
},
new DrawerItem
{
Text="Components",
Icon=SvgIcon.Categorize,
Description="Blazor is still a new technology and the component suite is young. We are constantly working on adding new features and components. Tell us which components you want implemented and how you intend to use them, and Blazor, at our feedback portal.",
Children=new List <DrawerItem> ()
{
new DrawerItem
{
Text="Grid",
Icon=SvgIcon.Grid,
Level=1,
Description="The Telerik Blazor Data Grid provides a comprehensive set of ready-to-use features covering everything from paging, sorting, filtering, editing, and grouping to row virtualization, optimized data reading, keyboard navigation and accessibility support." },
new DrawerItem
{
Text="Calendar",
Icon=SvgIcon.CalendarDate,
Level=1,
Description="The Calendar component allows the user to scroll through a calendar and select one or more dates. "
},
new DrawerItem
{
Text="Menu",
Icon=SvgIcon.Menu,
Level=1,
Description="The Menu component displays data (flat or hierarchical) in a traditional menu-like structure."
},
}
},
new DrawerItem
{
Text="Browser Support",
Icon=SvgIcon.Calendar,
Description="Browsers supported by Telerik UI for Blazor: Chrome (including Android and iOS), Edge, Firefox, Safari (including iOS)"
}
};
public async Task ToggleDrawer()=> await Drawer.ToggleAsync();
protected override void OnInitialized()
{
SelectedItem=Data.First();
}
public void OnItemSelect(DrawerItem selectedItem)
{
SelectedItem=selectedItem;
selectedItem.Expanded=!selectedItem.Expanded;
var newData=new List <DrawerItem> ();
foreach (var item in Data.Where(x=> x.Level <=selectedItem.Level))
{
newData.Add(item);
if (item==selectedItem && selectedItem.Expanded && (item.Children?.Any() ?? false))
{
foreach (var child in item.Children)
{
newData.Add(child);
}
}
if (item !=selectedItem && !(item.Children?.Contains(selectedItem) ?? false))
{
item.Expanded=false;
}
}
Data=newData;
}
public class DrawerItem
{
public string Title { get; set; }
public string Text { get; set; }
public ISvgIcon Icon { get; set; }
public bool Expanded { get; set; }
public int Level { get; set; }
public string Description { get; set; }
public IEnumerable <DrawerItem> Children { get; set; }
}
} You can run the above sample and hover over the "Getting Started" option to see the result. Regards, Hristian Stefanov Progress Telerik
