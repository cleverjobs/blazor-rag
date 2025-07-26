# Reduce the width of the Group Cell

## Question

**Dan** asked on 23 Feb 2023

Hi, I'm looking for a way to reduce group-cell width for the whole grid. I found the css class ( ) <td class="k-table-td k-group-cell" role="gridcell"> </td> But i can' figure out how to do . Here's a picture Can u help me ?

## Answer

**Hristian Stefanov** answered on 28 Feb 2023

Hi Daniel, I confirm that you can reduce the group cell width with some CSS. I have prepared an example for you that shows the approach: <style>.my-grid.k-group-col { width: 0px;
} </style> Drag the column header of the "Team" and/or "On Vacation" column to the group panel at the top <TelerikGrid Class=" my-grid " Data=@GridData Groupable="true" Pageable="true" Height="400px"> <GridColumns> <GridColumn Field=@nameof(Employee.Name) Groupable="false" /> <GridColumn Field=@nameof(Employee.Team) Title="Team" /> <GridColumn Field=@nameof(Employee.IsOnLeave) Title="On Vacation" /> </GridColumns> </TelerikGrid> @code {
public List <Employee> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Employee> ();
var rand=new Random();
for (int i=0; i <15; i++)
{
GridData.Add(new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3,
IsOnLeave=i % 2==0
});
}
}

public class Employee
{
public int EmployeeId { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public bool IsOnLeave { get; set; }
}
} Please run and test it to see if the result covers your needs. Let me know if any difficulties appear upon testing. Regards, Hristian Stefanov
