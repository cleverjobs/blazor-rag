# Showing filter state when setting in code

## Question

**Mar** asked on 27 Nov 2023

I have a filter on End Date set at start up. If I filter manual I get the filter indicator. How can I get the same result from code? This is the code that I am using. Called from event OnStateInit="@( (GridStateEventArgs <FundFirm> args)=> OnFundFirmGridStateInit(args) )" private async Task OnFundFirmGridStateInit ( GridStateEventArgs<FundFirm> args ) {
args.GridState.FilterDescriptors=new List<IFilterDescriptor>
{ new FilterDescriptor
{
Member="ExcludeDate", Operator=FilterOperator.IsGreaterThanOrEqualTo,
Value=DateTime.Today,
MemberType=typeof (DateTime)
}
};
}

### Response

**Hristian Stefanov** commented on 29 Nov 2023

Hi Martin, Upon reviewing the code snippet you shared, it seems there is a missing CompositeFilterDescriptor wrapping the FilterDescriptor. For your convenience, I've created an example below, demonstrating a Grid with an initial filter on a date column. You can use it as a reference. @using Telerik.DataSource <TelerikGrid Data="@GridData" Pageable="true" PageSize="5" Sortable="true" FilterMode="@GridFilterMode.FilterMenu" Groupable="true" OnStateInit="@( (GridStateEventArgs<Product> args)=> OnGridStateInit(args) )"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" /> <GridColumn Field="@nameof(Product.Released)" /> <GridColumn Field="@nameof(Product.Discontinued)" /> </GridColumns> </TelerikGrid> @code {
private List <Product> GridData { get; set; }

private async Task OnGridStateInit(GridStateEventArgs <Product> args)
{
var discontinuedColumnFilter=new CompositeFilterDescriptor()
{
FilterDescriptors=new FilterDescriptorCollection() {
new FilterDescriptor()
{
Member="Released",
Operator=FilterOperator.IsLessThan,
Value=DateTime.Today,
MemberType=typeof(DateTime)
}
}
};
args.GridState.FilterDescriptors.Add(discontinuedColumnFilter);
}

protected override void OnInitialized()
{
GridData=new List <Product> ();
var rnd=new Random();

for (int i=1; i <=12; i++)
{
GridData.Add(new Product()
{
Id=i,
Name=$"Product {i}",
Released=i==1 ? DateTime.Now : DateTime.Now.AddDays(-rnd.Next(1, 365)).AddYears(-rnd.Next(1, 10)).Date,
Discontinued=i % 3==0
});
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Feel free to reach out if you require more information or assistance. I'm here to help. Kind Regards, Hristian

### Response

**Martin Herløv** commented on 30 Nov 2023

Thanks. Now it works.
