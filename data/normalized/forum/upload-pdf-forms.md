# Upload PDF Forms

## Question

**Bri** asked on 16 Mar 2023

I would like my Blazor application to be able to upload PDF Forms (editable PDF documents) for storage that the application will later use by prefilling customer data into them. The PDFViewer shows an empty PDF when I read in the bytes and display them I then tried to copy the document using the PdfFormatProvider, on the import it fails. Code lines: PdfFormatProvider provider=new PdfFormatProvider(); RadFixedDocument document=new RadFixedDocument(); document=provider.Import(file.OpenReadStream()); Error: Cannot obtain value of the local variable or argument because it is not available at this instruction pointer, possibly because it has been optimized away. Not sure why the provider does not like these PDF files, also not sure if it is an issue or meant to work.

## Answer

**Nadezhda Tacheva** answered on 20 Mar 2023

Hi Brian, Opening an editable PDF document and filling forms in it is part of the Annotations story. The PDFViewer internally uses PDF.js to render PDF files in the browser. Currently, adding and editing annotations is an existing feature request at PDF.js. Once this is implemented in PDF.js, we will be able to consider such enhancement for the PDFViewer in UI for Blazor. You may vote for and follow the public feature request here: [https://feedback.telerik.com/blazor/1583630-view-annotations.](https://feedback.telerik.com/blazor/1583630-view-annotations.) Having the above in mind, the PDFViewer cannot currently open an editable file. I hope you will find this information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva

### Response

**Brian** commented on 20 Mar 2023

That is part of the question. Maybe it answers the first part as well. Is the PDF.js used also PdfFormatProvider.Import? that is the first part that is failing.

### Response

**Brian** commented on 20 Mar 2023

Also to add to it a PDF Annotation is not the same thing as a PDF Form. A PDF Form has editable fields in it that allow you to fill in a space like a name of the person filling it out. An Annotation is like a note in the document about something.

### Response

**Nadezhda Tacheva** commented on 21 Mar 2023

Hi Brian, Let me address your questions separately: File import Generally speaking, it is not needed to additionally copy the file using the PdfFormatProvider - the PDFViewer can accept the file directly through the Data parameter. For example: [https://blazorrepl.telerik.com/wnYncFPG005QUYa843.](https://blazorrepl.telerik.com/wnYncFPG005QUYa843.) The key point in this scenario is that the user will not be able to type or add objects on top of the document. This functionality is dependent on PDF.js as we've discussed. So, even if you successfully copy the file using the PdfFormatProvider, the PDFViewer will not be able to display it and allow typing as it depends on the PDF.js. PDF Annotation vs Editing We are considering form filling as annotations since in essence, PDF annotating allows users to add objects to an existing PDF file. Editing, on another hand, would mean changing the actual file content. Check [https://helpx.adobe.com/acrobat/using/fill-and-sign.html](https://helpx.adobe.com/acrobat/using/fill-and-sign.html) for reference. I hope this provides more clarity on the matter.

### Response

**Brian** commented on 21 Mar 2023

Ok a display is all I want at first. I will review what you added to see if i can get that to work.

### Response

**Brian** commented on 22 Mar 2023

I am not getting this to work. Here is some of my code (I am not able to upload the actual PDF form I am using here) Index.razor <div class="container"> <main role="main" class="pb-3"> <h3>Add Document Template</h3> <TelerikButton OnClick="@ReturnDocPreviewClick">Return to Document Template List</TelerikButton> <br /><br /> <TelerikForm Model="@previewdoc" OnSubmit="@TemplateSubmit"> <FormItems> <FormItem Field="@nameof(previewdoc.DocTypCd)" LabelText="Document Type Code" Enabled="false" /> <FormItem Field="@nameof(previewdoc.DocFormatCd)" LabelText="Document Format Code*"> <Template> @{ <label>Document Format Code*</label> <TelerikDropDownList Data="docformats" @bind-Value="@previewdoc.DocFormatCd" TextField="@nameof(Doc.DocFormatCd)" ValueField="@nameof(Doc.DocFormatCd)" /> } </Template> </FormItem> <FormItem Field="@nameof(previewdoc.Descript)" LabelText="Description" /> <FormItem Field="@nameof(previewdoc.EffDate)" LabelText="Effective Date" /> <FormItem Field="@nameof(previewdoc.InActiveDate)" LabelText="Inactive Date" /> <FormItem> <Template> @{ <InputFile OnChange="OnDocSelectChange" /> <br /> <div class="k-form-hint">Accepted files: <strong>PDF</strong></div> <br /> if (fileloaderrors.Count> 0) { <h5>Load Errors</h5> <ul class="text-danger"> @foreach (var error in fileloaderrors) { <li>@error</li> } </ul> } } </Template> </FormItem> </FormItems> </TelerikForm> <br /> <TelerikPdfViewer @ref="@PdfViewerRef" Width="100%" Height="800px" Data="@previewbytedata" /> </main> </div> private async Task OnDocSelectChange(InputFileChangeEventArgs item) { fileloaderrors.Clear(); IBrowserFile file=item.File; //Verify the selected file is a PDF (again this is assuming we only want PDF Templates) string ext=Path.GetExtension(file.Name).ToLower(); if (ext !=".pdf") { string error="Selected file is not valid"; fileloaderrors.Add(error); return; } using Stream st=file.OpenReadStream(); byte[] buffer=new byte[file.Size]; await st.ReadAsync(buffer); previewbytedata=buffer; DocBin docbin=new DocBin(); docbin.DocContent=buffer; docbin.TenantNbr=long.Parse(tenantnbr); previewdoc.DocBin=docbin; } The TelerikPdfViewer is empty when the byte array is used. Hopefully that gives to some info on what I am seeing.

### Response

**Nadezhda Tacheva** commented on 24 Mar 2023

Hi Brian, I see that you are using an InputFile inside the Form. As I understand the desired scenario is to allow the user add a file to the form and then display that file in the PDFViewer. I'd like to mention that the PDFViewer has an integrated FIleSelect that allows one to directly drop the file in the component or open the select files dialog to choose a file. However, if you still want to use a dedicated file input, you may consider the standalone FIleSelect component. You may subscribe to its OnSelect event to get the file and pass it to the PDFViewer. Here is a runnable sample: [https://blazorrepl.telerik.com/cRORmION22DXrgVt31.](https://blazorrepl.telerik.com/cRORmION22DXrgVt31.) Tip: you may need to increase t he SignalR WebSocket message size for the Blazor application. I hope this helps.
