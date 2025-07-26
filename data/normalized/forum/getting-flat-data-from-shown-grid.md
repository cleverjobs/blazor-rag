# Getting "flat" data from shown Grid

## Question

**Ray** asked on 20 Aug 2021

Hi, I want to export the data which is shown in a Grid. The Grid is filterable, groupable and contains a Sum aggregate. The built-in export function is a bit too inflexible regarding the the formatting etc. So I need to create an own Excel report and I need to pull the (flat) data out of the Grid. Only data which is shown on the page (filtered etc) should be exported. So I need to get the "processed" Grid data. Does anyone know how to get the data? I've already tried to use the OnRead event pull that data. But together with grouping and a Sum aggregate the I get the error: "Error: System.InvalidOperationException: No generic method 'Sum' on type 'System.Linq.Enumerable' is compatible with the supplied type arguments and arguments. No type arguments should be provided if the method is non-generic." This behaviour is already explained here: [https://feedback.telerik.com/blazor/1516871-manual-source-operations-with-grouping-and-aggregates.](https://feedback.telerik.com/blazor/1516871-manual-source-operations-with-grouping-and-aggregates.) But no solution so far. Best regards, Rayko
