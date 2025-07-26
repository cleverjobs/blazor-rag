# Spinner when setting new page size

## Question

**Ray** asked on 05 May 2020

Hi, In our project we handle a lot of data and try to use the Telerik Grid for it. Most of time consuming (async) actions trigger a spinner to show when the user waits for a result. With a few thousand lines in the grid even changing the page size can take a while. Here we would like to have a spinner as well. Is there a specific event to hook to achieve this? Best regards, Rayko

## Answer

**Marin Bratanov** answered on 05 May 2020

Hello Rayko, You can Follow the implementation of such a feature in this page: [https://feedback.telerik.com/blazor/1446689-animation-during-grid-load.](https://feedback.telerik.com/blazor/1446689-animation-during-grid-load.) I've added your Vote on your behalf to raise its priority. For paging specifically, you can use the PageChanged event to show an external loading sign: [https://docs.telerik.com/blazor-ui/components/grid/events#pagechanged.](https://docs.telerik.com/blazor-ui/components/grid/events#pagechanged.) If you are using the OnRead event to supply only the current page of data, you could use that too to display a loading sign. Doing so can also improve the performance of your grid and backend. Here's more information on this event and how to use it: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) Last but not least, I strongly advise against using page sizes in the thousands for a grid. This will impact the performance negatively and won't be very user-friendly anyway. I'd suggest keeping the page size down to something around 20-30 items per page that is still easily usable for the human browsing the grid. Alternatively, virtual scrolling can help you show many rows with improved performance: [https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling.](https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling.) Regards, Marin Bratanov

### Response

**Rayko** answered on 05 May 2020

Hi Marin, Thank you for adding my vote! I hope this feature can be implemented soon. I've already tried the PageChanged event. But this event is triggern on a page change, not when I change the page size. The OnRead event also looked promissing. But there I can just handle the way of binding the data. Yes, it takes a moment to retrieve the data from DB. But this action is done async and I already have a spinner around this. The only part which is done automatically and which also takes a lot of time is the rendering of the grid after selecting a new page size. There I can't find any point to start or end my spinner. And yes, you are right saying it isn't a good idea to have so many rows in one page. Unfortunately we need this option nevertheless. Virtual scrolling and column virtualization are already good helpers for us. Best regards, Rayko

### Response

**Marin Bratanov** answered on 05 May 2020

Hello Rayko, With Virtual scrolling, the grid shows loading indicators on the new rows while their data is loading, and there isn't a pager, or changing of the page size, so this can fit your case well without any extra code. On changing the page size - the grid UI does not offer such a feature, and there is no event in the grid for this. If you change the PageSize parameter value, this means some other code is changing the value of the view-model field it is populated from, so this code is the place to add the loading sign, just before you alter the PageSize value. Regards, Marin Bratanov

### Response

**Rayko** answered on 05 May 2020

Hi Marin, Yes, the virtual scrolling could do the trick. We'll investigate this further. I've already tried to activate the loading sign right before changing the page size value. The problem is... when should I deactivate it? I don't know any event which is triggered once the grid has finished rendering. Best regards, Rayko

### Response

**Marin Bratanov** answered on 06 May 2020

Hi Rayko, I'd encourage you to give the virtual scrolling a try as the first option as it will require less code on your part. If you choose to keep using paging and altering the page size in your logic - the way to activate the sign is to use the current place where you change the page size, the place to hide it is after the data comes back in the OnRead handler, something like this: @using Telerik.DataSource.Extensions

<TelerikButton OnClick="@ChangePageSize">Change page size to 20 </TelerikButton>

@if (shouldShowWaitingSign)
{
<div>the waiting sign. Style as needed ( e.g., in a relative container with the grid ).</div>
}

<TelerikGrid Data=@GridData PageSize="@ThePageSize" TotalCount=@Total OnRead=@ReadItems
FilterMode=@GridFilterMode.FilterRow Sortable=true Pageable=true EditMode="@GridEditMode.Inline">
<GridColumns>
<GridColumn Field=@nameof (Employee.ID) />
<GridColumn Field=@nameof (Employee.Name) Title="Name" />
<GridColumn Field=@nameof (Employee.HireDate) Title="Hire Date" />
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

@code { int ThePageSize { get; set; }=10; bool shouldShowWaitingSign { get; set; } async Task ChangePageSize ( ) {
shouldShowWaitingSign=true; //StateHasChanged(); // add this if the loading sign does not show up ThePageSize=20;
} public List<Employee> SourceData { get; set; } public List<Employee> GridData { get; set; } public int Total { get; set; }=0; protected override void OnInitialized ( ) {
SourceData=GenerateData();
} protected async Task ReadItems ( GridReadEventArgs args ) {
Console.WriteLine( "data requested: " + args.Request.PageSize); await Task.Delay( 2000 ); //simulate network delay from a real async call var datasourceResult=SourceData.ToDataSourceResult(args.Request);

GridData=(datasourceResult.Data as IEnumerable<Employee>).ToList();
Total=datasourceResult.Total; //hide loading signs - we already have the data shouldShowWaitingSign=false;

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
} There is no event in the framework for when something has finished rendering. The closest one is the OnAfterRenderAsync event, but it fires after every render - so, for example, it will fire after every button click and so on. You can easily see how that behaves if you add the following snippet to the example above and monitor the console: protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (!firstRender)
{
Console.WriteLine( "this component just rendered" );
}
} Regards, Marin Bratanov
