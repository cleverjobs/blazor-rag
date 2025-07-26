# Set selected grid row/item after a Filter event is triggered?

## Question

**RobRob** asked on 30 Jun 2025

Problem: User filters a grid but there is no "selected" row/item when filter returns results to the grid. I'd like to set the selected item for a grid that supports: SelectionMode="GridSelectionMode.Single"

SelectedItems="@_selectedBookings" I'm not sure what event I need to respond to, there doesn't appear to be a "Filter" button click event so I'm guessing I need to work with the Grid events like, OnUpdate or OnStateChanged? Idea is to force first row to be selected from the Filter return set (which could be 0, 1, or many): private void OnBookingGridUpdate ( GridCommandEventArgs args ) { if (_bookingList.Any())
{ var updatedItem=(BookingModel)args.Item;
_selectedBookings.Clear();
_selectedBookings.Add(updatedItem);
}
} Thoughts?

## Answer

**Dimo** answered on 01 Jul 2025

Hi Rob, Depending on the desired behavior, you need the Grid OnRead or OnStateChanged events, or both. The OnRead event allows you to easily find the first rendered Grid row in the UI. You can also check if any of the current data items belongs to the current SelectedItems collection. Be aware of the potential need to override the Equals () method of Grid model class to do that. The OnStateChanged event allows you to track the Grid filtering state. I am not sure why do you mention the OnUpdate event - it's related to editing, not filtering. Regards, Dimo Progress Telerik

### Response

**Rob** commented on 01 Jul 2025

I had tried the OnRead per your documentation and that resulted in nothing being displayed in the grid and ToDataSourceResult was null (even though I know there were results). The OnStateChanged looked like it had promise as it does fire after I click on "Filter" for a column, but I couldn't figure out how to get the filtered results let alone set selectedItem so that a row highlights and triggers other related grid updates. The OnUpdate was from your sample code you linked for OnStateChanged here. But I agree, shouldn't be relevant but was trying to extrapolate from your sample code. Basically I have the same question as this user here, but for Blazor-Server .NET 9 The OnRead doesn't seem like the correct event either ... I'm not interested in population of the grid only after the grid is populated. All I want to do is set the selectedItem (so I get a highlighted row) after the filter completes ... a task I assumed would be super simple, but once again seems to have A LOT of coding overhead and still no solution. Surely there must be an easy solution to this? Rob.

### Response

**Dimo** commented on 02 Jul 2025

>> I had tried the OnRead per your documentation and that resulted in nothing being displayed in the grid If DataSourceResult.Data is empty and DataSourceResult.Total is 0, this means that the request arguments in args.Request do not match any items in the data.>> The OnStateChanged looked like it had promise as it does fire after I click on "Filter" for a column, but I couldn't figure out how to get the filtered results let alone set selectedItem so that a row highlights The purpose of the Grid OnStateChanged event is to provide information about the latest Grid state configuration. This event is not supposed to provide access to the current Grid data, but the event can help you obtain it if necessary. Moreover, OnStateChanged fires before the Grid rebinds, so the event can't know what the new data (e.g. after filtering) will be.>> The OnRead doesn't seem like the correct event either The OnRead event allows you to obtain the current page of data items in the Grid. This is the easiest way to find out which is the first data row the Grid component will render. Please review this REPL page: [https://blazorrepl.telerik.com/mTOVOlOT57RRkIze23](https://blazorrepl.telerik.com/mTOVOlOT57RRkIze23) It shows how to select the first row after filtering, if there are no other visible selected rows. The logic is inside the OnRead handler: private async Task OnGridRead ( GridReadEventArgs args ) {
DataSourceResult result=await GridData.ToDataSourceResultAsync(args.Request);

args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults; var gridSelectedItemsList=GridSelectedItems as List<Product>; var argsDataList=args.Data.Cast<Product>().ToList(); if (args.Request.Filters.Count> 0 && args.Total> 0 && !argsDataList.Any(x=> gridSelectedItemsList!.Contains(x))) {
GridSelectedItems=new List<Product>() { argsDataList.First() };
}
}

### Response

**Rob** commented on 02 Jul 2025

I must not be communicating well as to what I'm trying to accomplish. 1. Trigger to set the first row as "selectedItem" from when a user clicks on the Filter button from a column: On page init the populated Grid and notice first row is selected (highlight blue): User clicks on Customer Filter icon and enters value "ONE" and clicks on the F ilter button: The grid is now filtered but the first row is NOT selected... this is what I need to do, select the first row (if present) after the filter button is clicked: What I would LIKE to do after the filter is this: The first row is selected. BUT, I can't find a relatively painless way (or any method) to do this. If I implement the OnGridRead per what you outlined and linked to, the OnGridRead is immediately triggered whether or not a filter has been defined and will create a null exception. In your sample you don't define the Data? I'm NOT trying to populate a separate grid with selectedItems, I set one and ONLY one selectedItem. Here is what I'm working with where Data is populated in "OnAfterRenderAsync" method (if firstRender). <TelerikGrid Data="@_bookingList" TItem="@BookingModel" @ref="@BookingGridRef" Height="calc(34vh - 10rem)" Resizable="false" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" SelectionMode="GridSelectionMode.Single" SelectedItems="@_selectedBookings" OnRowClick="@OnBookingRowClick" OnRowDoubleClick="@OnBookingRowDoubleClick" OnRead="@OnBookingGridRead" Sortable="true" Reorderable="true" Pageable="true" PageSize="25"> and in my event handler similar to what you described which doesn't make sense to me and I don't see how it would work? private async Task OnBookingGridRead ( GridReadEventArgs args ) { if (_bookingList !=null )
{
DataSourceResult result=await _bookingList.ToDataSourceResultAsync(args.Request);
args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults; var gridSelectedItemsList=_selectedBookings as List<BookingModel>; var argsDataList=args.Data.Cast<BookingModel>().ToList(); if (args.Request.Filters.Count> 0 && args.Total> 0 && !argsDataList.Any(x=> gridSelectedItemsList!.Contains(x)))
{
_selectedBookings.Clear();

_selectedBookings=new List<BookingModel>() { argsDataList.First() };
}
}
} This results in an empty grid because the bound _bookingList is null at the time the OnGridRead is triggered. I hope this is more clear? Rob.

### Response

**Rob** commented on 02 Jul 2025

In addition, it looks like your sample code here is not correct. // always use async Task, and not async void private async Task OnGridRead ( GridReadEventArgs args ) { var result=GridData.ToDataSourceResult(args.Request);
args.Data=result.Data;
args.Total=result.Total; var now=DateTime.Now;
LastOnRead=now.ToLongTimeString() + "." + now.Millisecond;
} this should be result. Result.Data (at least that's how it is on my version of Telerik 9): // always use async Task, and not async void private async Task OnGridRead ( GridReadEventArgs args ) { var result=GridData.ToDataSourceResult(args.Request);
args.Data=result.Result.Data;
args.Total=result.Result.Total; var now=DateTime.Now;
LastOnRead=now.ToLongTimeString() + "." + now.Millisecond;
} After removing the reference below from my Grid definition: Data="@_bookingList" IMPORTANT: I discovered the OnRead is executed BEFORE my _bookingList is populated from protected override async Task OnAfterRenderAsync(bool firstRender)... so it seems OnRead REQUIRES using protected override async Task OnInitializedAsync() which is going to cause a lot of other issues for me. This is slowly turning into a nightmare of code changes for what I expected to be the most simple of tasks " Just set the selectedItem to first row in the grid after a filter is executed ". My expectation was just one or two additional lines of code and not a complete reconstruction of how to work population of my grid and related event processing. Rob.

### Response

**Dimo** commented on 03 Jul 2025

Rob - Based on my understanding, the provided REPL page should do what you need - namely, "just set the selected item to the first row in the Grid after a filter is executed". What I have done additionally is to select the first row after filtering only if there is no other selected row. This logic can easily be removed if necessary. Here are a few additional comments:>> If I implement the OnGridRead per what you outlined and linked to, the OnGridRead is immediately triggered whether or not a filter has been defined and will create a null exception. Yes, OnRead fires every time the Grid needs data. However, you can easily detect if: This is the first time OnRead fires (add some counter). There is filtering applied (check args.Request.Filters ).>> In your sample you don't define the Data? Data and OnRead must not be used at the same time.>> In addition, it looks like your sample code here is not correct. this should be result.Result.Data No, that's not true. ToDataSourceResult() returns a DataSourceResult object, which has no "Result" property. If you try to use result.Result.Data in this example, you will get an error.>> OnRead is executed BEFORE my _bookingList is populated from protected override async Task OnAfterRenderAsync(bool firstRender) Yes, that is expected. If you are getting the Grid data after the first OnRead call, then you can: Render (create) the Grid after its Data becomes available. Request the data earlier, in OnInitializedAsync (). Do not request the Grid data separately and simply move the relevant code to the OnRead handler. Set empty args.Data and zero args.Total in the first OnRead call. Then, when the Grid data is available, execute BookingGridRef.Rebind()

### Response

**Rob** commented on 03 Jul 2025

Dimo,>> No, that's not true. ToDataSourceResult() returns a DataSourceResult object, which has no "Result" property. If you try to use result.Result.Data in this example, you will get an error. Yes, BUT I was using ToDataSourceResultAsync() because in your example code you use Async Task (see below): Anyway, I moved my code to OnInitializedAsync() and as soon as the OnRead is triggered when I get to BookingGridRef.Rebind() it triggers a null exception. The _bookingList never gets populated with data and YES it should be populated with data as I know the query works and has worked prior to trying this rather convoluded approach to just simply setting the selectedRow. protected override async Task OnInitializedAsync () { if (MenuService.IsEnabled( "/booking/profile" ))
{ if (_renderCounter==0 )
{
_loadingMessage=(SearchBookingNumber !=null ) ? "Please wait, searching...": "Please wait, loading...";
_isLoading=true;
StateHasChanged(); // RunTimer(); var authState=await AuthenticationStateProvider.GetAuthenticationStateAsync(); var user=authState.User;
_username=ClaimsHelper.GetPreferredName(user); // Determine processing base date _baseDate=await ProcessingService.GetMostRecentActivityDate(Configuration); // Default range _startDate=_baseDate.AddMonths( -12 );
_endDate=_baseDate.AddMonths( 6 ); if (SearchBookingNumber !=null )
{
_startDate=_baseDate.AddYears( -20 );
_endDate=_baseDate.AddYears( 3 );
} // Get the Bookings (THIS TRIGGERS the OnRead) _bookingList=await bookingService.GetByDate(_startDate, _endDate, SearchBookingNumber); // Populate Dropdown Lists for Equipment (Equipment Request Types, Equipment Class) _equipmentTypeList=await equipmentTypeService.Get(includeInactive: true );
_equipmentSubclassList=await equipmentSubclassService.Get(includeInactive: true );
_temperatureTypeList=await temperatureTypeService.GetAll(); // Populate Dropdown Lists for Commodities _CommodityList=await commodityTypeService.Get(includeInactive: false );
_WeightMeasureTypeList=await weightTypeService.GetBivalentList();
_PackageTypeList=await packageTypeService.GetBivalentList(); // Default to the first Booking if one exists if (_bookingList !=null )
{
_isEquipmentProcessingEnabled=(_bookingList.Count> 0 ); if (_bookingList.Count> 0 )
{
_selectedBookings.Add(_bookingList[ 0 ]);
_selectedBooking=_bookingList[ 0 ]; // OnRowClick is not triggered so need to do an update await BookingRefresh(_bookingList[ 0 ]);
}
}

_isLoading=false;
_loadingMessage="";
StateHasChanged();

}
}
} this statement triggers the OnRead _bookingList=await bookingService.GetByDate(_startDate, _endDate, SearchBookingNumber); the OnRead private async Task OnBookingGridRead(GridReadEventArgs args)
{

var result=_bookingList.ToDataSourceResultAsync(args.Request);
args.Data=result.Result.Data;
args.Total=result.Result.Total;
args.AggregateResults=result.Result.AggregateResults;

BookingGridRef.Rebind();

if (_bookingList.Count> 0)
{
_selectedBookings.Clear();
_selectedBookings.Add(_bookingList[0]);
_selectedBooking=_bookingList[0];
}

} The grid definition: <TelerikGrid TItem="@BookingModel" @ref="@BookingGridRef" Height="225px" Resizable="false" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" SelectionMode="GridSelectionMode.Single" SelectedItems="@_selectedBookings" OnRowClick="@OnBookingRowClick" OnRowDoubleClick="@OnBookingRowDoubleClick" OnRead="@OnBookingGridRead" Sortable="true" Reorderable="true" Pageable="true" PageSize="25"> It's NOT working as described unless you are suggesting I shouldn't use Async? Sorry if I sound frustrated, but all I'm trying to achieve is to set the first row after a filter as the "selectedItem" ... I honestly can't believe it's it requires significant changes? We buy these controls to reduce our workload, NOT increase it. If it really requires this much work (and so far I can't get it to work) to accomplish such a simple task, then I'd recommend Telerik provide a Grid attribute like "AutoSelectFirstRow"=true/false. Rob.

### Response

**Rob** commented on 03 Jul 2025

I moved my data reading code into OnRead: private async Task OnBookingGridRead ( GridReadEventArgs args ) { if (_renderCounter==0 )
{ // Get booking data from DB _bookingList=await bookingService.GetByDate(_startDate, _endDate, SearchBookingNumber); // Populate Dropdown Lists for Equipment (Equipment Request Types, Equipment Class) _equipmentTypeList=await equipmentTypeService.Get(includeInactive: true );
_equipmentSubclassList=await equipmentSubclassService.Get(includeInactive: true );
_temperatureTypeList=await temperatureTypeService.GetAll(); // Populate Dropdown Lists for Commodities _CommodityList=await commodityTypeService.Get(includeInactive: false );
_WeightMeasureTypeList=await weightTypeService.GetBivalentList();
_PackageTypeList=await packageTypeService.GetBivalentList(); if (_bookingList.Count> 0 )
{
_selectedBookings.Clear();
_selectedBookings.Add(_bookingList[ 0 ]);
_selectedBooking=_bookingList[ 0 ];
}

} var result=_bookingList.ToDataSourceResultAsync(args.Request);
args.Data=result.Result.Data;
args.Total=result.Result.Total; // Have to convert IEnumerable to List in order to get based on Index var argsDataList=args.Data.Cast<BookingModel>().ToList(); if (args.Request.Filters.Count> 0 )
{ if (args.Total> 0 )
{
_selectedBookings.Clear();
_selectedBookings.Add(argsDataList[ 0 ]);
_selectedBooking=argsDataList[ 0 ];
}
}

BookingGridRef.Rebind();

_renderCounter +=1;

} The grid does now populate and first item is selected. BUT, if I have a breakpoint anywhere in my OnBookingGridRead it will hit the breakpoint endlessly as if always being executed every millisecond, never stops and I end up with this (even after I remove the breakpoint): rotating circle threesome ... the console windows shows OnBookingGridRead being called in an endless loop? My _renderCounter will be over 100,000 in a minute or less. Rob.

### Response

**Hristian Stefanov** commented on 08 Jul 2025

Hi Rob, You are encountering an infinite loop because BookingGridRef.Rebind() is being called inside the OnRead handler. This causes the Grid to continuously request data, which repeatedly triggers OnRead. This is not specific to async usage—calling Rebind() inside OnRead will always result in this loop, regardless of whether you use async or not. Thus, as a next step, remove BookingGridRef.Rebind() from your OnBookingGridRead method and: The Grid will automatically refresh when the OnRead logic completes. There is no need to call Rebind() within OnRead. This will immediately stop the endless loop and the high _renderCounter. Overall, you do not need to restructure your code or implement complex logic to select the first row after filtering. You can set the selected item inside OnRead after the data is updated, as you are doing. Best, Hris

### Response

**Rob** commented on 08 Jul 2025

Hi Hris, Yes, that didn't make sense to me either putting a ReBind in the OnRead. I did remove it and made a few other adjustments and have the process working per requirements. Per Dimo's comment earlier in this thread and why I had the ReBind in the OnRead ... perhaps a misinterpretation? Set empty args.Data and zero args.Total in the first OnRead call. Then, when the Grid data is available, execute BookingGridRef.Rebind() Rob EDIT: I'll disagree with you on the code restructure. I should NOT have to switch to OnRead for something this simple default to first row selected. A property of the Grid called "DefaultToFirstRowSelected"=true or false would have improved efficiency so I highly recommend you add this feature to the grid for future versions. Moving my logic out of OnAfterRenderAsync() with if (firstRender) into OnInitializedAsync() and then move all that logic out into OnRead and then remove the Data="mydatasource" on the Grid and then convert args.Data (from OnRead) into a List so I can set the selectedItem ... is DEFINITELY restructuring my code/implementation.

### Response

**Hristian Stefanov** commented on 11 Jul 2025

Hi Rob, I appreciate your feedback on this. It’s possible there was some misinterpretation around using the Rebind method within the OnRead event. As for introducing a new parameter to support the behavior you’re looking for, I’d recommend submitting your idea as a feature request in our public
