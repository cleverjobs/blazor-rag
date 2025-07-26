# GridExcelExportColumn Position

## Question

**Isr** asked on 05 Sep 2023

Hello forum, does anyone know how can I get the position of GridExcelExportColumn? I need to insert a few Hidden Columns in a specific place on grid's OnAfterExport Event is this the way to go? GridExcelExportColumn afterThisColumnIWantToInsertHiddenColumns=args.Columns.Find(x=> x.Field==nameof (Model.Property)); var index=args.Columns.IndexOf( afterThisColumnIWantToInsertHiddenColumns ) args.Columns.InsertRange( index, hiddenColumns);

### Response

**Hristian Stefanov** commented on 08 Sep 2023

Hi Israel, From the provided information, I understand that your main goal is to add hidden columns at a specific place that will appear in the exported Grid file. To achieve this, the way I recommend is to use the OnBeforeExport event instead of OnAfterExport. By doing so, you can easily insert the desired hidden columns at whatever index you need to see it in the exported file. To illustrate this concept, I have prepared an example for you in this REPL link. Please run and test it to determine whether the result is what you are looking for. If I missed addressing something or I misunderstood the general idea, I remain at your disposal to assist further. Kind Regards, Hristian
