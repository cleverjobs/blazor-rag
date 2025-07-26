# Bug Virtual Grid TotalCount > 3.000.000

## Question

**WimWim** asked on 19 Jan 2021

The virtual grid breaks when there are more than 3.000.000 records in TotalCount. It overlays the actual Grid with extra height.

## Answer

**Marin Bratanov** answered on 19 Jan 2021

Hi Wim, Can you reproduce this for me with the snippet below? On my end, the grid looks well in terms of overflowing content (see this article for some more details on common issues with the configuration of the feature), yet I cannot get to the end of the items. Is this what you see too (screenshot attached at the end)? @using Telerik.DataSource.Extensions

Total items: @GridData.Count

<TelerikGrid Data=@CurrentPage
ScrollMode="@GridScrollMode.Virtual" Height="480px" RowHeight="60" PageSize="20" Sortable="true" FilterMode="@GridFilterMode.FilterMenu" OnRead="@OnReadHandler" TotalCount="@Total">
<GridColumns>
<GridColumn Field="Id" />
<GridColumn Field="Name" Title="First Name" />
<GridColumn Field="LastName" Title="Last Name" />
<GridColumn Field="HireDate" Width="200px" DisplayFormat="{0:MMMM dd, yyyy}" />
</GridColumns>
</TelerikGrid>

@code { public List<SampleData> GridData { get; set; } public IEnumerable<SampleData> CurrentPage { get; set; } int Total { get; set; } async Task OnReadHandler ( GridReadEventArgs e ) { var result=await GridData.ToDataSourceResultAsync(e.Request);

CurrentPage=result.Data as IEnumerable<SampleData>;
Total=result.Total; await InvokeAsync(StateHasChanged);
} protected override async Task OnInitializedAsync ( ) {
GridData=await GetData();
} private async Task<List<SampleData>> GetData()
{ return Enumerable.Range( 1, 3000000 ).Select(x=> new SampleData
{
Id=x,
Name=$"name {x} ",
LastName=$"Surname {x} ",
HireDate=DateTime.Now.Date.AddDays(-x % 1000 )
}).ToList();
} public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Wim** answered on 20 Jan 2021

Actually this is more our situation, we do our filtering, virtual pagination, etc.. on the back-end. So everytime the onread is called we get 25 records from the database, where the virtual grid is situated at the moment with filtering if set. We do not get 3.000.000 records at once. But the TotalCount will be that amount. 550.000 records work fine, 600.000 records not. @using Telerik.DataSource.Extensions @attribute [Authorize] Total items: @GridData.Count <TelerikGrid Data=@CurrentPage ScrollMode="@GridScrollMode.Virtual" Height="480px" RowHeight="60" PageSize="20" Sortable="true" FilterMode="@GridFilterMode.FilterMenu" OnRead="@OnReadHandler" TotalCount="@Total"> <GridColumns> <GridColumn Field="Id" /> <GridColumn Field="Name" Title="First Name" /> <GridColumn Field="LastName" Title="Last Name" /> <GridColumn Field="HireDate" Width="200px" DisplayFormat="{0:MMMM dd, yyyy}" /> </GridColumns> </TelerikGrid> @code { public List<SampleData> GridData { get; set; } public IEnumerable<SampleData> CurrentPage { get; set; } int Total { get; set; } async Task OnReadHandler(GridReadEventArgs e) { GridData=await GetData(); var result=await GridData.ToDataSourceResultAsync(e.Request); CurrentPage=result.Data as IEnumerable<SampleData>; Total=result.Total; await InvokeAsync(StateHasChanged); } protected override async Task OnInitializedAsync() { GridData=new List<SampleData>(); } private async Task<List<SampleData>> GetData() { return Enumerable.Range(1, 3000000).Select(x=> new SampleData { Id=x, Name=$ "name {x}", LastName=$ "Surname {x}", HireDate=DateTime.Now.Date.AddDays(-x % 1000) }).ToList(); } public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; } } }

### Response

**Wim** answered on 20 Jan 2021

Also the GridToolBar disappears with the latest version 2.21, even with TotalCount 50 records. @using Telerik.DataSource.Extensions @attribute [Authorize] Total items: @GridData.Count <TelerikGrid Data=@CurrentPage ScrollMode="@GridScrollMode.Virtual" Height="480px" RowHeight="60" PageSize="20" Sortable="true" FilterMode="@GridFilterMode.FilterMenu" OnRead="@OnReadHandler" TotalCount="@Total"> <GridToolBar> <GridCommandButton Icon="@IconName.Reload"></GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field="Id" /> <GridColumn Field="Name" Title="First Name" /> <GridColumn Field="LastName" Title="Last Name" /> <GridColumn Field="HireDate" Width="200px" DisplayFormat="{0:MMMM dd, yyyy}" /> </GridColumns> </TelerikGrid> @code { public List<SampleData> GridData { get; set; } public IEnumerable<SampleData> CurrentPage { get; set; } int Total { get; set; } async Task OnReadHandler(GridReadEventArgs e) { GridData=await GetData(); var result=await GridData.ToDataSourceResultAsync(e.Request); CurrentPage=result.Data as IEnumerable<SampleData>; Total=result.Total; await InvokeAsync(StateHasChanged); } protected override async Task OnInitializedAsync() { GridData=new List<SampleData>(); } private async Task<List<SampleData>> GetData() { return Enumerable.Range(1, 50).Select(x=> new SampleData { Id=x, Name=$ "name {x}", LastName=$ "Surname {x}", HireDate=DateTime.Now.Date.AddDays(-x % 1000) }).ToList(); } public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; } } }

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hi Wim, We've been reviewing this and the problem stems from a browser limitation - elements can only be so large in a browser, which limits how many rows you would be able to see. I made this KB article to explain the situation better: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-virtualization-many-records.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-virtualization-many-records.) As for the content overflowing - since the grid does not have such a border by default, my best guess is that there is some additional CSS in the project that affects it and causes that appearance. I think such custom CSS is also contributing to the toolbar issue you are having - the grid in the screenshot does not seem to be using the built-in Telerik Theme. I am attaching here a sample app that works and looks as expected for me with 2.21.0 so you can compare against it. Regards, Marin Bratanov

### Response

**Wim** answered on 20 Jan 2021

Thank you for the clarification, the virtual scroll has indeed a limitation because if the browser. The issue with the toolbar and the content overflowing is happening when I use the bootstrap theme of kendo <link href="_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css" rel="stylesheet" /> It happens also in the sample. When I use the default theme it works fine.

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hi Wim, Could you try clearing the browser cache? Perhaps your browser has an old stylesheet cached. I am attaching the sample and a video with the bootstrap theme where they still look as expected for me, it also shows how you can clear your browser cache easily. Regards, Marin Bratanov

### Response

**Wim** answered on 20 Jan 2021

Ok it changes one thing, I changed the count of the data

### Response

**Wim** answered on 20 Jan 2021

Ok it changes one thing, I changed the count of the data to 600.000. No problem with the default template, but an extra border with the bootstrap template.

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hello Wim, That's a symptom of the same browser limitation. When the element size is hit, the browser does not render it properly and it goes out of the bounds of its parent element. I've updated the KB article with this information (see the Steps To Reproduce section). The solution is still the same - switch to regular paging if you have so many records that you hit the browser limit. Regards, Marin Bratanov
