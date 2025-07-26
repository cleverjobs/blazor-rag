# Grid export with large dataset filtered results

## Question

**Dea** asked on 16 Oct 2023

Ok I have a grid with many pages and a total of say 1million plus rows! User filters this grid down to say 7000 rows. When I click the export all button it will export the rows they filtered. Alls good. But when they export the whole dataset I have to intercept that to do the export myself and email them a link to it. My issue is I cant seem to find a way to figure out how many rows are in the filtered version. So currently I have: ( in the async Task gridRpt_OnBeforeExcelExport(GridBeforeExcelExportEventArgs args) ) If the grid.count> 1000000 then go do my email export procedure ELSE do the grids default export. Problem is when the grid is filtered That grid.count is still the big dataset count not the filtered count. How do I know the filtered count and if that filtered count is still over 1mil how to I export only that filtered set? Hope that makes sense. Thanks Deasun.

## Answer

**Dimo** answered on 19 Oct 2023

Hello Deasun, There are two Grid features that can help you in this case. Use one or both, according to your preferences. To detect user filtering operation in advance, use the Grid OnStateChanged event and the information in the Grid state. You can maintain a flag variable, which indicates if the Grid is filtered or not, and use it in OnBeforeExport. However, you can't obtain the total number of filtered rows on all pages. Bind the Grid with its OnRead event and keep track of the filtering configuration in the DataSourceRequest and the returned filtered data and total filtered item count. When you export all pages, OnRead will fire again before OnBeforeExport. You will be able to detect an imminent Excel export, because args.Request.PageSize will be 0. Regards, Dimo Progress Telerik
