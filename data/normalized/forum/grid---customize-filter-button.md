# Grid - Customize Filter Button

## Question

**TimTim** asked on 14 Sep 2022

I would like to change the buttons to display the filter menu in the column headings since it will be unfamiliar to our users. Is it possible to replace the filter icon that looks like a funnel with the word "Filter"? Thanks

## Answer

**Dimo** answered on 15 Sep 2022

Hello Tim, There is a hackish CSS technique to inject a text label inside the filter button. However, I would recommend you to educate the users to recognize the filter icon. You will skip the workaround and moreover, the default button is a lot more compact. Regards, Dimo Progress Telerik

### Response

**Tim** commented on 15 Sep 2022

Hi Dimo, Thanks for the reply. I can't get the REPL to work. I can't see anything other than the boilerplate code and when I click on Run, I see errors. Any idea how I can fix it? Thanks, Tim

### Response

**Dimo** commented on 18 Sep 2022

Hm, try clearing the browser cache. Here is the example code: <TelerikGrid Data="@GridData" TItem="@Product" Pageable="true" Sortable="true" FilterMode="GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" /> <GridColumn Field="@nameof(Product.Active)" /> </GridColumns> </TelerikGrid> <style>.k-grid-header th.k-filterable { padding-right: 5em;
}.k-grid-header th.k-filterable>.k-cell-inner { margin-right: - 5em;
}.k-grid-header.k-grid-filter-menu { width: 4em; border: 1px solid rgba ( 0, 0, 0,. 08 );
}.k-grid-header.k-grid-filter-menu::before { content: "Filter";
}.k-grid-header.k-grid-filter-menu>.k-icon { display: none;
} </style> @code {
List<Product> GridData { get; set; } protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=7; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name="Product " + i,
Price=(decimal)rnd.Next( 1, 100 ),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next( 60, 1000 )),
Active=i % 3==0 });
}
} public class Product { public int Id { get; set; } public string Name { get; set; } public decimal Price { get; set; } public DateTime ReleaseDate { get; set; } public bool Active { get; set; }
}
}

### Response

**Tim** commented on 19 Sep 2022

I still can't get the REPL link to work, but thanks for the code.

### Response

**Stamo Gochev** commented on 22 Sep 2022

Hi Tim, Can you provide more information about not being able to run the Telerik Blazor REPL snippet? Can you send some screenshots or a video what happens on your side when you click on the "Run" button in the top right part of the app? Are there any errors logged in the DevTools console that you can share?

### Response

**Tim** commented on 22 Sep 2022

It's probably something on my end. My company firewall blocks access to servers in certain countries. Thanks

### Response

**Stamo Gochev** commented on 26 Sep 2022

Hi Tim, It is indeed possible for firewall configurations to block resources, so I am attaching the full code of the Telerik Blazor REPL snippet provided above: <TelerikGrid Data="@GridData" TItem="@Product" Pageable="true" Sortable="true" FilterMode="GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" /> <GridColumn Field="@nameof(Product.Active)" /> </GridColumns> </TelerikGrid> <style>.k-grid-header th.k-filterable { padding-right: 5em;
}.k-grid-header th.k-filterable>.k-cell-inner { margin-right: - 5em;
}.k-grid-header.k-grid-filter-menu { width: 4em; border: 1px solid rgba ( 0, 0, 0,. 08 );
}.k-grid-header.k-grid-filter-menu::before { content: "Filter";
}.k-grid-header.k-grid-filter-menu>.k-icon { display: none;
} </style> @code {
List <Product> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Product> ();
var rnd=new Random();

for (int i=1; i <=7; i++)
{
GridData.Add(new Product()
{
Id=i,
Name="Product " + i,
Price=(decimal)rnd.Next(1, 100),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next(60, 1000)),
Active=i % 3==0
});
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime ReleaseDate { get; set; }
public bool Active { get; set; }
}
} You can try the code in a separate project to test the result and then use the idea or improve on it based on your requirements.
