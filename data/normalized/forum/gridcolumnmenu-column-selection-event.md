# GridColumnMenu Column selection Event

## Question

**RobRob** asked on 10 Jan 2022

I'm designing a grid that requests only the data for currently selected columns. I'd like to drive this using the GridColumnMenu, but I need notification on the user selecting new columns so I can update the query and pull in new data. Is there an event or other method I can detect which columns are currently enabled by the user?

## Answer

**Dimo** answered on 13 Jan 2022

Hi Rob, You can use a ColumnMenuChooser with a <Template>. Instead of <GridColumnMenuChooserItem> s, use <TelerikCheckBox>'s that are bound to boolean properties, which control the Visible property of each column. Finally, use the checkbox events to trigger Grid reload. UPDATE: The built-in Apply and Reset buttons will not work with such a custom setup. Hide them with CSS and use your own buttons. @page "/t1548868" @inject IJSRuntime js

<TelerikGrid Data="@GridData" ShowColumnMenu="true">
<GridColumns>
<GridColumn Field=@nameof (Product.ID) Title="Product ID" />
<GridColumn Field=@nameof (Product.Name) Title="Product Name" Id="Name" Visible="@(ColumnVisibility[" Name "])" />
<GridColumn Field=@nameof (Product.Price) Title="Price" Id="Price" Visible="@(ColumnVisibility[" Price "])" />
<GridColumn Field=@nameof (Product.Quantity) Title="Units In Stock" Id="Quantity" Visible="@(ColumnVisibility[" Quantity "])" />
</GridColumns>
<GridSettings>
<GridColumnMenuSettings>
<GridColumnMenuChooser>
<Template>
@{ var columns=context.Columns;
foreach ( var column in columns)
{ if (! String.IsNullOrEmpty(column.Id))
{
<div>
<label>
<TelerikCheckBox Value="@ColumnVisibility[column.Id]" ValueChanged="@( (bool newValue)=> SetColumnVisibility(newValue, column.Id) )" /> @column.DisplayTitle
</label>
</div>
}
}
}
<div class="k-actions k-hstack k-justify-content-stretch">
<TelerikButton>Reset</TelerikButton>
<TelerikButton OnClick="@ApplyNewVisibility" Primary="true">Apply</TelerikButton>
</div>
</Template>
</GridColumnMenuChooser>
</GridColumnMenuSettings>
</GridSettings>
</TelerikGrid>

<style>
.k-columnmenu-item-wrapper .k-column-list-wrapper> .k-actions {
display: none;
}
</style>

<script suppress-error="BL9992"> function blurColumnMenu ( ) { document.body.dispatchEvent( new Event( 'pointerdown' ));
}
</script> @code {
List<Product> GridData { get; set; }
bool PriceVisible { get; set; }=true;
bool QuantityVisible { get; set; }=true;

Dictionary<string, bool> ColumnVisibility=new Dictionary<string, bool>() {
{ "Name", true },
{ "Price", true },
{ "Quantity", false }
};

Dictionary<string, bool> NewColumnVisibility { get; set; } void SetColumnVisibility(bool newValue, string columnId)
{
NewColumnVisibility[columnId]=newValue;
} async Task ApplyNewVisibility()
{
ColumnVisibility=new Dictionary<string, bool>(NewColumnVisibility); await js.InvokeVoidAsync( "blurColumnMenu" );
} protected override void OnInitialized()
{
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=5; i++)
{

GridData.Add( new Product()
{
ID=i,
Name="Product " + i.ToString(),
Price=(decimal)rnd.Next( 1, 100 ),
Quantity=(short)rnd.Next( 1, 100 )
});
}

NewColumnVisibility=new Dictionary<string, bool>(ColumnVisibility);
} public class Product
{ public int ID { get; set; } public string Name { get; set; } public decimal Price { get; set; } public short Quantity { get; set; }
}
} Regards, Dimo

### Response

**Rob** commented on 13 Jan 2022

Of course, I should have thought of that. Thanks!

### Response

**Rob** commented on 13 Jan 2022

This works until the user clicks the apply button. The apply button then sets the previous visibility for each column.

### Response

**Rob** commented on 14 Jan 2022

Thanks for the detailed answer!! I actually just used the style to remove the Ok/Cancel buttons, since the checkbox applies the style immediately. The Reset/Apply buttons would be nicer and could be re-implemented but ultimately not worth the work. Seeing the data instantly is kinda nice anyway!

### Response

**Dimo** commented on 14 Jan 2022

I agree that it is easier to just hide the buttons and switch column visibility immediately. However, I thought you would like to have a final user confirmation before making a data request.
