# PivotGrid - Retrieve groups from cell

## Question

**Jea** asked on 13 Mar 2025

Hello everyone, Is there a way to get access to the group names at the cell level of a PivotGrid? The PivotGridDataCellTemplateContext has internal IGroup properties that would fit my need, but those are internals. Is there of way to access/stored them or any work arounds? My goal would be to generate a cell "onclick=@()=>MyMethod(Group1, Group2)" event that would pass those informations to a method. Ultimatly, the method would filter a List/Grid under the PivotGrid. Thank you very much

## Answer

**Anislav** answered on 13 Mar 2025

It looks like the PivotGrid is a Razor component that is imported from Telerik UI for ASP.NET Core. Unfortunately, it does not provide built-in events like "on cell selected," which would be useful in this case. The only workaround I can think of is to use the DataCellTemplate, implement the onclick event as you mentioned, and trigger some JavaScript to extract the group data. However, this approach won’t be straightforward. Unlike the regular TelerikGrid, the rendered HTML table and rows in the PivotGrid do not include attributes like data-render-row-index or data-col-index. This means you would need to determine these indices manually. Regards, Anislav Atanasov

### Response

**Jean-François** answered on 13 Mar 2025

Thank you for your feed back! I wanted to avoid the JavaScript approach and it seems to be my only option (as of now with the PivotGrid). I'll take a look at the TelerikGrid component. The features you described might be enough for my needs. Thank you, JF
