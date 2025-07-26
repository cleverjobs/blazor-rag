# How to clear the list of files from FileSelector after they've been uploaded?

## Question

**Ale** asked on 23 Feb 2022

I have a handler for OnSelect, where I take the files and store them on the server. However, after this is done, the FileSelector still shows the files to the user, for no reason. I couldn't find anyway in the code to clear the list of files or to indicate to the FileSelector that the uploading was done. It doesn't look right when I tell the user "Upload Done!", yet the files selected by the user are still listed visible in the FileSelector.

## Answer

Hi Alex, I agree that clearing the file list can be helpful. There is a feature request to add a Clear method for the FileSelect. In the meantime, you can use a workaround with JavaScript. You can call this function through JS Interop after the upload is complete: @inject IJSRuntime js <div style="width:300px"> <TelerikFileSelect Class="custom-class" Multiple="true"> </TelerikFileSelect> </div> <TelerikButton OnClick="@clearList"> Clear Files </TelerikButton> <script suppress-error="BL9992"> function clearFileSelect ( ) { document.querySelector( ".custom-class .k-upload-files" ).innerHTML="";
} </script> @code { void clearList ( ) {
js.InvokeVoidAsync( "clearFileSelect" );
} } (Remove suppress-error="BL9992" after you move the <script> to a proper place in the app.) The above JavaScript function will remove all previously selected files. Note that I set a custom CSS Class for the FileSelect to avoid conflicts if you have multiple FileSelect or Upload components on the page. Regards, Apostolos
