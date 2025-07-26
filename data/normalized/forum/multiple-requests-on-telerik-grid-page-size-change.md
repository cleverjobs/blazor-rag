# Multiple requests on telerik grid page size change

## Question

**Sus** asked on 06 Sep 2022

I have a telerik grid having paginations functionality. On page change, sorting I need to make a request to server, get the filtered data and populate it in the telerik grid. I have used the OnRead="ReadItems" event of telerik grid to achieve this functionality. Issue: When I am in any page other than 1 and I change the number of items per page, it makes multiple calls to the function ReadItems. This will make multiple api calls. How can I achieve all the filtering functionalities without making multiple calls? Code: <TelerikGrid TItem="@Employee" OnRead="@ReadItems" PageSizeChanged="@PageSizeChangedHandler" Pageable="true" PageSize="@PageSize"> <GridSettings> <GridPagerSettings PageSizes="@PageSizes"> </GridPagerSettings> </GridSettings> <GridColumns> <GridColumn Field=@nameof(Employee.Id) Title="ID" /> <GridColumn Field=@nameof(Employee.Name) Title="Name" /> </GridColumns> </TelerikGrid> @code {

int PageSize { get; set; }=15;
int CurrentPage { get; set; }=3;
protected List<int?> PageSizes { get; set; }=new List<int?> { 15, 30, 50 };
bool pageSizeChanged=false;
protected async Task ReadItems(GridReadEventArgs args)
{

Console.WriteLine("pageSizeChanged: " + pageSizeChanged);
Console.WriteLine("Page: " + args.Request.Page);

Console.WriteLine("data requested: " + args.Request);

DataEnvelope DataResult=await FetchPagedData(args.Request.Page, args.Request.PageSize);
args.Data=DataResult.CurrentPageData;
args.Total=DataResult.TotalItemCount;
}

public async Task <DataEnvelope> FetchPagedData(int pageNumber, int pageSize)
{
Console.WriteLine("Making api call");
List <Employee> fullList=new List <Employee> ();

int totalCount=100;
for (int i=1; i <=totalCount; i++)
{
fullList.Add(new Employee()
{
Id=i,
Name="Name " + i,
});
}

DataEnvelope result=new DataEnvelope();

result.CurrentPageData=fullList.Skip(pageSize * (pageNumber - 1)).Take(pageSize).ToList();
result.TotalItemCount=fullList.Count;

await Task.Delay(1000);

return result;
}

public class DataEnvelope
{
public List <Employee> CurrentPageData { get; set; }
public int TotalItemCount { get; set; }
}

public class Employee
{
public int Id { get; set; }
public string Name { get; set; }
}

void PageSizeChangedHandler(int newPageSize)
{
pageSizeChanged=true;
PageSize=newPageSize;
Console.WriteLine("PageSize: " + PageSize);
}
}

## Answer

**Tsvetomir** answered on 09 Sep 2022

Hi Susan, Thank you for taking the time to share the steps needed to replicate the defect with the multiple OnRead event triggers. Indeed, this is a bug on our side and I have logged it in our public feedback portal. You should be automatically subscribed to the item so whenever a change in its status is present - you'll get notified. Kind regards, Tsvetomir Progress Telerik
