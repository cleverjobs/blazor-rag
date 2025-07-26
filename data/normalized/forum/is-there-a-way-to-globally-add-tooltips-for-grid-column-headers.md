# Is there a way to globally add tooltips for grid column headers?

## Question

**Mik** asked on 05 Mar 2025

In many cases the header text of columns gets truncated to an ellipses if the columns aren't wide enough. It would be nice if there was a global way to display a tooltip for each column header that is made up of the header text. I know that I can do this using the column header template, but that will require that I create a template for every column in all of my grids. I'm looking for a way to have it work globally. Thanks, Mike

## Answer

**Anislav** answered on 05 Mar 2025

Hi Mike, I haven’t seen such an option in the documentation. So, I looked into the internal component code, including Grid, GridHeaderRow, and GridHeaderCell, and there is no way to globally customize column headers without explicitly providing a HeaderTemplate for each GridColumn in every instance where the Grid is used. Recently, a similar question was raised on the forum: Reusing GridColumns like WPF Resource Dictionaries. This suggests there is demand for such a feature. You might consider proposing it for implementation here: Telerik Blazor Feedback Portal. Regards, Anislav Atanasov
