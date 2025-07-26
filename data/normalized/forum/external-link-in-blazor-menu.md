# external link in Blazor Menu

## Question

**Chr** asked on 28 Jun 2023

I'm trying to add a link that is outside of Blazor, in a menu component. I think this is more of a Blazor routing issue than the menu component but I can't figure out how to work around it. Blazor's default integration with AD includes a logout link. <a href="MicrosoftIdentity/Account/SignOut"> Log in </a> I'm trying to add that link to the Menu component and I think its routing like an internal blazor page. Below is the menu code and the last menu item is the logout. protected async override Task OnInitializedAsync () { var authState=await authenticationState; var user=authState?.User;
IsAdmin=user.IsInRole( "TaxonomyAdmin" ); var logoutUrl=string.Concat(Navigator.BaseUri, "MicrosoftIdentity/Account/SignOut" );

MenuItems=new List<MenuItem>()
{ new MenuItem{
Url="/",
Icon=FontIcon.Menu,
Items=new List<MenuItem>(){ new MenuItem {Text="Home", Url="/" }, new MenuItem {Text="New Request", Url="/newrequest" }, new MenuItem {Text="Admin", Url="/", Disabled=!IsAdmin }, new MenuItem {Text="Logout", Url=logoutUrl}
}
}
}; base.OnInitialized();
} It takes me to the correct url which is [https://localhost:7261/MicrosoftIdentity/Account/SignOut](https://localhost:7261/MicrosoftIdentity/Account/SignOut) and I get the routing error: "Sorry there is nothing at this address". If I click return and rerun that URL it routes to the logout as expected. Any suggestions?

### Response

**Bryan** commented on 30 Jan 2024

*bump* We're having a very similar issue. External links to correct blazor routes are giving us that "Sorry there is nothing at this address" message. While testing, we were able to strip this down to a very basic blazor project wherein the issue is introduced when adding a script reference to telerik-blazor.js. Commenting out the reference allows the page to load the hyperlink without issue.

### Response

**Chris** commented on 30 Jan 2024

My issue was as much a bad url as anything. I ended up with this in the MenuItems and it works fine now. new MenuItem {Text="Logout", Url="[https://login.microsoftonline.com/common/oauth2/v2.0/logout"}](https://login.microsoftonline.com/common/oauth2/v2.0/logout"})
