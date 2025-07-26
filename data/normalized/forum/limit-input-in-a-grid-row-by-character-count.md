# Limit input in a grid row by character count

## Question

**Kie** asked on 12 Dec 2020

Hi, In my Telerik Blazor grid, I'm looking to limit the amount of characters a user can input in a particular column. So in my column below I want the user only to be able to enter max 50 characters when they are adding or updating a row. <GridColumn Field="Description"> <Template> @((context as Model1).Desc.ToString()) </Template> </GridColumn> Thanks for any pointers!

## Answer

**Svetoslav Dimitrov** answered on 14 Dec 2020

Hello Kieran, You can take advantage of the item passed to your handler for the Create and Update operations to limit the number of characters. Below, I have made a sample implementation. If the length of the string is more than 50 when creating a new item a Notification component will appear. Could you give this example a try and see if it works as expected for you. If it does not you could follow up on our discussion so I can suggest a different approach. Editing is cancelled for the first two records.
<br />
<strong>There is a deliberate delay</strong> in the data source operations in this example to mimic real life delays and to showcase the async nature of the calls.

<TelerikNotification @ref="@NotificationReference"></TelerikNotification>

<TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="400px" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler" OnCancel="@CancelHandler">
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

@logger

@code { public TelerikNotification NotificationReference { get; set; } async Task EditHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; //prevent opening for edit based on condition if (item.ID <3 )
{
args.IsCancelled=true; //the general approach for cancelling an event }

AppendToLog( "Edit", args);
} async Task UpdateHandler ( GridCommandEventArgs args ) {
AppendToLog( "Update", args);

SampleData item=(SampleData)args.Item; // perform actual data source operations here through your service await MyService.Update(item); // update the local view-model data with the service data await GetGridData();
} async Task DeleteHandler ( GridCommandEventArgs args ) {
AppendToLog( "Delete", args);

SampleData item=(SampleData)args.Item; // perform actual data source operation here through your service await MyService.Delete(item); // update the local view-model data with the service data await GetGridData();

} async Task CreateHandler ( GridCommandEventArgs args ) {
AppendToLog( "Create", args);

SampleData item=(SampleData)args.Item; if (item.Name.Length> 50 )
{
NotificationReference.Show( new NotificationModel()
{
Text=$"The lenght of the Name is too long. Max 50 characters",
ThemeColor="error",
Closable=true,
CloseAfter=0 });
} else { // perform actual data source operation here through your service await MyService.Create(item); // update the local view-model data with the service data await GetGridData();
}
} async Task CancelHandler ( GridCommandEventArgs args ) {
AppendToLog( "Cancel", args);

SampleData item=(SampleData)args.Item; // if necessary, perform actual data source operation here through your service await Task.Delay( 1000 ); //simulate actual long running async operation } // this method and field just display what happened for visual cues in this example MarkupString logger; void AppendToLog ( string commandName, GridCommandEventArgs args ) { string currAction=string.Format( "<br />Command: <strong>{0}</strong>; is cancelled: <strong>{1}</strong>; is the item new: <strong>{2}</strong>",
commandName,
args.IsCancelled,
args.IsNew
);
logger=new MarkupString(logger + currAction);
} // in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; }
}

List<SampleData> MyData { get; set; } async Task GetGridData ( ) {
MyData=await MyService.Read();
} protected override async Task OnInitializedAsync ( ) { await GetGridData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API will look like and works for this standalone page public static class MyService { private static List <SampleData> _data { get; set; }=new List<SampleData>(); public static async Task Create ( SampleData itemToInsert ) { await Task.Delay( 1000 ); // simulate actual long running async operation itemToInsert.ID=_data.Count + 1;
_data.Insert( 0, itemToInsert);
} public static async Task<List<SampleData>> Read()
{ await Task.Delay( 1000 ); // simulate actual long running async operation if (_data.Count <1 )
{ for ( int i=1; i <50; i++)
{
_data.Add( new SampleData()
{
ID=i,
Name="Name " + i.ToString()
});
}
} return await Task.FromResult(_data);
} public static async Task Update ( SampleData itemToUpdate ) { await Task.Delay( 1000 ); // simulate actual long running async operation var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
} public static async Task Delete ( SampleData itemToDelete ) { await Task.Delay( 1000 ); // simulate actual long running async operation _data.Remove(itemToDelete);
}
}
} Regards, Svetoslav Dimitrov

### Response

**Kieran** answered on 14 Dec 2020

Hi Svetoslav, Thanks for the detailed reply. It works great when they get the notification - except that the row they were trying to add then disappears as the createhandler runs through. I would like the user to be able to change the character count of the field to get it below 50 - after they see the notification. Ideally the row should still be there for them to change until they get the count correct, or they cancel. Thanks, Kieran

### Response

**Svetoslav Dimitrov** answered on 16 Dec 2020

Hello Kieran, You can achieve this behavior by using our PopUp editing mode for the Grid. When the window opens and the user types a name longer than 50 characters a Validation message would appear and the window will not be closed until the string passes certain conditions. Would this be a suitable solution for your application? Below, I have put a sample implementation which you can give a try. Get back to me if I could further assist you. @using System.ComponentModel.DataAnnotations
@* Used for the model annotations only *@<strong>Editing is cancelled for the first two records.</strong>

<TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="500px" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler" OnCancel="@CancelHandler">
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

@code { void EditHandler ( GridCommandEventArgs args ) {
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
SampleData item=(SampleData)args.Item; // perform actual data source operation here through your service await MyService.Create(item); // update the local view-model data with the service data await GetGridData();

Console.WriteLine( "Create event is fired." );
} async Task CancelHandler ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item; // if necessary, perform actual data source operation here through your service Console.WriteLine( "Cancel event is fired." );
} // in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } [ Required(ErrorMessage="The employee must have a name" ) ]
[ MaxLength(50, ErrorMessage="Max lenght of the name is 50 characters" ) ] public string Name { get; set; } } public List<SampleData> MyData { get; set; } async Task GetGridData ( ) {
MyData=await MyService.Read();
} protected override async Task OnInitializedAsync ( ) { await GetGridData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <SampleData> _data { get; set; }=new List<SampleData>(); public static async Task Create ( SampleData itemToInsert ) {
itemToInsert.ID=_data.Count + 1;
_data.Insert( 0, itemToInsert);
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
} Regards, Svetoslav Dimitrov

### Response

**Kieran** answered on 17 Dec 2020

Thanks Svetoslav. That worked great with the popup edit mode too.
