# Multiple toolbars

## Question

**Nik** asked on 26 Sep 2019

Hello! Is there a way to have multiple GridToolBar's? If i add multiple ToolBar's to the grid, only the last one is used. It would be very nice to have multiple ToolBars below each other (with more GridCommand types likes Dropdown Lists, ...) Greetings, Niklas

## Answer

**Marin Bratanov** answered on 27 Sep 2019

Hi Niklas, The toolbar is basically a property that gets set and only the last value will have actual effect. Would you agree that the actual feature you need is to be able to put arbitrary HTML/Components in the toolbar of the grid so you can create a more complex layout? If so, here's a basic example based off the Toolbar article: @result

<TelerikGrid Data=@MyData Pageable="true" PageSize="15" EditMode="@GridEditMode.Inline" Height="500px" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler">
<GridToolBar>
<div style="background:yellow">
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</div>
<div style="background: green;">
<TelerikDropDownList Data="@( new List<string>() { " first ", " second ", " third " } )" TValue="string" TItem="string" ValueChanged="@( (string itm)=> result=itm )"></TelerikDropDownList>
</div>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof (SampleData.Name) Title="Employee Name" />
<GridColumn Field=@nameof (SampleData.HireDate) Title="Hire Date" />
<GridCommandColumn>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { string result; private void UpdateHandler ( GridCommandEventArgs args ) {
SampleData alteredItem=args.Item as SampleData;

result=string.Format( "Employee with ID {0} now has name {1} and hire date {2}", alteredItem.ID, alteredItem.Name, alteredItem.HireDate);

StateHasChanged();
} private void CreateHandler ( GridCommandEventArgs args ) {
SampleData alteredItem=args.Item as SampleData;

result=string.Format( "On {2} you added the employee {0} who was hired on {1}.", alteredItem.Name, alteredItem.HireDate, DateTime.Now);

StateHasChanged();
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov
