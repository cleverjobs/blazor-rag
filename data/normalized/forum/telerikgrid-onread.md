# TelerikGrid OnRead

## Question

**kha** asked on 05 Jan 2020

hello it seems there is a problem with OnRead in TelerikGrid when i try to use OnRead for virtual mode it works fine first time page renders it works and also on scroll it works too but when i navigate to another page and try to change the Data and then navigate back to the page it seems it kept the last state and i see the previous Data untill i use filter , sort , i scroll

## Answer

**Marin Bratanov** answered on 06 Jan 2020

Hello, The following seems to update the data correctly on my end. Please try comparing against it to see what is the difference causing the problem (make sure that you are using the Skip parameter of the data source request when using virtualization): <TelerikGrid Data=@GridData TotalCount=@Total
PageSize=15 OnRead=@ReadItems
ScrollMode="@GridScrollMode.Virtual" Height="300px" RowHeight="60">
<GridColumns>
<GridColumn Field=@nameof (Employee.Id) Title="ID" />
<GridColumn Field=@nameof (Employee.Name) Title="Name" />
</GridColumns>
</TelerikGrid>

<TelerikButton OnClick="@ChangeData">Change data</TelerikButton>

@code { public List<Employee> GridData { get; set; } public int Total { get; set; }=0;
Telerik.DataSource.DataSourceRequest lastRequest { get; set; } async Task ChangeData ( ) { await GetData();
} protected async Task ReadItems ( GridReadEventArgs args ) {
lastRequest=args.Request; await GetData();
} async Task GetData ( ) { //with Virtual Scrolling, make sure to use the Skip parameter for paging DataEnvelope DataResult=await FetchPagedData(lastRequest.Skip, lastRequest.PageSize);
GridData=DataResult.CurrentPageData;
Total=DataResult.TotalItemCount;

StateHasChanged();
} public async Task<DataEnvelope> FetchPagedData ( int skip, int pageSize ) {
List<Employee> fullList=new List<Employee>();

DateTime now=DateTime.Now; int totalCount=100; for ( int i=0; i <totalCount; i++)
{
fullList.Add( new Employee()
{
Id=i,
Name=$"Name {i} {now.Millisecond} " });
}

DataEnvelope result=new DataEnvelope();

result.CurrentPageData=fullList.Skip(skip).Take(pageSize).ToList();
result.TotalItemCount=fullList.Count; await Task.Delay( 2000 ); //simulate network delay from a real async call return result;
} public class DataEnvelope { public List<Employee> CurrentPageData { get; set; } public int TotalItemCount { get; set; }
} public class Employee { public int Id { get; set; } public string Name { get; set; }
}
} If I am missing something from the scenario, please modify this sample to showcase the problem so I can review the issue. If you need to send more files or some confidential data, you can also open a private support ticket from your account. Regards, Marin Bratanov
