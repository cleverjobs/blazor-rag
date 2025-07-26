# Values from previously selected row

## Question

**Lar** asked on 04 Mar 2021

Is it possible to capture field value (namely Id) from a selected row in a grid when selecting a different row? I read a post that sounded like using some kind of leave event is probably impractical as a feature request but that templates can be used along with StateChanged events. I've been experimenting with that but I seem to only be able to get an Id from the current row selected, and I also need to retain the Id from the last row that was selected prior to selecting a different row.

## Answer

**John** answered on 04 Mar 2021

hook up to the rowselect event, have a variable "selectedRow" and update/compare that in that method?

### Response

**Larry** answered on 05 Mar 2021

That's along the lines of what I'm attempting. So far I'm only able to pull the Id value of the currently selected row. It seems that I need to figure out how retain the Id from the previously selected row into some kind of temp storage in order to make the comparison. I don't have the option of using something like a 'BeforeRowSelect' to retain the old value to use for comparison before it's overridden with current row selected. With that in mind I'm still a long way from getting proficient with Blazor and the Telerik grid so I'm hoping that there is a fairly easy trick for something like this.

### Response

**Nadezhda Tacheva** answered on 09 Mar 2021

Hi Larry, Here is an example of how to achieve the desired behavior using the approach suggested by John. You can use a variable to store the previous selection and use it where needed - see the code comments for more details. <h6>Selected: @CurrSelectedEmployee.Name</h6>
<h6>Last Selected: @LastSelectedEmployee.Name</h6>

<TelerikGrid Data=@GridData
SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<Employee> employeeList)=> OnSelect(employeeList))" SelectedItems="@SelectedItems" Pageable="true" Height="300px">
<GridColumns>
<GridColumn Field=@nameof(Employee.Name) />
<GridColumn Field=@nameof(Employee.Team) Title="Team" />
</GridColumns>
</TelerikGrid>

@code { public List<Employee> GridData { get; set; } public IEnumerable <Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); public Employee CurrSelectedEmployee { get; set; }=new Employee(); public Employee LastSelectedEmployee { get; set; }=new Employee(); protected void OnSelect ( IEnumerable<Employee> employees ) { //store the selection in a variable and do not update it with the value from the SelectedItemsChanged EventCallback LastSelectedEmployee=CurrSelectedEmployee; //update the current selection with the value from the SelectedItemsChanged EventCallback CurrSelectedEmployee=employees.FirstOrDefault(); // update the collection so that the grid can highlight the correct item // when two-way binding is used this happens automatically, but the framework does not allow two-way binding and the event at the same time SelectedItems=new List<Employee> { CurrSelectedEmployee };
} //data generation and model protected override async Task OnInitializedAsync ( ) {

GridData=new List<Employee>(); for ( int i=0; i <15; i++)
{
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3 });
}
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; }
}
} If any further questions appear after reviewing and testing the above snippet, please do not hesitate to contact us. Regards, Nadezhda Tacheva
