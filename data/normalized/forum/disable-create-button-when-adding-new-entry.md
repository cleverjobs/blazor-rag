# Disable create button when adding new entry

## Question

**BobBob** asked on 19 Feb 2021

Is there any way to disable the ListViewCommandButton with Command "Add" after it is clicked? The problem I am having is that users are accidentally clicking on the "Add" button again instead of the "Save" button when adding a new row to the ListView. I would like to disable the Add button while the Add new row dialog is open and not enable it again until they either click Save or Cancel button on the new row.

## Answer

**Eric R | Senior Technical Support Engineer** answered on 20 Feb 2021

Hi Bob, Thank you for the detailed description. In this case, the ListViewCommandButton exposes an OnClick event and an Enabled property. I recommend creating a boolean page variable that, when true, the Add button is enabled, and when false, the button is disabled. Let me provide an example of this below. Example Using the ListView Editing example, we can add an IsEnabled variable to the page, intialize it to true and then use a ClickHandler to set IsEnabled to false. Then in the OnUpdate, OnEdit, and OnCancel event handlers we can set it to true. See the following code snippets for how to do this. The Component Markup <TelerikListView Data="@ListViewData" Pageable="true" OnCreate="@CreateHandler" OnDelete="@DeleteHandler" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnCancel="@CancelHandler"> <EditTemplate> <div style="border: 1px solid green; margin: 10px; padding: 10px; display: inline-block;"> <TelerikTextBox @bind-Value="@context.Name" Label="Name" /> <br /> <TelerikDropDownList Data="@Teams" @bind-Value="@context.Team" /> <ListViewCommandButton Command="Save" Icon="save"> Save </ListViewCommandButton> <ListViewCommandButton Command="Cancel" Icon="cancel"> Cancel </ListViewCommandButton> </div> </EditTemplate> <Template> <div style="border: 1px solid black; margin: 10px; padding: 10px; display: inline-block;"> Employee: @context.Id <br /> Name: @context.Name in team: @context.Team <ListViewCommandButton Command="Edit" Icon="edit" OnClick="@IsEnabledHandler"> Edit </ListViewCommandButton> <ListViewCommandButton Command="Delete" Icon="delete"> Delete </ListViewCommandButton> </div> </Template> <HeaderTemplate> <ListViewCommandButton Command="Add" Icon="plus" Enabled=" @IsEnabled " OnClick=" @IsEnabledHandler "> Add Employee </ListViewCommandButton> <p> In this sample, the first item will not open for editing because of the code in the OnEdit handler </p> </HeaderTemplate> </TelerikListView> The @code Section List<Employee> ListViewData { get; set; }
List<string> Teams { get; set; } bool IsEnabled=true; void IsEnabledHandler ( EventArgs args ) { IsEnabled=false; } async Task UpdateHandler ( ListViewCommandEventArgs args ) {
Employee item=(Employee)args.Item; // perform actual data source operation here through your service await MyService.Update(item); // update the local view-model data with the service data await GetListViewData(); // Re-enable Add button after a succesful update IsEnabled=true; } async Task DeleteHandler ( ListViewCommandEventArgs args ) {
Employee item=(Employee)args.Item; // perform actual data source operation here through your service await MyService.Delete(item); // update the local view-model data with the service data await GetListViewData();
} async Task CreateHandler ( ListViewCommandEventArgs args ) {
Employee item=(Employee)args.Item; // perform actual data source operation here through your service await MyService.Create(item); // update the local view-model data with the service data await GetListViewData(); // Re-enable Add button after a succesful create IsEnabled=true; } void EditHandler ( ListViewCommandEventArgs e ) {
Employee currItem=e.Item as Employee; // prevent opening an item for editing on condition if (currItem.Id <2 )
{
e.IsCancelled=true; // Re-enable Add button after a logically cancelled edit IsEnabled=e.IsCancelled; }
} void CancelHandler ( ListViewCommandEventArgs e ) {
Employee changedItem=e.Item as Employee; // this is the item as the user edited it, but chose to cancel editing/inserting Console.WriteLine( $"user changed item {changedItem.Id} to have Name: {changedItem.Name} and Team: {changedItem.Team} " ); // Re-enable Add button after a cancelled event IsEnabled=true; } // data and models follow async Task GetListViewData ( ) {
ListViewData=await MyService.Read();
Teams=await MyService.GetTeams();
} protected override async Task OnInitializedAsync ( ) { await GetListViewData();
} public class Employee { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; }
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <Employee> _data { get; set; }=new List<Employee>(); private static List<string> _teams=new List<string> { "Sales", "Dev", "Support" }; public static async Task Create ( Employee itemToInsert ) {
itemToInsert.Id=_data.Count + 1;
_data.Insert( 0, itemToInsert);
} public static async Task<List<Employee>> Read()
{ if (_data.Count <1 )
{ for ( int i=1; i <50; i++)
{
_data.Add( new Employee()
{
Id=i,
Name=$"Name {i} ",
Team=_teams[i % _teams.Count]
});
}
} return await Task.FromResult(_data);
} public static async Task<List<string>> GetTeams()
{ return await Task.FromResult(_teams);
} public static async Task Update ( Employee itemToUpdate ) { var index=_data.FindIndex(i=> i.Id==itemToUpdate.Id); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
} public static async Task Delete ( Employee itemToDelete ) {
_data.Remove(itemToDelete);
}
} Wrapping Up Please give the above implementation a try and let me know the results. Thank you for using the Blazor forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Bob** answered on 23 Feb 2021

Thank you, that worked perfect. I didn't realize you could use both the OnClick and the Command items on the buttons.
