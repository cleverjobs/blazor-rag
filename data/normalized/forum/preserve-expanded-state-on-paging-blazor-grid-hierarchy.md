# Preserve expanded state on paging blazor grid hierarchy.

## Question

**Sar** asked on 23 Mar 2023

I have a Parent/Child blazor grid hierarchy. It will hold a large amount of date therefore it's necessary to apply paging to display, there was too much lag if displaying all on one page. I am preserving the grid state of collapse/expansion programmatically and each new record that is found (live data) is added to the grid in the expanded state. I am using the OnRead and RebindGrid methods and it works great if there is only 1 page. Whenever the page is changed all rows are automatically collapsed and only a refresh will expand - but it takes me to page 1. How can I preserve the state between pages?

## Answer

**Dimo** answered on 28 Mar 2023

Hello Sara, In this case, you need the OnStateChanged event to detect paging operations and set the ExpandedItems again. Note that this is done in OnAfterRenderAsync with a boolean flag: <TelerikGrid @ref="@GridRef" Data="@GridData" Pageable="true" PageSize="3" OnStateInit="@( (GridStateEventArgs<Product> args)=> OnGridStateInit(args) )" OnStateChanged="@( (GridStateEventArgs<Product> args)=> OnGridStateChanged(args) )"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" /> </GridColumns> <DetailTemplate> Detail Template should be expanded by default </DetailTemplate> </TelerikGrid> @code {
TelerikGrid<Product> GridRef { get; set; }

List<Product> GridData { get; set; }=new List<Product>(); bool ShouldExpandItems { get; set; } void OnGridStateInit ( GridStateEventArgs<Product> args ) {
args.GridState.ExpandedItems=GridData;
} void OnGridStateChanged ( GridStateEventArgs<Product> args ) { if (args.PropertyName=="Page" ) {
ShouldExpandItems=true;
}
} protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (ShouldExpandItems) {
ShouldExpandItems=false; var gridState=GridRef.GetState();

gridState.ExpandedItems=GridData; await GridRef.SetStateAsync(gridState);
} await base.OnAfterRenderAsync(firstRender);
} protected override void OnInitialized ( ) { for (int i=1; i <=9; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name=$ "Product {i}" });
}
} public class Product { public int Id { get; set; } public string Name { get; set; }=string.Empty;
}
} Regards, Dimo
