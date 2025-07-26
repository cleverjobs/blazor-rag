# Grid Loader for initial page

## Question

**Mic** asked on 29 Aug 2021

Hello, I want to display a database table's content in a TelerikGrid object. I am working with Linq and Entity Framework. TelerikGrid's Data property is set with a Linq IQueryable object. Why an IQueryable ? Because TelerikGrid manages paging, sorting and filtering. Working with an IQueryable object make possible the execution of a single SQL optimized query. I have made a very basic loader (animation). I have a flag: When this flag is set to true, the loader is displayed. When the flag is set to false, the grid is displayed instead of the loader. I don't know when set my flag to false. I am working with an IQueryable. So i don't know when the SQL query is finished. The execution of this SQL query is fired by the TelerikGrid. There are no events like "DataReady", or "DataLoadDone" in TelerikGrid. How can i do ? Please note the embedded loader inside the TelerikGrid is not displayed for the first page. I can see it when i change TelerikGrid page. Thanks

## Answer

**Marin Bratanov** answered on 30 Aug 2021

Hi Mickael, Check out this demo that explains the scenario: [https://demos.telerik.com/blazor-ui/grid/loading-animation](https://demos.telerik.com/blazor-ui/grid/loading-animation) Regards, Marin Bratanov Progress Telerik

### Response

**Mickael** commented on 30 Aug 2021

Hello, i've already read this document and i have looked the demo. The problem in your case is you are working with Lists, not IQueriable. That means your line bellow is blocking execution until SQL query has returned data GridData=result.Data.Cast <ProductBindingModel> ().ToList(); In my case, i am doing something like that: GridData=dbContext.Products.Where(....); This is for performance issue: This line does not execute SQL query. The SQL query is runned by TelerikGrid. Why am i working like this: It is because in my case TelerikGrid adds pagination (fetch, offset), filters and sort before executing query

### Response

**Mickael** commented on 30 Aug 2021

The problem is my GridData affectation only takes a few millisecond. So loader is not managed properly. This problem only occurs on first grid apparition.

### Response

**Mickael** commented on 31 Aug 2021

By the way, it seems this OnRead design does not work with Virtual ScrollMode. Do you confirm ?

### Response

**Marin Bratanov** commented on 31 Aug 2021

The OnRead event is a great place to add your own custom loading sign if you want to do so, read more here - OnRead will fire on the initial load of data and you can capture that as well as subsequent requests. OnRead also works with virtualization without problems, the key thing is to use the Skip parameter, not Page, see more in the Notes section. With using OnRead you will have to do the pagination, filtering and so on, but we have an extension method that can facilitate that, see here and here.

### Response

**Mickael** commented on 31 Aug 2021

Thanks, yes i know for ToDataSourceResult(request) for paging, filtering and sorting. But i do not understand what you say about Skip parameter. I've read all your documentation and i do not understand the goal of this parameter. I have tried to add Skip="10" and i have a runtime error saying there is no Skip parameter for TelerikGrid. Do you have an example of Virtualization and onRead usage together ? Thanks

### Response

**Marin Bratanov** commented on 01 Sep 2021

Just enable virtualization in the .ToDataSourceResult() example I linked, our code knows what to do. If you will be preforming the data operations yourself (that is - neither letting the grid do all the work, nor using .ToDataSourceResult()) - only then do you need to use the Skip field in the DataSourceRequest the grid gives you - so you have the correct offset to pass on to your data service. Here is the snippet from the docs with virtualization enabled (I highlighted the addition I made to the code): Using Telerik DataSource extension methods to manipulate all the data into paged chunks and also perform other operations like filtering, sorting, etc. There is a deliberate delay in the data source operations in this example to mimic real life delays and to showcase the async nature of the calls.

@using Telerik.DataSource.Extensions

<TelerikGrid Data=@GridData TotalCount=@Total OnRead=@ReadItems
FilterMode=@GridFilterMode.FilterRow Sortable=true EditMode="@GridEditMode.Inline" ScrollMode="@GridScrollMode.Virtual" Height="500px" RowHeight="50" PageSize="15">
<GridColumns>
<GridColumn Field=@nameof(Employee.ID) />
<GridColumn Field=@nameof(Employee.Name) Title="Name" />
<GridColumn Field=@nameof(Employee.HireDate) Title="Hire Date" />
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
<GridCommandButton Command="Delete" Icon="delete">Delete</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
<GridToolBar>
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</GridToolBar>
</TelerikGrid>

@code { public List<Employee> SourceData { get; set; } public List<Employee> GridData { get; set; } public int Total { get; set; }=0; protected override void OnInitialized ( ) {
SourceData=GenerateData();
} protected async Task ReadItems ( GridReadEventArgs args ) {
Console.WriteLine( "data requested: " + args.Request); //you need to update the total and data variables //the ToDataSourceResult() extension method can be used to perform the operations over the full data collection //in a real case, you can call data access layer and remote services here instead, to fetch only the necessary data await Task.Delay( 2000 ); //simulate network delay from a real async call var datasourceResult=SourceData.ToDataSourceResult(args.Request);

GridData=(datasourceResult.Data as IEnumerable<Employee>).ToList();
Total=datasourceResult.Total;

StateHasChanged();
} //This sample implements only reading of the data. To add the rest of the CRUD operations see //[https://docs.telerik.com/blazor-ui/components/grid/editing/overview](https://docs.telerik.com/blazor-ui/components/grid/editing/overview) private List<Employee> GenerateData ( ) { var result=new List<Employee>(); var rand=new Random(); for ( int i=0; i <100; i++)
{
result.Add( new Employee()
{
ID=i,
Name="Name " + i,
HireDate=DateTime.Now.Date.AddDays(rand.Next( -20, 20 ))
});
} return result;
} public class Employee { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
}
}

### Response

**Mickael** commented on 02 Sep 2021

Thanks. I have forgot TotalCount. This is why scrolling was not working. There is something very strange: If i remove Task.Delay(2000) and if a put a real slow query, the loader is not displayed for the initial display. I think Task.Delay creates another thread and let the UI refresh. Is there a way to display the loader for the initial grid display without Task.Delay ? Please note the loader works fine for scroll or pagination.

### Response

**Marin Bratanov** commented on 03 Sep 2021

Please check out the implementation through the IsInitialDataLoadComplete flag in this demo: [https://demos.telerik.com/blazor-ui/grid/loading-animation](https://demos.telerik.com/blazor-ui/grid/loading-animation) - note how this initial load is handled outside of the grid. This is the way to do that for the initial load.

### Response

**Mickael** commented on 03 Sep 2021

Try to remove this line: await Task.Delay(3000); And put a "real" slow query instead of your query. You will see loader is not displayed for the initial load.

### Response

**Marin Bratanov** commented on 05 Sep 2021

Could you give this a try in one of these sample projects that is closest to your setup: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server?](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server?) The initial load is not different from the grid's perspective than subsequent calls to OnRead, and if the ORM used does not release the UI rendering thread, then you won't see the loading sign, but there isn't anything the grid can do about this. I'm attaching here a modified version of the server app that goes to a web api backend from the service - I added two artificial delays in the webapi service so that I don't touch the main thread myself with Task.Delay() calls in the UI app. This still shows the expected loading indicators for me - the custom one for the initial load, and also the built-in one on subsequent operations. I suggest you compare with that to see where the difference lies and where the rendering thread does not get released as expected in your case. That said, another thing that might be going wrong is something in the LoaderContainer setup itself - in the demo we have it should be visible as soon as the component renders, and hiding it happens in the OnRead handler, so something in the UI/CSS part may be going wrong in your case. Of course, removing the delay from the demo setup will have the data load far too quickly for the loading animation to be visible to a human, so that might also be a problem.
