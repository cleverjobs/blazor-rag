# Why doesn't the correct filter get passed down?

## Question

**Col** asked on 08 May 2023

Hello, I have the following grid: <TelerikGrid Data="@Customers" Pageable="false" Sortable="true" ScrollMode="@GridScrollMode.Virtual" OnRead="@ReadItems" LoadGroupsOnDemand="true" FilterMode="@GridFilterMode.FilterRow" PageSize="20"> <GridColumns> <GridColumn Field="Number" Title="Nr" Width="150px" /> <GridColumn Field="Zip" Title="ZIP"> </GridColumn> <GridColumn Field="City" Title="City"> </GridColumn> <GridColumn Field="FirstName" Title="First"> </GridColumn> <GridColumn Field="LastName" Title="Last"> </GridColumn> </GridColumns> </TelerikGrid> with code-behind: public async Task<DataEnvelope<CustomerDTO>> FetchPagedData(DataSourceRequest dataSourceRequest)
{ var result=await Http.PostAsJsonAsync(ApiRoutes.Customer.POST_Lazy(), dataSourceRequest); var fullList=await result.Content.ReadFromJsonAsync<DataEnvelope<CRMCustomerDTO>>(); return fullList;
} protected async Task ReadItems ( GridReadEventArgs args ) { var dataResult=await FetchPagedData(args.Request); if (args.Request.Groups.Count> 0 )
{
args.Data=dataResult.GroupedData.Cast<object>().ToList();
} else {
args.Data=dataResult.CurrentPageData.Cast<object>().ToList();
}

args.Total=dataResult.TotalItemCount;

StateHasChanged();
} and web-api: [ HttpPost( "Lazy" ) ] public async Task<DataEnvelope<CustomerDTO>> GetLazy([FromBody] DataSourceRequest dataSourceRequest)
{
DataEnvelope<CustomerDTO> dataEnvelope=new (); var customers=await _context.Customer
.Include(c=> c.Address)
.ToListAsync(); var customerDTOs=_mapper.Map<List<CustomerDTO>>(customers);

DataSourceResult result=customerDTOs.ToDataSourceResult(dataSourceRequest); if (dataSourceRequest.Groups.Count> 0 )
{
dataEnvelope=new DataEnvelope<CustomerDTO>
{
GroupedData=result.Data.Cast<AggregateFunctionsGroup>().ToList(),
TotalItemCount=result.Total
};
} else {
dataEnvelope=new DataEnvelope<CustomerDTO>{
CurrentPageData=result.Data.Cast<CustomerDTO>().ToList(),
TotalItemCount=result.Total
};
} return dataEnvelope;
} Now, when im calling the method FetchPagedData() the filters are set correctly. However, in GetLazy() the filters are not. The correct amount of filters is set, but every set filter is empty with the operator IsEqualTo. Why is that and how can I fix it? I tried building my own object with the filters and recreate it from there, but I can't access the members of IFilterDescriptor. Any help is much appreciated!
