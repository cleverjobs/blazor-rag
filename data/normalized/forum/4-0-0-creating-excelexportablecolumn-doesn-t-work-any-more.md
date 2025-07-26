# 4.0.0 Creating ExcelExportableColumn doesn't work any more

## Question

**BobBob** asked on 18 Jan 2023

Since updating to 4.0.0 I am getting error when creating a new ExcelExportableColumn now. var isBugColumn=new Telerik.Blazor.Common.Export.Excel.ExcelExportableColumn() { Field="IsBug", Title="Is Bug" }; Getting error that "ExcelExportableColumn is inaccessible due to its protection level"

## Answer

**Nadezhda Tacheva** answered on 20 Jan 2023

Hi Bob, In UI for Blazor 4.0. we introduced enhancements for the export functionality. More specifically, we removed the NumberFormat and Width properties of the column for CSV export as they were not applicable for CSV documents. This change required dividing the ExcelExportableColumn object that both of the exports shared in order to deliver the different behavior. Thus, instead of ExcelExportableColumn which is now internal, one should use the corresponding object type based on the export type - GridExcelExportColumn for Excel export and GridCsvExportColumn for CSV export. I realize this change is not listed in the breaking changes article and the export documentation, so please accept my apologies for the trouble. I will update the articles as soon as possible. While I was investigating the case, I came upon an issue with the GridExcelExportColumn and GridCsvExportColumn classes - currently, they do not have public parameterless constructors, so it is not possible to create instances of them in the OnBeforeExport handler in order to add a hidden column to the exported file. I already informed our development team and they were able to fix it. There is a logged issue in the public portal, so you and any other affected parties may track it: I cannot add exportable column through OnBeforeExport event We will plug the fix into a patch release that will be live in the upcoming week. Regards, Nadezhda Tacheva Progress Telerik
