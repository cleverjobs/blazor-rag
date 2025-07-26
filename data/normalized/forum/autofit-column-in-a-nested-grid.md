# Autofit column in a nested grid

## Question

**Joh** asked on 11 Dec 2024

I'm trying to figure out how to autofit a column in a nested grid. In the Detail Template of a grid (Grid A), there is a another grid (Grid B). This nested grid (Grid B) has a column that shows the selections from a MultiSelect component. This could be a single value or multiple values. I know that there are methods that resize a column based on the column id or resize multiple columns, but these methods require a grid object reference. Since this nested grid (Grid B) is templated and therefore has multiple instances, I can't directly get a reference to it. Also, it seems that all the relevant Grid event handlers only have arguments return references to the data bound to the grid, but not a reference to the grid object. Is there a way to get a reference to a specific grid instance in a Detail Template or is there another way to auto size a specific column in a nested grid? Thanks

## Answer

**Dimo** answered on 13 Dec 2024

Hi Johnathan, Here is how to get all detail Grid instances. Each detail Grid reference is available for programmatic use in the next OnAfterRenderAsync call after the user expands a master row. Grid OnRowExpand event Grid OnStateChanged event Regards, Dimo Progress Telerik
