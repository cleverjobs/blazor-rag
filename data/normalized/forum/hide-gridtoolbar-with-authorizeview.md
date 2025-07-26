# Hide GridToolBar with AuthorizeView

## Question

**Ger** asked on 28 Jan 2021

I have the following: <GridToolBar> <AuthorizeView> <GridCommandButton Command="Add" Icon="add">Add Product</GridCommandButton> </AuthorizeView> </GridToolBar> It works, except a visible, empty tool bar is still rendered. Is there an elegant way to get it to not render when there are no buttons in it. My first attempt to wrap the entire GridToolBar in an AuthorizeView component doesn't work. Regards, Gerhard

## Answer

**Marin Bratanov** answered on 29 Jan 2021

Hi Gerhard, The toolbar renders if its template (render fragment) is not null, something like @if (@GridToolBar !=null )
{
render the contents here
} Once you put the AuthorizeView there, the render fragment is never null anymore, even if the authorize view renders empty. So, the grid will render its toolbar always. So, a way to define the toolbar conditionally is to create the render fragment with your own code and decide whether to return null or not, something like the following snippet, where your application logic can determine the value of the flag (not a button like in this example): @result

<TelerikButton OnClick="@( ()=> HasToolbar=!HasToolbar )">Toggle toolbar</TelerikButton>

<TelerikGrid Data=@MyData Pageable="true" PageSize="15" EditMode="@GridEditMode.Inline" Height="500px" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler" GridToolBar="@GetToolbarTemplate()">
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="Employee ID" />
<GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" />
<GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" />
<GridCommandColumn>
<GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { bool HasToolbar { get; set; }=false; public RenderFragment GetToolbarTemplate ( ) { //if toolbar is not allowed return null so it does not render if (!HasToolbar)
{ return null;
} RenderFragment ToolbarTemplate=__builder=>
{
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
}; return ToolbarTemplate; } //sample data and crud string result; public List<SampleData> MyData { get; set; } private async Task UpdateHandler ( GridCommandEventArgs args ) {
SampleData item=args.Item as SampleData; // perform actual data source operations here through your service SampleData updatedItem=await MyService.Update(item); // update the local view-model data with the service data await GetGridData();

result=string.Format( "Employee with ID {0} now has name {1} and hire date {2}", updatedItem.ID, updatedItem.Name, updatedItem.HireDate);
} private async Task CreateHandler ( GridCommandEventArgs args ) {
SampleData item=args.Item as SampleData; // perform actual data source operations here through your service SampleData insertedItem=await MyService.Create(item); // update the local view-model data with the service data await GetGridData();

result=string.Format( "On {2} you added the employee {0} who was hired on {1}.", insertedItem.Name, insertedItem.HireDate, DateTime.Now);
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} async Task GetGridData ( ) {
MyData=await MyService.Read();
} protected override async Task OnInitializedAsync ( ) { await GetGridData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <SampleData> _data { get; set; }=new List<SampleData>(); public static async Task<SampleData> Create ( SampleData itemToInsert ) {
itemToInsert.ID=_data.Count + 1;
_data.Insert( 0, itemToInsert); return await Task.FromResult(itemToInsert);
} public static async Task<List<SampleData>> Read()
{ if (_data.Count <1 )
{ for ( int i=1; i <50; i++)
{
_data.Add( new SampleData()
{
ID=i,
Name="Name " + i.ToString(),
HireDate=DateTime.Now.AddDays(-i)
});
}
} return await Task.FromResult(_data);
} public static async Task<SampleData> Update ( SampleData itemToUpdate ) { var index=_data.FindIndex(i=> i.ID==itemToUpdate.ID); if (index !=-1 )
{
_data[index]=itemToUpdate; return await Task.FromResult(_data[index]);
} throw new Exception( "no item to update" );
}
}
} Another approach would be to keep using the authorize view to hide the contents of the toolbar, but to hide the toolbar with CSS depending on the user role (this snippet is based on the one above with the simple bool flag with the button, but you can tie it to the actual user rights): <style>.no-toolbar.k-toolbar { display: none;
} </style> <TelerikButton OnClick="@( ()=> HasToolbar=!HasToolbar )"> Toggle toolbar </TelerikButton> <TelerikGrid Data=@MyData Pageable="true" PageSize="15" EditMode="@GridEditMode.Inline" Height="500px" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler" Class="@( HasToolbar ? " ": " no-toolbar " )"> <GridToolBar> <AuthorizeView> <GridCommandButton Command="Add" Icon="add"> Add Employee </GridCommandButton> </AuthorizeView> </GridToolBar> Regards, Marin Bratanov

### Response

**Gerhard** answered on 29 Jan 2021

Neither approach is pretty per se, but if it works hey? I'll try the CSS approach first. Thank you Marin.

### Response

**Marin Bratanov** answered on 29 Jan 2021

Hello Gerhard, I've seen a number of people do that - either if-blocks around some buttons, or some conditional CSS. So, I'd say it's a viable option. Regards, Marin Bratanov
