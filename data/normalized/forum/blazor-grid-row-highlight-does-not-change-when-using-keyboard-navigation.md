# Blazor Grid Row highlight does not change when using keyboard navigation.

## Question

**And** asked on 09 May 2023

I have a Blazor Grid with the following properties: <TelerikGrid OnRead="@OnGridRead" Data="Data" Pageable="true" PageSize="10" Width="100%" Sortable="true" Navigable="true" Groupable="true" SelectionMode="GridSelectionMode.Single" SortMode="@SortMode.Single" FilterMode="@GridFilterMode.FilterMenu" Resizable="true" OnRowClick="OnRowClickCallback" Reorderable="true" AutoGenerateColumns="true"> When I click on a row the row is highlighted, but when I use the keyboard to navigate the highlight stays on the last row I clicked on. The keyboard navigates to a cell and draws a thin, barely visible, border on the cell, when I hit enter the `OnRowClickCallback` is called on the new row but the highlight remains on the old row. How do I get the row highlight to change with the navigation?

## Answer

**Dimo** answered on 12 May 2023

Hi Andre, By design, Grid selection with the keyboard requires a space key press. The gray border shows focus, so that the user can move through cells and rows. The desired behavior will be possible to implement when we expose a focus event for the Grid rows or cells. Please vote and follow the item to receive status updates and help us prioritize. Regards, Dimo Progress Telerik

### Response

**Andre** commented on 16 May 2023

Thanks for the reply. The confusing part is that the actual focus/selection is changed but the highlight is not. What does the highlighted row even mean when the focused cell is on a different row? Is there a workaround that I can implement now? I will probably vote on the issue, but it's not something I can wait for (if it even gets attention in the first place). Regards, Andre

### Response

**Dimo** commented on 16 May 2023

Hi Andre, The cell focus shadow shows the user which is the cell/row that the user can edit or select. A possible workaround is to intercept the arrow key events in the Grid and change the selected item programmatically. The example below is basic and by no means fool-proof, but you can enhance it, depending on your preferences and exact scenario. You can also use: the Grid state to check if the Grid is in edit mode JSInterop to check which is the focused cell and if it's next to the selected row <div @onkeyup="@OnGridKeyUp"> <TelerikGrid Data="@GridData" TItem="@Product" SelectionMode="@GridSelectionMode.Single" @bind-SelectedItems="@GridSelectedItems" Navigable="true"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> </GridColumns> </TelerikGrid> </div>

@code {
List<Product> GridData { get; set; }=new List<Product>();

IEnumerable<Product> GridSelectedItems { get; set; }=new List<Product>(); async Task OnGridKeyUp ( KeyboardEventArgs args ) { if (GridSelectedItems.Any() && (args.Key=="ArrowDown" || args.Key=="ArrowUp" ))
{ var selectedRowIndex=GridData.FindIndex( x=> x.Id==GridSelectedItems.First().Id); if (args.Key=="ArrowDown" )
{
GridSelectedItems=new List<Product>() { GridData[ Math.Min(selectedRowIndex + 1, GridData.Count - 1 )] };
} else if (args.Key=="ArrowUp" )
{
GridSelectedItems=new List<Product>() { GridData[ Math.Max(selectedRowIndex - 1, 0 )] };
}
}
}

protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=7; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name=$ "Product {i}",
});
}
}

public class Product {
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
public decimal Price { get; set; }
public DateTime ReleaseDate { get; set; }
public bool Active { get; set; }
}
}

### Response

**Andre** commented on 16 May 2023

Thanks, I'll try that.
