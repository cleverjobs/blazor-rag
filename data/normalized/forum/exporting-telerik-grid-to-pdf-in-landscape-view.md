# Exporting Telerik Grid to PDF in Landscape View

## Question

**jul** asked on 24 Mar 2025

I am currently using the Telerik Grid and have successfully exported data to PDF in portrait orientation. However, I need to export the grid in landscape view to better fit the data. Is there a built-in way or any workaround to achieve this?

## Answer

**Anislav** answered on 26 Mar 2025

You should be able to achieve this by adding the following code snippet inside your TelerikGrid definition: <GridExport> <GridPdfExport PageOrientation="GridPdfExportPageOrientation.Landscape" /> </GridExport> Regards, Anislav Atanasov

### Response

**Anislav** commented on 08 Apr 2025

Does it work for you?

### Response

**julien** commented on 08 Apr 2025

Yes thank you
