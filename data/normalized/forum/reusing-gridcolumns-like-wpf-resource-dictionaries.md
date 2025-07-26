# Reusing GridColumns like WPF resource dictionaries

## Question

**Had** asked on 04 Feb 2025

Hi! I'm doing a migration from a WPF application to Blazor and I would like to know if there is a way to make a column of a grid reusable. Example: In WPF you can have a resource dictionary and reference it from the component in question to represent data with the same UI, in Blazor I think this is not possible, the only thing I can think of is to componentize the columns but I'm not sure if this is the right way to do it. Is there any contemplated or recommended way? Thanks in advance! Telerik WPF - CellTemplate

## Answer

**Anislav** answered on 13 Mar 2025

Hi Hadrian, If the changes you need cannot be achieved with a custom theme ( [https://www.telerik.com/blazor-ui/documentation/styling-and-themes/custom-theme](https://www.telerik.com/blazor-ui/documentation/styling-and-themes/custom-theme) ), then I agree that the best approach would be to create a custom column component that wraps the GridColumn and customize it as needed. Here’s an article from the knowledge base with an example of a reusable custom column: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-create-reusable-columns](https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-create-reusable-columns) Regards, Anislav Atanasov
