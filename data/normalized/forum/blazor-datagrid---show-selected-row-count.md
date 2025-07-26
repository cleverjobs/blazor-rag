# Blazor DataGrid - show selected row count

## Question

**Hub** asked on 24 Apr 2023

Hi, we would like to change the grid in blazor so it shows the number of selected rows in the bottom right corner, where it now shows " 21 - 30 of 91 items". We would like to change it to something like " 21 - 30 of 91 items / selected: 5 items". Is there a way to achieve this? The paging part on the bottom left should stay as it is.

## Answer

**Justin** answered on 25 Apr 2023

Hello Hubert, To achieve the desired functionality, first use Two-way Binding of SelectedItems to track the number of selected items. Then, use the CSS workaround in this example in our REPL, to add the text and count to the paging element. Telerik Grid: <TelerikGrid Data=@GridData SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="SelectedItems" Pageable="true" @bind-Page="@GridPage " PageSize="@GridPageSize " Class=" custom-pager-info " Height="400px"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field=@nameof(Employee.Name) /> <GridColumn Field=@nameof(Employee.Team) Title="Team" /> </GridColumns> </TelerikGrid> <style>.custom-pager-info>.k-grid-pager.k-pager-info { font-size: 0;
}.custom-pager-info>.k-grid-pager.k-pager-info::before { font-size: 14px; content: " @GridPagerInfo ";
} </style> C# @code { int GridPage { get; set; }=1; int GridPageSize { get; set; }=10; int GridTotal=> GridData.Count; string GridPagerInfo=> $" {(GridPage - 1 ) * GridPageSize + 1 } - {GridPage * GridPageSize} of {GridTotal.ToString( "n0" )} items / selected: {SelectedItems.Count()} items"; public List<Employee> GridData { get; set; } public IEnumerable <Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); protected override void OnInitialized ( ) {
GridData=new List<Employee>(); for ( int i=0; i <15; i++)
{
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3 });
} // select Employee with 3 through 5. Not required SelectedItems=GridData.Skip( 2 ).Take( 3 ).ToList();
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; }
}
} I hope this helps. Regards, Justin Progress Telerik

### Response

**Hubert** commented on 02 May 2023

Thank you very much! Works perfectly!
