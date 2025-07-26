# Grid sellection check box.

## Question

**Jac** asked on 21 Oct 2022

I want to prevent user to deselct one of grid rows. Grid has check box sellection turned on. Grid purpose is an users sellection for an application role. I want user to be unable to remove Administrator user from Administrators role by deselecting it. Now, in SelectedItemsChanged event i'm exammining selected users collection for Role is Administrators and user Administrator not present in sellected users collection. If so, i'm adding it back and submit MySelectedItems=IEnumerable (MySelectedItems is two way bound to SelectedItems of grid) with Administrator user added. After that, sittuation go a little bit shizophremic. The Administrator user row remains selected on the grid but the CheckBox selector of that user remains deselected... So, haw to prevent check box sellection of a single row?

## Answer

**Dimo** answered on 25 Oct 2022

Hello Jacek, Indeed, this is an existing bug, sorry about the hassle. The linked page shows a possible JavaScript-based workaround. There is an easier option, if SelectAll="false" and CheckBoxOnlySelection="true" - use the Grid OnCellRender event to hide the checkboxes that shouldn't be (un)checked. <TelerikGrid Data="@GridData" TItem="@Product" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="@GridSelectedItems">
<GridColumns> <GridCheckboxColumn SelectAll="false" OnCellRender="@OnGridCellRender" CheckBoxOnlySelection="true" /> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" />
<GridColumn Field="@nameof(Product.Active)" />
</GridColumns>
</TelerikGrid> <style>
.disabled-checkbox .k-checkbox {
visibility: hidden;
}
</style> @code {
List<Product> GridData { get; set; }

IEnumerable<Product> GridSelectedItems { get; set; }=new List<Product>(); void OnGridCellRender ( GridCellRenderEventArgs args ) { var product=(Product)args.Item; if (!product.Active)
{
args.Class="disabled-checkbox";
}
} protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for ( int i=1; i <=7; i++)
{
GridData.Add( new Product()
{
Id=i,
Name="Product " + i,
Price=( decimal )rnd.Next( 1, 100 ),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next( 60, 1000 )),
Active=i % 3!=0 });
}

GridSelectedItems=GridData.Where(x=> !x.Active);
} public class Product { public int Id { get; set; } public string Name { get; set; } public decimal Price { get; set; } public DateTime ReleaseDate { get; set; } public bool Active { get; set; }
}
} Regards, Dimo
