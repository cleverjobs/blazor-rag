# Grid Error after SelectedItemsChanged is fired

## Question

**Gra** asked on 03 Mar 2020

Hi, I am getting the following exception from the grid and cannot understand why. The collection supplied to the function is definitely not empty and my function exits without a throw. Is there a way to understand why the code inside the grid is throwing an error? Then the circuit crashes and the blazor application is now dead. If I use a GridCommandColumn no errors are raised. Unhandled exception rendering component: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index' )<br>System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index' )<br> at System.Collections.Generic.List`1.get_Item(Int32 index)<br> at Telerik.Blazor.Components.Grid.GridDataCellBase`1.get_Column()<br> at Telerik.Blazor.Components.Grid.GridContentCell`1.get_BoundColumn()<br> at Telerik.Blazor.Components.Grid.GridContentCell`1.OnClick()<br> at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)<br> at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)<br>fail: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[111]<br> Unhandled exception in circuit '-1BdfTDXKpRyAHNMXnaoanw8GipVDkrJ6NXuvg48GmA'.<br>System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index' )<br> at System.Collections.Generic.List`1.get_Item(Int32 index)<br> at Telerik.Blazor.Components.Grid.GridDataCellBase`1.get_Column()<br> at Telerik.Blazor.Components.Grid.GridContentCell`1.get_BoundColumn()<br> at Telerik.Blazor.Components.Grid.GridContentCell`1.OnClick()<br> at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)<br> at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

## Answer

**Marin Bratanov** answered on 04 Mar 2020

Hello Wayne, Could you try comparing with this sample to see what's the difference causing this: [https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event?](https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event?) The stack trace points to accessing the grid's Column collection, so if I have to guess, I'd say that there is something going wrong there - for example, the columns are built dynamically in a foreach loop and when the event happens, the grid has to repaint, but the data for the loop is changed or no longer there, which throws the error. If this does not help you resolve it, please post here a modified version of the snippet from the documentation that shows the error so I can take a look. Regards, Marin Bratanov

### Response

**Grant** answered on 05 Mar 2020

Hi Marin, I have refactored the application to use a ShellComponent that uses properties for the its children and I still get the error.The list is not destroyed when the component is "swapped" out as I have a persistent ViewModel for the ShellComponent. However, I do use RenderFragments and am wondering if I have stumbled on to a LifeCycle issue here. As long as I dont "navigate" for the RouterComponent everything works fine. But if I "navigate" to the required page,the error is triggered - so its something about destroying a component hosting the grid. Hope this example make sense and helps us identify just where the problem is: Issue with my understanding of RenderFragment Issue with the Grid on dispose inside a RenderFragment Template Issue with the way the Lifecycle events are called within this sample So inside my MVC page I use this to initialise the blazor app: <component type="typeof(ApplicationShell)" render-mode="ServerPrerendered" /> That application shell razor syntax looks like this: <TelerikRootComponent> <CrudComponentRouter> <SearchComponent> <PickupSequenceSearch HaveSearchData="@ViewModel.HaveSearchData" SearchResults="@ViewModel.SearchResults" PlanSelected="@OnPlanSelected" /> </SearchComponent> <EditComponent> <PickupSequenceEditShell /> </EditComponent> <DeleteComponent> </DeleteComponent> <CreateComponent> </CreateComponent> </CrudComponentRouter> </TelerikRootComponent> The CrudComponentRouter markup looks as such: @inject CrudComponentRouterService RouterService @switch (RouteState) { case RouterState.Search: @SearchComponent break; case RouterState.Create: @CreateComponent break; case RouterState.Delete: @DeleteComponent break; case RouterState.Edit: @EditComponent break; } @code { [Parameter] public RouterState RouteState { get; set; } [Parameter] public RenderFragment SearchComponent { get; set; } [Parameter] public RenderFragment EditComponent { get; set; } [Parameter] public RenderFragment DeleteComponent { get; set; } [Parameter] public RenderFragment CreateComponent { get; set; } protected override async Task OnInitializedAsync() { await base.OnInitializedAsync(); this.RouterService.RegisterRouter( this ); } public void Navigate(RouterState state) { this.RouteState=state; StateHasChanged(); } } My Search Component has this grid definition: <TelerikGrid Data="@SearchResults" FilterMode="@GridFilterMode.FilterMenu" SelectionMode="@GridSelectionMode.Single" Pageable="false" PageSize="10" SelectedItemsChanged="@((IEnumerable<SearchHarvestPlanPickupSequenceViewModel> lst)=> OnGridRowSelect(lst))"> <GridColumns> <GridColumn Field=@nameof(SearchHarvestPlanPickupSequenceViewModel.Name) Title="Name"></GridColumn> <GridColumn Field=@nameof(SearchHarvestPlanPickupSequenceViewModel.Version) Title="Version"></GridColumn> <GridColumn Field=@nameof(SearchHarvestPlanPickupSequenceViewModel.TotalHoldover) Title="Holdover"> <Template> @{ var totalHoldover=(context as SearchHarvestPlanPickupSequenceViewModel).TotalHoldover; <NumberDisplay T="long" Number="@totalHoldover" /> } </Template> </GridColumn> <GridColumn Field=@nameof(SearchHarvestPlanPickupSequenceViewModel.TotalHarvesting) Title="Harvesting"> <Template> @{ var totalHarvesting=(context as SearchHarvestPlanPickupSequenceViewModel).TotalHarvesting; <NumberDisplay T="long" Number="@totalHarvesting" /> } </Template> </GridColumn> </GridColumns> </TelerikGrid> And just for completeness the NumberDisplay component is just dumb: @typeparam T <span>@string.Format( "{0:n0}", Number)</span> @code { [Parameter] public T Number { get; set; } }

### Response

**Marin Bratanov** answered on 05 Mar 2020

Hi Wayne, I am attaching here two samples I built on top of this code - one is a real server-side blazor app, the other uses the same razor components in an MVC view. Both seem to work fine for me and I suggest you try comparing against them to see what is the difference causing trouble. If this does not help you resolve this, please modify either of them to showcase the issue so I can review it too. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 05 Mar 2020

Hello again Wayne, We had another report that the same error was caused by hiding the grid from within its SelectedItemsChanged handler, you can see if this is your case here: [https://feedback.telerik.com/blazor/1456628-system-argumentoutofrangeexception-index-was-out-of-range-when-hiding-a-grid-from-its-selecteditemschanged-handler](https://feedback.telerik.com/blazor/1456628-system-argumentoutofrangeexception-index-was-out-of-range-when-hiding-a-grid-from-its-selecteditemschanged-handler) Regards, Marin Bratanov

### Response

**Grant** answered on 06 Mar 2020

Hi Marin, Was about to test this but yes, technically my code will hide the grid on the GridRowSelect callback. The reason mine hides is the switch() in my router component. So I would have to agree my issue is exactly the same problem, albeit, triggered a different way. I just removed the switch statement in my router (matching your example code) and can verify that the problem has gone away. So the two issues can be merged as they are the same problem.

### Response

**Marin Bratanov** answered on 06 Mar 2020

Hi Wayne, Thank you for confirming this. Indeed, it should be the same problem - the stack trace is the same, and the scenario boils down to the same issue. Regards, Marin Bratanov
