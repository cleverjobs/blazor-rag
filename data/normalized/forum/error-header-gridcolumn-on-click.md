# Error Header Gridcolumn on click

## Question

**Jos** asked on 17 Oct 2023

I have a problem in the Grid, I have created a calculated field that for the example is the calculated date, this field does not belong to the TelerikGrid Data model, when clicking on the column header of said field an error occurs. It is very necessary to perform calculations and display them in a column, the data in my project is generated from a dbcontext, so I do not want to alter the SQL tables that I have been managing. There is a way to avoid this error, the error occurs even when removing the filter from the column, please, if someone has a solution it would help me out of trouble. [https://blazorrepl.telerik.com/GRPYFhvp14M25Tft34](https://blazorrepl.telerik.com/GRPYFhvp14M25Tft34) @page "/Grid"

@using Telerik.Blazor.Services
@using Telerik.FontIcons;
@using Telerik.Blazor.Components.Grid <TelerikGrid Data="@GridData" Height="550px" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" Pageable="true" PageSize="20" Groupable="true" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Name" /> <GridColumn Field="@nameof(Product.Price)" DisplayFormat="{0:C2}" /> <GridColumn Field="@nameof(Product.Released)" DisplayFormat="{0:D}" /> <GridColumn Field="@nameof(Product.Discontinued)" /> <GridColumn Field="Date Calculated (NO PRESENT IN MODEL)" Width="220px" DisplayFormat="{0:dddd, dd MMM yyyy}"> <Template> @{
var fecha=(Product)context;
double FechaCalculada;
TimeSpan diferencia=DateTime.Today - fecha.Released;
double difDouble=5+diferencia.TotalDays / 365.25; // considerando años bisiestos
FechaCalculada=Math.Round(difDouble, 2);
} <TelerikNumericTextBox Decimals="2" @bind-Value=@FechaCalculada DebounceDelay="200" Enabled=false Arrows="false" /> </Template> </GridColumn> </GridColumns> </TelerikGrid> @code {
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
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Kind regards.

## Answer

**Hristian Stefanov** answered on 20 Oct 2023

Hi Jose, The error stems from the Grid column's 'Field' parameter, which requires a model property association for the component's operation. When clicking the column header, it initiates sorting, and this sorting mechanism relies on the 'Field' parameter. In the scenario here, the 'Field' parameter lacks a valid association with a model property. To resolve this issue, it's necessary to establish a dedicated property within the model and perform the calculations within that model. I have prepared an illustrative example for you that demonstrates this approach, along with the improved code: @using Telerik.Blazor.Services
@using Telerik.FontIcons;
@using Telerik.Blazor.Components.Grid <TelerikGrid Data="@GridData" Height="550px" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" Pageable="true" PageSize="20" Groupable="true" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Name" /> <GridColumn Field="@nameof(Product.Price)" DisplayFormat="{0:C2}" /> <GridColumn Field="@nameof(Product.Released)" DisplayFormat="{0:D}" /> <GridColumn Field="@nameof(Product.Discontinued)" /> <GridColumn Field=" @nameof(Product.FechaCalculada) " Width="220px" DisplayFormat="{0:dddd, dd MMM yyyy}"> <Template> <TelerikNumericTextBox Decimals="2" @bind-Value="@((context as Product).FechaCalculada)" DebounceDelay="200" Enabled=false Arrows="false" /> </Template> </GridColumn> </GridColumns> </TelerikGrid> @code {
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
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; } public double FechaCalculada
{
get
{
TimeSpan diferencia=DateTime.Today - Released;
double difDouble=5 + diferencia.TotalDays / 365.25; // considering leap years
return Math.Round(difDouble, 2);
}
set { }
} }
} Regards, Hristian Stefanov Progress Telerik

### Response

**Jose** commented on 20 Oct 2023

I understand, adding more fields to the model would make the Grid recognize the fields, but the detail is that that class is part of my DbContext, so if I add more fields to the class, these will not be in the sql server table, so which gives an error in the connection. It is not feasible to add more fields to the sql table to make it compatible, so adding more fields to the class is not feasible. Greetings

### Response

**Hristian Stefanov** commented on 25 Oct 2023

Hi Jose, I confirm that for the Grid to execute sorting, filtering, and other operations correctly for a specific column, it needs properly mapped data. The Grid's design requires that every "Field" value is mapped to a property of the model bound to the component. Alternative However, if you still desire a column that isn't directly mapped to a property of the model, there is an alternative. You can simply omit the "Field" parameter from the syntax. This adjustment will prevent any errors when clicking the column header because the sorting operation will not be triggered. To illustrate this, here's a practical example you can test: @using Telerik.Blazor.Services
@using Telerik.Blazor.Components.Grid <TelerikGrid Data="@GridData" Height="550px" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" Pageable="true" PageSize="20" Groupable="true" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" Title="Name" /> <GridColumn Field="@nameof(Product.Price)" DisplayFormat="{0:C2}" /> <GridColumn Field="@nameof(Product.Released)" DisplayFormat="{0:D}" /> <GridColumn Field="@nameof(Product.Discontinued)" /> <GridColumn Width="220px" DisplayFormat="{0:dddd, dd MMM yyyy}" Title="Fecha Calculada"> <Template> @{
var fecha=(Product)context;
double FechaCalculada;
TimeSpan diferencia=DateTime.Today - fecha.Released;
double difDouble=5 + diferencia.TotalDays / 365.25; // considerando años bisiestos
FechaCalculada=Math.Round(difDouble, 2);
} <TelerikNumericTextBox Decimals="2" @bind-Value="@FechaCalculada" DebounceDelay="200" Enabled=false Arrows="false" /> </Template> </GridColumn> </GridColumns> </TelerikGrid> @code {
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
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
public DateTime Released { get; set; }
public bool Discontinued { get; set; }
}
} Kind Regards, Hristian

### Response

**Jose** commented on 26 Oct 2023

Thanks, this is what I wanted, it was so simple that I don't know why I couldn't see it, thanks this has worked. Kind regards
