# Hierarchical Drawer on an Authorized Page

## Question

**Jes** asked on 04 Jun 2020

I am currently working on a getting a new Blazor site set up. This site will be using Azure AD for authentication and restricts the entire site to only users logged in. Right now I am working on getting the Hierarchical Drawer in to the site. I have run in to the following issue, The child content element 'Template' of component 'TelerikDrawer' uses the same parameter name ('context') as enclosing child content element 'Authorized' of component 'AuthorizeView'. Specify the parameter name like: '<Template Context="another_name"> to resolve the ambiguity. <Authorized> <div class="main"> <div class="top-row px-4"> <a class="logo" href="/"> <img src="img/Logo.png" /> </a> <div class="user-info"> <LoginDisplay /> </div> </div> <TelerikDrawer @ref="@Drawer" Data="DrawerItems" MiniMode="@true" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> <ul> @foreach (var item in context) { var selectedClass=item==SelectedItem ? "k-state-selected" : string.Empty; <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass"> <div class="k-level-@(item.Level)"> <TelerikIcon Icon="@item.Icon"></TelerikIcon> <span class="k-item-text">@item.Text</span> </div> @if (item.Expanded && (item.Children?.Any() ?? false)) { <span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span> } else if (!item.Expanded && (item.Children?.Any() ?? false)) { <span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span> } </li> } </ul> </div> </Template> <Content> <div class="content px-4"> @Body </div> </Content> </TelerikDrawer> </div> </Authorized> I have tried the following: <Authorized Context="AuthContext"> <div class="main"> <div class="top-row px-4"> <a class="logo" href="/"> <img src="img/Logo.png" /> </a> <div class="user-info"> <LoginDisplay /> </div> </div> <TelerikDrawer @ref="@Drawer" Data="DrawerItems" MiniMode="@true" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded"> <Template> <div class="k-drawer-items" role="menubar" aria-orientation="vertical"> <ul> @foreach (var item in context) { var selectedClass=item==SelectedItem ? "k-state-selected" : string.Empty; <li @onclick="@(()=> OnItemSelect(item))" class="k-drawer-item @selectedClass"> <div class="k-level-@(item.Level)"> <TelerikIcon Icon="@item.Icon"></TelerikIcon> <span class="k-item-text">@item.Text</span> </div> @if (item.Expanded && (item.Children?.Any() ?? false)) { <span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span> } else if (!item.Expanded && (item.Children?.Any() ?? false)) { <span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height: inherit; margin: 0 8px"></span> } </li> } </ul> </div> </Template> <Content> <div class="content px-4"> @Body </div> </Content> </TelerikDrawer> </div> </Authorized> But then get the following error: NullReferenceException: Object reference not set to an instance of an object. In debugging, I found that this error was at the following line of code: @foreach (var item in context) and the context is null. If anyone has any insight in to have a Hierarchical Drawer on a Authorized page? Thank you for taking a look, Jesse

## Answer

**Marin Bratanov** answered on 04 Jun 2020

Hello Jesse, The issue with nested RenderFragments (which is the root cause of the identical names of the context variables) is explained here: [https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment.](https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment.) Here's a sample of the solution put in the demo: <TelerikDrawer @ref="@Drawer" Data="Data" MiniMode="false" Mode="@DrawerMode.Push" TItem="DrawerItem" SelectedItemChanged="@OnItemSelect" @bind-Expanded="@Expanded">
<Template Context="myChangedContextName">
<div class="k-drawer-items" role="menubar" aria-orientation="vertical">
<ul>
@foreach ( var item in myChangedContextName )
{ var selectedClass=item==SelectedItem ? "k-state-selected": string.Empty; Regards, Marin Bratanov

### Response

**Jesse** answered on 04 Jun 2020

Marin, Thank you very much for the prompt response. I have now bookmarked that Nest Render Fragments page. Jesse
