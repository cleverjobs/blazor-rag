# How to make the grid more compact and tighter, what classes and methods to accomplish?

## Question

**Jst** asked on 26 May 2022

I'm looking for suggestions on how to compress and tighten up the grid display. The end-user wants the grid to look more like an excel spreadsheet. What CSS classes should I target? or is there a logical process for adjusting those sorts of things in the grid? Also open to any articles or tips. Thanks

## Answer

**Svetoslav Dimitrov** answered on 31 May 2022

Hello John, I have prepared an example for you where the Grid takes advantage of the elastic design and reduces the size of the font, and padding. Additionally, you can use the Width and Height parameters of the component to reduce its size. <style> div.smallerFont, div.smallerFont.k-filtercell * { font-size: 10px;
} div.smallerFont.k-dropdown.k-header.k-dropdown-operator { width: calc ( 8px + 2em )!important;
} div.smallerFont.k-grid-table td { padding: 8px;
}
</style> <TelerikGrid Data=" @GridData "
Pageable="true" Class="smallerFont" Sortable="true" FilterMode="@GridFilterMode.FilterRow">
<GridColumns>
<GridColumn Field="Name" Title="Product Name" />
<GridColumn Field="Price" />
<GridColumn Field="@(nameof(Product.Released))" />
<GridColumn Field="@(nameof(Product.Discontinued))" />
</GridColumns>
</TelerikGrid>

@code {
List<Product> GridData { get; set; }

protected override void OnInitialized()
{
GridData=Enumerable.Range ( 1, 30 ).Select (x=> new Product
{
Id=x,
Name="Product name " + x,
Price=(decimal)(x * 3.14 ),
Released=DateTime.Now.AddMonths (-x).Date,
Discontinued=x % 5==0 }).ToList ();

base.OnInitialized ();
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Regards, Svetoslav Dimitrov
