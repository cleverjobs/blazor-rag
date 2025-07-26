# Is it possible to set the width of the grid columns programmatically?

## Question

**Fla** asked on 27 Apr 2023

I would like to retrieve the width of the gris columns (to save it) and programmatically set it when needed. I tried using gridref.GridColumns but I don't know how to retrieve gridcolumn object.

### Response

**Flavio** commented on 27 Apr 2023

Edit I used this way to set width programmatically but I dont know how to retrieve current columns width to save it: the method "GetColumnWidth" retrieve column width by column name and set it. <GridColumns>
<GridCheckboxColumn />
<GridColumn Field=@nameof(Order.Id) Width="@GetColumnWidth(" Id " )" Title="ID" Editable="false" Filterable="false" />

## Answer

**Dimo** answered on 02 May 2023

Hi Flavio, The correct way to retrieve Grid column information is via the Grid state. See this example in the article. Regards, Dimo Progress Telerik
