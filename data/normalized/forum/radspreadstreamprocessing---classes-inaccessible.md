# RadSpreadStreamProcessing - classes inaccessible

## Question

**Dea** asked on 17 Jan 2025

Hi, I'm sure I'm being stupid but could anyone help with why the following classes are inaccessible when I try to follow the example at [https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-custom-cell-formatting-with-radspreadstreamprocessing#custom-cell-formatting-of-the-exported-file-with-radspreadstreamprocessing?](https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-custom-cell-formatting-with-radspreadstreamprocessing#custom-cell-formatting-of-the-exported-file-with-radspreadstreamprocessing?) It's not like they are completely unrecognised, just inaccessible due to their protection level. What am I missing? Thanks, Dean 'CellValueType' is inaccessible due to its protection level 'IWorkbookImporter' is inaccessible due to its protection level 'SpreadImporter' is inaccessible due to its protection level 'IWorksheetImporter' is inaccessible due to its protection level 'IWorkbookImporter.WorksheetImporters' is inaccessible due to its protection level 'IWorksheetImporter.Name' is inaccessible due to its protection level 'IRowImporter' is inaccessible due to its protection level 'IWorksheetImporter.Rows' is inaccessible due to its protection level 'IRowImporter.RowIndex' is inaccessible due to its protection level 'ICellImporter' is inaccessible due to its protection level 'IRowImporter.Cells' is inaccessible due to its protection level 'ICellImporter.Value' is inaccessible due to its protection level 'ICellImporter.Format' is inaccessible due to its protection level 'ICellImporter.ColumnIndex' is inaccessible due to its protection level 'ICellImporter.RowIndex' is inaccessible due to its protection level 'ICellImporter.ColumnIndex' is inaccessible due to its protection level 'IRowImporter.RowIndex' is inaccessible due to its protection level

## Answer

**Dimo** answered on 17 Jan 2025

Hi Dean, All these are public, so this is either some Visual Studio bug (try restarting it), or something is misconfigured in the app itself. Try the example from our documentation in a brand new empty app and then compare the two apps. [https://docs.telerik.com/devtools/document-processing/api/telerik.windows.documents.spreadsheet.model.cellvaluetype](https://docs.telerik.com/devtools/document-processing/api/telerik.windows.documents.spreadsheet.model.cellvaluetype) [https://docs.telerik.com/devtools/document-processing/api/telerik.documents.spreadsheetstreaming.iworkbookimporter](https://docs.telerik.com/devtools/document-processing/api/telerik.documents.spreadsheetstreaming.iworkbookimporter) [https://docs.telerik.com/devtools/document-processing/api/telerik.documents.spreadsheetstreaming.spreadimporter](https://docs.telerik.com/devtools/document-processing/api/telerik.documents.spreadsheetstreaming.spreadimporter) Regards, Dimo Progress Telerik

### Response

**Dean** commented on 17 Jan 2025

Is there a minimum version of Telerik.Documents.SpreadsheetStreaming I need? I'm only on 2022.2.428.

### Response

**Dimo** commented on 17 Jan 2025

Each Telerik UI for Blazor version requires a specific version of Telerik Document Processing: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/dpl-version-conflict-detected-telerik-zip#upgrade-or-downgrade-nuget-package-versions](https://www.telerik.com/blazor-ui/documentation/knowledge-base/dpl-version-conflict-detected-telerik-zip#upgrade-or-downgrade-nuget-package-versions)

### Response

**Dean** commented on 20 Jan 2025

I get the same behaviour in a brand new empty app - see attached

### Response

**Dimo** commented on 20 Jan 2025

@Dean - thanks for the app. I dug deeper and it turned out that the KB example is using Telerik Document Processing features, which are not available for your version 2022.2.428. The situation is:.NET 8 is supported by Telerik UI for Blazor 5.x. I recommend at least 5.1.1, which requires Telerik Document Processing 2024.1.124. If I use these two versions, then the app builds and runs fine. If you must use older Telerik product versions, then you can go with.NET 6 + Telerik UI for Blazor 3.6.1 + Telerik Document Processing 2022.3.906. This is the oldest DPL version that can integrate with the code in the discussed KB without compilation errors.

### Response

**Dean** commented on 20 Jan 2025

Ok, I can actually use 2022.3.906 with Telerik UI for Blazor 3.3.0, and this fixes the problem and doesn't appear to have broken anything else. Thanks.
