# Grid: Changing Color of text in Header cell on Filter changed

## Question

**Vol** asked on 06 May 2024

Hello, i want to change the color of a header cell text when the user enters some filter criteria for this column in the filter row. can you help me? How can i implement this? best regards Volkhard

## Answer

**Hristian Stefanov** answered on 06 May 2024

Hi Volkhard, To change the header color of the currently filtered column, use the HeaderClass parameter to target the corresponding column and apply the desired color via CSS. Use also the Grid state to track which column is filtered. Here is an example I have prepared for you: @using Telerik.DataSource
@using Telerik.DataSource.Extensions <style>.k-header. @(FilteredColumn) { background-color: #FFF0F5; color: #191970;
} </style> <TelerikGrid Data=@GridData FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Pageable="true" Height="400px" OnStateChanged="@( (GridStateEventArgs<Employee> args)=> OnGridStateChanged(args) )"> <GridColumns> <GridColumn Field=@nameof(Employee.Name) HeaderClass="name" /> <GridColumn Field=@nameof(Employee.Age) HeaderClass="age" /> <GridColumn Field=@nameof(Employee.Date) HeaderClass="date" /> <GridColumn Field=@nameof(Employee.Vacation) HeaderClass="vacation" /> </GridColumns> </TelerikGrid> @code {
private List <Employee> GridData { get; set; } private string FilteredColumn { get; set; } private async Task OnGridStateChanged(GridStateEventArgs <Employee> args)
{
if(args.PropertyName=="FilterDescriptors")
{
if (args.GridState.FilterDescriptors.Count !=0)
{
var filterDescriptors=new List <IFilterDescriptor> (args.GridState.FilterDescriptors);
var filterDescriptor=filterDescriptors[0] as CompositeFilterDescriptor;
var filteredColumn=filterDescriptor.FilterDescriptors[0] as FilterDescriptor;

FilteredColumn=filteredColumn.Member.ToLower();
}
else
{
FilteredColumn=string.Empty;
}
}
} protected override void OnInitialized()
{
GridData=new List <Employee> ();
var rand=new Random();
for (int i=0; i <100; i++)
{
GridData.Add(new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Age=rand.Next(10, 80),
Date=DateTime.Now.Date.AddDays(rand.Next(-20, 20)),
Vacation=i % 3==0
});
}
}

public class Employee
{
public int? EmployeeId { get; set; }
public string Name { get; set; }
public int? Age { get; set; }
public DateTime Date { get; set; }
public bool Vacation { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Volkhard** commented on 07 May 2024

Hello Hristian, thanks for this - this was very helpfull.
