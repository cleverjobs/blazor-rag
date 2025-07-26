# TelerikGrid with popup TelerikContextMenu very slow to popup and show menu items on certain nested components.

## Question

**Adr** asked on 22 Jun 2021

I have a TelerikGrid inside of a Blazor component (this blazor component sits within a Telerik tab control which in turn sits on a Blazor page). The last column in the grid is a button that pops up a context menu for that selected row. The context menu code in the component looks like this: <TelerikContextMenu @ref="@ContextMenuRef" Data="@MenuItems" OnClick="@((TelerikGridContextMenuItem item)=> OnContextMenuItemClick(item))"> </TelerikContextMenu> The code for the last grid column looks like this: <GridColumn Width="60px" Filterable="false" Groupable="false" Reorderable="false" Locked="true"> <Template> <span @onclick:stopPropagation="true"> <TelerikButton Primary="true" OnClick="@((MouseEventArgs e)=> ShowContextMenuOptionsForRow(e, context as TyreCatalogueInfo))" Icon="more-vertical"> </TelerikButton> </span> </Template> </GridColumn> The MenuItems for the context menu are set in the OnInitializedAsync method for the component like this: protected override async Task OnInitializedAsync ( ) { if (IsEnvironmentSet())
{
MenuItems=new List<TelerikGridContextMenuItem>
{ new () {Text="Edit Tyre", Icon="edit", Action=EditSelectedTyre}
}; await base.OnInitializedAsync();
}
} When any of the buttons in the last grid column are clicked this invokes the ShowContextMenuOptionsForRow which is on a base class which the Blazor component inherits from. The code for that looks like this: protected async Task ShowContextMenuOptionsForRow ( MouseEventArgs e, TRowInfoType row ) {
SelectedRowInfo=row; await ContextMenuRef.ShowAsync(e.ClientX, e.ClientY);
} If I stick a breakpoint on the first line SelectedRowInfo=row; within the ShowContextMenuOptionsForRow method it pretty much immediately hits. If I then hit F5 to continue it takes a further x seconds for the popup menu to appear. I'm not sure where the time is being spent/lost. See supporting video which demonstrates the slowness. [https://drive.google.com/file/d/1My5gpDx9qPRi2Fz4tpab7LEWGQZDG3eY/view](https://drive.google.com/file/d/1My5gpDx9qPRi2Fz4tpab7LEWGQZDG3eY/view) I have used this same pattern for other pages (pages that have the grid directly on it, with no other child Blazor components involved) and the speed of the popup is instantaneous. UPDATE The slow performance seems to be linked to the Blazor ShouldRender property which is defaulted to true in the Blazor framework. If I override the ShouldRender property by setting private member field _shouldRender to false when the context menu is invoked by the user, then it appears on screen instantly. I can reset the private member field _shouldRender back to true when the user click on one of the context menu items. The issue I have is that once the context menu is invoked by the user they could click anywhere else on the page to dismiss the context menu and that would leave the private member field _shouldRender as false and have a negative effect on other interactions that need the ShouldRender property to return true. The code I originally posted I have updated as follows: private bool _shouldRender=true; protected override bool ShouldRender ( ) { return _shouldRender;
} protected async Task ShowContextMenuOptionsForRow ( MouseEventArgs e, TRowInfoType row ) {
_shouldRender=false;

SelectedRowInfo=row; await ContextMenuRef.ShowAsync(e.ClientX, e.ClientY);
} protected async Task OnContextMenuItemClick ( TelerikGridContextMenuItem item ) {
_shouldRender=true; if (item.Action !=null )
{ await InvokeAsync(item.Action);
}
}

## Answer

**Nadezhda Tacheva** answered on 25 Jun 2021

Hello Adrian , I used the provided code blocks to reproduce a scenario that matches yours as close as possible. I tested with both Blazor Server-side and Blazor WASM projects and the outcome is as follows: In Blazor Server-side I did not experience any delay. The context menu opens right after the click of the button In the Blazor WASM application I did notice a slight delay between clicking the button and opening the context menu. This is expected having in mind that generally Blazor WASM works slower compared to Blazor Server-side. However, the delay I experienced looks significantly less than the one visible on the video you sent (you can check the attached video of the result I am getting). In order to isolate the problem I am attaching both of the projects that I used for testing, so you can test them as well for whichever Blazor type you are using for your application. In case the project works as expected on your side, too and you don't experience such a delay, could you modify it to try reproducing the delay you are hitting in your application? Thus, we will be able to investigate further and provide some more insights. In regards to the update you provided, indeed this is the way Blazor framework works. However, overriding the ShouldRender might be a bit tricky. We are handling this internally for the components. When you set it to false, you will be blocking the rendering of the whole page an thus any changes whilst it is false will not be visible in the viewport. As it is very likely a user to close the context menu without clicking on an item in it, changing the ShouldRender value to true in the OnContextMenuItemClick may not even get triggered and thus ShouldRender will remain false as you have correctly stated. Another approach you may try is setting it to true in the ShowContextMenuOptionsForRow right after the ShowAsync of the context menu. I have included that in the sample projects, it is currently commented out. Uncomment it in order to test it yourself and see if it delivers the desired result. I will be looking forward to receiving your feedback after testing! Regards, Nadezhda Tacheva Progress Telerik

### Response

**Adrian** answered on 28 Jun 2021

I have updated your sample to better show how we are using the grid and context menus. The updated sample has 3 scenarios A grid of 1000 rows with no paging A grid with 1000 records paged with 100 rows per page (the grid column definitions are defined in the same component) A grid with 1000 records paged with 100 rows per page (the grid column definitions are defined in a separate generic component) All 3 scenarios seems to have a slow context menu.

### Response

**Nadezhda Tacheva** answered on 01 Jul 2021

Hi Adrian, Thank you for being able to reproduce and send us the sample application with the behavior you are experiencing! Indeed, the Context menu is displayed with a couple of seconds delay in your scenario. However, the reason behind this is not in the Context menu but in the Grid setup itself. Having in mind the Blazor WASM rendering performance at this stage of the framework development, we should consider that it is still substantially slower than a Blazor Server-side application. In addition, since the Grid operates with such a massive data source loaded all at once, that will also affect the rendering performance of the application. As Blazor WASM applications operate in one thread, if you have a task that takes longer to be executed it actually blocks the other actions while it is completed. Thus comes the delay in the Context menu opening - once you click the button to open it, the Grid re-renders and as this process is slow it also visibly affects the Context menu opening. With that being said, I would suggest taking some steps towards optimizing the Grid performance as a start. Context menu will inevitably benefit from that. This article proposes a couple of approaches for a better rendering performance that you may try. In general, a good practice is to avoid loading all the data at once, you will achieve better performance if you only load and render relevant portions. You can enable either the Paging or Virtual Scrolling of the Grid. In case you choose to proceed with Paging, we recommend using a reasonable page size (for example, 10 to 20 or 40, as more than 20 items can rarely fit on a screen anyway). 100 items per page may also take longer to load. Another optimization you can also try is changing the ShowContextMenuOptionsForRow in ListEntityBase.cs and ContextMenuClick in ListVehicleBase.cs to void instead of async Task. Asynchronous operations introduce more re-rendering in WASM and that also affects the application performance. We've tested this approach as well as loading less elements on the page and the outcome is Context menu opening right away. //ListEntityBase.cs row 59: protected void ShowContextMenuOptionsForRow ( MouseEventArgs e, TRowInfoType row ) {
SelectedRowInfo=row;

ContextMenuRef.ShowAsync(e.ClientX, e.ClientY);
} //ListVehiclesBase.cs row 45: protected void ContextMenuClick ( (MouseEventArgs MouseEventArgs, TRowInfoType ContextRow ) args) {
ShowContextMenuOptionsForRow(args.MouseEventArgs, args.ContextRow);
} I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Regards, Nadezhda Tacheva Progress Telerik
