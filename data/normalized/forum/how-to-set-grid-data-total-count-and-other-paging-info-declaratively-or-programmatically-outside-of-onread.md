# How to set Grid data, total count, and other paging info declaratively (or programmatically outside of OnRead)?

## Question

**Joh** asked on 03 Mar 2022

We have data coming from an API endpoint that handles paging, filtering, and sorting, so we are using manual data source operations through OnRead. All of the documentation examples show this pattern protected async Task OnRead ( GridReadEventArgs args ) { var result=await FetchData(args.Request.Page, args.Request.PageSize); args.Data=result.Data;
args.Total=result.TotalCount;
} This is not a usable pattern for us. We dispatch api calls using a Redux/Flux pattern (Fluxor library). Here is a trimmed down version of what we are doing <TelerikGrid @* Data=CaseState.Value.Cases // since 3.x does nothing if using OnRead *@@* TotalCount=CaseState.Value.TotalCount // not available since 3.x*@PageSize=100 Pageable=true Sortable=true Resizable=true Reorderable=true OnRead=@OnRead Width="100%" @ref=_grid> <GridColumns>... </GridColumns> </TelerikGrid> Code behind: ... [ Inject ] private IState<CaseState> CaseState { get; set; }=default!;
... protected void OnRead ( GridReadEventArgs args ) { var pageRequest=CreateRequestFromArgs(args); // This is a void method and returns immediately Dispatcher.Dispatch( new GetCaseListAction() { SearchRequest=pageRequest });
} When the api call returns (handled elsewhere) another action is dispatched to the store which updates the CaseState (which in turn triggers StateHasChanged() for the component). Prior to 3.x we used to be able to pass the collection to the Data parameter AND make use of OnRead. This is no longer possible and results in a NullReferenceException because the Data is not being set on the GridReadEventArgs. I looked at using GridState as it contains some of paging, filtering, and sorting info, but not the Total Count or the actual data. Is there a way to pass Data, TotalCount and the rest of the state in one place either declaratively through component parameters or programmatically via a component ref?

## Answer

**Marin Bratanov** answered on 06 Mar 2022

Hello John, The new approach of using OnRead that was introduced with 3.0.0 requires that the Data and TotalCount are given to the grid in the OnRead handler. If the data service cannot expose a suitable "async Task" method that can be properly awaited within the OnRead handler until it returns the needed data, I can suggest that you "hack" around this with things like Task.Run() as there is no other way to use custom data source operations in the grid. The only other possibility is if you can have all the data at once in the grid - if you have literally all the items in the Data collection, the grid can do everything else in memory without additional requests and without OnRead. Whether that's possible mostly depends on how much data you'd have and how bad it would be if you got it all at once initially. Regards, Marin Bratanov

### Response

**Ecofip** answered on 11 Mar 2022

Hello John, We have encountered the same problem since the Telerik 3.0.0 migration. I've created another post on this forum (We have not found yours before) if you wanna see the details of our implementation. To be able to keep the Flux approach for grids with server side pagination in our application, we use a hack with a suscription to the action dispatched on the result of the "query" action. As you can see below, we subscribe to the HousesSetHousesAction, and then we call the Rebind() method on the grid. It will fire the OnRead event of the grid. private void UpdateGridData ( HousesSetHousesAction action ) { // callback when the action is fired if (GridRef is null ) return;
GridRef.Rebind();
} protected void ReadItems ( GridReadEventArgs args ) { //This method is bind on the OnRead event of the grid var total=this.HousesState.Value.TotaCount; var data=this.HousesState.Value.Items;

args.Total=total;
args.Data=data ?? Enumerable.Empty<HouseItem>();
} It works perfectly, but it seems that we pass through the Flux approach by doing that. I don't know if Telerik team plans to look into this, but it could be a good thing to bring to developers any way to do so! If you need any information on the implementation we've done in our project with Fluxor, do not hesitate to ask. Thanks, // Dylan

### Response

**John** commented on 14 Mar 2022

Hi Dylan, Thanks for the information. Glad I'm not the only one who hit this scenario. I thought maybe I was just missing something obvious. I am curious where/how are you triggering the dispatch of your "fetch" actions for subsequent paging, sorting and filtering? ie, when the users clicks column heading for sorting or clicks paging controls? Those are events are what trigger OnRead. How do you avoid an infinite loop?

### Response

**John** commented on 14 Mar 2022

Ok. I think I figured it out. This works protected override void OnInitialized ( ) {

SubscribeToAction<GetCaseListSuccessAction>(_=>
{
_shouldDispatch=false;
_grid?.Rebind();
}); base.OnInitialized();
} private Task OnRead ( GridReadEventArgs args ) { if (_shouldDispatch)
{
Dispatcher.Dispatch(FromArgs(args));
}

args.Total=CaseState.Value.TotalCount;
args.Data=CaseState.Value.Cases ?? Array.Empty<CaseSummaryResponse>();

_shouldDispatch=true; return Task.CompletedTask;
}

### Response

**Ecofip** commented on 15 Mar 2022

Hello John, In our scenarios, we use the OnStateInit and the OnStateChanged events, with the following as implementation example: protected void ReadItems ( GridReadEventArgs args ) { var total=this.AffaireState.Value.GridInfo.Total; var data=this.AffaireState.Value.GridInfo.Items;

args.Total=total;
args.Data=data ?? Enumerable.Empty <IAffaireFull> ();
} void OnStateInitHandler ( GridStateEventArgs <IAffaireFull> args ) { if ( this.AffaireState.Value.GridInfo.GridState !=null ) {
args.GridState=this.AffaireState.Value.GridInfo.GridState;
} else {
args.GridState.SortDescriptors=DefaultSorts; this.StateFacade.SetAffairesGridState(args.GridState);
} this.StateFacade.LoadAffaires(args.GridState);
} void OnStateChangedHandler ( GridStateEventArgs <IAffaireFull> args ) { if (args.PropertyName=="SortDescriptors" || args.PropertyName=="FilterDescriptors" || args.PropertyName=="Page" ) { this.StateFacade.PersistAffairesGridState(args.GridState); this.StateFacade.LoadAffaires(args.GridState);
}
} There are some custom logic in this code but I think you can get the general meaning. Note that it is just one possibility, and maybe your approach is better by using the OnRead event. But indeed we used it to avoid infinite loop, so it could be a better think to do. Do not hesitate if you have another question :) // Dylan
