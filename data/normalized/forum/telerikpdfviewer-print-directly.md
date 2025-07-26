# TelerikPdfViewer: Print directly

## Question

**Hen** asked on 06 Jul 2023

I create a PDF-Document on the fly and want print it immediately afterwards. Actually I am using TelerikPdfViewer to show the PDF on screen but the user has to click on the Print-Button and the another time in the follwing print dialog from the browser. I would like to print immediately to the default printer without preview. And to spice it up: I would like to print it 3 times! Is there by any chance to achieve that ?

## Answer

**Dimo** answered on 07 Jul 2023

Hi Hendrik, Use the Print() method of the PDF Viewer to print without the user having to click on a button. However, the app has no control over the print preview behavior of the browser. Regards, Dimo

### Response

**Hendrik** commented on 14 Jul 2023

Hi Dimo, Thank you very much for your answer. Technically, it is correct. Unfortunately my requirements are a bit more complicated: In my MainLayout I have a "Print" component with a TelerikWindow and inside the WindowContent is the PDFViewer. The component is invisible. When the user presses a button a PDF is generated and the Print component is set to Visible and the PDF is displayed nicely. When I use the .Print() method, the browser print dialog is displayed as expected, but the PDFViewer is still open and the user has to close it manually. This is too many clicks. I just want to show the browser dialog without showing the PDF/PDF viewer. I tried setting IsVisible to false after the .Print() method, but then the browser dialog is no longer displayed. Maybe my whole approach is too complicated, but so far it was a very convinient solution until I wanted a "silent" Printmode. I still want to have it both ways. With preview of the PDF and without, depending on the Users Preferences.. I hope you get what I try to explain...

### Response

**Dimo** commented on 14 Jul 2023

The desired behavior requires some kind of a hack. If the PdfViewer is inside a Window, the Window must have Visible="true" to be rendered on the page (together with the PdfViewer). So either apply position, which will move the Window outside the viewport, or don't use a Window at all. The example below shows how to move the Window outside the viewport. However, the Window remains open even after printing. Since you don't know when exactly the user will start printing, you will have to think when to actually remove the Window from the page via Visible="false". <TelerikButton OnClick="@PrintPdf">Print</TelerikButton> <TelerikWindow @bind-Visible="@WindowVisible" Top="-1000px" Left="-1000px" Width="600px" Height="600px"> <WindowContent> <TelerikPdfViewer @ref="@PdfViewerRef" Data="@PdfSource"> </TelerikPdfViewer> </WindowContent> </TelerikWindow> @code {
bool WindowVisible { get; set; }

private byte[] PdfSource { get; set; }

TelerikPdfViewer PdfViewerRef { get; set; }=null!; async Task PrintPdf ( ) {
WindowVisible=true; await Task.Delay( 500 );

PdfViewerRef.Print(); // think of when and how to set Visible="false" for the Window sometime later }

protected override void OnInitialized ( ) {
PdfSource=Convert.FromBase64String(PdfBase64);

base.OnInitialized();
}

private const string PdfBase64="JVBERi0xLjEKMSAwIG9iajw8L1R5cGUvQ2F0YWxvZy9QYWdlcyAyIDAgUj4+ZW5kb2JqCjIgMCBvYmo8PC9UeXBlL1BhZ2VzL0tpZHNbMyAwIFJdL0NvdW50IDEvTWVkaWFCb3ggWy00MCAtNjQgMjYwIDgwXSA+PmVuZG9iagozIDAgb2JqPDwvVHlwZS9QYWdlL1BhcmVudCAyIDAgUi9SZXNvdXJjZXM8PC9Gb250PDwvRjE8PC9UeXBlL0ZvbnQvU3VidHlwZS9UeXBlMS9CYXNlRm9udC9BcmlhbD4+ID4+ID4+L0NvbnRlbnRzIDQgMCBSPj5lbmRvYmoKNCAwIG9iajw8L0xlbmd0aCA1OT4+CnN0cmVhbQpCVAovRjEgMTggVGYKMCAwIFRkCihUZWxlcmlrIFBkZlZpZXdlciBmb3IgQmxhem9yKSBUagpFVAplbmRzdHJlYW0KZW5kb2JqCnhyZWYKMCA1CjAwMDAwMDAwMDAgNjU1MzUgZgowMDAwMDAwMDIxIDAwMDAwIG4KMDAwMDAwMDA4NiAwMDAwMCBuCjAwMDAwMDAxOTUgMDAwMDAgbgowMDAwMDAwNDkwIDAwMDAwIG4KdHJhaWxlciA8PCAgL1Jvb3QgMSAwIFIgL1NpemUgNSA+PgpzdGFydHhyZWYKNjA5CiUlRU9G";
}

### Response

**Hendrik** commented on 14 Jul 2023

Hi Dimo, that does the trick !! Thank you very much. Although it is not Telerik related, but do you have any Idea how to set the Window of the Browser-Print-Dialog to a certain size ? It opens in a kind of ugly way (Microsoft Edge) and how can I preset the number of copies to 3 in the dialog ? You would become my hero for the day if you have an answer to this... (no pressure) ;-)

### Response

**Dimo** commented on 14 Jul 2023

The small print preview window might be related to the small dummy PDF file in my example. Or at least a "true" larger PDF file also triggers a larger print preview window on my side.

### Response

**Hendrik** commented on 18 Jul 2023

Hello Dimo, thank you for your support. I solved it now totally different without the PDF-Viewer. In this case the Viewer is not neccessary anyways.
