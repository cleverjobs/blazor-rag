# Grid entering two times in same read method call

## Question

**Alb** asked on 16 Dec 2019

I have a grid that when loading the data it is entering two times in ReadISHandler. I can see in debugger that enter and stops two times in LoadIS(); causing a performance problem, any idea what is happening <TelerikGrid Data=@GridDataIS TotalCount=@Total Height=@Height ScrollMode="@GridScrollMode.Virtual" Sortable=false RowHeight="40" OnRead=@ReadISHandler> protected async Task ReadISHandler(GridReadEventArgs args) { Skip=args.Request.Skip; await LoadIS(); }

## Answer

**Marin Bratanov** answered on 16 Dec 2019

Hi Alberto, Could you check if this is the situation that you hit: [https://feedback.telerik.com/blazor/1442276-onread-called-twice-on-initialization?](https://feedback.telerik.com/blazor/1442276-onread-called-twice-on-initialization?) We are aware of such behavior during initialization and for the time being you can work around it through flags. Regards, Marin Bratanov

### Response

**Alberto** answered on 16 Dec 2019

yes looks like the same problem read is invoked two times.

### Response

**Alberto** answered on 11 Jan 2020

do you have any sample code on how to avoid this with flags? Will this be fixed in next versions as i see the issue approved but not planned to any version.

### Response

**Marin Bratanov** answered on 13 Jan 2020

Hello Alberto, I posted one workaround in the public page: [https://feedback.telerik.com/blazor/1442276-onread-called-twice-on-initialization](https://feedback.telerik.com/blazor/1442276-onread-called-twice-on-initialization) You can click the Follow button there to get notified about status changes. It will be fixed, because it is a valid issue, even if I cannot say in which release that will happen. Regards, Marin Bratanov

### Response

**Jason** answered on 04 Jun 2020

I'm stuck with this same issue trying to follow the sample code which definitely will not work. If you look at OnAfterRenderAsync, it has bool firstRender as a parameter so we can check for first render. It seems like OnRead should have that same parameter to work properly for Blazor Server. In the workaround, a counter is suggested, but this counter never gets reset so I'm not sure how that would work either.

### Response

**Marin Bratanov** answered on 05 Jun 2020

Hi Jason, In a server-side Blazor app this behavior is expected - the pre-rendering actually initializes all components twice - once on the server for the pre-rendering, and once the client-side portion of the app spins up. This is the case with all components, not just the grid. For example, if you fetch data in the OnInitialized event, it will be called twice too. For example, if you make a GET for the FetchData page from the default template, and modify it as follow,s you will find that statement twice in the console: protected override async Task OnInitializedAsync ( ) { Console.WriteLine( "fetching data" ); forecasts=await ForecastService.GetForecastAsync(DateTime.Now);
} This behavior is expected and valid - for proper pre-rendering the components need to initialize and render, and for the grid that also means getting data. If you want to reduce the calls, you must use some business logic to do that, for example, flag raised in the OnAfterRender event so you can call the OnRead handler yourself only then (a basic example of storing the grid request is available here: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#cache-data-request](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#cache-data-request) ). Here's another I made for you that uses a flag from OnAfterRender: @using Telerik.DataSource

<TelerikGrid Data=@GridData TotalCount=@Total
Pageable=true PageSize=15 OnRead=@ReadItems>
<GridColumns>
<GridColumn Field=@nameof (Employee.Id) Title="ID" />
<GridColumn Field=@nameof (Employee.Name) Title="Name" />
</GridColumns>
</TelerikGrid>

@code { public List<Employee> GridData { get; set; } public int Total { get; set; }=0; bool hasComponentRenderedOnce { get; set; }
DataSourceRequest CurrentRequest { get; set; } protected async Task ReadItems ( GridReadEventArgs args ) {
CurrentRequest=args.Request; if (hasComponentRenderedOnce)
{ await FetchData();
}
} protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{
hasComponentRenderedOnce=true;
FetchData();
}
} async Task FetchData ( ) { if (CurrentRequest==null )
{ return;
}

Console.WriteLine( "ReadItems" ); // fetch actual data here and populate Total and GridData } public class Employee { public int Id { get; set; } public string Name { get; set; }
}
} Regards, Marin Bratanov

### Response

**Paul Wood** commented on 09 Nov 2021

If you don't want to use OnRead and are using the simpler protected override async Task OnInitializedAsync ( ) { await LoadData();
} are there any issues with just replacing the above with the following instead to avoid the two calls to the database?: protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await LoadData();
StateHasChanged();
}

### Response

**Marin Bratanov** commented on 09 Nov 2021

That's the typical approach people tend to take in such cases. I would only suggest you call await InvokeAsync(StateHasChanged); so that you are sure it executes in the main thread.

### Response

**Thomas** commented on 16 Jul 2025

@Marin Bratanov What if I am not using pre-rendering, and this is still happening? I have set: @rendermode="new InteractiveServerRenderMode(prerender: false)"

### Response

**Dimo** commented on 16 Jul 2025

@Thomas - I don't observe such a behavior. Please review the attached test app and send a similar one if necessary.

### Response

**Thomas** commented on 16 Jul 2025

@Dimo Thanks for the sample, that does indeed work. If you add manual sorting than it executes again, which I guess makes sense. Can this be avoided? I added the following code to your sample, making the OnGridRead execute twice. protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await ApplySorting();
}
} public async Task ApplySorting () { var gridState=GridRef.GetState(); if (!gridState.SortDescriptors.Any())
{
gridState.SortDescriptors.Add( new SortDescriptor()
{
Member="Price",
SortDirection=ListSortDirection.Ascending
}); await GridRef.SetStateAsync(gridState);
}
}

### Response

**Dimo** commented on 16 Jul 2025

>> If you add manual sorting than it executes again, which I guess makes sense. Yes, OnRead fires by design when using SetStateAsync (). In the future, the event may not fire if the Grid state change is not related to the data, but in your case it still will.>> Can this be avoided? Apply the initial sorting in OnStateInit. If this is not possible for some reason, then skip the database call in the first OnRead execution and set args.Data to an empty collection.

### Response

**Thomas** commented on 16 Jul 2025

Thanks Dimo, that works perfectly!
