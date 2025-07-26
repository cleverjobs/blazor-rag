# grid operations (sort, filter) release rows per page in pager

## Question

**Ale** asked on 26 Sep 2021

so if you have several options to select from in pager & selected non default one (100 - default, 200 - selected) than filter or sort grid, the value in pager will be reset to default

## Answer

**Dimo** answered on 29 Sep 2021

Hi Aleksandr, Here is a test page, which works as expected. I assume you need to change something in the Grid paging configuration. Let me know of your findings. <TelerikGrid Data="@GridData" Pageable="true" @bind -PageSize="@PageSize" Sortable="true" FilterMode="GridFilterMode.FilterRow">
<GridSettings>
<GridPagerSettings PageSizes="@PageSizes" />
</GridSettings>
<GridColumns>
<GridColumn Field=@nameof (Product.Name) Title="Product Name" />
<GridColumn Field=@nameof (Product.Price) Title="Price" />
<GridColumn Field=@nameof (Product.Quantity) Title="Units In Stock" />
</GridColumns>
</TelerikGrid> @code {
List<Product> GridData;

int PageSize { get; set; }=5;
List<int?> PageSizes { get; set; }=new List<int?> { 5, 6, 7, 20, null }; protected override void OnInitialized()
{
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=50; i++)
{

GridData.Add( new Product()
{
ID=i,
Name="Product " + i.ToString(),
Price=(decimal)rnd.Next( 1, 100 ),
Quantity=(short)rnd.Next( 1, 100 )
});
}
} public class Product
{ public int ID { get; set; } public string Name { get; set; } public decimal Price { get; set; } public short Quantity { get; set; }
}
} Regards, Dimo
