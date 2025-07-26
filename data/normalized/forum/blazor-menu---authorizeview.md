# Blazor Menu - AuthorizeView

## Question

**Rob** asked on 27 Apr 2020

How do I integrate Authentication/Authorization with the TelerikMenu for Blazor? I don't see any options. I'd like to allow on certain menu items based on user authentication. Like this: <AuthorizeView> <Authorized> <NavLink class="list-group-item list-group-item-action bg-light" href="/" Match="NavLinkMatch.All"> <span class="oi oi-home" aria-hidden="true"></span> Home </NavLink> <NavLink class="list-group-item list-group-item-action bg-light" href="/employeeoverview"> <span class="oi oi-list-rich" aria-hidden="true"></span> Employees </NavLink> <NavLink class="list-group-item list-group-item-action bg-light" href="/employeeedit"> <span class="oi oi-list-rich" aria-hidden="true"></span> Add new employee </NavLink> <NavLink class="list-group-item list-group-item-action bg-light" href="Logout"> <span class="oi oi-list-rich" aria-hidden="true"></span> Log out (@context.User.Claims.FirstOrDefault(c=> c.Type=="[http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name")?.Value)](http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name")?.Value)) </NavLink> </Authorized> <NotAuthorized> <NavLink class="list-group-item list-group-item-action bg-light" href="Login"> <span class="oi oi-list-rich" aria-hidden="true"></span> Log in </NavLink> </NotAuthorized> </AuthorizeView>

## Answer

**Marin Bratanov** answered on 27 Apr 2020

Hi Rob, I made the following article that explains the situation: [https://docs.telerik.com/blazor-ui/knowledge-base/menu-authorize-view.](https://docs.telerik.com/blazor-ui/knowledge-base/menu-authorize-view.) Regards, Marin Bratanov
