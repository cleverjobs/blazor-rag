# Hide Blazor PdfViewerToolbar

## Question

**Mar** asked on 06 Nov 2023

I can hide the toolbar buttons by defining a blank toolbar component. But the toolbar, or the space that the toolbar occupies is still visible. <TelerikPdfViewer Data="Document.Image"> <PdfViewerToolBar> </PdfViewerToolBar> </TelerikPdfViewer>

## Answer

**Hristian Stefanov** answered on 07 Nov 2023

Hi Mark, By defining a blank toolbar component, the container indeed remains visible. Therefore, to hide the entire toolbar easily, use the following CSS style: <style>.k-pdf-viewer.k-toolbar { display: none;
} </style> <TelerikPdfViewer Data="@PdfSource" /> @code {
private byte[] PdfSource { get; set; }
} Please run and test the above code snippet to see the result. Regards, Hristian Stefanov Progress Telerik
