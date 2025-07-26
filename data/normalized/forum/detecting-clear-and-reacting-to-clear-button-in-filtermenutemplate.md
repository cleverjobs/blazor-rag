# Detecting Clear and reacting to Clear Button in FilterMenuTemplate

## Question

**Tim** asked on 29 May 2021

I am trying to do a custom filter as FilterMenuTemplate in a Grid. Filtering works fine. When I attempt to "unfilter", I get lost in how to detect and handle it. I have two different styles of handing the filtering in the below, yet neither can I get to work. How do I have FilterMenuTemplate with a dropdown (custom) and detect the user clicking the "Clear" button? <TelerikGrid Data="@_vehicleParts" Pageable="true" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Resizable="true" Reorderable="true" PageSize="20" Navigable="true" OnRead=@OnVehiclePartsRead TotalCount="@TotalCount"> <GridColumns> <GridColumn Width="10%" Field="@nameof(VehiclePartModel.YearId)"> </GridColumn> <GridColumn Width="10%" Field="@nameof(VehiclePartModel.BrandModelName)"> <FilterMenuTemplate Context="brandModelNameFilterContext"> <TelerikDropDownList Data="@_brandModels" TextField="@nameof(BrandModel.Name)" ValueField="@nameof(BrandModel.Id)" @bind-Value="@BrandModelIdFilter" /> </FilterMenuTemplate> </GridColumn> <GridColumn Width="10%" Field="@nameof(VehiclePartModel.MakeName)"> <FilterMenuTemplate Context="makeNameFilterContext"> @{ this._makeNameFilterContext=makeNameFilterContext;} <TelerikDropDownList Data="@_makes" TextField="@nameof(Make.Name)" Value="@MakeIdFilter" ValueField="@nameof(Make.Id)" ValueChanged="@((int value)=> ColumnValueChanged(value, nameof(VehiclePartModel.MakeName), makeNameFilterContext.FilterDescriptor))" /> </FilterMenuTemplate> </GridColumn>

## Answer

**Svetoslav Dimitrov** answered on 01 Jun 2021

Hi Timothy, The grid always has a filter descriptor for the Field of the given column. This means that the StateChanged event will fire when the state of the grid changes, and you can hook to that event to know what happened. You can read more about this in the Grid State article (the particular example is in the "Get and Override User Action That Changes The Grid" section but I recommend you review the whole article, it opens up a lot of possibilities): [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) See also the "Set Grid Options Through State" section and the second snippet on working with filters to see more details on how there is always a default filter. For getting a cleared filter - checking if the filter descriptors for the given field contain information will let you know if it is now gone. You can also store a previous grid state to compare against if this is important to you. I also advise you take a peek at this article on using the FilterMenuTemplate because there is a bit more code involved in creating a custom menu than what I see in the first template in the provided snippet: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-menu-template.](https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-menu-template.) Regards, Svetoslav Dimitrov

### Response

**Timothy J** answered on 03 Jun 2021

In the example for "Get and Override User Action That Changes The Grid", the line below seems suspicious. args.GridState.FilterDescriptors is a collection of FilterDescriptorBase, not FilterDescriptor as cast below: foreach (FilterDescriptor item in args.GridState.FilterDescriptors) I cannot enumerate as FilterDescriptor Please advise.

### Response

**Svetoslav Dimitrov** answered on 07 Jun 2021

Hello Timothy, Let me first offer a summary of the issue: You are unable to use a syntax similar to FilterDescriptor currentItem=args.GridState.FilterDescriptors[i], where "i" comes from a for loop. The issue stems from the ICollection that is the collection holding the FilterDescriptors. It is an enumerable collection, but not indexable. In order to take an indexed item you can use the collection.ElementAt() method. The FilterDescriptor class inherits the FilterDescriptorBase and thus you can cast it. Below, I have added a code snippet that showcases that: @using Telerik.DataSource

<TelerikGrid Data="@MyData" Sortable="true" FilterMode="@GridFilterMode.FilterRow" AutoGenerateColumns="true" Pageable="true" OnStateChanged="@((GridStateEventArgs<SampleData> args)=> OnStateChangedHandler(args))" @ref="GridRef">
</TelerikGrid>

@code {
TelerikGrid<SampleData> GridRef { get; set; } async void OnStateChangedHandler ( GridStateEventArgs<SampleData> args ) {
Console.WriteLine(args.PropertyName); // get the setting that was just changed (paging, sorting,...) if (args.PropertyName=="FilterDescriptors" ) // sorting changed for our example { // ensure certain state based on some condition // in this example - ensure that the ID field is always filtered with a certain setting unless the user filters it explicitly bool isIdFiltered=false; for ( int i=0; i <args.GridState.FilterDescriptors.Count; i++)
{ FilterDescriptor currentItem=(FilterDescriptor)args.GridState.FilterDescriptors.ElementAt(i); if (currentItem.Member=="Id" )
{
isIdFiltered=true;
} // you could override a user action as well - change settings on the corresponding parameter // make sure that the .SetState() method of the grid is always called if you do that if (currentItem.Member=="Name" )
{
currentItem.Value="name 1";
currentItem.Operator=FilterOperator.Contains;
}
} if (!isIdFiltered)
{
args.GridState.FilterDescriptors.Add( new FilterDescriptor
{
Member="Id",
MemberType=typeof ( int ),
Operator=FilterOperator.IsLessThan,
Value=15 });
} // needed only if you will be overriding user actions or amending them // if you only need to be notified of changes, you should not call this method await GridRef.SetState(args.GridState);
}
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 300 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
}); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Svetoslav Dimitrov
