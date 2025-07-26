# Iterating over a List to create columns

## Question

**Jam** asked on 03 Apr 2023

Hi All, I'm looking to iterate over a list in my data model to dynamically create columns in a TelerikGrid. Is this functionality possible at the moment? Ideally i wanted to do something like this: <TelerikGrid Data="@GridRowItems"> <GridColumns> <GridColumn Field="@nameof(GridRowItem.Name)"> </GridColumn> @{
var gridRowItem=context as GridRowItem;
foreach (var childField in gridRowItem.ChildFields)
{ <GridColumn Title="@childField.Name"> <Columns> <GridColumn Field="@nameof(childField.Value1)"> </GridColumn> <GridColumn Field="@nameof(childField.Value2)"> </GridColumn> </Columns> </GridColumn> }
} </GridColumns> </TelerikGrid> class GridRowItem{
string Name;
List <ChildField> ChildFields;
}

class ChildField{
string Name;
double Value1;
double Value2;
} I can guarantee that every GridRowItem has the same number of ChildFields, but that number is variable Thanks

## Answer

**Ivan** answered on 07 Apr 2023

Hello! Try to use ExpandoObject: [https://blazorrepl.telerik.com/wnueYhFG25zuDqCr27](https://blazorrepl.telerik.com/wnueYhFG25zuDqCr27)
