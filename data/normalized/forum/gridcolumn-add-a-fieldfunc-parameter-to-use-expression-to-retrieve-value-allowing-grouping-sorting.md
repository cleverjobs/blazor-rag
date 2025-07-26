# GridColumn => Add a FieldFunc parameter to use expression to retrieve value allowing grouping, sorting ....

## Question

**Vin** asked on 23 Jan 2025

I have put an example where Field argument cannot fulfil what I need to do. The Column names and Field names are only discovered at runtime. I can get the values to be displayed as I want using the <Template> element/component however I cannot grouping or sorting on these columns. <TelerikGrid Data="@simplePropertiescollection" Height="500px" Sortable="true" Groupable="true" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SimpleProperties.Name))" Title="Name" /> @foreach (string prop in PropColumns)
{ <GridColumn FieldFunc="(v)=>v.GetProps(prop)" Title="@prop"> <Template> @{
// FieldFunc would replace the code below
string text=(context as SimpleProperties)?.GetProp(prop);
}
@text </Template> </GridColumn> } </GridColumns> </TelerikGrid> @code
{

List <SimpleProperties> simplePropertiescollection=new List <SimpleProperties> ();

List <string> PropColumns { get; set; }=new();

public class SimpleProperties
{
public string Name {get; set;}

public List<SimpleProperty?>? Properties { get; set; }

public string? GetProp(string name)
{
return Properties.FirstOrDefault((SimpleProperty o)=> o?.Name==name)?.Value;
}
}
public class SimpleProperty
{
public string? Name { get; set; }

public string? Value { get; set; }
}
}

## Answer

**Dimo** answered on 27 Jan 2025

Hello Vincent, The provided sample code relies on the following stepping stones: The Grid column definition depends on the data. Our Grid concept is the opposite - the column instances are created before the component is bound to data. The Grid column FieldFunc receives a data item as an argument and returns a data item value ("cell value") of unknown type. On the other hand, the existing Field parameter receives a property name as a string. So the two mechanisms are not an alternative to each other. A potential FieldFunc would be an unnecessary overhead, duplicate existing column template functionality, and require additional coupling with the data. If you need to configure columns at runtime after the data is received, please see some examples in the following articles: Bind the Grid to ExpandoObject How to maintain correct column order when generating columns in a loop Regards, Dimo Progress Telerik
