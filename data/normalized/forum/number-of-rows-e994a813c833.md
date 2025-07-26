# Number of rows

## Question

**And** asked on 09 Mar 2020

Hello, I cannot find a way to figure out a number of all rows
in virtual scrolling grid. And I need to find a number of selected
rows as well. And I need the same info: number of all rows and number of selected rows in page-able Blazor grid as well. Thanks.

## Answer

**Andrey** answered on 09 Mar 2020

My question is about Blazor server side. Thanks.

### Response

**Svetoslav Dimitrov** answered on 10 Mar 2020

Hello Andrey, The total number of items the grid can show depends on the data source you provide, so you can usually extract its count from the collection. The only exception I can think of is knowing how many items the user can actually see if they have filtered the grid. With the standard paging, the pager will show that, and you can read an example for virtual scrolling below. After that, there is an answer to your question about the selected items. In order to find the total number of rows in both Virtual Scrolling Grid and the Paging Grid you could do follow the steps below: You can use the OnRead event of the Grid. More information about it can be found on the link here After that you should use the Telerik DataSourceResult Extension Method (documentation here ) Use the Total property to extract the count of the all items present in the grid To further demonstrate that i have created the code snippet below: @using Telerik.DataSource.Extensions <TelerikGrid Data="@GridData" TotalCount="@GridTotal" Sortable="true" FilterMode="@GridFilterMode.FilterRow" Height="460px" RowHeight="60" PageSize="10" ScrollMode="@GridScrollMode.Virtual" OnRead="@OnGridRead">
<GridColumns>
<GridColumn Field="@nameof(Product.ID)" />
<GridColumn Field="@nameof(Product.Name)" />
</GridColumns>
</TelerikGrid>

<p> Total rows in the Grid: @GridTotal.ToString() </p>

@code { public List<Product> Data { get; set; } public List<Product> GridData { get; set; } public int GridTotal { get; set; } protected override void OnInitialized ( ) {
Data=new List<Product>(); for ( int i=1; i <=500; i++)
{
Data.Add( new Product()
{
ID=i,
Name="Product " + i.ToString()
});
}
} protected void OnGridRead ( GridReadEventArgs args ) { var datasourceResult=Data.ToDataSourceResult(args.Request);
GridData=(datasourceResult.Data as IEnumerable<Product>).ToList();
GridTotal=datasourceResult.Total;
} public class Product { public int ID { get; set; } public string Name { get; set; }
}
} To see the count of the selected items in both Virtual Scroll and Paging Grid you could follow the instructions below: Add SelectionMode="GridSelectionMode.Multiple" Add a GridCheckboxColumn Add all selected items to a IEnumerable collection with two-way data binding - @bind-SelectedItems More on the multiple selection you can find in the documentation here or the live demo here. There is an important difference between multi-selection in Virtual Scroll and Paging Grid - In virtual scroll you can select only rows on the current page of the grid, whereas in Paging you can select from all pages. Again, I have created a sample demo to demonstrate the way to extract the count of the selected items: <TelerikGrid Data=@GridData
Height=@Height
Pageable="true" PageSize=@PageSize SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedItems"> <GridColumns>
<GridCheckboxColumn SelectAll="true"></GridCheckboxColumn>
<GridColumn Field=@nameof (Product.ProductName) Title="Product Name" />
<GridColumn Field=@nameof (Product.DeliveryDate) Title="Delivery Date">
</GridColumn>
<GridColumn Field=@nameof (Product.UnitPrice) Title="Unit Price">
<Template>
@(String.Format( "{0:C2}", (context as Product).UnitPrice))
</Template>
</GridColumn>
</GridColumns>
</TelerikGrid> <p>
Selected items in grid: @SelectedItems.Count()
</p> @code { public class Product { public int ProductId { get; set; } public string ProductName { get; set; } public int SupplierId { get; set; } public decimal UnitPrice { get; set; } public short UnitsInStock { get; set; } public DateTime DeliveryDate { get; set; }
} public List<Product> GridData { get; set; } int PageSize=10; string Height="400px"; public IEnumerable<Product> SelectedItems=new List<Product>(); protected override void OnInitialized ( ) {
GridData=new List<Product>(); for ( int i=0; i <100; i++)
{
GridData.Add( new Product()
{
ProductId=i,
ProductName="Product " + i.ToString(),
SupplierId=i,
UnitPrice=( decimal )(i * 3.14 ),
UnitsInStock=( short )(i * 1 ),
DeliveryDate=DateTime.Now.AddDays( 4 )
});
}
}
} Regards, Svetoslav Dimitrov
