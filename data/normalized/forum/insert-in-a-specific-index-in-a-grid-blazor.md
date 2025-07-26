# Insert in a specific index in a grid Blazor

## Question

**Dav** asked on 11 Apr 2022

I am considering purchasing blazor components. I'm doing tests with the trial version. I would like to know if it is possible to insert new data in a specific grid position. Specifically, I would like to insert the data after the selected row of the grid.

## Answer

**Svetoslav Dimitrov** answered on 11 Apr 2022

Hello Davide, I am happy to report that you can insert a new item in the Grid at any position you would like. In this specific instance, in the handler for the OnCreate event, you can check the index of the SelectedItem in the collection passed to the Data parameter of the Grid and use the Insert() method and use the index to insert the item at the given position. Below, you can see a sample code snippet where such an approach is implemented. @using System.ComponentModel.DataAnnotations @* for the validation attributes *@Use the command buttons to control the CUD operations.
<br />
<strong>Editing is cancelled for the first two records</strong>.

<TelerikGrid Data=@MyData
EditMode="@GridEditMode.Inline" Pageable="true" Height="500px" SelectionMode="@GridSelectionMode.Single" @bind-SelectedItems="@SelectedItems" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler" OnCancel="@CancelHandler">
<GridToolBar>
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Title="ID" Editable="false" />
<GridColumn Field=@nameof(SampleData.Name) Title="Name" />
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
<GridCommandButton Command="Delete" Icon="delete">Delete</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { private IEnumerable <SampleData> SelectedItems { get; set; }=Enumerable.Empty<SampleData>(); void EditHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // prevent opening for edit based on condition if (item.ID <3 )
{
args.IsCancelled=true; // the general approach for cancelling an event }

Console.WriteLine( "Edit event is fired." );
} async Task UpdateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // perform actual data source operations here through your service await MyService.Update(item); // update the local view-model data with the service data await GetGridData();

Console.WriteLine( "Update event is fired." );
} async Task DeleteHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // perform actual data source operation here through your service await MyService.Delete(item); // update the local view-model data with the service data await GetGridData();

Console.WriteLine( "Delete event is fired." );
} async Task CreateHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; var selectedItem=SelectedItems.FirstOrDefault(); var indexOfSelectedItem=MyData.IndexOf(selectedItem); await MyService.Create(item, indexOfSelectedItem ); // perform actual data source operation here through your service // update the local view-model data with the service data await GetGridData();

Console.WriteLine( "Create event is fired." );
} async Task CancelHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // if necessary, perform actual data source operation here through your service Console.WriteLine( "Cancel event is fired." );
} // in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; }
[ Required ] public string Name { get; set; }
} public List<SampleData> MyData { get; set; } async Task GetGridData ( ) {
MyData=await MyService.Read();
} protected override async Task OnInitializedAsync ( ) { await GetGridData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <SampleData> _data { get; set; }=new List<SampleData>(); public static async Task Create ( SampleData itemToInsert, int index ) { int indexToInsert=index + 1; itemToInsert.ID=_data.Count + 1;
_data.Insert( indexToInsert, itemToInsert);
} public static async Task<List<SampleData>> Read()
{ if (_data.Count <1 )
{ for ( int i=1; i <50; i++)
{
_data.Add( new SampleData()
{
ID=i,
Name="Name " + i.ToString()
});
}
} return await Task.FromResult(_data);
} public static async Task Update ( SampleData itemToUpdate ) { var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
} public static async Task Delete ( SampleData itemToDelete ) {
_data.Remove(itemToDelete);
}
}
} Regards, Svetoslav Dimitrov Progress Telerik
