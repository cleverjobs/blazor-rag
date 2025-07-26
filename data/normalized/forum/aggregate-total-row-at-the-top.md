# Aggregate/total row at the top

## Question

**Eri** asked on 15 Jan 2023

Is there a way to display the totals row at the top of the grid instead of at the bottom?

## Answer

**Hristian Stefanov** answered on 18 Jan 2023

Hi Eric, You can achieve the desired result by using the GroupHeaderTemplate. Here is a sample I have prepared for you: REPL link. Please run and test it to see if the result suits your scenario needs. If further assistance is needed, let me know. Regards, Hristian Stefanov

### Response

**Eric** commented on 18 Jan 2023

Assuming I am understanding the groupheadertemplate functionality, it appears it will only show the values in in the group header for columns that are grouped. In my case I don't want to group by anything, just show totals at the top. I would also like to have the sum total for each column over each column, like another row (or the header row). I should mentioned that my grid has upwards of 50+ columns. Is that possible? Thanks in advance.

### Response

**Hristian Stefanov** commented on 23 Jan 2023

Hi Eric, Thank you for getting back to me with more information about the scenario. Now, as far as I understand, you are not using grouping, and the desired result is to move the FooterTemplate (totals) to the top of the Grid columns. That is easily achievable with some custom CSS styles for the position. I have prepared a new sample for you that seems to cover your scenario needs: <style>.my-grid.k-grid-footer { position: absolute; border-bottom: solid; border-bottom-width: 1px; border-bottom-color: rgba ( 0, 0, 0, 0.08 ); /* required for responsiveness */ width: 100%;
}.my-grid.k-grid-header { margin-top: 55px;
} </style> <TelerikGrid Class="my-grid" Data=@GridData Pageable="true" Height="500px"> <GridAggregates> <GridAggregate Field=@nameof(Employee.Name) Aggregate="@GridAggregateType.Count" /> <GridAggregate Field=@nameof(Employee.Team) Aggregate="@GridAggregateType.Count" /> <GridAggregate Field=@nameof(Employee.Salary) Aggregate="@GridAggregateType.Max" /> <GridAggregate Field=@nameof(Employee.Salary) Aggregate="@GridAggregateType.Sum" /> </GridAggregates> <GridColumns> <GridColumn Field=@nameof(Employee.Name) Groupable="false"> <FooterTemplate> Total: @context.Count employees. <br /> @{
// you can use aggregates for other fields/columns by extracting the desired one by its
// field name and aggregate function from the AggregateResults collection
// The type of its Value is determined by the type of its field - decimal for the Salary field here
decimal salaries=(decimal)context.AggregateResults
.FirstOrDefault(r=> r.AggregateMethodName=="Sum" && r.Member=="Salary")?.Value;
}
Total salaries: @salaries.ToString("C0") </FooterTemplate> </GridColumn> <GridColumn Field=@nameof(Employee.Team) Title="Team"> <FooterTemplate> Total: @context.Count teams. </FooterTemplate> </GridColumn> <GridColumn Field=@nameof(Employee.Salary) Title="Salary" /> <GridColumn Field=@nameof(Employee.ActiveProjects) Title="Active Projects" /> </GridColumns> </TelerikGrid> @code {
public List <Employee> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Employee> ();
var rand=new Random();
for (int i=0; i <15; i++)
{
Random rnd=new Random();
GridData.Add(new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3,
Salary=rnd.Next(1000, 5000),
ActiveProjects=i % 4==0 ? 2 : 5
});
}
}

public class Employee
{
public int EmployeeId { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public decimal Salary { get; set; }
public int ActiveProjects { get; set; }
}
} The sample uses " Class " to specify the desired component instance. Please run and test it to see the result. Kind Regards, Hristian
