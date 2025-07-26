# Drawer Content Scroll

## Question

**Jes** asked on 09 Jun 2020

Hello, I was wondering if anyone has worked with the Drawer much and has found that if the content takes up more vertical space than the window can handle and the scroll bar appears. When this happens for me and I scroll down, the drawer menu moves as well. Is there any possible way to make the k-drawer fixed while keeping the k-drawer-content scrollable? Thank you so very much for your input, Jesse

## Answer

**Marin Bratanov** answered on 11 Jun 2020

Hi Jesse, We just made an example of this: [https://github.com/telerik/blazor-ui/tree/master/drawer/sidenav](https://github.com/telerik/blazor-ui/tree/master/drawer/sidenav) Regards, Marin Bratanov

### Response

**David** commented on 09 Jun 2021

I ran this demo as-is and it worked as advertised. However, I cannot get it to work when implementing in my application. The drawer and top header component scroll off the top of the view, unlike the demo version. I created a Telerik Web Assembly project (which is still very bare-bones, at the moment). Then I replaced my MainLayout content with what was in the demo's MainLayout and then I replaced my site.css with the one in the demo. I just can't get it to work and can't find any relevant differences between my app. and the demo. Finally, I started from scratch and created a new, blank, Telerik Blazor WASM project. Then I copied the demo code to it and it does not work. So it seems this solution only works for Blazor server applications. Any advice?

### Response

**Marin Bratanov** commented on 12 Jun 2021

Probably there is a slightly different set of CSS selectors you need. Maybe the templates the apps were made from have a different structure - the one in the repo has an <app> element that was the older approach, and since then <div id="app"> is preferred instead, so the selector would have to change from app to #app. That difference is in index.html and _Host.cshtml - it is above the layout itself. There might be something else that I can't guess right now, but the goal is to see where scrollbars come from and to ensure they are on a lower-level element in the layout, not the top-level ones like html, body, app (or #app) - only the content should scroll, not the whole layout. What I am certain of is that this behavior is about finding the right CSS rules and/or selectors for the app, it is not related to the app being WASM-based or server-side Blazor.

### Response

**Jesse** answered on 11 Jun 2020

Marin, As always, thank you so much. That works beautifully. Jesse

### Response

**David Ocasio** answered on 21 Sep 2020

So I need to merge the example supplied in the demo area and this sidenav example mentioned here. Specifically I need some content including the hamburger button to be placed outside of the drawer. I do want the drawer content to handle the scrolling and not the browser as you show in your example. For the most part this works except for the scrollbar initially showing . I am sure it is due to the 100% placed on both the outside container and the content. Unfortunately my CSS is rusty and I cannot seem to get it to show no vertical scrollbar initially. any assistance would be appreciated. please see attached code and images @layout TelerikLayout @inherits LayoutComponentBase @inject NavigationManager NavigationManager <div class="drawer-container"> <div class="custom-toolbar"> <TelerikButton OnClick="@( ()=> DrawerRef.ToggleAsync() )" Icon="@IconName.Menu"></TelerikButton> <span class="title">Dashboard</span> </div> <TelerikDrawer Data="@NavigablePages" @bind-Expanded="@DrawerExpanded" MiniMode="true" Mode="@DrawerMode.Push" @ref="@DrawerRef" @bind-SelectedItem="@SelectedItem"> <Content> <div class="main"> <div class="content px-4"> @Body </div> </div> </Content> </TelerikDrawer> </div> <style> html, body, app, .k-drawer-container, .k-drawer-content, .main { width: 100%; height: 100%; max-height: 100%; } /* vertical scroll should happen in the main portion of the content - where the Body is This keeps the header sticky at the top */ .main { overflow-y: auto; } /* horizontal scroll happens in the drawer content to keep the drawer on the left side of the screen */ .k-drawer-content { overflow-x: auto; } /* sizing of the header */ .top-row { left: 0; } /* sizing of the header */ .top-row { left: 0; } .drawer-container { width: 100%; height: 100%; } .k-icon { font-size: 20px; } .custom-toolbar { width: 100%; background-color: #f6f6f6; line-height: 10px; border-bottom: inset; border-bottom-width: 1px; padding: 3px 8px; color: #656565; } .title { margin-left: 20px; font-weight: bold; font-size: 17px; width: 100%; } </style> @code{ bool DrawerExpanded { get; set; }=true; DrawerItem SelectedItem { get; set; } TelerikDrawer<DrawerItem> DrawerRef { get; set; } // in this sample we hardcode the existing pages, in your case you can // create the list based on your business logic (e.g., based on user roles/access) List<DrawerItem> NavigablePages { get; set; }=new List<DrawerItem> { new DrawerItem {Text="Home", Url="/", Icon="home"}, new DrawerItem {IsSeparator=true, Url=string.Empty}, //define a URL to separators to make the pre-selection logic easier new DrawerItem {Text="Counter", Url="counter", Icon=IconName.Cart}, new DrawerItem {Text="FetchData", Url="fetchdata", Icon=IconName.Grid} }; protected override void OnInitialized() { // pre-select the page the user lands on // as the user clicks items, the DOM changes only in the Body and so the selected item stays active string currPage=NavigationManager.Uri; DrawerItem ActivePage=NavigablePages.Where(p=> p.Url.ToLowerInvariant()==GetCurrentPage().ToLowerInvariant()).FirstOrDefault(); if (ActivePage !=null) { SelectedItem=ActivePage; } base.OnInitialized(); } public string GetCurrentPage() { string uriWithoutQueryString=NavigationManager.Uri.Split("?")[0]; string currPage=uriWithoutQueryString.Substring(Math.Min(NavigationManager.Uri.Length, NavigationManager.BaseUri.Length)); return string.IsNullOrWhiteSpace(currPage) ? "/" : currPage; } // generally, this should go into its own file, but it is here to keep all the drawer-related code in one place public class DrawerItem { public string Text { get; set; } public string Url { get; set; } public string Icon { get; set; } public bool IsSeparator { get; set; } } }

### Response

**Marin Bratanov** answered on 22 Sep 2020

Hello David, If you want the hamburger icon inside the drawer, you may want to use the template as shown here: [https://github.com/telerik/blazor-ui/tree/master/drawer/template](https://github.com/telerik/blazor-ui/tree/master/drawer/template) In the provided snippet and screenshot, the header also takes up some height and that is added to the 100% of the main content, so the total height of the content becomes over 100% which causes the scrollbar. Regards, Marin Bratanov

### Response

**David Ocasio** answered on 22 Sep 2020

No I do not want the hamburger icon inside the drawer. Yes I agree the header is skewing the total height over 100% Any suggestions how to tackle the CSS to account for the header. What I have tried so far doesn't seem to work. Thanks DCO

### Response

**Marin Bratanov** answered on 22 Sep 2020

Hello David, You can consider using a calc() expression for the height of the content element so that you can subtract the height of the header. Regards, Marin Bratanov

### Response

**Leland** commented on 14 Sep 2023

calc() ended up resolving the issue for me, but it took a bit for me to get it set up correctly. For anyone else seeing this later, here is what I ended up using: :root { --appbarheight: 68px; /*change as needed*/ } /* explicitly setting the height of the appbar so that it can be subtracted from the drawer container height */.k-appbar-top { height: var (--appbarheight);
} /* the size of the containers will fill up their parents up to the viewport */ html, body, app,.k-drawer-container,.k-drawer-content,.main { width: 100%;
} html, body, app,.k-drawer-content,.main { height: 100%; max-height: 100%;
} /* the drawer container should fill the viewport minus the height of the appbar */.k-drawer-container { height: calc ( 100% - var (--appbarheight));
}

### Response

**Hristian Stefanov** commented on 19 Sep 2023

Hi Leland, Thank you for sharing your outcome so other developers can benefit from it. I'm glad to see you found a working solution for your scenario. Kind Regards, Hristian
