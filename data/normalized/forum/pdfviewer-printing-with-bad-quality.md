# PdfViewer printing with bad quality

## Question

**Dom** asked on 09 Aug 2023

I have a byte[] of a PDF file that i show the user in a PdfViewer. In the toolbar, the user has the option to download the file or print it, in addition to other functions. If the user downloads the file, opens the PDF in Google Chrome and prints it, the print quality is the same as the PDF file. On the other hand, if the user prints directly from the PdfViewer, the quality shown in the preview is lower and the margins are different - it looks like it renders the print as an image of an A4 paper. Example of the bottom right corner in the Google Chrome print preview: Example of the bottom right corner in the PdfViewer print preview: Unfortunately, it is clearly visible that the quality is lower and the positioning is not the same. Is there a workaround for this issue?

### Response

**Georgi** commented on 14 Aug 2023

Hi Domingos Portela, The PDF print quality is lower due to the PDFViewer rendering documents as a <canvas> and printing them as a base64 raster image of this canvas. That is the standard way to print web page content directly from the browser. This can produce a different result compared to any vector content. We have a public task logged in our
