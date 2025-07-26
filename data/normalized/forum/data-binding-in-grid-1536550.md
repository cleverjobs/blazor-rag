# Data binding in Grid

## Question

**Chr** asked on 23 Sep 2021

Hello, I have the following data model which I want to display in TelerikGrid. The columns should be Name, Price (which is easy), but I also want to display the topping columns, where each caption is the key of the dicionary entry and the displayed value should be the value from the dictionary entry: Expected result: Name | Price | Tomato | Cheese | Bacon Cheese | 8.99 | low | very much | no Tomato | 5.99 | very much | not so much | no Bacon | 10.99 | low | not so much | three pieces Is that possible by using the TelerikGrid and how should the data binding look like ? I took the sample code from the expando sample to create the columns based on the dictionary entries but I didn't get the values from the dictionary to display each value in the rows. public class Pizza { public string Name { get; set; } public decimal Price { get; set; } public IDictionary<string, string> Toppings { get; set; } public static IList<Pizza> PizzaRecipies ( ) { return new List<Pizza>()
{ new Pizza()
{
Name="Cheese",
Price=8.99 M,
Toppings=new Dictionary<string, string>()
{
{ "Tomato", "low" },
{ "Cheese", "very much" },
{ "Bacon", "no" }
}
}, new Pizza()
{
Name="Tomato",
Price=5.99 M,
Toppings=new Dictionary<string, string>()
{
{ "Tomato", "very much" },
{ "Cheese", "not so much" },
{ "Bacon", "no" }
}
}, new Pizza()
{
Name="Bacon",
Price=10.99 M,
Toppings=new Dictionary<string, string>()
{
{ "Tomato", "low" },
{ "Cheese", "not so much" },
{ "Bacon", "three pieces" }
}
}

};
}
}

## Answer

**Radko** answered on 27 Sep 2021

Hi Christian, In this case, you can bind the Grid in several ways. If you prefer using a Dictionary, a GridColumn Template might do the job for you: First, you need to introduce a collection with all the available toppings, which will be used to generate the columns: public List<string> Toppings=> new List<string> { "Tomato", "Cheese", "Bacon" }; Then, within the Grid, you can iterate the Toppings collection to generate a column for each topping: <TelerikGrid Data="@Data">... foreach (var topping in Toppings)
{ <GridColumn Title="@topping"> <Template> @((context as Pizza).Toppings.First(entry=> entry.Key==topping).Value) </Template> </GridColumn> } ... </TelerikGrid> The final result looks like the desired one (the source code is also attached): Another approach would be to use a dynamic ExpandoObject and populate the columns dynamically. We have a demo for this here - Binding to Expando object Lastly, as mentioned in these docs - Grid Data Bound Columns - Notes, it might be best to simply flatten the Dictionary before passing it to the Grid. I trust the above will help you resolve this. In case of any more questions, do not hesitate to reach out. Thank you! Regards, Radko Stanev
