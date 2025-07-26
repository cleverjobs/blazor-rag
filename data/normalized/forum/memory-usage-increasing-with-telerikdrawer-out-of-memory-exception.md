# Memory usage increasing with TelerikDrawer (Out of Memory exception)

## Question

**Nic** asked on 10 May 2021

I have a Right Drawer containing a nested Left Drawer. In the OnInitializedAsync, i have a loop doing nothing: this loop increases my RAM usage until my application crashes with "Out of memory", like there was a memory leak. If i remove the nested Left Drawer, memory usage doesn't increase anymore. I've made the loop part just to simulate the "Out of memory" we get in the real application, when we have to handle a lot of SignalR events. <TelerikDrawer @ref="RightDrawer" Class="right-drawer" Data="RightMenuItems" Mode="DrawerMode.Overlay" Position="DrawerPosition.Right" @bind-Expanded="IsRightMenuExpanded"> <Template> <div class="k-drawer-items"> <ul> @foreach (var item in RightMenuItems)
{ <li @onclick:stopPropagation @onclick="(()=> RightMenuItemClick(item))" class="k-drawer-item @GetSelectedRightMenuItemCssClass(item)" style="height: 40px; vertical-align: middle; padding-top: 0; padding-bottom: 0; white-space: nowrap"> <div> <span class="@item.IconClass" style="vertical-align:middle;"> </span> <span class="k-item-text" style="vertical-align:middle;"> @item.Text </span> @if (RightDrawer.Expanded && item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-down" style="position:absolute; right:0; line-height:inherit; margin:0 8px; vertical-align:middle;"> </span> }
else if (RightDrawer.Expanded && !item.Expanded && (item.Children?.Any() ?? false))
{ <span class="k-icon k-i-arrow-chevron-right" style="position:absolute; right:0; line-height:inherit; margin:0 8px; vertical-align:middle;"> </span> } </div> </li> } </ul> </div> </Template> <Content> <!-- The nested drawer is the Push drawer - the CSS rule above reduces its z-index so it does not show up above the overlay of the other --> <TelerikDrawer Class="left-drawer" Data="LeftMenuItems" Mode="DrawerMode.Push"> <Content> <div id="main-layout-content"> @Body </div> </Content> </TelerikDrawer> </Content> </TelerikDrawer> This is the OnInitializedAsync: protected override async Task OnInitializedAsync ( ) {
StateHasChanged();

Text="Start"; await Task.Delay( 1000 ); for ( int i=0; i <10000000; i++)
{ await Task.Delay( 1 );
} await Task.Delay( 1000 );
Text="End";

}

## Answer

**Marin Bratanov** answered on 10 May 2021

Hello Nicola, This looks like a problem with this setup - the delay in this event alone is over two hours for each OnInitialized call (if you have server pre-rendering, that's two calls). Such code will definitely break the app. That said, I did a few tests and even though the performance monitor glitched a few times - there was no memory consumption or leak that I can see with or without the drawer. I am attaching here the scenario which I used for the video recording (also attached) so you can see if I am missing something. If there is a Telerik component problem with memory leaks, please showcase it in a valid and meanigful scenario. In the meantime, I would encourage you to consider the following: perform such slow operations in events like OnAfterRenderAsync so they fire only once and so they don't automatically try to re-render the component tree consider optimizing the workflow of the app - thousands of half-open connections will weigh down the app, and are likely to weight down the server even more since it will have to handle many clients that keep such connections extract them in properly cancellable methods like shown in the Cancellable Background Work section of the MSDN docs: [https://docs.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-5.0#cancelable-background-work](https://docs.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-5.0#cancelable-background-work) Regards, Marin Bratanov Progress Telerik
