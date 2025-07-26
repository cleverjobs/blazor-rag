# Disable Blazor pdfViewer context menu

## Question

**wae** asked on 02 Oct 2024

1how i disable context menu in telerik pdfviewer how i disable text selection or copying

## Answer

**Hristian Stefanov** answered on 03 Oct 2024

Hi Wael, If by "context menu" you're referring to the component's toolbar, I can confirm that it can be easily hidden using CSS, along with disabling text selection and copying. Here's an example: <style> /* Disables text selection/copying */.k-pdf-viewer.k-canvas {
user-select: none; pointer-events: none;
} /* Removes toolbar */.k-pdf-viewer.k-toolbar { display: none;
} </style> <TelerikPdfViewer Data="@PdfSource" OnDownload="@OnPdfDownload" Height="600px"> </TelerikPdfViewer> @code {
private byte[] PdfSource { get; set; }

private async Task OnPdfDownload(PdfViewerDownloadEventArgs args)
{
args.FileName="PDF-Viewer-Download";
}

protected override void OnInitialized()
{
PdfSource=Convert.FromBase64String(PdfBase64);

base.OnInitialized();
}

private const string PdfBase64="JVBERi0xLjEKMSAwIG9iajw8L1R5cGUvQ2F0YWxvZy9QYWdlcyAyIDAgUj4+ZW5kb2JqCjIgMCBvYmo8PC9UeXBlL1BhZ2VzL0tpZHNbMyAwIFJdL0NvdW50IDEvTWVkaWFCb3ggWy00MCAtNjQgMjYwIDgwXSA+PmVuZG9iagozIDAgb2JqPDwvVHlwZS9QYWdlL1BhcmVudCAyIDAgUi9SZXNvdXJjZXM8PC9Gb250PDwvRjE8PC9UeXBlL0ZvbnQvU3VidHlwZS9UeXBlMS9CYXNlRm9udC9BcmlhbD4+ID4+ID4+L0NvbnRlbnRzIDQgMCBSPj5lbmRvYmoKNCAwIG9iajw8L0xlbmd0aCA1OT4+CnN0cmVhbQpCVAovRjEgMTggVGYKMCAwIFRkCihUZWxlcmlrIFBkZlZpZXdlciBmb3IgQmxhem9yKSBUagpFVAplbmRzdHJlYW0KZW5kb2JqCnhyZWYKMCA1CjAwMDAwMDAwMDAgNjU1MzUgZgowMDAwMDAwMDIxIDAwMDAwIG4KMDAwMDAwMDA4NiAwMDAwMCBuCjAwMDAwMDAxOTUgMDAwMDAgbgowMDAwMDAwNDkwIDAwMDAwIG4KdHJhaWxlciA8PCAgL1Jvb3QgMSAwIFIgL1NpemUgNSA+PgpzdGFydHhyZWYKNjA5CiUlRU9G";
} Regards, Hristian Stefanov Progress Telerik
