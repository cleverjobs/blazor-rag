# SelectedItemsChanged firing only on the current page

## Question

**Afr** asked on 17 Apr 2023

Hi, I am using the Telerikgrid in my code to display the data. I have also implemented the SelectedItemsChanged event to handle and updating a value in the IEnumerable list. The problem which I am facing is the following: When I am checking or unchecking the TelerikgridCheckboxColumn the SelectedItemsChanged event is firing only on the items which are displaying on the current page not the entire list. I want this event should fire for all the items in the list not just on the current page. Can you please help to fix this issue? Do I need to set some property of the Telerikgrid? Thanks, Afreen

## Answer

**Dimo** answered on 20 Apr 2023

Hi Alfreen, I assume that you are talking about the selection checkbox in the header. The desired behavior is supported only if the Grid is bound with the Data parameter. When using OnRead, the Grid knows only about the items on the current page, so it can't select items on other pages. Below is a test page that compares the two data binding mechanisms and selection behavior. If you like, you can use a HeaderTemplate for the CheckBox column and implement some custom logic, which will select items on other pages as well. For example, use a boolean flag for "all items are selected" and when the Grid rebinds and fires OnRead, select all newly received items programmatically. @using Telerik.DataSource @using Telerik.DataSource.Extensions

<p>Selected items count for the first Grid: @SelectedItemsCount1.ToString()</p> <TelerikGrid Data="@GridData" TItem="@Product" Pageable="true" SelectionMode="@GridSelectionMode.Multiple" SelectedItems="@GridSelectedItems1" SelectedItemsChanged="@OnGridSelectedItemsChanged1" Height="300px"> <GridColumns> <GridCheckboxColumn SelectAllMode="@GridSelectAllMode.All" /> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" /> <GridColumn Field="@nameof(Product.Active)" /> </GridColumns> </TelerikGrid> <p> Selected items count for second Grid: @SelectedItemsCount2.ToString() </p> <TelerikGrid OnRead="@OnGridRead" TItem="@Product" Pageable="true" SelectionMode="@GridSelectionMode.Multiple" SelectedItems="@GridSelectedItems2" SelectedItemsChanged="@OnGridSelectedItemsChanged2" Height="300px"> <GridColumns> <GridCheckboxColumn SelectAllMode="@GridSelectAllMode.All" /> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" /> <GridColumn Field="@nameof(Product.Active)" /> </GridColumns> </TelerikGrid> @code {
List<Product> GridData { get; set; }

int SelectedItemsCount1 { get; set; }
int SelectedItemsCount2 { get; set; }

IEnumerable<Product> GridSelectedItems1 { get; set; }=new List<Product>();
IEnumerable<Product> GridSelectedItems2 { get; set; }=new List<Product>(); void OnGridSelectedItemsChanged1 ( IEnumerable<Product> newSelectedItems ) {
GridSelectedItems1=newSelectedItems;

SelectedItemsCount1=newSelectedItems.Count();
} void OnGridSelectedItemsChanged2 ( IEnumerable<Product> newSelectedItems ) {
GridSelectedItems2=newSelectedItems;

SelectedItemsCount2=newSelectedItems.Count();
} async Task OnGridRead ( GridReadEventArgs args ) { await Task.Delay( 200 );

DataSourceResult result=GridData.ToDataSourceResult(args.Request);

args.Data=result.Data;
args.Total=result.Total;
args.AggregateResults=result.AggregateResults;
} protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=50; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name=$ "Product {i}",
Price=(decimal)rnd.Next( 1, 100 ),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next( 60, 1000 )),
Active=i % 3==0 });
}
} public class Product { public int Id { get; set; } public string Name { get; set; } public decimal Price { get; set; } public DateTime ReleaseDate { get; set; } public bool Active { get; set; }
}
} Regards, Dimo Progress Telerik
