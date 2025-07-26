# Drawer as nav bar with URL parameters

## Question

**Dou** asked on 26 May 2021

Hello, I'm using the Drawer component as a nav bar based on your example in github and it works great except for one thing. One of my pages (components) can accept optional URL parameters, i.e. it has two @page directives. If I supply the URL parameters in the address bar I get an object reference error. I tried adding the parameters to the URL when building the DrawerItem the same way they are in the @page directive but that doesn't work. Can you please show me how to make this work? Thank you.

### Response

**Matthias** commented on 27 May 2021

I use the Drawer in the exact way. My solution is simple: Drawer-Class: public class DrawerItem { public string Text { get; set; } public string Icon { get; set; } public bool Expanded { get; set; } public int Level { get; set; } public string Description { get; set; } public bool OpenPage { get; set; } public string PageUrl { get; set; } public bool IsSeparator { get; set; }=false; public IEnumerable<DrawerItem> Children { get; set; } } component with the drawer; foreach (var item in Mandants) { DrawerList.Add(new DrawerItem {Text=item.Bezeichnung, Icon="user", Level=1, Description=".", OpenPage=true, PageUrl=$"KundenPG/{item.MandantId}"}); } the page itself has also two parameters: @page "/KundenPG" @page "/KundenPG/{paramMandant}" this works perfect in my scenario regards Matthias

### Response

**Doug** commented on 27 May 2021

Thanks for the response, that helps but I have a couple follow up questions: I assume you still have to declare a parameter for paramMandant in the code section of your page, correct? And how does that value get assigned to item.MandantId?

### Response

**Matthias** commented on 27 May 2021

Yes you need the parameter in the code-section: [Parameter] public string paramMandant { get; set; } with „how does that value get assigned...“ you ask about the value of item.MandantID? This is a list (generated via an API) As soon as you assigned the value in $"KundenPG/{item.MandantId}"}); And item.MandantID is 5, the parameter will be: KundenPG/5 And you can get the value in your Page (in my example KundenPG)

### Response

**Doug** commented on 27 May 2021

Thanks for the quick reply. I wonder if we're doing something a little different here. I'm not going to have drawer items for every parameter option that could be sent in. My site can be linked to from another site and that site will send the parameters in via url parameters and I need to link straight to that page without the user clicking on a drawer item. If the user were to simply click the drawer item then I would set up the page in a default way, but if I get parameters in the URL then I need to set it up based on the parameters, effectively bypassing the drawer. However I would need the drawer to understand which page is displayed so it would be highlighted in the drawer. As of now if I send in the parameters I just get a null reference exception and the page won't display.

### Response

**Matthias** commented on 27 May 2021

Ok Have a look at the example from Telerik [https://github.com/telerik/blazor-ui/blob/master/drawer/sidenav/Shared/MainLayout.razor](https://github.com/telerik/blazor-ui/blob/master/drawer/sidenav/Shared/MainLayout.razor) You may need to parse the url in GetCurrentPage() and decide which page and Drawer Item is active including the parameters But I think this is not a Telerik topic

### Response

**Doug** commented on 27 May 2021

That's what I based my drawer off of but even outside of selecting the current page in the drawer (I might even be able to live without that), when I send it URL parameters the site bombs out with the null reference exception and I'm not sure how to get past that. From the console: System.NullReferenceException: Object reference not set to an instance of an object. at VeritivLogistics.Web.Shared.MainLayout.<BuildRenderTree>b__0_5(RenderTreeBuilder __builder6) at Telerik.Blazor.Components.TelerikRootComponent.<BuildRenderTree>b__26_0(RenderTreeBuilder __builder2) at Microsoft.AspNetCore.Components.CascadingValue`1.Render(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()

### Response

**Doug** commented on 27 May 2021

You rock Matthias! Your mention of GetCurrentPage() set me on the right path. I had to split off the route parameters before returning the URL. That made the active page non-null which avoids the null reference exception and now my page loads correctly whether I give it parameters in the URL or if the user clicks the drawer item. Thanks so much!

### Response

**Matthias** commented on 27 May 2021

That’s great! Thanks for your reply and nice to hear, that it works
