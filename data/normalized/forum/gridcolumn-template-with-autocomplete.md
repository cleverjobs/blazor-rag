# GridColumn Template with AutoComplete

## Question

**Dre** asked on 20 Apr 2021

Hi, Trying to use AutoComplete within the Grid as the option to fill data on a column - with EditTemplate, however, when open to Add a new item, the list of values is not presented. Changing from AutoComplete to DropDownList, works as expected. Could you please indicate on the snippet below what is wrong? <GridColumn Field="@(nameof(ItemRateio.Projeto))" Title="Projeto" Width="150px"> <EditorTemplate> @{ var ItemToEdit=context as ItemRateio; <TelerikAutoComplete Data="@Projects" Placeholder="Selecione Projeto" @bind-Value="@ItemToEdit.Projeto"> </TelerikAutoComplete> } </EditorTemplate> </GridColumn> Projects is a List<string> and ItemRateio.Projeto is also a string. Thanks

## Answer

**Svetoslav Dimitrov** answered on 23 Apr 2021

Hello Marcello, From what I can see the code snippet is correct. To open the dropdown list part of the AutoComplete component you should start typing in the input part. This is the expected behavior of the component and you can see it from the AutoComplete online demo. I believe that this is the behavior you are describing in your post. If you would like to be able to open a dropdown list and still be able to type in the input you could see the ComboBox component. This component provides a filtering option and you can see the behavior from our online demo. Below, you can see a code snippet that includes a ComboBox in the EditorTemplate for the Grid. Could you run it and see if it is the expected behavior. <TelerikGrid Data=@MyData
EditMode="@GridEditMode.Inline" Pageable="true" Height="300px" OnCreate="@CreateHandler" OnUpdate="@UpdateHandler">
<GridToolBar>
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="ID" />
<GridColumn Field=@nameof(SampleData.Name) Title="Name" />
<GridColumn Field=@nameof(SampleData.Role) Title="Position"> <EditorTemplate>
@{
CurrentlyEditedEmployee=context as SampleData;

<TelerikComboBox Data="@Roles" @bind-Value="@CurrentlyEditedEmployee.Role" Filterable="true" FilterOperator="@StringFilterOperator.Contains"></TelerikComboBox>
}
</EditorTemplate> </GridColumn>
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code {
List<SampleData> MyData { get; set; }
List<string> Roles { get; set; }
SampleData CurrentlyEditedEmployee { get; set; } public async Task UpdateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // perform actual data source operations here through your service await MyService.Update(item); // update the local view-model data with the service data await GetGridData();
} async Task CreateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // perform actual data source operation here through your service await MyService.Create(item); // update the local view-model data with the service data await GetGridData();

Console.WriteLine( "Create event is fired." );
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public string Role { get; set; }
} async Task GetGridData ( ) {
MyData=await MyService.Read();
Roles=await MyService.GetRoles();
} protected override async Task OnInitializedAsync ( ) { await GetGridData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <SampleData> _data { get; set; }=new List<SampleData>(); private static List<string> Roles=new List<string> { "Manager", "Employee", "Contractor" }; public static async Task<List<SampleData>> Read()
{ if (_data.Count <1 )
{ for ( int i=1; i <50; i++)
{
_data.Add( new SampleData()
{
ID=i,
Name="Name " + i.ToString(),
Role=Roles[i % Roles.Count]
});
}
} return await Task.FromResult(_data);
} public static async Task<List<string>> GetRoles()
{ return await Task.FromResult(Roles);
} public static async Task Create ( SampleData itemToInsert ) {
itemToInsert.ID=_data.Count + 1;
_data.Insert( 0, itemToInsert);
} public static async Task Update ( SampleData itemToUpdate ) { var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
}
}
} Regards, Svetoslav Dimitrov
