# start grid cell edit from row click

## Question

**Cla** asked on 21 Jan 2025

Hi, as you can see from the sample below, i would like to edit a cell from row click (in addition to click on the editable cell), but if i click on the row (in other column who is not editable) the edit start and immediately stop. How to solve? In addition i would like to have the editing row selected Thanks [https://blazorrepl.telerik.com/cTObGvvb54Hji0uL20](https://blazorrepl.telerik.com/cTObGvvb54Hji0uL20)

## Answer

**Dimo** answered on 23 Jan 2025

Hello Claudio, The issue occurs due to a race condition, as the Grid is not designed to start editing when clicking on a non-editable cell. Please move the edit initiation code to OnAfterRenderAsync. I also recommend to optimize the custom logic, so that it's executed only when clicking on a non-editable cell. Otherwise it's not necessary. <TelerikGrid @ref="Grid" Data="Data" SelectionMode="GridSelectionMode.Single" EditMode="GridEditMode.Incell" OnUpdate="OnGridUpdate" OnRowClick="@OnGridRowClick"> <GridColumns> <GridColumn Editable="false" Field="Id" /> <GridColumn Field="ReceiptDate" /> </GridColumns> </TelerikGrid>

@code {
private TelerikGrid<Model> Grid { get; set; }
private List<Model> Data { get; set; } private Model? ItemToEdit; protected override void OnInitialized ( ) {
base.OnInitialized();

Data=new List<Model> { new Model ( ) { Id=Guid.NewGuid(), ReceiptDate=DateTime.Now }, new Model ( ) { Id=Guid.NewGuid(), ReceiptDate=DateTime.Now }, new Model ( ) { Id=Guid.NewGuid(), ReceiptDate=DateTime.Now }
};
} private void OnGridRowClick ( GridRowClickEventArgs args ) { if (args.Field==nameof(Model.Id))
{
ItemToEdit=(Model)args.Item;
}
} protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (ItemToEdit !=null )
{ var gridState=Grid.GetState(); if (gridState.EditItem !=null ) return;

gridState.EditField=nameof(Model.ReceiptDate);
gridState.OriginalEditItem=ItemToEdit;
gridState.EditItem=ItemToEdit.Clone(); await Grid.SetStateAsync(gridState);
} await base.OnAfterRenderAsync(firstRender);
}

private async Task OnGridUpdate ( GridCommandEventArgs args ) { ItemToEdit=null; var item=(Model)args.Item; var dataItem=Data.FirstOrDefault( obj=> obj.Id==item.Id); if (dataItem !=null )
dataItem.ReceiptDate=item.ReceiptDate;
}

public class Model {
public Guid Id { get; set; }
public DateTime ReceiptDate { get; set; }

public Model Clone ( ) { return new Model
{
Id=Id,
ReceiptDate=ReceiptDate
};
}
}
} Regards, Dimo Progress Telerik

### Response

**Claudio** commented on 23 Jan 2025

Thanks for the sample, it work but if i start edit a cell, and click on another row, it close the current cell editing and i need to click another one in the new row to start edit. I would like to pass from one row edit to another one with a single click on the desired row, and if i click on a row with an edit in progress it must remain in edit and not close the edit cell. It is possible to handle? Thanks

### Response

**Dimo** commented on 23 Jan 2025

The event sequence when clicking on another cell while in edit mode is: OnRowClick OnUpdate OnAfterRenderAsync What happens is that OnUpdate deletes ItemToEdit before it can be used on OnAfterRenderAsync. You can modify the logic like this: private DateTime LastRowClick { get; set; }=DateTime.Now; private void OnGridRowClick ( GridRowClickEventArgs args ) { LastRowClick=DateTime.Now; if (args.Field==nameof (Model.Id))
{
ItemToEdit=(Model)args.Item;
}
} private async Task OnGridUpdate ( GridCommandEventArgs args ) { var now=DateTime.Now; // optional, helps debugging if (now - LastRowClick> new TimeSpan( 0, 0, 1 ))
{
ItemToEdit=null;
} var item=(Model)args.Item; var dataItem=Data.FirstOrDefault(obj=> obj.Id==item.Id); if (dataItem !=null )
dataItem.ReceiptDate=item.ReceiptDate;
}

### Response

**Claudio** commented on 23 Jan 2025

i put your sample in a repl, but it seem still not working: [https://blazorrepl.telerik.com/QpOFGRPx238vuc6320](https://blazorrepl.telerik.com/QpOFGRPx238vuc6320) click from an editing row to another, close the source row edit but does not open the new one in edit mode, also click on an editing row close the edit in progress instead of mantain the row in edit.

### Response

**Dimo** commented on 23 Jan 2025

Hm, my previous suggestion only works in server apps. Here is another example that works both in Server and WebAssembly mode: [https://blazorrepl.telerik.com/mzulQHFx53VuJXEU18](https://blazorrepl.telerik.com/mzulQHFx53VuJXEU18) I admit that I don't like the approach, so I would think of ways to adjust the user behavior, rather than push the code to its limits. Why would a user click repetitively on cell A and expect to edit cell B?

### Response

**Claudio** commented on 23 Jan 2025

Thanks Dimo, your last sample code works fine! I have a grid with a single editable column and the goal is to focus the user to compile the only editable field when managing the grid, indipendent on where he click.
