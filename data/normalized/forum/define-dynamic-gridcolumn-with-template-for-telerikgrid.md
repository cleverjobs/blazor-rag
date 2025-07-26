# Define dynamic GridColumn with Template for TelerikGrid

## Question

**Dom** asked on 19 Jul 2022

Hello, the first Output of "i" ( <GridColumn Title="@($" Grid { i }")"> ) works, the Output is 1,2,3,4,...10, but the second output ( <p> @($"pos: {ctx.GridSizePosition} - i: {i}") </p> ) "i" is always 11 (the last value +1 from of the loop). <GridColumn Field="@(nameof(ArticlePriceSize.PriceListKey))" /> @{
for (int i=0; i <=10; i++)
{ <GridColumn Title="@($" Grid { i }")"> <Template> @{
var ctx=context as ArticlePriceSize; <p> @($"pos: {ctx.GridSizePosition} - i: {i}") </p> } </Template> </GridColumn> }
} <GridColumn Field="@(nameof(ArticlePriceSize.AMSGridSizePosition))" /> How can I use the variable "i" in the Template?

## Answer

**Hristian Stefanov** answered on 22 Jul 2022

Hi Dominik, The described problem can get easily fixed. Using an additional variable instead directly the "i" will fix it. Let me share some information on the situation below. The current behavior is expected due to the way the Blazor framework renders child content. Rendering components inside a "for" loop requires a local index variable. Upon interest for more details, here is the Microsoft documentation. I have also prepared for you an example to show the above approach: <TelerikGrid Data="@GridData" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterRow"> <GridColumns> <GridColumn Field="Name" Title="Product Name" /> @for (int i=0; i <5; i++)
{ var count=i; <GridColumn Field="Price" Title="@($" Price - { count }")"> <Template> @{
var ctx=context as Product; <p> @($"pos: {ctx.Price} - i: { count }") </p> } </Template> </GridColumn> } </GridColumns> </TelerikGrid> @code {
List <Product> GridData { get; set; }

protected override void OnInitialized()
{
GridData=Enumerable.Range(1, 30).Select(x=> new Product
{
Id=x,
Name="Product name " + x,
Price=(decimal)(x * 3.14)
}).ToList();

base.OnInitialized();
}

public class Product
{
public int Id { get; set; }
public string Name { get; set; }
public decimal Price { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Dominik** commented on 25 Jul 2022

Hi Hristian, thank you, works perfect. Regards Dominik
