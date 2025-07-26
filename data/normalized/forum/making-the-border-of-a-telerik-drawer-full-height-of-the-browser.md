# Making the border of a Telerik Drawer full height of the browser

## Question

**Abh** asked on 18 Apr 2022

Hello, I have implemented a Telerik Drawer from the documentation. Right now, there is only a vertical border for elements that are toggled or showing. However, I am trying to make the border full height at all times, even if the Drawer container is not "full". I have tried changing some of the Telerik CSS but I am unsure on how to get the border full height. Below is the code where the drawer is implemented and I am using the default, unmodified Telerik CSS files. @inject IFacilityService FacilityService
@inject ILocationService LocationService
@using SensorDashboard.Pages

<div class="custom-toolbar d-flex align-items-center nowrap ">
<div class="hamburger" style="padding-right:0em;margin-right:0em;">
<TelerikButton OnClick="@ToggleDrawer" Icon="menu" FillMode="@(ThemeConstants.Button.FillMode.Flat)"></TelerikButton>
</div>
<div class="logo-icon">
<a class="wilder-logo d-none d-lg-block">
<img src="/images/wilder-logo.png" />
</a>
</div>
<div class="logo-text d-none d-lg-block" style="width:12%; height:auto; margin-left:1em; padding-right:2em; margin-right:1em;">
<div>
<h3 class="font-text" style="height:100% !important;">Sensor Dashboard</h3>
</div>
</div>
<div class="k-form-field-wrap " style="padding-left:1em; padding-right:0em; margin-right:0em; margin-left:0em;">
<TelerikDropDownList Data="@Facilities" TextField="DisplayName" ValueField="Id" @bind-Value="@SelectedFacilityId" Width="140px">
<!--width 12 %-->
<DropDownListSettings>
<DropDownListPopupSettings Height="auto"></DropDownListPopupSettings>
</DropDownListSettings>
</TelerikDropDownList>
</div>
<div class="date-pick">
<TelerikDatePicker Min="@DateTime.Parse( " 2021 -01 -01 " )" Max="@DateTime.Today" @bind-Value="@SelectedDateTime" Width="9em" />
</div>
<TelerikButtonGroup Class="date-range-group">
<ButtonGroupToggleButton @bind-Selected="@_day" Rounded="0" Class="toggle-button" @ref="_selectDayButton" OnClick="SelectDay">Day</ButtonGroupToggleButton>
<ButtonGroupToggleButton @bind-Selected="@_week" Rounded="0" Class="toggle-button" @ref="_selectWeekButton" OnClick="SelectWeek">Week</ButtonGroupToggleButton>
<ButtonGroupToggleButton @bind-Selected="@_month" Rounded="0" Class="toggle-button" @ref="_selectMonthButton" OnClick="SelectMonth">Month</ButtonGroupToggleButton>
</TelerikButtonGroup>
<div class="icon-buttons">
<TelerikButton Icon="arrow-rotate-cw"></TelerikButton>
<TelerikButton Icon="file-pdf"></TelerikButton>
<TelerikButton Icon="file-csv"></TelerikButton>
<TelerikButton Icon="bell"> </TelerikButton>
</div>

<div class="logout-btn d-none d-lg-block position-absolute top-0 end-0 " style="margin-left:45%;">
<!--style="margin-left:70em;" -->
<TelerikButton Icon="logout"> </TelerikButton>
</div>
<div class="logout-btn d-none d-sm-block d-md-block d-lg-none" style="margin-left:0em; padding-left:0em;">
<TelerikButton Icon="logout"> </TelerikButton>
</div>
</div>
<!--end of toolbar-->

<TelerikDrawer @ref="@_drawer" Data="Data" MiniMode="false" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded">
<Template>
<div class="k-drawer-items" role="menubar" aria-orientation="vertical">
<!--<LoginDisplay />-->
<ul>
@foreach ( var item in context)
{ var selectedClass=item==SelectedDrawerItem ? "k-state-selected": string.Empty;

<li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass">
<div class="k-level-@(item.Level)">
<TelerikIcon Icon="@item.Icon"></TelerikIcon>
<span class="k-item-text">@item.Text</span>
</div>

@if (item.Expanded && (item.Children?.Any() ?? false ))
{
<span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span>
} else if (!item.Expanded && (item.Children?.Any() ?? false ))
{
<span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span>
}
</li>
}
</ul>
</div>
</Template>

<DrawerContent>
@if( SelectedDrawerItem is not null && ! string.IsNullOrWhiteSpace( SelectedDrawerItem.Id ) )
{ if ( SelectedDrawerItem.IsImage )
{
<Pictures LocationId="@SelectedDrawerItem.Id" LocationName="@SelectedDrawerItem.Description" />
} else {
<Sensors LocationId="@SelectedDrawerItem.Id" LocationName="@SelectedDrawerItem.Description" />
}
}
</DrawerContent>
</TelerikDrawer>
<!--- <NotAuthorized>
<a href="authentication/login">Log in </a>
</NotAuthorized>-->

@code { // component references private TelerikDrawer<DrawerItem> _drawer=null!; private ButtonGroupToggleButton _selectDayButton=null!; private ButtonGroupToggleButton _selectWeekButton=null!; private ButtonGroupToggleButton _selectMonthButton=null!; private bool _day=true; private bool _week=false; private bool _month=false; private string Size { get; set; }=ThemeConstants.Button.Size.Medium; public Dictionary<string, string> Sizes { get; set; }=new Dictionary<string, string>
{
{ "Small", ThemeConstants.Button.Size.Small },
{ "Medium", ThemeConstants.Button.Size.Medium },
{ "Large", ThemeConstants.Button.Size.Large }
}; public Facility[] Facilities
{ get; set; }=Array.Empty<Facility>(); public Guid SelectedFacilityId
{ get; set; } public DateTime SelectedDateTime
{ get; set; }=DateTime.Today; public DrawerItem? SelectedDrawerItem
{ get; set; } public bool Expanded
{ get; set; }=true; public IEnumerable<DrawerItem> Data
{ get; set; }=Array.Empty<DrawerItem>(); protected override async Task OnInitializedAsync ( ) { await base.OnInitializedAsync();

Data=new List<DrawerItem> { new DrawerItem { Id=$" {Guid.Empty:d} ", Text="Loading..." } };

StateHasChanged();

Facilities=await FacilityService.GetFacilitiesAsync();
SelectedFacilityId=Facilities.Select( el=> el.Id ).FirstOrDefault(); if ( SelectedFacilityId==Guid.Empty ) return;

StateHasChanged(); var drawers=new List<DrawerItem>(); var rooms=await LocationService.GetGrowRoomLocationsAsync( SelectedFacilityId ); foreach ( var room in rooms )
{ var room_item=new DrawerItem { Id=$" {room.Id:d} ", Text=room.DisplayName, Icon="home", Level=0, Children=new List<DrawerItem>() }; var room_sensors=new DrawerItem { Id=$" {room.Id:d} ", Text="Sensors", Description=$" {room.DisplayName} Sensors", Icon="chart-line", Level=1 }; var room_images=new DrawerItem { Id=$" {room.Id:d} ", IsImage=true, Text="Images", Description=$" {room.DisplayName} Images", Icon="image", Level=1 };
room_item.Children.Add( room_sensors );
room_item.Children.Add( room_images ); foreach ( var tower in room.GrowTowers )
{ var tower_item=new DrawerItem { Id=$" {tower.Id:d} ", Text=tower.DisplayName, Icon="layout-side-by-side", Level=1, Children=new List<DrawerItem>() };
room_item.Children.Add( tower_item ); var tower_sensors=new DrawerItem { Id=$" {tower.Id:d} ", Text="Sensors", Description=$" {room.DisplayName} {tower.DisplayName} Sensors", Icon="chart-line", Level=2 }; var tower_images=new DrawerItem { Id=$" {tower.Id:d} ", IsImage=true, Text="Images", Description=$" {tower.DisplayName} Images", Icon="image", Level=2 };
tower_item.Children.Add( tower_sensors );
tower_item.Children.Add( tower_images ); foreach ( var level in tower.GrowTowerLevels )
{ var level_item=new DrawerItem { Id=$" {level.Id:d} ", Text=level.DisplayName, Icon="minus", Level=2, Children=new List<DrawerItem>() };
tower_item.Children.Add( level_item ); var level_sensors=new DrawerItem { Id=$" {level.Id:d} ", Text="Sensors", Description=$" {room.DisplayName} {tower.DisplayName} {level.DisplayName} Sensors", Icon="chart-line", Level=3 }; var level_images=new DrawerItem { Id=$" {level.Id:d} ", IsImage=true, Text="Images", Description=$" {level.DisplayName} Images", Icon="image", Level=3 };
level_item.Children.Add( level_sensors );
level_item.Children.Add( level_images ); foreach ( var tray in level.GrowTrays )
{ var tray_item=new DrawerItem { Id=$" {tray.Id:d} ", Text=$"Tray {tray.Position} ", Description=$" {room.DisplayName} {tower.DisplayName} {level.DisplayName} Tray {tray.Position} Sensors and Pictures", Icon="group-section", Level=3 };
level_item.Children.Add( tray_item );
}
}
}

drawers.Add( room_item );
}

Data=drawers;
SelectedDrawerItem=drawers.FirstOrDefault();

StateHasChanged();
} public async Task ToggleDrawer ( )=> await _drawer.ToggleAsync(); private Task SelectDay ( ) { return Task.CompletedTask;
} private Task SelectWeek ( ) { return Task.CompletedTask;
} private Task SelectMonth ( ) { return Task.CompletedTask;
} public void OnItemSelect ( DrawerItem selectedItem ) {
SelectedDrawerItem=selectedItem;

selectedItem.Expanded=!selectedItem.Expanded; var newData=new List<DrawerItem>(); foreach ( var item in Data.Where( x=> x.Level <=selectedItem.Level ) )
{
newData.Add( item ); if ( item==selectedItem && selectedItem.Expanded && ( item.Children?.Any() ?? false ) )
{ foreach ( var child in item.Children )
{
newData.Add( child );
}
} if ( item !=selectedItem && !( item.Children?.Contains( selectedItem ) ?? false ) )
{
item.Expanded=false;
}
}

Data=newData;
} public class DrawerItem { public string Id
{ get; set; }=string.Empty; public string Text
{ get; set; }=string.Empty; public string Icon
{ get; set; }=string.Empty; public bool Expanded
{ get; set; } public int Level
{ get; set; } public string Description
{ get; set; }=string.Empty; public bool IsImage
{ get; set; }=false; public IList<DrawerItem>? Children
{ get; set; }
}
}

<!--drawer specific styles-->
<style> #demo-runner { height: 600 px;
}
.k-drawer-content {
padding: 25 px;
font-size: 18 px;
}
.k-drawer-container {
position: relative;
width: 100 %;
height: 95 %;

}
.k-drawer .k-drawer-item {
white-space: nowrap;
overflow: hidden;
} /* these control the padding of the different children */.k-level -1 {
padding-left: 20 px;
}
.k-level -2 {
padding-left: 40 px;
}

.k-level -3 {
padding-left: 60 px;
}
.custom-toolbar {
width: 100 % !important;
background-color: #fdf4e0; line-height: 10 px;
border-bottom: inset;
border-bottom-width: 1 px;
color: #656565; height: 5 em;
}
.wilder-logo {
padding-left: 2 em;
max-height: 3 em;
margin-right: 0 em;
padding-left: 0 em;
margin-bottom: 1 em;
margin-top: 1 em;
}

.nowrap {
white-space: nowrap;
}

.date-pick {
width: 10 em !important;
padding: 0;
margin-left: 15 em;
padding-right: 0 em;
margin-right: 0 em;
display: inline-block;
vertical-align: top;
padding-left: 1 em !important;
margin-left: 0 em !important;
padding-right: 0 em !important;
margin-right: 0 em !important;
}

.btn- group {
padding-left: 1 em;
width: 5 em;
padding-right: 5 em;
margin-right: 5 em;
}

.refresh-btn {
border-color: white;
margin-left: 0 em;
height: 100 %;
padding-left: 0 em;
}

.pdf-btn {
border-color: white;
margin-left: 1 em;
height: 100 %;
}

.alert-btn {
border-color: white;
margin-left: 1 em;
height: 100 %;
}

.date-range- group {
margin-left: 1 em;
margin-right: 1 em;
}

.toggle-button {
min-width: 5 em;
border-color: white
}

.logout-btn {
margin-top: 0 em;
margin-bottom: 0 em;

margin-right: 0 em;
}

.logo-text {
max-width: 100 %;

padding-right: 0 em;
margin-right: 0 em;
}

.logo-icon {
margin-right: 0 em;
padding-right: 0 em;
}

.font-text{
font-family:Voyage;
color:black;
padding-left: 0 em;
margin-left: 0 em !important;
font-size: 1.8 vw;
height: 3 em;
padding-right: 3 em;
margin-right: 4 em;
}

.icon-buttons{

}
.icon-button{
font-size: 4 em;
height: 1 em;
}
.date-range- group {
padding-right: 0 em;
margin-right: 0 em;
}
</style>

## Answer

**Dimo** answered on 20 Apr 2022

Hello Abhay, Set a custom CSS Class to the Drawer component and apply a suitable height style. Razor <TelerikDrawer Class="expand-height" /> CSS .expand-height { height: calc ( 100vh - 40px );
} 100vh is the viewport height. 40px is the height of the content outside the Drawer, which depends on your app layout. Generally, you can use any other height style, as long as it suits your scenario. Keep in mind that percentage heights require an explicit parent element height. The browser's DOM inspector will help you to track all parents. Regards, Dimo

### Response

**Abhay** commented on 20 Apr 2022

Hello Dimo, Thank you, this made the border height of the Drawer full height. However, now a vertical scrollbar is created within the drawer when items are expanded and it is causing formatting issues. I tried adding a class with "overflow-y:hidden" but it did not hide the scrollbar within the Drawer. Any help would be greatly appreciated.

### Response

**Dimo** commented on 21 Apr 2022

Abhay - use the DOM inspector to see which is the exact scrollable container and which is the content that overflows it. Then, decide if you will disable scrolling for the container, or reduce the size of the content. Inspect the HTML output of a page See the applied styles for a specific element For a start, check if reducing the height style from my previous response resolves the issue.

### Response

**Jon** commented on 24 Aug 2023

Thanks for the tips Dimo! In our situation, we had a wizard in the drawer content. If a subsequent step in the wizard caused the drawer content to grow, when the user scrolled down, the drawer no longer went all the way to the bottom. For our situation, we did this: body { min-height: calc(100vh - 40px);
}.expand-height { min-height: calc(100vh - 40px);
}
