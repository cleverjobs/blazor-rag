# TelerikGrid<T>.TotalCount inaccessible after updating from 4.0.1 to 4.3.0

## Question

**Twa** asked on 21 Jun 2023

After updating from UI for Blazor 4.0.1 to 4.3.0 I'm getting the following error: Error CS0122 'GridBase<T>.TotalCount' is inaccessible due to its protection level The closest I have found to get that information is grid.Data.Count() but I am not sure that is the right way. So, here's my question: How to access TotalCount from now on? Regards. Twain.

### Response

**Twain** commented on 26 Jun 2023

Forget about using grid.Data.Count(). Isn't a valid alternative.

### Response

**Hristian Stefanov** commented on 26 Jun 2023

Hi Twain, I can confirm that in our most recent updates, the "TotalCount" property was intentionally removed from the Grid component to streamline and enhance our API. The decision to remove the property was primarily motivated by the fact that the Grid did not have a "TotalCount" parameter in its razor markup, and exposing the property "TotalCount" through its reference was not considered a best practice. However, I would appreciate it if you could provide further details on why utilizing the "grid.Data.Count()" approach as an alternative is not suitable for your specific scenario. Understanding your specific requirements will enable me to better assist you in finding an appropriate solution. I eagerly await your response. Thank you for your cooperation. Thank you. Kind Regards, Hristian

### Response

**Twain** commented on 27 Jun 2023

Hi Hristian, I'm using TotalCount value as part of the dynamic calculation of the rows quantity that fit the current grid size. protected override async Task OnWindowResized () {
Task<int> calculateTask=CalculateGridPageSize(_credentialsGridRef.Id); // Get the page size based on grid size _credentialGridPageSize=await calculateTask; // Check for safe pagination if (_credentialsGridRef.CurrentPage * _credentialGridPageSize> _credentialsGridRef.TotalCount)
{ var div=( double )_credentialsGridRef.TotalCount / _credentialGridPageSize;
_credentialsGridRef.CurrentPage=Convert.ToInt32(Math.Ceiling(div));
} // We're outside of the component's lifecycle, it has to be re-render. StateHasChanged();
} If TotalCount is less than the current page multiplied by the grid's page size, it would display a page with no values. Therefore, I calculate which page to display based on the new values. Hope this information will be useful. Regards. Twain.

### Response

**Hristian Stefanov** commented on 30 Jun 2023

Hi Twain, Thank you for providing us with additional information. I have shared it with our development team for further analysis. Still, to assist you in achieving the desired outcome and provide a suitable solution, we need some further clarification: Could you please explain the purpose and functionality of the "CalculateGridPageSize" function? Understanding its role will help us better comprehend the scenario. It would be helpful to know the initial state of the Grid before resizing the Window and the desired state you wish to achieve after the resizing. This information will assist us in identifying the specific behavior you are aiming for. Could you please clarify what you mean by "check for safe pagination"? Understanding the context and requirements of this check will aid us in addressing the pagination aspect appropriately. In order to better understand the behavior you described, can you please send a small runnable sample that demonstrates the issue? This will allow us to thoroughly investigate the behavior and provide you with a more tailored solution. For your convenience, you can use the REPL platform to share the sample, eliminating the need to attach an entire project. As always, we highly appreciate your cooperation, and we eagerly await hearing from you. Kind Regards, Hristian

### Response

**Twain** commented on 03 Jul 2023

Hi Hristian. Added some comments to your questions: Could you please explain the purpose and functionality of the "CalculateGridPageSize" function? Understanding its role will help us better comprehend the scenario. The CalculateGridPageSize function utilizes JSInterop to retrieve the size of document.getElementById('grid_name').getElementsByClassName('k-grid-content').item(0).clientHeight and calculates the number of rows that can be displayed in the grid without any vertical scroll bars. It would be helpful to know the initial state of the Grid before resizing the Window and the desired state you wish to achieve after the resizing. This information will assist us in identifying the specific behavior you are aiming for. It doesn't seem necessary to delve into this. It is not related. Could you please clarify what you mean by "check for safe pagination"? Understanding the context and requirements of this check will aid us in addressing the pagination aspect appropriately. 'Safe Pagination' refers to not being positioned on the incorrect page of the grid. Essentially, this recalculates the page where we should be positioned after the size of the grid has changed (and consequently the pageSize). My implementation prevents vertical scrolling in grids when their size changes. This is accomplished by recalculating the pageSize of the grid whenever its size changes. To achieve this, I use JavaScript to retrieve the height of the grid's content. Then, based on the height of a row, I calculate how many rows can fit in the grid and perform the pagination accordingly. Best regards. Twain.

### Response

**Hristian Stefanov** commented on 06 Jul 2023

Hi Twain, Thank you once again for your cooperation and patience. Based on all the information provided so far, I assume that the reason "grid.Data.Count()" may not be a suitable alternative is due to the usage of the OnRead event. In this case, to obtain the number of rows, you can rely on the "datasourceResult.Total", which is set to "args.Total" within the OnRead handler. Please refer to the highlighted part in the code snippet below: @using Telerik.DataSource.Extensions Rows number: <strong> @RowsNumber </strong> <TelerikGrid @ref="@GridRef" TItem="Employee" OnRead="@ReadItems" FilterMode="@GridFilterMode.FilterRow" Sortable="true" Pageable="true"> <GridColumns> <GridColumn Field=@nameof(Employee.ID) /> <GridColumn Field=@nameof(Employee.Name) Title="Name" /> <GridColumn Field=@nameof(Employee.HireDate) Title="Hire Date" /> </GridColumns> </TelerikGrid> @code {
TelerikGrid <Employee> GridRef{ get; set; }
public List <Employee> SourceData { get; set; } public int RowsNumber { get; set; } protected async Task ReadItems(GridReadEventArgs args)
{
Console.WriteLine("data requested: " + args.Request);

//update the Data and Total properties
//the ToDataSourceResult() extension method can be used to perform the operations over the full data collection
//in a real case, you can call data access layer and remote services here instead, to fetch only the necessary data

await Task.Delay(1000); //simulate network delay from a real async call var datasourceResult=SourceData.ToDataSourceResult(args.Request); args.Data=datasourceResult.Data; RowsNumber=args.Total=datasourceResult.Total; //get rows number }

protected override void OnInitialized()
{
SourceData=GenerateData();
}

private List <Employee> GenerateData()
{
var result=new List <Employee> ();
var rand=new Random();
for (int i=0; i <100; i++)
{
result.Add(new Employee()
{
ID=i,
Name="Name " + i,
HireDate=DateTime.Now.Date.AddDays(rand.Next(-20, 20))
});
}

return result;
}

public class Employee
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}
} I hope this information proves helpful to you. Please let me know if there are any further details I may have overlooked in the scenario or if you require further assistance. Kind Regards, Hristian

### Response

**Twain** commented on 20 Jul 2023

Hello Hristian. Thank you very much for the alternative solution. Actually, I came up with a very similar one on my own. I still prefer the one I originally developed, but apparently, it won't be possible to use it. Sorry for the delay in responding; I've just returned to work. Regards. Twain

### Response

**Doug** commented on 17 Jan 2024

It would be great to have the TotalCount field. When using the Grid Search the grid filters the rows by the search value. However, I don't see a way to determine the number of rows being shown after a search. So, let's say there are 100 rows and I enter the search term "ohio". Within the rows only 10 have ohio in them, so 10 rows are displayed. Using the GridReference I have no way to determine how many rows are currently being displayed. I am not using OnRead, instead I'm using the Data property. Is there a way to expose the TotalCount field? That field has the data I would like to use.

### Response

**Hristian Stefanov** commented on 22 Jan 2024

Hi Doug, Thank you for sharing your insights on the removal of the TotalCount field. I confirm that there's still a way to determine the number of rows after a search by utilizing the OnStateChanged event. We've documented this approach in a knowledge base article, which includes a runnable sample and more in-depth details on how to extract the needed information from the state: Get Filtered and Sorted Data from Grid. Feel free to let me know if you encounter any challenges in applying the above approach. Kind Regards, Hristian

### Response

**Doug** commented on 23 Jan 2024

Hi Hristian, I actually just implemented that yesterday, but it basically performs the filtering twice and takes a long time to process when there are 1000+ rows. It is not a good solution performance-wise. Can Telerik just expose the TotalCount field? The solution presented in that link also adds quite a few lines of code for a field that is available without all that code if it is just marked as public. Thanks, Doug

### Response

**Hristian Stefanov** commented on 25 Jan 2024

Hi Doug, I'm glad to hear that you already explored that OnStateChanged option. It is also true that using OnRead with 1000+ rows is more performance-wise. Regarding the "TotalCount" removal, I confirm that our statement remains the same - this property was intentionally removed from the Grid component to streamline and enhance our API. The decision to remove the property was primarily motivated by the fact that the Grid did not have a "TotalCount" parameter in its razor markup, and exposing the property "TotalCount" through its reference is not considered a best practice. Kind Regards, Hristian
