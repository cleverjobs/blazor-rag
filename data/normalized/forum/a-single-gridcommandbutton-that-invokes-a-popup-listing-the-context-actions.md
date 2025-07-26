# A single GridCommandButton that invokes a popup listing the context actions

## Question

**Adr** asked on 23 Mar 2021

I have a grid and on each row context you can perform 10+ action. I don't want to add 10+ different GridCommandButtons as that wouldn't look good. I would like to have a single button on each row that the user can click and when its clicked a popup of available actions appears for them to select. Is that possible on a Blazor Grid ? I would like it to look something like this image.

## Answer

**Marin Bratanov** answered on 24 Mar 2021

Hi Adrian, You can use the context menu component for that. You can show it through code on an event of your choice (say, @onclick) of any button in the grid. You can store the current row model for use in the context menu clicks too. You can find similar examples here: [https://docs.telerik.com/blazor-ui/components/contextmenu/integration.](https://docs.telerik.com/blazor-ui/components/contextmenu/integration.) The context menu also offers the separators I see in the provided screen recording. As for invoking actions on the grid - you can use the grid state to, for example, put an item in edit mode: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) The rest of the actions seem custom actions anyway. To get the row model you would have to use a "regular" grid column, not a command column. The command column will provide the current row when this is implemented. Another UX approach would be using a split button when it becomes available: [https://feedback.telerik.com/blazor/1435750-split-button.](https://feedback.telerik.com/blazor/1435750-split-button.) If you would prefer that, Vote and Follow that feature. Regards, Marin Bratanov Progress Telerik

### Response

**Adrian** answered on 24 Mar 2021

Thanks. I have it working when right-clicking on a row but need it to work when left-clicking on the GridCommandButton. I'm struggling to trigger the ContextMenu from the OnClick event of a GridCommandButton. The GridCommandEventArgs doesn't contain MouseEventArgs so am not able to position the context menu next to the GridCommandButton. Do you have any examples of doing this? Many thanks.

### Response

**Marin Bratanov** answered on 25 Mar 2021

Hi Adrian, You can use a regular button whose onclick event gives you the MouseEventArgs. Here's an example I made for you based on the docs example, tweaked to use left click: @using System.Collections.Generic
@using System.Collections.ObjectModel

<TelerikContextMenu @ref="@ContextMenuRef" Data="@MenuItems" OnClick="@((MenuItem item)=> OnItemClick(item))"></TelerikContextMenu>

<TelerikGrid Data="@GridData" @ref="@GridRef" EditMode="@GridEditMode.Inline" Height="500px" Pageable="true" OnCreate="@CreateItem" OnUpdate="@UpdateHandler" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedItems">
<GridToolBar>
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Editable="false" />
<GridColumn Field=@nameof(SampleData.Name) /> <GridColumn>
<Template>
<span @onclick:stopPropagation="true">
<TelerikButton OnClick="@( (MouseEventArgs e)=> ShowRowOptions(e, context as SampleData) )" Icon="more-vertical"></TelerikButton>
</span>
</Template>
</GridColumn> </GridColumns>
</TelerikGrid>

@if (SelectedItems.Any())
{
<ul>
@foreach ( var item in SelectedItems)
{
<li>@item.Name</li>
}
</ul>
}

@code { //data sources ObservableCollection<SampleData> GridData { get; set; }
List<MenuItem> MenuItems { get; set; }
IEnumerable<SampleData> SelectedItems { get; set; }=Enumerable.Empty<SampleData>(); //metadata for the context menu actions SampleData SelectedPerson { get; set; } //component references so we can use their methods TelerikContextMenu<MenuItem> ContextMenuRef { get; set; }
TelerikGrid<SampleData> GridRef { get; set; } // sample menu item class public class MenuItem { public string Text { get; set; } public string Icon { get; set; } public Action Action { get; set; } public string CommandName { get; set; }
} // show the context menu for a particular row async Task ShowRowOptions ( MouseEventArgs e, SampleData row ) {
SelectedPerson=row; await ContextMenuRef.ShowAsync(e.ClientX, e.ClientY);
} // sample handling of the context menu click async Task OnItemClick ( MenuItem item ) { // one way to pass handlers is to use an Action, you don't have to use this if (item.Action !=null )
{
item.Action.Invoke();
} else { // or you can use local code to perform a task // such as put a row in edit mode or select it switch (item.CommandName)
{ case "BeginEdit": // read more at [https://localhost/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item](https://localhost/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item) var currState=GridRef.GetState();
currState.InsertedItem=null;
SampleData itemToEdit=SampleData.GetClonedInstance(GridData.Where(itm=> itm.ID==SelectedPerson.ID).FirstOrDefault());
currState.OriginalEditItem=itemToEdit; await GridRef.SetState(currState); break; case "ToggleSelect": var selItems=SelectedItems.ToList(); if (SelectedItems.Contains(SelectedPerson))
{
selItems.Remove(SelectedPerson);
} else {
selItems.Add(SelectedPerson);
}
SelectedItems=selItems; break; default: break;
}
}
SelectedPerson=null; // clean up } // generate data protected override void OnInitialized ( ) { // context menu items MenuItems=new List<MenuItem>()
{ new MenuItem(){ Text="Select", Icon="checkbox-checked", CommandName="ToggleSelect" }, new MenuItem(){ Text="Edit", Icon="edit", CommandName="BeginEdit" }, new MenuItem(){ Text="Delete", Icon="delete", Action=DeleteItem }
}; // generate data for the grid GridData=new ObservableCollection<SampleData>(); var rand=new Random(); for ( int i=0; i <100; i++)
{
GridData.Add( new SampleData()
{
ID=i,
Name="Employee " + i.ToString(),
});
}
} // CUD operations for the grid async Task CreateItem ( GridCommandEventArgs args ) { var argsItem=args.Item as SampleData; // call the actual data service here argsItem.ID=GridData.Count + 1;

GridData.Insert( 0, argsItem);
} void DeleteItem ( ) // not async so it can be passed as an Action { var argsItem=SelectedPerson; // call the actual data service here GridData.Remove(argsItem);
} async Task UpdateHandler ( GridCommandEventArgs args ) { var argsItem=args.Item as SampleData; // call the actual data service here var index=GridData.ToList().FindIndex(i=> i.ID==argsItem.ID); if (index !=-1 )
{
GridData[index]=argsItem;
}
} public class SampleData { public int ID { get; set; } public string Name { get; set; } public override bool Equals ( object obj ) { if (obj is SampleData)
{ return this.ID==(obj as SampleData).ID;
} return false;
} public SampleData ( ) {

} public SampleData ( SampleData itmToClone ) { this.ID=itmToClone.ID; this.Name=itmToClone.Name;
} public static SampleData GetClonedInstance ( SampleData itmToClone ) { return new SampleData(itmToClone);
}
}
} Regards, Marin Bratanov Progress Telerik
