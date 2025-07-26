# avoid multiple calls of async UpdateHandler when pressing enter

## Question

**Mir** asked on 02 Nov 2020

Hi, I have a problem that you described here: [https://docs.telerik.com/blazor-ui/components/grid/editing/incell](https://docs.telerik.com/blazor-ui/components/grid/editing/incell) Unfortunately your proposed solution doesn't work or am I missing something? I am using an EditorTemplate with a method called ChangeHandler(). After clicking in another row everything works fine but if I leave the cell by pressing enter the UpdateHandler gets called more than two times and comparing args.Item with the GridItem doesn't help because the calls are asynchronous. I implemented it like this: public async Task ChangeHandler( ) { var state=Grid?.GetState(); if (state.EditItem !=null ) { await UpdateHandler( new GridCommandEventArgs() { Item=state.EditItem, Field=state.EditField }); } state.OriginalEditItem=state.EditItem=default; await Task.Delay(50); // let the grid re-render and close the cell if keyboard navigation is enabled await Grid?.SetState(state); } public async Task UpdateHandler(GridCommandEventArgs args) { var viewModel=args.Item as ViewModel; var index=GridItems.FindIndex(i=> i.Id==viewModel.Id); if (index !=-1) { if (GridItems[index].Equals(viewModel)) return; ...some more code //save data UpdateGridMengen(viewModel); ... StateHasChanged(); } }

## Answer

**Joana** answered on 04 Nov 2020

Hello Miriam, Thank you for bringing this issue to us. When using templates, we provide flexibility for the content in them, and thus we leave the editor to define when to update/cancel edit operation. However, indeed capturing the Enter key on a grid cell results in two calls of the Update handler using the snippet from the documentation article. Also, it brings an inconsistency in how we handle keyboard interaction and how we handle mouse interaction. So, I've raised a discussion with our development team about the configuration of EditorTemplates in the Grid, and we do think that we could improve our code. After reviewing the possible resolutions, we believe that the best approach to go with is by adding a context in the EditorTemplate that will allow our users to Save/Cancel changes without the usage of the Grid State. This will clear the code and here is a small dummy snippet how it would look like: <EditorTemplate> <TelerikTextBox @bind-Value=@context.Item.Name OnChange="@(()=> context.Save())" Width="100%" /> </EditorTemplate> However, such change will introduce a breaking change, and we should carefully research it and plan it accordingly for 3.0 release. In the meantime, using the article that you referred to, I could suggest the following workaround to capture the bubbling Enter key and prevent the update execution in the handler: <TelerikGrid @ref="@Grid" Data=@MyData EditMode="@GridEditMode.Incell" Pageable="true" Height="500px" OnUpdate="@UpdateHandler" Navigable="true"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Name"> <EditorTemplate> @{
currentItem=context as SampleData; <span @onkeydown="@OnKeyDown"> <TelerikTextBox @bind-Value=@currentItem.Name OnChange="@CloseEditor" Width="100%" /> </span> } </EditorTemplate> </GridColumn> <GridColumn Field=@nameof(SampleData.Ranking) Title="Ranking" Width="120px"> <EditorTemplate> @{
currentItem=context as SampleData; <TelerikNumericTextBox @bind-Value=@currentItem.Ranking OnChange="@CloseEditor" Width="100%" Max="10" Min="0" Step="1"> </TelerikNumericTextBox> } </EditorTemplate> </GridColumn> <GridColumn Field=@nameof(SampleData.Role) Title="Position" Width="200px"> <EditorTemplate> @{
currentItem=context as SampleData; <TelerikDropDownList Data="@Roles" @bind-Value="@currentItem.Role" OnChange="@CloseEditor" Width="120px" PopupHeight="auto"> </TelerikDropDownList> } </EditorTemplate> </GridColumn> <GridCommandColumn> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Save </GridCommandButton> </GridCommandColumn> </GridColumns> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add Employee </GridCommandButton> </GridToolBar> </TelerikGrid> @code {
// handling the custom editor template for InCell editing
public TelerikGrid <SampleData> Grid { get; set; }
public SampleData currentItem { get; set; } public bool ShouldUpdateItem { get; set; } public void OnKeyDown(KeyboardEventArgs args)
{
if (args.Key=="Enter")
{
ShouldUpdateItem=false;
}
} async Task CloseEditor()
{
var state=Grid?.GetState();

if (currentItem.ID==0 && state.InsertedItem !=null)
{
// insert operation - the item is new
await CreateHandler(new GridCommandEventArgs()
{
Item=state.InsertedItem
});
}
else
if (currentItem.ID> 0 && state.EditItem !=null)
{
// edit operation on an existing item

await UpdateHandler(new GridCommandEventArgs()
{
Item=state.EditItem,
Field=state.EditField
});
}

state.InsertedItem=state.OriginalEditItem=state.EditItem=default;

await Task.Delay(20); // let the grid re-render and close the cell if keyboard navigation is enabled

await Grid?.SetState(state);
}

//Create and Update operations

async Task UpdateHandler(GridCommandEventArgs args)
{
SampleData item=(SampleData)args.Item; if (ShouldUpdateItem==false)
{
ShouldUpdateItem=true;
return;
} var index=MyData.FindIndex(i=> i.ID==item.ID);
if (index !=-1)
{
// with keyboard navigation and Enter key press in the component
// both the grid, and the OnChange handler will raise the update event
// you may want to add an equality comparison for the item to only call the database once
// when the item has changed, not both times
if (!MyData[index].Equals(item))
{
MyData[index]=item;
Console.WriteLine("update");
//perform actual data source operations here
}
}
}

// data sources

protected override void OnInitialized()
{
MyData=new List <SampleData> ();

for (int i=1; i <50; i ++)
{ MyData.Add ( new SampleData ()
{ ID=i, Name="name " + i, Ranking=i % 10 });
}
} public class SampleData { public int ID { get; set; } public string Name { get; set; } public string Role { get; set; } public int Ranking { get; set; } public override bool Equals ( object obj )
{ if ( obj!=null && obj is SampleData )
{ SampleData curr=obj as SampleData; return ( ID==curr.ID) && ( Name==curr.Name) && ( Role==curr.Role) && ( Ranking==curr.Ranking); } return false;
}
} List <SampleData> MyData { get; set; }
static List <string> Roles=new List <string> { "Manager", "Employee", "Contractor" };
} Let me know if I could assist you further. Regards, Joana

### Response

**Joana** answered on 04 Nov 2020

Hey Miriam, As a follow-up, I logged a feature request in our portal on your behalf where you could track its progress. [https://feedback.telerik.com/blazor/1493770](https://feedback.telerik.com/blazor/1493770) Regards, Joana

### Response

**Miriam** answered on 09 Nov 2020

Thank you very much! I used the workaround and it works fine :)

### Response

**Miriam** answered on 11 Nov 2020

Hi, now I discovered another Problem: Your solution works fine as long as I do not enter the very first value in my grid and it makes no difference which row is changed. When I enter the first value then the UpdateHandler does not get triggered. Only my ChangeHandler. Do you have an idea why this is happening?

### Response

**Joana** answered on 13 Nov 2020

Hello Miriam, It seems that I have missed this when I was testing the solution. My apologies for that. The issue stems from the default value of the flag that we created for this case. public bool ShouldUpdateItem { get; set; }=true; ShouldUpdateItem default value should be true, to accept the first call of the Update handler. I hope this will fullfil your scenario. Let me know if I could help you further. Regards, Joana
