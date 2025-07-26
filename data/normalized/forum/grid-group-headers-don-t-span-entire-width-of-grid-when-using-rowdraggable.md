# Grid group headers don't span entire width of grid when using RowDraggable.

## Question

**Die** asked on 16 Dec 2021

Hi, I've noticed a problem with the Grid when using grouping as well as grid row drag and drop functionality. If both are enabled, the group headers don't span the entire width of the grid. The rendered data cell that represents the group header gets a colspan attribute that is 1 below the desired number. For example, if my Grid has grouping enabled and has 2 GridColums and 1 GridCheckboxColumn, the colspan should be 4 (see first attachment), which is correct. But, when I also enable the drag and drop functionality (using RowDraggable), the computed colspan is still 4, even though it should be scaled up to 5 (see second attachment). Is there any way we can override this behaviour, or is there any other work-around? Kind regards, Diederik

## Answer

**Marin Bratanov** answered on 18 Dec 2021

Hello Diederik, The Groupable feature cannot work with draggable rows, this is listed as its limitation: [https://docs.telerik.com/blazor-ui/components/grid/row-drag-drop#limitations.](https://docs.telerik.com/blazor-ui/components/grid/row-drag-drop#limitations.) If you enable both there will be an exception thrown. Regards, Marin Bratanov

### Response

**Diederik** commented on 07 Jan 2022

Hi Marin, I'm not using the "default" grouping feature. Instead, I'm using static grouping (where Groupable=false). This is working perfectly fine in combination with draggable rows and no exception is thrown. The only (visual) problem that arises is with the group header colspan as described above. The following simple example will reproduce the problem: @using Telerik. DataSource <TelerikGrid Data=" @_gridData " OnStateInit=" @( ( GridStateEventArgs <object> args)=> OnStateInitHandler (args) ) " Groupable="false" RowDraggable="true" Height="100%" Pageable="true" SelectionMode=" @GridSelectionMode. Multiple "> <GridColumns> <GridCheckboxColumn SelectAll="true" SelectAllMode=" GridSelectAllMode. All " /> <GridColumn Field=" @nameof ( Group. GroupId ) " FieldType=" @typeof ( int ) " Visible="false"> <GroupHeaderTemplate> @{ var groupedData=_grouping [( int )context. Value ]; } <div> City: <span class="bold"> @groupedData. City </span> </div> </GroupHeaderTemplate> </GridColumn> <GridColumn Title="Name" Field=" @( $ "Employee.{ nameof ( EmployeeModel. Name ) }" ) " /> <GridColumn Title="Age" Field=" @( $ "Employee.{ nameof ( EmployeeModel. Age ) }" ) " /> <GridColumn Title="City" Field=" @( $ "Employee.{ nameof ( EmployeeModel. City ) }" ) " /> </GridColumns> </TelerikGrid> @code { private record EmployeeModel { public string Name { get; init; }=string. Empty; public int Age { get; init; } public string City { get; init; }=string. Empty; } private Dictionary <int, GroupData> _grouping=new (); private class GroupData { public int GroupId { get; init; } public string City { get; init; }=string. Empty; } private List <EmployeeModel> _employees=new () { new EmployeeModel { Name="Brian", Age=25, City="London" }, new EmployeeModel { Name="Jason", Age=29, City="London" }, new EmployeeModel { Name="Sarah", Age=28, City="Berlin" }, new EmployeeModel { Name="Dorothy", Age=31, City="Berlin" } }; private class Group { public int GroupId { get; set; } public EmployeeModel? Employee { get; init; } } private List <Group> _gridData=new (); private void OnStateInitHandler ( GridStateEventArgs <object> args) { args. GridState=new GridState <object> () { GroupDescriptors=new List <GroupDescriptor> { new () { Member=nameof ( Group. GroupId ), MemberType=typeof ( int ), } } }; _grouping=_employees . GroupBy (g=> new { g. City }) . Select ((grouping, index)=> new GroupData () { GroupId=index, City=grouping. Key. City }) . ToDictionary (s=> s. GroupId ); var groupedEmployees=_employees. Select (employeeModel=> new Group { Employee=employeeModel }). ToList (); foreach ( var group in groupedEmployees) { var groupId=_grouping. First (kv=> kv. Value. City==group. Employee!. City ). Key; group. GroupId=groupId; } _gridData=groupedEmployees; } }

### Response

**Marin Bratanov** commented on 08 Jan 2022

That's still a grouped grid, Diederik, so it is not supported. You are likely getting an exception, too.

### Response

**Diederik** commented on 10 Jan 2022

I'm not getting any exception with the example above. This only happens when dynamic grouping is enabled (Groupable=true), which I don't use. For others encountering this problem, it is "solvable" by adding an extra column with an empty title and a width set to 0: <GridColumn Title="" Width="0" /> Kind regards, Diederik

### Response

**Rami** commented on 28 Feb 2025

Thank you Diederik, just bumped into the same issue with the group header and your work around with the 0 width column is perfect. It's weird that this grouping and dragging isn't officially supported when it works perfectly fine
