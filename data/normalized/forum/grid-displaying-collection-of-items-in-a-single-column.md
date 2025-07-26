# Grid: Displaying Collection Of Items In A Single Column

## Question

**Tim** asked on 03 Feb 2023

Let's say you have a grid of customers and you want to show the last five order numbers for that customer in a single column. How could this be done WITH data binding? So, specifically you have a grid with two columns: Name & Last 5 Order Numbers and it might looks like Name | Last 5 Order Numbers Acme | #1, #100, #200, #201, #202 Ford | #11, #1100, #1200, #1201, #1202 Example Model public class CustomerModel { public string Name { get; set; } public List <string> Last5OrderNumber { get; set; }=new List<string>();
} I came up with this, but wondering if there's a better way: [https://blazorrepl.telerik.com/cnEmunlL45zKNYAF51](https://blazorrepl.telerik.com/cnEmunlL45zKNYAF51)

## Answer

**Svetoslav Dimitrov** answered on 08 Feb 2023

Hello Timothy, What you need to do is to add a string property in the CustomerModel and link it to the Last5OrderNames. I have created a basic code snippet that I believe does the things with a smaller amount of code: <TelerikGrid Data=@customers Pageable="true" Height="400px"> <GridToolBarTemplate> <span class="k-toolbar-spacer"> </span> @* add this spacer to keep the searchbox on the right *@<div onkeydown="event.stopPropagation()"> <GridSearchBox /> </div> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@(nameof(CustomerModel.Name))" /> <GridColumn Field=@nameof(CustomerModel.Orders) /> </GridColumns> </TelerikGrid> @code {
public List <CustomerModel> customers { get; set; }=new List <CustomerModel> ()
{
new CustomerModel()
{
Name="Acme",
Last5OrderNumber=new List <string> (){ "#1", "#100", "#200" }
},
new CustomerModel()
{
Name="Ford",
Last5OrderNumber=new List <string> (){ "#11", "#13", "#22" }
}
};

public class CustomerModel
{
public string Name { get; set; }
public List <string> Last5OrderNumber { get; set; }=new List <string> (); public string Orders=> String.Join(", ", Last5OrderNumber); }
} Regards, Svetoslav Dimitrov
