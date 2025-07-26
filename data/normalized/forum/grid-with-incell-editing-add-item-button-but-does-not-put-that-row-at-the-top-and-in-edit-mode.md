# Grid with Incell editing Add Item button but does not put that row at the top and in edit mode.

## Question

**Jst** asked on 22 Dec 2022

I am trying to make the add a new row in my grid work the same as in the demo below but am not able to get the new row to be at the top of the grid and in edit mode as the demo does. Grid Incell editing Demo The data is being retrieved from an OData endpoint. When I click the add button a new record is created in the database and the grid refreshes, but I need to have that row be given the focus and be in edit mode. I would also like it at the top of the grid for editing as the demo does. Why is my code not working as the demo does? What do I need to change to get it working like the demo? My razor page: <TelerikGrid SelectionMode="@GridSelectionMode.Single" TItem="@WarningVM" OnRead="@ReadWarnings" EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnCreate="@CreateHandler" OnCancel="@OnCancelHandler" Resizable="true" Reorderable="true" PageSize="15" Navigable="true" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterMenu"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add Warning </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Title=" " Width="4em" Filterable="false"> <Template> <span class="large-icons"> <TelerikIcon Icon="info-circle" Class="infoIcon"> </TelerikIcon> </span> </Template> </GridColumn> <GridColumn Field="@(nameof(WarningVM.Id))" Width="7em" Editable="false" /> <GridColumn Field="@(nameof(WarningVM.ValueType))" Title="Value Type" /> <GridColumn Field="@(nameof(WarningVM.Value1))" Title="Value #1" /> <GridColumn Field="@(nameof(WarningVM.Value2))" Title="Value #2" /> <GridColumn Field="@(nameof(WarningVM.ReasonAdded))" Title="Reason Added" /> <GridColumn Field="@(nameof(WarningVM.IsActive))" Title="Active" /> <GridCommandColumn Width="250px"> <GridCommandButton Command="Delete" Icon="delete"> </GridCommandButton> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> My back end code: public async Task ReadWarnings ( GridReadEventArgs args ) {
ODataWarningsResponse data=await warningService.GetWarnings(args.Request);
args.Data=data.Warnings;
args.Total=data.Total;
} private async Task UpdateHandler ( GridCommandEventArgs args ) { var test=await warningService.UpdateWarning((WarningVM)args.Item);
} private async Task EditHandler ( GridCommandEventArgs args ) { var warningVM=(WarningVM)args.Item; await warningService.UpdateWarning(warningVM);
} private void CreateHandler ( GridCommandEventArgs args ) {
WarningVM item=(WarningVM)args.Item;
warningService.UpdateWarning(item);
}

## Answer

**Stamo Gochev** answered on 26 Dec 2022

Hello John, If you click on the View Source -> ProductService.cs file from the demo and then navigate to the "CreateProduct" method: public void CreateProduct ( ProductDto product ) { if (!_products.Any())
{
product.ProductId=1;
} else {
product.ProductId=_products.Max(p=> p.ProductId) + 1;
} _products.Insert( 0, product); } you will see that the new item is inserted at the first position of the products collection. This ensures that when the Grid is updated, the item with index 0 will be displayed at the top. The code snippet that you provided for the create handler: private void CreateHandler ( GridCommandEventArgs args ) {
WarningVM item=(WarningVM)args.Item;
warningService.UpdateWarning(item);
} seems to update an already existing item instead of creating a new one and putting it in a specific position (index 0). Note that if there are other actions involved, e.g. filtering, sorting, etc., the index should be updated accordingly, so that the newly created item is visually displayed at the top of the Grid. Can you try the above suggestion and inform me about the result? Regards, Stamo Gochev Progress Telerik
