# PDFViewer Print from PrintButton different to printing PDF

## Question

**TimTim** asked on 13 Dec 2022

When printing from the print button on the PDF viewer (on Edge or Chrome), the print is inconsistent with printing the downloaded document. It seems to be printing an image of a web page containing the PDF rather an actually printing the PDF document In particular, when printing from the button: The print quality is visibly lower (printing is more gray than black). The document extents are smaller on the page. In some cases, the document prints across more pages than the actual PDF (e.g. 3 pages, when document is 1 page) If Chrome header options are on, the page shows web page printing headers and footers as well. Is this intended behaviour, or are there ways to modify this? We'd like to use the control, as it removes the need for JavaScript code used in our current control, but the print quality probably precludes using it at the moment. Thanks Tim McMaster

## Answer

**Dimo** answered on 13 Dec 2022

Hi Tim, The PDFViewer renders PDF documents as a <canvas> and prints them as a base64 raster image of this canvas. This can indeed produce a perceived difference in the end result, compared to any vector content. That's the standard way to print web page content directly from the browser. Otherwise, users will have to (download and) open the PDF document separately outside the context of a web page. How do you print the PDF documents currently? Regards, Dimo
