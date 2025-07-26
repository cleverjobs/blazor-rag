# Change background color of a tooltip inside a grid

## Question

**CJCJ** asked on 28 Jan 2025

Hello, I want to change the background color of TelerikTooltip which is displayed inside a TelerikGrid in blazor. I have tried following two examples but they do not seem to work for tooltips in the grid. Change Tooltip color ? in UI for Blazor | Telerik Forums Blazor Custom ToolTip Styles and Colors - Telerik UI for Blazor This is an example of GridColumn in the TelerikGrid. Is there any other way to change the background color of the tooltip? <GridColumn Field="ABC" Title="Title" Width="15%"> <HeaderTemplate> <span class="k-column-title k-column-title-word-break"> Column Title </span> </HeaderTemplate> <Template> @{
var item=(MyModel)context;
} <div class="tooltip-target-a"> <MyCustomComponent /> </div> <TelerikTooltip TargetSelector=".tooltip-target-a" Position="@TooltipPosition.Top"> <Template Context="ttipContext"> <div> Hello from tooltip </div> </Template> </TelerikTooltip> </Template> </GridColumn> Thanks!

## Answer

**Tsvetomir** answered on 28 Jan 2025

Hello Charith, Generally, defining the Tooltip inside a Grid column template is not recommended because it could lead to unexpected behavior, like overlapping content. With that in mind, I recommend defining the Tooltip outside the Grid and applying the CSS styles from the second link that you've provided - Custom ToolTip Styles and Colors. For your convenience, I'm sharing a REPL example to see the result. Regards, Tsvetomir Progress Telerik

### Response

**CJ** commented on 28 Jan 2025

Hi Tsvetomir, Thanks for your reply. I have moved the tooltip out of the Grid , but still it doesn't work as per Blazor Custom ToolTip Styles and Colors - Telerik UI for Blazor example. Also, PERL example page you provided does not load? Can you please post the code in here? Regards!

### Response

**Tsvetomir** commented on 28 Jan 2025

Hi Charith, The provided REPL example is working on my side. However, I'm posting the code snippet here: <p> This example shows how to load content on demand for a tooltip that targets elements inside a Grid. Hover over an employee name. </p> <TelerikGrid Data="@GridData" Height="400px" Pageable="true"> <GridColumns> <GridColumn Field="@(nameof(Employee.Id))" Width="120px" /> <GridColumn Field="@(nameof(Employee.Name))" Title="Employee Name"> <Template> @{
Employee employee=(Employee)context; <span data-employeeId="@employee.Id" class="tooltip-target"> @employee.Name </span> } </Template> </GridColumn> <GridColumn Field="@(nameof(Employee.Team))" Title="Team" /> </GridColumns> </TelerikGrid> <TelerikTooltip TargetSelector=".tooltip-target " Position="@TooltipPosition.Right" Class="custom-tooltip"> <Template Context="ttipContext"> <h6> Employee Details </h6> </Template> </TelerikTooltip> <style>.custom-tooltip.k-tooltip { background: green;
}.custom-tooltip.k-tooltip.k-callout { color: green;
} </style> @code {
private List <Employee> GridData { get; set; }=new();

// This shows that the Tooltip will work even if the Grid is bound after the Tooltip is initialized.
protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
GridData=await GetEmployees();
StateHasChanged();
}
}

private async Task<List <Employee>> GetEmployees()
{
if (GridData==null || !GridData.Any())
{
GridData=Enumerable.Range(1, 90).Select(x=> new Employee
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
}).ToList();
}

return await Task.FromResult(GridData);
}

private Employee GetEmplyeeDetails(int employeeId)
{
Random rnd=new Random();
Employee employee=GridData.First(empl=> empl.Id==employeeId);
employee.Salary=rnd.Next(1000, 5000);
employee.ActiveProjects=rnd.Next(2, 10);
employee.HireDate=DateTime.Now.AddYears(-rnd.Next(1, 10)).AddMonths(-rnd.Next(0, 10)).AddDays(-rnd.Next(0, 10));

return employee;
}

public class Employee
{
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
public string Team { get; set; }=string.Empty;
public DateTime HireDate { get; set; }
public int ActiveProjects { get; set; }
public decimal Salary { get; set; }
}
} If you still face difficulties, let me know. Regards, Tsvetomir

### Response

**CJ** commented on 28 Jan 2025

Thanks Tsvetomir, that works! Just FYI, PERL Page doesn't load on my side and showing " An unhandled error has occurred. Reload " error at the bottom.
