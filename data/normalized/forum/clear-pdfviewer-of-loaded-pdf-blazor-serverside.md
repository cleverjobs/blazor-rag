# Clear PdfViewer of Loaded PDF (Blazor serverside)

## Question

**AlAl** asked on 27 Jun 2025

I have a page where users select a row in a grid to change the document that should be loaded into the PdfViewer component (Blazor serverside). They will not have the ability to use the open document button or select document button provided by the component. When I select a row in the grid, the PdfViewer component shows the corresponding pdf properly. However, if the page gets in a state where there are no rows in that grid, I want the PdfViewer component to revert to an empty state. It should not be showing the previously selected PDF. I have tried the following based on a previous post ( [https://www.telerik.com/forums/how-do-i-clear-the-pdfviewer](https://www.telerik.com/forums/how-do-i-clear-the-pdfviewer) ): -setting the byte array to [] -setting the byte array to null -calling Rebind on the PdfViewer component -calling StateHasChanged -having the method changing the byte array be synchronous and asynchronous Setting the byte array to [] just flashes the loading indicator briefly but the component still shows the previous pdf. Setting the byte array to null just keeps the loading indicator displayed indefinitely with the previously displayed pdf underneath. The other suggestions had no other effect. How do I unload the PDF from the PdfViewer component?

## Answer

**Ivan Danchev** answered on 29 Jun 2025

Hello Al, To clear the loaded pdf, pass an empty byte array to the Data parameter of the PDFViewer and re-render it. See this example: [https://blazorrepl.telerik.com/mJYgmtcl319b4x5T04](https://blazorrepl.telerik.com/mJYgmtcl319b4x5T04) Note how the PDFViewerVisible property is used to show (re-render) PDFViewer after a small delay. Regards, Ivan Danchev Progress Telerik

### Response

**Al** commented on 03 Jul 2025

Thanks Ivan, that helped a lot. A note for others, sometimes I had to use the Task.Delay as demonstrated above, and sometimes StateHasChanged worked.

### Response

**Ivan Danchev** commented on 08 Jul 2025

Just a note, we do have a bug report related to clearing an already loaded file: [https://feedback.telerik.com/blazor/1589890-deleting-manually-the-pdfviewer-document-data-causes-endless-loader](https://feedback.telerik.com/blazor/1589890-deleting-manually-the-pdfviewer-document-data-causes-endless-loader) The suggested workaround is valid for this case, but once the issue is fixed, re-initializing the component won't be needed.
