# Export All Pages as a button instead of a checkbox?

## Question

**Jas** asked on 05 Jan 2022

I would like two buttons that Export Page and Export All Pages, instead of the checkbox in the example. I tried setting the ExportAllPages in the OnClick, but as expected, the export runs before that OnClick. Maybe I'm missing an easier way to set that on a button? <GridToolBar> <GridCommandButton Command="CsvExport" Icon="file-csv" OnClick="(()=> SetExportAllPages())"> Export All Pages </GridCommandButton> <GridCommandButton Command="CsvExport" Icon="file-csv" OnClick="(()=> SetExportOnePage())"> Export Page </GridCommandButton>.... <GridExport> <GridCsvExport FileName="export" AllPages="@ExportAllPages" /> </GridExport>

## Answer

**Marin Bratanov** answered on 08 Jan 2022

Hello Jason, Thank you for bringing this up. Indeed, the CSV export does not seem to honor the AllPages settign, but the Excel one seems to on my end so hopefully that can be a workaround for you. I also logged this for review and you can Follow it here: [https://feedback.telerik.com/blazor/1548720-saveascsvfileasync-does-not-honor-allpages.](https://feedback.telerik.com/blazor/1548720-saveascsvfileasync-does-not-honor-allpages.) Regards, Marin Bratanov
