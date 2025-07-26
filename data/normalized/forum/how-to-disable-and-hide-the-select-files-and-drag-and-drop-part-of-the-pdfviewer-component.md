# How to disable and hide the Select Files and Drag and Drop part of the PDFViewer component?

## Question

**BenBen** asked on 20 Oct 2023

Hi, I want to disable and hide the marked part of the PDFViewer component. How can i do that? Thanks, Ben

## Answer

**Hristian Stefanov** answered on 23 Oct 2023

Hi Ben, To remove the marked part from the PDFViewer, you can use the following CSS style: <style>.k-pdf-viewer-pages.k-icon-xxxl,.k-pdf-viewer-pages.k-upload { display: none;
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

private const string PdfBase64="";
} Regards, Hristian Stefanov Progress Telerik

### Response

**John** commented on 21 Oct 2024

I also had to add the class ".k-dropzone-hint" to style to get rid of the text " Drag and drop files here to upload".

### Response

**Hristian Stefanov** commented on 22 Oct 2024

Hi John, Thank you for sharing your additions to the example so other developers can benefit from this. Kind Regards, Hristian
