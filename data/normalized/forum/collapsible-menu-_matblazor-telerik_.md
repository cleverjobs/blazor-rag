# Collapsible Menu (MatBlazor + Telerik)

## Question

**Jam** asked on 12 Sep 2019

Hey guys, here is my MainLayout.razor page. The idea here is to have a side bar nav menu, which can be collapsed to give the user more screen real estate. I am using MatBlazors app bar and drawer components to have the "collapsing" feature. And then using the Telerik Menu with some custom styling to incorporate the nav links. @inherits LayoutComponentBase

@using Telerik.Blazor.Components.RootComponent
@using MatBlazor;
@using Telerik.Blazor.Components.Menu;
@inject NavigationManager navigationManager
@inject Blazored.LocalStorage.ILocalStorageService localStorage
@using Newtonsoft.Json;
@using System.Threading.Tasks;

<head>
<style>
span.k- in.k-menu-link {
display: flex;
}

.mdc-top-app-bar__row {
display: flex;
position: relative;
box-sizing: border-box;
width: 100 %;
height: 32 px !important;
background-color: #fafafa !important; top: 0 px;
position: fixed;
}

.mdc-top-app-bar-- fixed -adjust {
padding-top: 40 px !important;
}

.mdc-drawer {
z-index: 1;
box-shadow: -4 px 1 px 14 px 0 px black !important;
} /*MOBILE*/ @@media (min-width: 320 px) {
.mdc-drawer__content {
overflow-y: auto;
-webkit-overflow-scrolling: touch;
margin-top: 8 px;
background: #fafafa !important; height: 88 vh;
}

.mdc-drawer.mdc-drawer--open:not(.mdc-drawer--closing) + .mdc-drawer-app-content {
margin-left: 170 px;
margin-right: 0;
}

.mdc-drawer {
width: 170 px !important;
}

.Banner {
width: 100 %;
background-color: #3f9d2f !important; height: 110 px;
margin-top: -2 px;
box-shadow: -2 px -7 px 15 px 7 px black;
padding: 10 px;
}

.UserIcon {
font-size: 50 px !important;
color: #FFFFFF; margin-left: 39 % !important;
cursor: pointer;
margin-top: -7 px;
}

.WideScreenClass {
display: none;
}

.MobileClass{
display:block;
}

.BannerUsernameHeading{
margin: auto;
color: #FFFFFF; text-align: center;
font-weight: 500;
font-size: 30 px !important;
}

.BannerCompanyNameHeading{
margin: auto;
color: #FFFFFF; text-align: center;
font-size: 15 px !important;
margin-top: -9 px;
}

.k-menu- group.k-item> .k-link, .k-menu-vertical .k-item> .k-link {
color: black !important;
margin-bottom: 2 px !important;
margin-top: 2 px !important;
line-height: 1.6!important;
font-family: Roboto !important;
font-variant: all-petite-caps !important;
font-size: larger !important;
}

} /*WIDE SCREEN*/ @@media (min-width: 1280 px) {
.mdc-drawer__content {
height: 100 %;
overflow-y: auto;
-webkit-overflow-scrolling: touch;
margin-top: 48 px;
background: #fafafa !important; }

.mdc-drawer.mdc-drawer--open:not(.mdc-drawer--closing) + .mdc-drawer-app-content {
margin-left: 256 px;
margin-right: 0;
}

.mdc-drawer {
width: 256 px !important;
}

.Banner {
width: 100 %;
background-color: #3f9d2f !important; height: 175 px;
margin-top: -2 px;
box-shadow: -2 px -7 px 15 px 7 px black;
padding: 10 px;
}

.UserIcon {
font-size: 64 px !important;
color: #FFFFFF; margin-left: 36 % !important;
cursor: pointer;
}

.main> div {
padding-left: 2 rem !important;
padding-right: 1.5 rem !important;
margin-top: 48 px;
}

.MobileClass {
display: none;
}

.WideScreenClass{
display:block;
}

.BannerUsernameHeading{
margin: auto;
color: #FFFFFF; text-align: center;
font-weight: 500;
font-size: 42 px !important;
}

.BannerCompanyNameHeading{
margin: auto;
color: #FFFFFF; text-align: center;
font-size: 18 px !important;
}

.k-menu- group.k-item> .k-link, .k-menu-vertical .k-item> .k-link {
color: black !important;
margin-bottom: 2 px !important;
margin-top: 2 px !important;
line-height: 2!important;
font-family: Roboto !important;
font-variant: all-petite-caps !important;
font-size: larger !important;
}

}

:not(.mdc-list--non-interactive)> :not(.mdc-list-item--disabled).mdc-list-item { /*material chips*/ color: black;
}

.mdc-drawer .mdc-list-item { /*make text in side menu black*/ color: black;
}

.Title {
padding-left: 20 %;
}

.mat-accordion .mat-expansion-panel__summary .after {
color: black;
}

.mat-accordion .mdc-nav-menu .mat-expansion-panel__content .mdc-list-item {
font-weight: 500;
}

div #matBlazor_id_8e6ee3bc-7b6e-41e2-854a-b965730195b1 { overflow: hidden;
}

div #matBlazor_id_e44a318f-9585-474c-9dca-8576f4594719 { overflow: hidden;
}

div #matBlazor_id_d3b57f8a-30d5-4bf2-894e-2527d97e6529 { overflow-y: hidden;
}

.material-icons {
font-size: 56 px;
color: white;
}

.LogoutButton {
width: 100 % !important;
background: #3f9d2f !important; border-radius: 25 px;
color: white;
height: 50 px;
}

.mdc-chip {
background-color: #3f9d2f !important; color: rgb( 255, 255, 255 ) !important;
}

.AnimationDiv {
transition-property: all;
transition-property: transform;
transition-duration: 0.3 s;
}
</style>

<style>
a { /*make links a certain way*/ font-weight: 500!important;
color: black !important;
line-height: 2!important;
font-variant: all-small-caps !important;
font-family: Roboto !important;
padding: 10 px !important;
font-size: larger !important;
}
</style>

</head>

<TelerikRootComponent>
<MatAppBarContainer>
<MatAppBar Fixed="false" Style="height:48px; background-color:#3f9d2f !important; color:#FFFFFF !important;">
<MatAppBarRow Style="height:48px; ">
<MatAppBarSection>

@if (Opened==true )
{
<div>
<MatIconButton OnClick="@((e)=> ButtonClicked())"> <span class="fas fa-grip-lines"></span></MatIconButton>
</div>
} else {
<div>
<MatIconButton OnClick="@((e)=> ButtonClicked())"> <span class="fas fa-grip-lines-vertical"></span></MatIconButton>
</div>
}
<MatAppBarTitle>
@ModuleName
</MatAppBarTitle>
</MatAppBarSection>
</MatAppBarRow>
</MatAppBar>
<MatAppBarContent>
</MatAppBarContent>
</MatAppBarContainer>

<MatDrawerContainer Style="width:100%; overflow-y:hidden; min-height:100vh">
<MatDrawer @bind-Opened="@Opened" Mode="@MatDrawerMode.Dismissible">
<div class="Banner">
<div>
<i class="fas fa-user-circle UserIcon"></i>
<MatH3 Class="BannerUsernameHeading">@Username</MatH3>
<MatH6 Class="BannerCompanyNameHeading">Company</MatH6>
</div>
</div>
<div class="WideScreenClass">
<br />
<br />
<TelerikMenu Data="@MenuItems" Orientation="Telerik.Blazor.MenuOrientation.Vertical" UrlField="@nameof(MenuItem.Page)" ItemsField="@nameof(MenuItem.SubSectionList)" TextField="@nameof(MenuItem.Section)" OnClick="@((MenuItem item)=> OnClickHandler(item))">

<ItemTemplate Context="item">
@{ if (item.Section=="Site Access" )
{
<NavLink href="@item.Page">@item.Section</NavLink> <br />
<MatChipSet>
<MatChip Label="5"></MatChip>
</MatChipSet>
} else {
<NavLink href="@item.Page">@item.Section</NavLink> <br />
}

}
</ItemTemplate>
</TelerikMenu>
<div style="position:absolute; bottom:10px; width:100%; padding:10px;">

<img src="/images/CompanyLogo.png" style="width:200px; margin:auto; margin-left: 20px;" />
<br />

<Telerik.Blazor.Components.Button.TelerikButton Class="LogoutButton" OnClick="Logout">
LOGOUT
</Telerik.Blazor.Components.Button.TelerikButton>

</div>
</div>

<div class="MobileClass">
<TelerikMenu Data="@MobileMenuItems" Orientation="Telerik.Blazor.MenuOrientation.Vertical" UrlField="@nameof(MenuItem.Page)" ItemsField="@nameof(MenuItem.SubSectionList)" TextField="@nameof(MenuItem.Section)" OnClick="@((MenuItem item)=> OnClickHandler(item))">

</TelerikMenu>
</div>
</MatDrawer>
<MatDrawerContent Style="overflow-y:hidden;">
<div class="main">
<div class="content px-4">
@Body
</div>
</div>
</MatDrawerContent>

</MatDrawerContainer>
</TelerikRootComponent>

@code { public MenuItem ClickedItem { get; set; } protected void OnClickHandler ( MenuItem item ) {
ClickedItem=item;
ModuleName=item.Section.ToString();
Console.WriteLine( "Telerik menu item: " + item.Section.ToString());
Opened=!Opened;
} public List<MenuItem> MenuItems { get; set; } public class MenuItem { public string Section { get; set; } public string Page { get; set; } public List<MenuItem> SubSectionList { get; set; }
} public List<MenuItem> MobileMenuItems { get; set; } protected override void OnInitialized ( ) {
MenuItems=new List<MenuItem>()
{ new MenuItem()
{
Section="Dashboard",
Page="dashboard" }, new MenuItem()
{
Section="Site Access",
Page="siteaccess" }, new MenuItem()
{
Section="History",
Page="history" }, new MenuItem()
{
Section="Reports",
Page="reports" }, new MenuItem()
{
Section="Settings",
Page="settings" }, new MenuItem()
{
Section="Users",
Page="users" }, new MenuItem()
{
Section="Vehicles",
Page="vehicles" }, new MenuItem()
{
Section="Drivers",
Page="drivers" }
};

MobileMenuItems=new List<MenuItem>()
{ new MenuItem()
{
Section="Dashboard",
Page="dashboard" }, new MenuItem()
{
Section="Access Manager",
Page="accessmanager" }, new MenuItem()
{
Section="Yard Manager",
Page="yardmanager" }, new MenuItem()
{
Section="Vehicle Registration",
Page="vehicleregistration" }, new MenuItem()
{
Section="LOGOUT",
Page="/" },
}; base.OnInitialized();
} public void Logout ( ) {
UriHelper.NavigateTo( "/" );
} public string ModuleName { get; set; }=""; bool Opened=true; string Name=""; public async Task GoToUsers ( ) {
ModuleName="USERS";
UriHelper.NavigateTo( "/user" );
} public async Task CloseMenu ( string name ) //this method will close the menu, and set the page name as the module name at the top of the app bar {
ModuleName=""; await Task.Delay( 20 );
Opened=!Opened; await Task.Delay( 20 );
ModuleName=name;
} void ButtonClicked ( ) {
Opened=!Opened;
} public string UserName { get; set; } public string UserID { get; set; } protected override async Task OnInitializedAsync ( ) {


UserID=await localStorage.GetItemAsync<string>( "userID" );

ModuleName="DASHBOARD";

Username=await localStorage.GetItemAsync<string>( "userName" );

} public string Username { get; set; }
Modules modules=new Modules();
GeneralConfiguration generalConfiguration=new GeneralConfiguration();

}

## Answer

**James** answered on 12 Sep 2019

Oh, some more information, this is a responsive page. Meaning, I've included some media screen size breakpoints in CSS, that will basically just render some of the components a different way to show correctly on a small screen (320x420)

### Response

**Marin Bratanov** answered on 12 Sep 2019

Thank you for sharing your code, experience and solution with the community, James. You will find your Telerik points updated as a small "thank you". Regards, Marin Bratanov
