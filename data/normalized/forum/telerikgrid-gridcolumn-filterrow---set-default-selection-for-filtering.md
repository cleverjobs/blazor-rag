# TelerikGrid GridColumn FilterRow - Set default selection for filtering

## Question

**Gle** asked on 23 Dec 2024

I have a TelerikGrid utilizing the FilterRow for FilterMode. One of the columns is called CurrentVersion where the CurrentVersion could be a copy of multiple other objects but it's Revision is higher. The objects with CurrentVersion=true, I want to be the only initially displayed items. If there is an item that is CurrentVersion=false, I still want it to be accessible by changing the filter to All instead of True, but I need true to be the default. How would I go about this? I've checked documentation and can't find a solution. I've also checked online and other forums posts and can't seem to find a solution. ChatGPT and CoPilot are also no help here. <TelerikGrid Data=@TestItemsList FilterMode="GridFilterMode.FilterRow" Sortable="true" EditMode="GridEditMode.Inline" Height="2000px"> <GridColumn Field="@nameof(TestModel.CurrentVersion)" Title="Current Version" Editable="true" Filterable="true"> </TelerikGrid>

## Answer

**Hristian Stefanov** answered on 24 Dec 2024

Hi Glenn, To set a default filter for the CurrentVersion column in your TelerikGrid, you can use the OnStateInit event to apply a filter programmatically when the grid is first rendered. This will ensure that only items where CurrentVersion is true are initially displayed, but users can change the filter to view all items if needed. Here's a code snippet demonstrating how to set the default filter for the CurrentVersion column: @using Telerik.DataSource <TelerikGrid Data="@GridData" Pageable="true" PageSize="5" Sortable="true" FilterMode="@GridFilterMode.FilterRow" OnStateInit="@( (GridStateEventArgs<Product> args)=> OnGridStateInit(args) )"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" /> <GridColumn Field="@nameof(Product.Category)" /> <GridColumn Field="@nameof(Product.CurrentVersion)" Title="Current Version" /> </GridColumns> </TelerikGrid> @code {
private List <Product> GridData { get; set; } private async Task OnGridStateInit(GridStateEventArgs <Product> args)
{
// Filter CurrentVersion products
var discontinuedColumnFilter=new CompositeFilterDescriptor()
{
FilterDescriptors=new FilterDescriptorCollection() {
new FilterDescriptor()
{
Member=nameof(Product.CurrentVersion),
MemberType=typeof(bool),
Operator=FilterOperator.IsEqualTo,
Value=true
}
}
};
args.GridState.FilterDescriptors.Add(discontinuedColumnFilter);
} protected override void OnInitialized()
{
GridData=new List <Product> ();
var rnd=new Random();

for (int i=1; i <=12; i++)
{
GridData.Add(new Product()
{
Id=i,
Name=$"Product {i}",
Category=$"Category {i % 2 + 1}",
CurrentVersion=i % 3==0
});
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public string Category { get; set; }
public bool CurrentVersion { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik
