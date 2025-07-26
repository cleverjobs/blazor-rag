# TelerikGrid Height:100% doesn't work with Parent Max-Height

## Question

**Mar** asked on 19 Aug 2024

Hi Telerik, I'm new to Blazor and I'm encountering an issue with the TelerikGrid component. Here's my problem: 1. I have a TelerikGrid inside a parent container with a max-height style. 2. I've set the Height property of the TelerikGrid to 100%. 3. The grid doesn't seem to conform to the max-height of its parent container. 4. It only works correctly when I set a fixed height on the parent, rather than using max-height. Is this expected behavior, or could it be a bug? If it's not a bug, how can I make the TelerikGrid respect its parent's max-height?

Here's a simplified version of my setup: [https://blazorrepl.telerik.com/cyaMvtYJ27JGxNSB59](https://blazorrepl.telerik.com/cyaMvtYJ27JGxNSB59) Any insights or workarounds would be greatly appreciated. Thanks in advance! Marcel

## Answer

**Hristian Stefanov** answered on 19 Aug 2024

Hi Marcel, The TelerikGrid isn't limited to 200px in height despite the parent div having a max-height of 200px because the grid is set to Height="100%". This makes the component try to fill the height of its parent container. However, CSS percentages work differently with max-height. The 100% height setting of the grid will cause it to look at the height of the parent container, but because the div is only setting max-height (not height ), the grid may end up ignoring the max height constraint. Solutions Set a fixed height on the parent container: If you set height: 200px on the parent div instead of max-height, the grid will respect this and adjust accordingly. <div style="height:200px;"> <TelerikGrid Height="100%" Data="@GridData" Pageable="false" ScrollMode="@GridScrollMode.Scrollable" FilterMode="@GridFilterMode.FilterRow"> <GridColumns> <GridColumn Field="Name" Title="Product Name" /> <GridColumn Field="Price" DisplayFormat="{0:C2}" /> <GridColumn Field="@nameof(Product.Released)" DisplayFormat="{0:D}" /> <GridColumn Field="@nameof(Product.Discontinued)" /> </GridColumns> </TelerikGrid> </div> @code {
private List <Product> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Product> ();

var rnd=new Random();

for (int i=1; i <=30; i++)
{
GridData.Add(new Product
{
Id=i,
Name="Product name " + i,
Price=(decimal)(rnd.Next(1, 50) * 3.14),
Released=DateTime.Now.AddDays(-rnd.Next(1, 365)).AddYears(-rnd.Next(1, 10)).Date,
Discontinued=i % 5==0
});

}

base.OnInitialized();
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Combine max-height with overflow: You can keep the max-height on the parent container and apply overflow: auto to ensure that the grid respects the height and scrolls if necessary. <div style="max-height:200px; overflow: auto;"> <TelerikGrid Height="100%" Data="@GridData" Pageable="false" ScrollMode="@GridScrollMode.Scrollable" FilterMode="@GridFilterMode.FilterRow"> <GridColumns> <GridColumn Field="Name" Title="Product Name" /> <GridColumn Field="Price" DisplayFormat="{0:C2}" /> <GridColumn Field="@nameof(Product.Released)" DisplayFormat="{0:D}" /> <GridColumn Field="@nameof(Product.Discontinued)" /> </GridColumns> </TelerikGrid> </div> @code {
private List <Product> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Product> ();

var rnd=new Random();

for (int i=1; i <=30; i++)
{
GridData.Add(new Product
{
Id=i,
Name="Product name " + i,
Price=(decimal)(rnd.Next(1, 50) * 3.14),
Released=DateTime.Now.AddDays(-rnd.Next(1, 365)).AddYears(-rnd.Next(1, 10)).Date,
Discontinued=i % 5==0
});

}

base.OnInitialized();
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Regards, Hristian Stefanov
