# Grid with inline edit: How to add new row and manage save / cancel request from code?

## Question

**Cla** asked on 21 Apr 2022

Hi, I would like to implement a grid with inline edit, but i would like to have full control over insert / save / cancel events and not delegate this tasks to the embedded grid functionality. So i need to manage my action buttons inside my page, instead of GridCommandButton. How to raise the Add / Edit / Delete / Save / Cancel tasks from my buttons? What methods i need to call? Thanks

## Answer

**Dimo** answered on 21 Apr 2022

Hello Claudio, We have a related demo in the Grid State documentation. To exit edit mode, set EditItem and OriginalEditItem to null. Saving will depend entirely on you, as far as I understand. Regards, Dimo

### Response

**Claudio** commented on 26 Apr 2022

Hi Dimo, Reading the docs you linked i can now manage add row with inline mode, but not edit an existing row. I tried the sample code with my environment, in particular the EditItemFour method in the sample, but the row does not go in edit mode. The only difference to the sample code is who i use the OnRead event to retrieve the grid data, and not set the Data property. I replied the issue with a sample code [https://blazorrepl.telerik.com/repl/embed/GwaewrvF30r0w9wR51?editor=true&result=true&errorList=true](https://blazorrepl.telerik.com/repl/embed/GwaewrvF30r0w9wR51?editor=true&result=true&errorList=true) if i use the Data attribute instead of the OnRead callback, edit row start fine, but i need to use OnRead to handle complex data read (pagination, filters...) What's wrong? Thanks

### Response

**Claudio** answered on 28 Apr 2022

I solved the problem with a workaround; The root cause of the issue is when SetState of grid is called, it raise OnRead callback. I call SetState to set the grid state in edit mode, setting GridState.EditItem and GridState.OriginalEditItem but this settings are lost immediatly after due to OnRead callback who reset the items of the grid. My workaround in OnRead method is: 1. Check if grid is in edit mode (Grid.GetState().EditItem !=null) 2. If grid is in edit mode set GridReadEventArgs.Data and GridReadEventArgs.Total to the last read values and exit method 3. If grid is not in edit mode, read the data, set GridReadEventArgs.Data and GridReadEventArgs.Total and save this values in a variable who store the last values read. private async Task OnReadAsync(GridReadEventArgs args)
{
//If edit mode return the last values read
var gridState=Grid?.GetState();
if (gridState?.EditItem !=null)
{
args.Data=CurrentData;
args.Total=CurrentTotal;
return;
}

//Read data from server
.var result=HttpServer.GetData();
args.Data=result.Data;
args.Total=result.Total;

//Update last values read
CurrentData=result.Data;
CurrentTotal=result.Total;
} This solution seem to work but i think raise OnRead when update the grid state to edit is a bug. It will be solved? There is a better solution? Thanks

### Response

**Dimo** commented on 29 Apr 2022

Claudio - hm, this workaround does not seem to be necessary on my side. See the test page below. Maybe there is something else in play here within the app. On a side note, it is expected for the Grid to call OnRead after SetState (). This is because the new state often applies settings that require a data request (new sorting or filtering state, etc.) The behavior is also documented (since version 3.0.1, the better way to refresh data is via Rebind ). @using Telerik.DataSource
@using Telerik.DataSource.Extensions

<TelerikButton OnClick="@StartInsert">Start Insert operation</TelerikButton> <TelerikButton OnClick="@EditUserCompanyAsync"> Edit Selected Row </TelerikButton> <TelerikGrid @ref="@GridRef" TItem="@Product" OnRead="@ReadGridData" EditMode="@GridEditMode.Inline" Navigable="true" OnUpdate="@UpdateItem" OnDelete="@DeleteItem" OnCreate="@CreateItem" Pageable="true" SelectionMode="@GridSelectionMode.Single" @bind-SelectedItems="@SelectedRows"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add New Item </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field=@nameof(Product.ProductName) Title="Product Name" /> <GridColumn Field=@nameof(Product.UnitPrice) Title="Unit Price" /> <GridColumn Field=@nameof(Product.UnitsInStock) Title="Units In Stock" /> <GridColumn Field=@nameof(Product.Discontinued) Title="Discontinued" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Delete" Icon="delete"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code {
List<Product> GridData { get; set; }
TelerikGrid<Product> GridRef { get; set; }
IEnumerable<Product> SelectedRows { get; set; }=new List<Product>(); async Task ReadGridData ( GridReadEventArgs args ) { await Task.Delay( 200 ); // simulate some network delay DataSourceResult result=GridData.ToDataSourceResult(args.Request);
args.Data=result.Data;
args.Total=result.Total;
} async Task StartInsert ( ) { var currState=GridRef.GetState(); // reset any current editing. Not mandatory. currState.EditItem=null;
currState.OriginalEditItem=null; // add new inserted item to the state, then set it to the grid // you can predefine values here as well (not mandatory) currState.InsertedItem=new Product ( ) { ProductName="some predefined value" }; await GridRef.SetState(currState); // note: possible only for Inline and Popup edit modes, with InCell there is never an inserted item, only edited items } async Task EditUserCompanyAsync ( ) { //Determinazione elemento in fase di edit var editItem=GridRef.SelectedItems.FirstOrDefault(); if (editItem==null ) return; var currState=GridRef.GetState();

currState.InsertedItem=null;
currState.OriginalEditItem=editItem;
currState.EditItem=editItem.Clone(); await GridRef.SetState(currState);
}

private void CreateItem ( GridCommandEventArgs args ) { var argsItem=args.Item as Product;

argsItem.ProductId=GridData.Count + 1;

GridData.Insert( 0, argsItem);
}

private void DeleteItem ( GridCommandEventArgs args ) { var argsItem=args.Item as Product;

GridData.Remove(argsItem);
}

private void UpdateItem ( GridCommandEventArgs args ) { var argsItem=args.Item as Product; var index=GridData.FindIndex( i=> i.ProductId==argsItem.ProductId); if (index !=- 1 )
{
GridData[index]=argsItem;
}
}

protected override void OnInitialized ( ) {
GridData=new List<Product>(); for (int i=1; i <=500; i++)
{
GridData.Add( new Product ( ) {
ProductId=i,
ProductName="Product " + i.ToString(),
UnitPrice=(decimal)(i * 3.14 ),
UnitsInStock=(short)(i * 1 ),
Discontinued=false });
}
}

public class Product {
public int ProductId { get; set; }
public string ProductName { get; set; }
public decimal? UnitPrice { get; set; }
public short? UnitsInStock { get; set; }
public bool Discontinued { get; set; }

public Product ( ) { }

public Product ( Product p ) { this.ProductId=p.ProductId; this.ProductName=p.ProductName; this.UnitsInStock=p.UnitsInStock; this.UnitPrice=p.UnitPrice; this.Discontinued=p.Discontinued;
}

public Product Clone ( ) { return new Product( this );
}
}
}

### Response

**Claudio** commented on 02 May 2022

Hi Dimo, The issue occurs when grid data is read from server, in your sample GridData property never change, so edit work well. You can reply the issue renaming in your sample protected override void OnInitialized() in protected void InitGridData() and call InitGridData() in the first row of ReadGridData method (so it simulate retrieve data from server)

### Response

**Claudio** commented on 04 May 2022

Dimo with this sample you can reply the issue: [https://blazorrepl.telerik.com/mQkTEyPy15OT1ZEO36](https://blazorrepl.telerik.com/mQkTEyPy15OT1ZEO36)

### Response

**Dimo** commented on 04 May 2022

Thanks, Claudio. The observed behavior is expected, because the data reload resets the data item object references. The general idea is to enter edit mode while preserving the current item's object reference. So your workaround is valid. Alternatively, if your data is likely to change often, first rebind the Grid, and then enter edit mode with the same workaround.
