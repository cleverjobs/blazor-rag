# How do I clear the PDFViewer?

## Question

**Gab** asked on 07 Jun 2024

Right now it is previewing a PDF, and neither rebinding, matching its data with array[0] or null, nor even matching the component reference with a new one works.

### Response

**Kirk** commented on 26 Jul 2024

I was able to set Data on the initial document. But when I changed document (data) it would not refresh properly. I was using an Async Void to set PdfViewer DATA and it would work the first time then not Rebind() (Refresh) on subsequent updates. I changed my method for updating to a Void or Async Function and return a Task and it works perfect when I update DATA on PdfViewer

### Response

**Kirk** commented on 26 Jul 2024

I had to change it to synchronous Void to get it to work correctly. I do have the PdfViewer inside a Telerik Window component. and I call StateHasChanged(); and the end of my method. (Not using PdfViewer.Rebind())
