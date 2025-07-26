# Export to excel performance from grid - Blazor Wasm

## Question

**Mar** asked on 15 Apr 2024

Hi Are there any plans on improving the performance on the default export to excel from a Telerik grid using Blazor Wasm? As seen in this example: [https://docs.telerik.com/blazor-ui/components/grid/export/excel#basics](https://docs.telerik.com/blazor-ui/components/grid/export/excel#basics) <TelerikGrid Data="@GridData" Pageable="true" Sortable="true" Resizable="true" Reorderable="true" FilterMode="@GridFilterMode.FilterRow" Groupable="true"> <GridToolBarTemplate> <GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileExcel"> Export to Excel </GridCommandButton> <label class="k-checkbox-label"> <TelerikCheckBox @bind-Value="@ExportAllPages" /> Export All Pages </label> </GridToolBarTemplate> <GridExport> <GridExcelExport FileName="telerik-grid-export" AllPages="@ExportAllPages" /> </GridExport> <GridColumns> Columns.. </GridColumns> </TelerikGrid> At the moment we have about 150 columns and 4000 rows that needs to be exported which takes quite a while. If not what are your recommendations in speeding up the excel export?

## Answer

**Dimo** answered on 18 Apr 2024

Hello Markus, The built-in Grid Excel export relies on a SpreadStreamProcessing routine, which is pretty simple. We have some feature requests for SpreadStreamProcessing performance improvements during large file and WASM export, but frankly, I am not sure we will be able to make WASM exporting of such large files instant in the foreseeable future. WebAssembly performance is generally worse in resource-intensive scenarios. My suggestion is to export the Grid data manually with SpreadStreamProcessing on the server and send the ready file to the user. Regards, Dimo Progress Telerik
