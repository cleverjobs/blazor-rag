# Grid Grouping Problem After Update 6.0.2

## Question

**Nol** asked on 31 Jul 2024

Hello, I'm receiving an exception after I upgraded to version 6.0.2. When I try to load a GroupDescriptor on StateInit of a grid, the page crashes. It seems like if the OnRead method is async and takes too long, it causes something to be null and throws a null argument exception. Here's an example for the error: fail: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[111]
Unhandled exception in circuit 'DlYqtxkSjOU4QLgOZWeNdQC1Z5gG3bJP4QfPcowK3-w'.
System.ArgumentNullException: Value cannot be null. (Parameter 'source' )
at System.Linq.ThrowHelper.ThrowArgumentNullException(ExceptionArgument argument)
at System.Linq.Enumerable.Select[TSource,TResult](IEnumerable`1 source, Func`2 selector)
at Telerik.Blazor.Components.TelerikGrid`1.SetProcessedGroups(IEnumerable data)
at Telerik.Blazor.Components.TelerikGrid`1.SetProcessedData(IEnumerable data)
at Telerik.Blazor.Components.Common.DataBoundComponent`1.ProcessOnReadResult(ReadEventArgs args)
at Telerik.Blazor.Components.Common.GridBase`1.<>n__0(ReadEventArgs args)
at Telerik.Blazor.Components.Common.GridBase`1.ProcessOnReadResult(ReadEventArgs args)
at Telerik.Blazor.Components.Common.DataBoundComponent`1.ProcessOnReadData()
at Telerik.Blazor.Components.Common.DataBoundComponent`1.StartDataProcessAsync()
at Telerik.Blazor.Components.Common.DataBoundComponent`1.ProcessDataOnParametersSetAsync()
at Telerik.Blazor.Components.Common.DataBoundComponent`1.OnParametersSetAsync()
at Telerik.Blazor.Components.TelerikGrid`1.OnParametersSetAsync()
at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) This was working fine when I was using version 5.1.1, but broke when I tried to upgrade to 6.0.2. I added a simplified example to reproduce the error I'm experiencing. I'm running the App in "Server" render mode in case that's relevant. Test code: _Host.cshtml ... <component type="typeof(App)" render-mode="Server" /> ... Test.razor @page "/" @using Telerik.DataSource
@using Telerik.DataSource.Extensions;

<div class="k-d-flex-col k-justify-content-center">

<TelerikGrid @ref="GridRef" TItem="Employee" Groupable="true" Pageable="true" Height="400px" OnRead="@ReadAsync" OnStateInit="@StateInit">
<GridAggregates>
<GridAggregate Field="Team" Aggregate="@GridAggregateType.Count" />
</GridAggregates>
<GridColumns>
<GridColumn Field=@nameof(Employee.Name) Groupable="false" />
<GridColumn Field=@nameof(Employee.Team) Title="Team" />
<GridColumn Field=@nameof(Employee.IsOnLeave) Title="On Vacation" />
</GridColumns>
</TelerikGrid>

</div>

@code { public TelerikGrid<Employee> GridRef { get; set; } public async Task ReadAsync ( GridReadEventArgs args ) { var data=new List<Employee>(); var rand=new Random(); for ( int i=0; i <50; i++)
{
data.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 5,
IsOnLeave=i % 2==0 }); await Task.Delay( 50 ); // simulating DB call }

DataSourceResult result=await data.ToDataSourceResultAsync(args.Request);
args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults;
} public void StateInit ( GridStateEventArgs<Employee> args ) {
args.GridState.GroupDescriptors=new List<GroupDescriptor>()
{ new GroupDescriptor()
{
Member="Team",
MemberType=typeof ( string )
}
};
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; } public bool IsOnLeave { get; set; }
}
} Any help would be appreciated.

## Answer

**Nadezhda Tacheva** answered on 05 Aug 2024

Hi Nolan, The behavior is due to a regression we had in the Grid: [Regression] Grid with aggregates never loads if data comes asynchronously. The fix is included in our upcoming 6.1.0 version that will be live this week. After you upgrade, you will not get this error. Regards, Nadezhda Tacheva
