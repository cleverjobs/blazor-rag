# BUnit unit test involving TelerikFileSelect

## Question

**Jer** asked on 29 Nov 2023

Hi, I am trying to setup a unit test around a component that involves a <TelerikFileSelect> <TelerikFileSelect
Id="fileSelect" AllowedExtensions="@AllowedExtensions" MaxFileSize="@MaxFileSize" OnSelect="@ImportHandler" Multiple="false" DropZoneId="dz" OnRemove="@ImportRemove" @ref="FileSelectRef">
<SelectFilesButtonTemplate>
<i class="fas fa-upload"></i>
Upload Excel Spreadsheet
</SelectFilesButtonTemplate>
</TelerikFileSelect> I am not sure how to setup the `FileSelectEventArgs` in order to test our response to the uploaded file var fileSelect=myComponent.FindComponent <TelerikFileSelect> (); await myComponent.InvokeAsync(async ()=> await fileSelect.Instance.OnSelect.InvokeAsync(new FileSelectEventArgs
{
Files=new List <FileSelectFileInfo> (new []{new FileSelectFileInfo
{
Id=null,
Name=null,
Size=0,
Extension=null,
InvalidExtension=false,
InvalidMinFileSize=false,
InvalidMaxFileSize=false,
Stream=null
}
}),
IsCancelled=false
})); It seems like 'Stream' is expecting a 'FileInfoStream' which in turn is expecting a 'FileSelectFileInfo', which is expecting a 'FileInfoStream' and so on How do I properly setup the FileSelectEventArgs to provide my test file? Not sure if it matters but I am using ClosedXML to generate a memory stream that contains the excel file, so just want to pass that to the TelerikFileSelect public MemoryStream MockImportExcelFile_HappyPath () { var workbook=new XLWorkbook(); var ws=workbook.Worksheets.Add( "Sheet 1" );
ws.Cell( "A1" ).Value="Header1";
ws.Cell( "A2" ).Value="asdfasdf"; var stream=new MemoryStream();
workbook.SaveAs(stream);
stream.Seek( 0, SeekOrigin.Begin); return stream;
} Thanks!

## Answer

**Dimo** answered on 04 Dec 2023

Hello Jeremy, Create the FileSelectFileInfo instance with a null Stream first, and then set its Stream property by passing the previously created FileSelectFileInfo object. This is how we do it in our source code: file.Stream=new FileInfoStream(file, this ); // this is the FileSelect component instance On a side note, the discussed test case appears to step outside of the "unit" concept, because it relies on an integration between the FileSelect component and the app's business logic. Instead, why not skip the FileSelect part (and the OnSelect invocation) and test what the app does with the byte array that is already obtained from the FileSelect Stream? Here is also a documentation article about bUnit and Telerik UI for Blazor. Regards, Dimo Progress Telerik

### Response

**Jeremy** commented on 04 Dec 2023

Thanks Dimo, this was helpful I was able to get there with what you posted. Also good note on it being outside the scope of a unit test I have some refactoring to do I think :) Thanks!
