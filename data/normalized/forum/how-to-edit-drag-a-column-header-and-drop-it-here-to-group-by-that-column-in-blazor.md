# How to edit "Drag a column header and drop it here to group by that column" in Blazor

## Question

**Chi** asked on 05 May 2023

Hi all, I want to edit the text "Drag a column header and drop it here to group by that column" to another text with a specific column's name. Please help me!!! Thank you,

## Answer

**Dimo** answered on 06 May 2023

Hi Chinh, Normally, this string is customized via localization. It's the Group_Empty key. However, I doubt that you want to hard-code a column name in the resource file. So another possible approach is a CSS hack. <TelerikGrid Data="@GridData" Groupable="true" Class="custom-group-text"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Product Name" /> <GridColumn Field="@nameof(Product.Price)" /> <GridColumn Field="@nameof(Product.ReleaseDate)" Title="Release Date" /> <GridColumn Field="@nameof(Product.Active)" /> </GridColumns> </TelerikGrid> <style>.custom-group-text.k-grouping-drop-container:first -child { font-size: 0;
}.custom-group-text.k-grouping-drop-container:first -child::before { font-size: 14px; content: "My custom drag text"; } </style> @code {
List <Product> GridData { get; set; }=new List <Product> ();

protected override void OnInitialized()
{
GridData=new List <Product> ();
var rnd=new Random();

for (int i=1; i <=7; i++)
{
GridData.Add(new Product()
{
Id=i,
Name=$"Product {i}",
Price=(decimal)rnd.Next(1, 100),
ReleaseDate=DateTime.Now.AddDays(-rnd.Next(60, 1000)),
Active=i % 3==0
});
}
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
public decimal Price { get; set; }
public DateTime ReleaseDate { get; set; }
public bool Active { get; set; }
}
} Regards, Dimo Progress Telerik

### Response

**Eric** commented on 27 Jun 2023

Any plans to build this text customization into the official functionality of the grid?

### Response

**Svetoslav Dimitrov** commented on 30 Jun 2023

Hello Eric, We do not have an open feature request for the ability to control the Group empty placeholder currently. If you wish to see one I can encourage you to open a feature request on our Public Feedback Portal for Blazor.
