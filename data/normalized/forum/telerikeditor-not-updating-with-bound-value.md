# telerikeditor not updating with bound value

## Question

**Law** asked on 09 Mar 2021

Hello-- i'm using the TelerikEditor component and binding it to a string that i fill with a word document that i import and convert to html. The code works and does load the string with the expected value in an async method but as odd as it sounds if i load the first document nothing is displayed but when i load the second document the first document then displays even though the string content is now set to the second document. I understand there could be issues with the async nature of the code but i don't see how that could be happening considering my code. here is my code: string documentContent { get; set; } private async void LoadDocumentFromDisk(InputFileChangeEventArgs e) { if (e.File !=null) { DocxFormatProvider docxProvider=new DocxFormatProvider(); HtmlFormatProvider htmlProvider=new HtmlFormatProvider(); var file=e.File; byte[] theBytes=new byte[file.Size]; var reader=file.OpenReadStream(10000000); var whatever=await reader.ReadAsync(theBytes); RadFlowDocument radFlowDocument=docxProvider.Import(theBytes); documentContent=htmlProvider.Export(radFlowDocument); } } here is the blazor/razor html for the control: <TelerikEditor @bind-Value="@documentContent"></TelerikEditor> Anyone seen anything like this and how to fix the problem? Thanks, LT.

## Answer

**Marin Bratanov** answered on 10 Mar 2021

Hi LT, Could you try changing the signature from private async void LoadDocumentFromDisk(InputFileChangeEventArgs e) to private async Task LoadDocumentFromDisk(InputFileChangeEventArgs e) An async void method won't actually await the execution of async calls and will move on to the next lines of code, so reading the stream async will happen after the documentContent field is set at the end of the method. The next time this is called, you will get the old values because now the method has executed already once, but that's the data from the previous run. Also, depending on how this is called, you may need to add a call to await InvokeAsync(StateHasChanged); at the end of the method - if it isn't called by an EventCallback, the framework might not re-render the components otherwise (EventCallback events call StateHasChanged() automatically). Regards, Marin Bratanov

### Response

**Lawrence** answered on 10 Mar 2021

You sir, are a genius..... that fixed it. Thank you.
