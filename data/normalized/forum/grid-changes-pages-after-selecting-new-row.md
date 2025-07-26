# Grid changes pages after selecting new row

## Question

**Mic** asked on 27 Mar 2020

I'm having a problem with selecting a row after changing pages that is reproducible with the attached code. To reproduce, click on any row on the first page, 'Employee 5' for example. Once 'Employee 5' is highlighted, navigate to page 4 using the selector at the bottom. On page 4, click on 'Employee 35'. The grid will immediately jump back to page 1. If you return to page 4 you will see that 'Employee 35' is selected (highlighted), it just didn't stay on that page. Is this a bug or am I doing something wrong? @page "/gridtest" @inject IJSRuntime JsInterop <TelerikGrid Data=@GridData Page="currentPage" SelectionMode="GridSelectionMode.Single" @bind-SelectedItems="SelectedItems" Pageable="true" PageSize="10" Height="500px" Class="@theGridClass"> <GridColumns> <GridColumn Field=@nameof(Employee.Name) /> <GridColumn Field=@nameof(Employee.Team) Title="Team" /> </GridColumns> </TelerikGrid> <div class="row justify-content-center" style="margin-top:5px;"> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> SelectItem(1, 5))">Select 5</TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> SelectItem(2, 15))">Select 15</TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> SelectItem(3, 25))">Select 25</TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@(()=> SelectItem(4, 35))">Select 35</TelerikButton> </div> @code { string theGridClass { get; set; }="theSpecialGrid"; int currentPage=1; async Task SelectItem( int page, int rowId) { // Select Grid Page currentPage=page; // Select Row SelectedItems=GridData.Where(item=> item.EmployeeId==rowId).ToList(); await Task.Delay(20); //rougly one rendering frame so this has the chance to render in the browser await JsInterop.InvokeVoidAsync( "scrollToSelectedRow", "." + theGridClass); } public List<Employee> GridData { get; set; } public IEnumerable<Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); protected override void OnInitialized() { GridData=new List<Employee>(); for ( int i=0; i <55; i++) { GridData.Add( new Employee() { EmployeeId=i, Name="Employee " + i.ToString(), Team="Team " + i % 3 }); } } public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; } } }

## Answer

**Marin Bratanov** answered on 27 Mar 2020

Hello Michael, The problem here is that the Page parameter of the grid only takes the currentPage variable, but never sets it. So, when the grid has to re-render (e.g., when an item is selected), the value of that field is taken and the grid shows the corresponding page. That's a typical problem when using only one-way binding and it is solved either by using two-way binding, or by manually updating the variable in a corresponding event (such as PageChanged ). That said, here's the simplest solution: <TelerikGrid Data=@GridData @bind- Page="currentPage" SelectionMode="GridSelectionMode.Single" @bind-SelectedItems="SelectedItems" Pageable="true" PageSize="10" Height="500px" Class="@theGridClass"> Regards, Marin Bratanov

### Response

**Michael** answered on 27 Mar 2020

Makes sense. Thanks!
