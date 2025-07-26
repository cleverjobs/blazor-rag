# blazor TelerikGrid

## Question

**kha** asked on 21 Oct 2019

hi i was using TelerikGrid and i ran to a problem ` <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" ScrollMode="@GridScrollMode.Virtual" Height="400px" RowHeight="40" PageSize="20"> ` this is my grid and it works fine but when use OnRead ` <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" ScrollMode="@GridScrollMode.Virtual" Height="400px" RowHeight="40" PageSize="20" OnRead="()=> { }"> ` i dont even need to do something in that function i give ity an empty function suddenly whenever i scroll to it just shows me first 15 when i scroll i can see other options but suddenly 1 to 15 jumps up and all i see is them but scroll doesnt go to first of grid and this is my whole code <style> .read{ color:red; } .not-yet{ color:green; } </style> <TelerikGrid Data=@GridData FilterMode="@GridFilterMode.FilterMenu" ScrollMode="@GridScrollMode.Virtual" Height="400px" RowHeight="40" PageSize="20" Class="@(isRead ?"read" : "not-yet")" OnRead="()=> { }"> <GridColumns> <GridColumn Field="Id" /> <GridColumn Field="Name" Title="First Name" /> <GridColumn Field="LastName" Title="Last Name" /> <GridColumn Field="HireData"> <Template> @(((SampleData)context).HireDate.ToString("MMMM dd, yyyy")) </Template> </GridColumn> </GridColumns> </TelerikGrid> @code { public List<SampleData> GridData { get; set; } public bool isRead=false; protected override async Task OnInitializedAsync() { GridData=await GetData(); } private async Task<List<SampleData>> GetData() { return Enumerable.Range(1, 100).Select(x=> new SampleData { Id=x, Name=$"name {x}", LastName=$"Surname {x}", HireDate=DateTime.Now.Date.AddDays(-x) }).ToList(); } async Task Test() { isRead=true; } public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; } } }

## Answer

**Marin Bratanov** answered on 22 Oct 2019

Hello, To use the OnRead event, there are several requirements that are described in the documentation about manual operations, but are not met in this snippet: there must be an actual handler that updates the actual data for the current page properly the TotalCount must be set to the correct value of all data source items, regardless of how many are in the current page I also advise that you set the RowHeight to a larger value so that the browser does not ignore it (with the default grid settings, and depending on the Theme, a row may be around 48px tall, and since that's a table the browser will ignore the inline 40px). That said, the following works fine for me so you can use it as comparison point: @using Telerik.DataSource.Extensions

<style>

.read {
color: red;
}

.not-yet {
color: green; /* in this sample, this rule will affect every other row where the grid does not have a heavier selector */ }
</style>

<TelerikGrid Data=@GridData TotalCount="@Total" FilterMode="@GridFilterMode.FilterMenu" ScrollMode="@GridScrollMode.Virtual" Height="400px" RowHeight="50" PageSize="20" Class="@(isRead ?" read " : " not-yet ")" OnRead="@ReadItems">
<GridColumns>
<GridColumn Field="Id" />
<GridColumn Field="Name" Title="First Name" />
<GridColumn Field="LastName" Title="Last Name" />
<GridColumn Field="HireData">
<Template>
@(((SampleData)context).HireDate.ToString( "MMMM dd, yyyy" ))
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { public List<SampleData> GridData { get; set; } public List<SampleData> DummyData { get; set; } public int Total { get; set; }=0; public bool isRead=false; protected override async Task OnInitializedAsync ( ) {
DummyData=await GetData();
} private async Task<List<SampleData>> GetData()
{ return Enumerable.Range( 1, 100 ).Select(x=> new SampleData
{
Id=x,
Name=$"name {x} ",
LastName=$"Surname {x} ",
HireDate=DateTime.Now.Date.AddDays(-x)
}).ToList();
} async Task Test ( ) {

isRead=true;
} protected async Task ReadItems ( GridReadEventArgs args ) {
GridData=DummyData.Skip(args.Request.Skip).Take(args.Request.PageSize).ToList();

Total=DummyData.Count;

StateHasChanged();
} public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov
