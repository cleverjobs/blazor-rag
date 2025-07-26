# ExcelExport in Blazor UI Grid

## Question

**Jay** asked on 30 Jun 2023

Hello, I want to change the filename dynamically after the initial loading of a grid in a razor page, So lets say I refresh a grid after a search and export to a file telerik_101123.xlsx. (10:11:23 being the current time). Then 2 min later I refresh the grid again and export it to telerik_101323.xlsx. How can I do that

### Response

**Deasun** commented on 03 Jul 2023

This is the grid tag you need to set: <GridExport> <GridExcelExport FileName="@msExportFileName" AllPages="@Revenue_ExportAllPages" OnBeforeExport="@Revenue_OnBeforeExcelExport" /> </GridExport> This is the variable you need for the name: msExportFileName In code behind: string msExportFileName="Rpt_"; where you set the name is the important thing. msExportFileName="Rpt_" + RptFilters.strFilter01.Replace("/", "") + "_" + msRevGrid_Lvl1Pick + "_" + strItemIs; { you'd set that with your naming convention. } try to do it somewhere before OnBeforeExcelExport gets called. Doing it in there wont work. So under a DDL or button object. Or in my case above where I have sub grids within main grid I do it on the OnRowExpand() & OnRowCollapse() Hope that helps. Deasun.

## Answer

**Yanislav** answered on 04 Jul 2023

Hello Jayakumar, The goal seems achievable. Allow me to offer the following steps to accomplish it: Create a custom button. In the OnClick event of the button, modify the file name and export the Grid using the SaveAsExcelFileAsync method. Here's a REPL example that demonstrates this approach: [https://blazorrepl.telerik.com/mHOLOebk00SDPXGU53](https://blazorrepl.telerik.com/mHOLOebk00SDPXGU53) I hope you find this information helpful. Regards, Yanislav
