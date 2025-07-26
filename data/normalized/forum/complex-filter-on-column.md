# Complex filter on column

## Question

**Wal** asked on 19 May 2020

GridFilterMode.FilterMenu allows to open popup with 2 conditions per column joined with logical conjunction: "and" "or". Is it possible to have more conditions per column? For example: Salary> 20 and Salary <100 and not ( Salary=50)

## Answer

**Marin Bratanov** answered on 20 May 2020

Hi Waldek, You will be able to implement custom filters to add more conditions when this gets implemented: [https://feedback.telerik.com/blazor/1407773-custom-filter-components-filter-template.](https://feedback.telerik.com/blazor/1407773-custom-filter-components-filter-template.) For the time being, the only option is to put desired popups (e.g., animation containers ) in the header template or outside of the grid so you can set the desired filter through the grid state. Regards, Marin Bratanov
