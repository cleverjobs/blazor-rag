# Preselect row from code in SelectionMode="GridSelectionMode.Single" mode

## Question

**And** asked on 15 Apr 2020

Hello, is it possible to pre-select the very first row in Grid in SelectionMode="GridSelectionMode.Single"? I need to do that by default when the Grid displays the very first time. I have second grid that based on this selection. I have already implemented the proper way of populating the second Grid and now just need to display display the first row selected. Thanks.

## Answer

**Marin Bratanov** answered on 16 Apr 2020

Hi Andrey, Here's how this should work: initialize the selected items collection so that the grid knows which item is selected update the SelectedEmployee (from the docs example - it is a separate field for clarity, you could use the collection) update the SelectedItems collection in the SelectedItemsChanged handler (as is the norm with one-way binding for a two-way bindable parameter) call the method that will populate the second grid when needed (e.g., in OnInitialized and in OnSelect) That said, here's an example that works fine for me: <TelerikGrid Data=@GridData
SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<Employee> employeeList)=> OnSelect(employeeList))" SelectedItems="@SelectedItems" Pageable="true" Height="300px">
<GridColumns>
<GridColumn Field=@nameof (Employee.Name) />
<GridColumn Field=@nameof (Employee.Team) Title="Team" />
</GridColumns>
</TelerikGrid>

@if (TeamMatesList !=null )
{
<h6>@SelectedEmployee.Team</h6>
<TelerikGrid Data="@TeamMatesList">
<GridColumns>
<GridColumn Field=@nameof (Employee.Name) />
</GridColumns>
</TelerikGrid>
}

@code { public List<Employee> GridData { get; set; } public List<Employee> TeamMatesList { get; set; } public IEnumerable<Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); public Employee SelectedEmployee { get; set; } protected override async Task OnInitializedAsync ( ) {

GridData=new List<Employee>(); for ( int i=0; i <15; i++)
{
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3 });
}

SelectedItems=new List<Employee> { GridData.FirstOrDefault() };
SelectedEmployee=GridData.FirstOrDefault(); await GetChildGridData();
} async Task GetChildGridData ( ) { if (TeamMatesList==null )
{
TeamMatesList=new List<Employee>();
}
TeamMatesList.Clear();
TeamMatesList=GridData.Where(empl=> empl.Team==SelectedEmployee.Team).ToList();
} protected async Task OnSelect ( IEnumerable<Employee> employees ) {
SelectedEmployee=employees.FirstOrDefault();
SelectedItems=new List<Employee> { SelectedEmployee }; await GetChildGridData();
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; }
}
} I've also updated the docs with this better example that also showcases how to properly initialize the collections. Regards, Marin Bratanov
