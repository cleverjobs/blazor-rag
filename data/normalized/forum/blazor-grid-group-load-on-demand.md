# Blazor Grid Group Load On Demand

## Question

**Rob** asked on 08 Oct 2024

Hi, We've implemented group load on demand in a grid and the rows in each group are editable. Is is possible to maintain the expanded state of a group after a row has been edited? I've amended the code in Toggle Group Load Mode at Runtime to show an example of the issue we have. @using Telerik.DataSource

<p>
<label>
<TelerikCheckBox Value="@GridLoadGroupsOnDemand" ValueChanged="@GridLoadGroupsOnDemandChanged" TValue="@bool" /> Load Groups On Demand
</label>
</p>

<TelerikGrid @ref="@GridRef" Data="@GridData" TItem="@Employee" Pageable="true" Sortable="true" Groupable="true" LoadGroupsOnDemand="@GridLoadGroupsOnDemand" FilterMode="GridFilterMode.FilterRow" OnStateInit="@OnGridStateInit" EditMode="@GridEditMode.Inline">
<GridColumns>
<GridColumn Field="@nameof(Employee.Name)" />
<GridColumn Field="@nameof(Employee.Team)" />
<GridColumn Field="@nameof(Employee.Salary)" />
<GridColumn Field="@nameof(Employee.OnVacation)" />
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil">Edit</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { private TelerikGrid<Employee>? GridRef { get; set; } private List<Employee> GridData { get; set; }=new (); private bool GridLoadGroupsOnDemand { get; set; } private void GridLoadGroupsOnDemandChanged ( bool newValue ) {
GridLoadGroupsOnDemand=newValue;

GridRef?.Rebind();
} private void OnGridStateInit ( GridStateEventArgs<Employee> args ) {
args.GridState.GroupDescriptors=new List<GroupDescriptor>();

args.GridState.GroupDescriptors.Add( new GroupDescriptor()
{
Member=nameof (Employee.Team),
MemberType=typeof ( string )
});
} protected override void OnInitialized () { var rnd=new Random(); for ( int i=1; i <=20; i++)
{
GridData.Add( new Employee()
{
Id=i,
Name="Name " + i,
Team="Team " + (i % 4 + 1 ),
Salary=( decimal )rnd.Next( 1000, 3000 ),
OnVacation=i % 3==0 });
}
} public class Employee { public int Id { get; set; } public string Name { get; set; }=string.Empty; public string Team { get; set; }=string.Empty; public decimal Salary { get; set; } public bool OnVacation { get; set; }
}
}

## Answer

**Dimo** answered on 09 Oct 2024

Hi Robert, I must admit that LoadGroupsOnDemand doesn't support programmatic group state control. I am sorry about that. Here are two relevant feature requests. I voted for them on your behalf: Persist groups' expanded / collapsed state after editing - shows a possible workaround when LoadGroupsOnDemand is false Manage group expanded / collapsed state programmatically when loading groups on demand Regards, Dimo Progress Telerik
