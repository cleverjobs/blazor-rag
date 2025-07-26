# FooterTemplate: @context.Sum does not return any value

## Question

**Mar** asked on 13 Sep 2021

I have added a footer to a column which is bound to a field of type nullable decimal. Now when I call in footer @context.Sum no value is displayed. Some fields are actually null. But I assume that these are not taken into account in the summation.

### Response

**Michal** commented on 12 Apr 2022

Hello, iam observed similar problem (version 3.1.0): - agreagates on footer are displayed only on FIRST load - after paging, sorting, filtering etc, whole footer row is "empty" using async task OnRead also using StateHasChanged inside OnRead causing "empty" footer agregates. Does it need any special treatment? Thank You <TelerikGrid TItem="XYZModel" Pageable="true" @ref="gHL" Sortable="true" Resizable="true" Reorderable="true" Groupable="false" AutoGenerateColumns="false" FilterMode="@((GridOrganize)?GridFilterMode.FilterMenu:GridFilterMode.FilterRow)" ShowColumnMenu="@GridOrganize" PageSize="50" OnRead=@GReadItems Height="calc(100vh - 80px)" OnStateInit="@((GridStateEventArgs<XYZModel> args)=> GStateGHLLoad(args,C_KeySestava))"> <GridToolBar>.... <GridAggregates> <GridAggregate Field=@nameof(VykazGModel._ColA) Aggregate="@GridAggregateType.Sum" /> <GridAggregate Field=@nameof(VykazGModel._ColB) Aggregate="@GridAggregateType.Sum" /> <GridAggregate Field=@nameof(VykazGModel._ColC) Aggregate="@GridAggregateType.Sum" /> <GridAggregate Field=@nameof(VykazGModel._ColD) Aggregate="@GridAggregateType.Sum" /> </GridAggregates> <GridColumns> <GridCommandColumn Id="cmd" Width="50px" Title="AA" />..... <GridColumn Field="@nameof(VykazGModel._ColA)" ShowFilterCellButtons="false" DisplayFormat="{0:n2}"> <FooterTemplate> @context.Sum?.ToString("N2") </FooterTemplate> </GridColumn>.... protected async Task GReadItems ( GridReadEventArgs args ) { // debouncing if (Notification==null ) return; //if (args.Data !=null && Fastload==false) if (FastLoad==false )
{
tokenSource.Cancel();
tokenSource.Dispose();

tokenSource=new CancellationTokenSource(); var token=tokenSource.Token; await Task.Delay(glob.Consts.C_DebounceDelay, token); // 500ms timeout for the debouncing } else { IsBusy=true; } //if (args.Data==null) IsBusy=true; FastLoad=false; try { //ctxhttp.HttpContext.User. var p=new DynPredef(); var f=SqlClass.GetSQLFiterString(args.Request);
p.Add( "Typ", value: 10, dbType: DbType.Int32);
p.Add( "TypCmd", value: 0, dbType: DbType.Int32);
p.Add( "UserName", value: ctxhttp.HttpContext.User.Identity.Name, dbType: DbType.String);
p.Add( "xWhere", value: f.xWhere, dbType: DbType.String);
....
...
args.Data=await glob.SQL.SQLGetWebDbConnection().QueryAsync<VykazGModel>(sql: "dbo.procedureXYZ", param: p, commandType: System.Data.CommandType.StoredProcedure);
args.Total=p.Get<int>( "CNT" ); //GridData1.Count(); }
catch (Exception ex)
{
Notification.ShowSQLErr(ex.Message);
} finally {
IsBusy=false;
IsFirstLoad=false; //StateHasChanged(); --- Also cause footer dissapear }

}

### Response

**Dimo** commented on 14 Apr 2022

@Michal - When using OnRead, you need to provide the aggregates in the OnRead handler. Set them to args.AggregateResults. This property is IEnumerable<AggregateResult>. If you are not using ToDataSourceResult, you will have to construct the object manually. async Task OnGridRead ( GridReadEventArgs args ) {
DataSourceResult result=ALLGridData.ToDataSourceResult(args.Request);

args.Data=result.Data;
args.Total=result.Total; args.AggregateResults=result.AggregateResults; } Currently, you are seeing (incorrect) aggregates for the first page only, which is a bug that we will resolve in the future. When you are ready with the aggregates implementation, Rebind () the Grid in OnAfterRenderAsync (), to show the correct aggregate values for the whole data. protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{ await Task.Delay( 100 );
GridRef.Rebind();
StateHasChanged();
}
}

### Response

**Michal** commented on 14 Apr 2022

Hi Dimo, according to the documentation, aggregateResult is not required, so disappearing is more like a small bug. You have described the second part of the solution :) " If you use OnRead, the Grid will calculate aggregates from the data on the current page only. It is still possible to calculate and display aggregates, which are based on all the data. [https://docs.telerik.com/blazor-ui/components/grid/grouping/aggregates](https://docs.telerik.com/blazor-ui/components/grid/grouping/aggregates) " It is desired functionality.

### Response

**Dimo** commented on 14 Apr 2022

Frankly, I am not sure if the bold sentence is a "feature" or "explanation for a limitation" from older times when the OnRead event was used together with the Data parameter. I will check this with the devs. In the meantime, do I understand you correctly, that you actually want the Grid to display aggregates for the current page only?

### Response

**Michal** commented on 14 Apr 2022

Yes, that make perfect sense and is expected result: 1) agregate "what you see/current page"=you dont want specify an aggregateResult 2) If someone wants to agregate "anything else/non visible/custom" so aggregateResult will be required. (and that is fully understandable, but different story) if option 1) is obsolete/not supported, so GridaAregates in grid definition doesnt make any sense, because you have to do hardwork in onread, template.... and just "visible agregate" becomes too complex task :)

### Response

**Dimo** commented on 15 Apr 2022

OK, thanks for the confirmation, Michal. I will forward this information to our devs. Update: So, the old behavior was expected limitation, and not a feature. The concept is that when using OnRead, the component should not perform any internal data processing or calculations. If the Grid should display aggregates over the current page only, then this is what args.AggregateResults should provide.

### Response

**Michal** commented on 15 Apr 2022

Thanks for clarification, from usability point of view its little step back. In descripbed situation, will be nice to have available ROW-data in grid context(or by grid referece Grid.Data), to perform simple calculation: <FooterTemplate> @((context.Data as XYZModel).Sum(...).ToString("N2")) </FooterTemplate> defining of: no agregates required no onread AgregateResults required no another reference to grid no another list of items Because this doesnt working also: <GridColumn Field="@nameof(VykazGModel._ColA)" ShowFilterCellButtons="false" DisplayFormat="{0:n2}"> <FooterTemplate> @((gHL.Data)?.Sum(p=>p._ColA)?.ToString("N2")) //!! self reference to gHL.Data is still null @context.Sum?.ToString("N2") //obsolete without AgregateResults defined </FooterTemplate> </GridColumn> Have a nice day Dimo

### Response

**Michal** commented on 15 Apr 2022

Maybe iam still not get the point: on the first page load, first call: OnRead (GridReadEventArgs args): args.Request.Aggregates=empty BUT the FooterTemplate context.Sum... is ok and context.AggregateResults is ok also after paging the grid,filtering ( seccond call of OnRead ) args.Request.Aggregates=contains values BUT the FooterTemplate context.Sum... is null and context.AggregateResults is null also it would be better option to not harcode by self: OnRead->args.AggregateResults=.... but even if ill give it a try, i dont now how to fill args.AggregateResults based on "empty" definition. Grid should do it automatically the same way as on the first load, if NOT, so for which reason is there definition of GridAggregates or, when using OnRead, we should forget about GridAggregates at grid markup and do it "somehow the hard way" in OnRead only? Thats what i dont understand :o

### Response

**Dimo** commented on 15 Apr 2022

Note the difference between these two - args. Request.Aggregates args.Aggregate Results The screenshot shows aggregates in the request. These are the aggregates, which the Grid expects to be set in args.AggregateResults by the application. In this case, the Grid is calculating aggregates on the first page by mistake - this is a bug. Since version 3.0, the component should not perform internal data operations when using OnRead. All aggregate values should be provided to the Grid via args.AggregateResults. args.AggregateResults is IEnumerable<AggregateResult>. You can refer to the linked API for the object structure, or debug result. AggregateResults in the OnRead handler from this REPL example to see how to construct the object manually.

### Response

**Michal** commented on 15 Apr 2022

Ok,thanks it helped a lot. When using OnRead: Future fix is - args. Request.Aggregates - should not be empty, when <GridAggregates> are defined at first OnRead. So this should work: ...OnRead(GridReadEventArgs args) { args.Data=await datafromRemoteSourceDBfilteredPaged; args.Total=p.Get<int>("CNT");//real number of rows for paging purpose.... args.AggregateResults=args.Data.ToDataSourceResult(args.Request).AggregateResults; //lets see about performance.... } Suggestions, for better reusability: - if <GridAggregates> are definied, its expected that grid will calculate available data for "@context.sum/count...." in grid-templates(best option :) ) OR - Allow access in templates @context.Data, then GridAggregates and A ggregate Results, doesnt need to be defined at all OR - Automatically calculate " @context.sum/count", when <GridAggregates> are defined and OnRead args. Aggregate Results is NULL otherwise,when someone define/rewrite values with own args. Aggregate Results, lets use this object.

### Response

**Dimo** commented on 15 Apr 2022

Michal - yes, the first suggestion is valid, but only for binding with the Data parameter. The second and third one contradict the OnRead idea and relevant Grid architecture. When using OnRead, all data retrieval and calculations should happen in OnRead. Surely, it's possible to calculate aggregates manually inside the FooterTemplate, but if you cache the current page of data inside OnRead.

### Response

**Michal** commented on 17 Aug 2023

Hello Dimo, iam back in party, looks like something has changed in verison 4.4.0. When working with OnRead and dynamically changing "column sets"/view runtime, the aggregates are empty in this scenario: 1) first enter to the page, OnRead, everything is ok 2) change the columnset to something else(completly different columns), where is NO aggregates at all 3) change columnset to same as at point 1) but runtime, no full reload of the page and aggregates are empty 4) after calling(grid.rebind()=which calls OnRead for the seccond time ) agregates are back(same data, same number of rows, same args.AggregateResults, but for the first time not displayed). As an hint point: After changing to version 4.4.0 i have to comment in code(sample below) "//args.Data=xdata.Data;", becouse after paging to page greater than 1, aggregates was OK, but data was not visible at all. I suspect that it is "somehow" connected/related with [https://www.telerik.com/forums/grid-columns-order-not-working-with-foreach-statement](https://www.telerik.com/forums/grid-columns-order-not-working-with-foreach-statement) and my last post at that thread " commented on 16 Aug 2023, 05:43 PM" Do you have any correct steps(maybe an order of assigning args.values are critical too), how to have aggregates calclulated per "viewing" page data displayed always at it should? Thanks <TelerikGrid TItem="ExpandoObject".... OnRead=@gHLReadItems
<GridAggregates>
@if (GridDef.ColStore !=null && GridDef.ColStore.Any(x=> x.Sumovat==true ))
{ foreach ( var it in GridDef.ColStore.Where(x=> x.Sumovat==true )
{
<GridAggregate Field=@it.FldName FieldType=@it.FldType Aggregate="@GridAggregateType.Sum" />
}
}
</GridAggregates>
<GridColumns> @foreach ( var it in GridDef.ColStore)
{
<GridColumn Field=@it.FldName FieldType=@it.FldType Title=@it.VerejnyNazev ShowFilterCellButtons="false" Width=@it.cSirkaSestava
TextAlign=@it.cZarovnani DisplayFormat="@it.Maska">
<FooterTemplate>
@if (it.Sumovat==true )
{
@context.Sum
}
</FooterTemplate>
</GridColumn>
}
</GridColumns>
... </TelerikGrid>

@code {.... protected async Task gHLReadItems ( GridReadEventArgs args ) {
args.Total=( int )GridDef.RowData.Total; //correct args.Data=GridDef.RowData.Data; //correct //!! TWEAKS to get aggregates to work at all. if (GridDef.ColStore !=null && GridDef.ColStore.Any(x=> x.Sumovat==true ))
{ args.Request.Aggregates.Clear(); foreach ( var it in GridDef.ColStore.Where(x=> x.Sumovat==true ))
{
args.Request.Aggregates.Add( new AggregateDescriptor
{
Member=it.FldName,
Aggregates=new List<AggregateFunction>()
{ new SumFunction()
{
SourceField=it.FldName,MemberType=it.FldType
}
}
}); foreach ( var xrow in GridDef.RowData.Data)
{ var v=((IDictionary<string, object>)xrow)[it.FldName]; //Type aa=it.FldType; if (v==null )
{ //aa.DefaultValue(); ((IDictionary<string, object>)xrow)[it.FldName]=it.FldType.DefaultValue();
}
}

} if (args.Total> 0 && args.Request.Aggregates.Count> 0 )
{ var xdata=args.Data.ToDataSourceResult(args.Request);

args.AggregateResults=xdata.AggregateResults; //StateHasChanged(); //args.Data=xdata.Data; //args.Data=GridDef.RowData.Data; }
}

### Response

**Dimo** commented on 17 Aug 2023

@Michal - I believe the described sequence and behavior is related to the OnRead + aggregates bug that I mentioned above on April 14, 2022. The workaround is to call an additional Rebind () after changing the columns via the state, as you have already observed.

## Answer

**Dimo** answered on 16 Sep 2021

Hello Martin, By design, the Grid calculates aggregates only if you declare them in advance. This improves the application performance. The provided code is too little and I am only guessing here, but I suspect the Grid is missing its GridAggregates. Please make sure that you have configured the Grid to work with aggregates. The Grid column footer template article provides additional information and examples. If you have the required configuration in place and the Grid still does not show the Sum, then please provide the whole component declaration and any other relevant code. Regards, Dimo Progress Telerik
