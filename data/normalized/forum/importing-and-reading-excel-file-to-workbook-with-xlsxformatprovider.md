# Importing and reading Excel file to Workbook with XlsxFormatProvider

## Question

**Chr** asked on 11 Feb 2025

I'm trying to read from an existing Excel file that the user will upload via FileSelect. When it gets to the last line trying to set the workbook variable: workbook=formatProvider.Import(selectedFile.Stream, TimeSpan.FromSeconds( 30 )); ...I get the error, "'System.NotImplementedException' in Telerik.Zip.dll: 'Synchronous actions on the file stream is not supported by the Blazor framework in Blazor Server-side apps due to the SignalR communication between the client and the host. Use the 'ReadAsync' method instead.'" If I try to copy the stream first like this: await selectedFile.Stream.CopyToAsync(ms); It never gets past that line and there is no error. Here is my stripped code: @page "/uploadtest" @using Microsoft.EntityFrameworkCore
@using IGPOSCore.Models
@using Microsoft.IdentityModel.Tokens
@using Telerik.Blazor.Components
@using Telerik.Blazor.Components.FileSelect
@using System.ComponentModel
@using Telerik.Windows.Documents.Spreadsheet.FormatProviders
@using Telerik.Windows.Documents.Spreadsheet.FormatProviders.OpenXml.Xlsx
@using Telerik.Windows.Documents.Spreadsheet.Model

<TelerikFileSelect @ref="fileSelect" OnSelect="@OnFileSelected" Multiple=false />
<TelerikButton OnClick="@(()=> LoadExcelFile())">
Upload
</TelerikButton>

@code { private TelerikFileSelect? fileSelect { get; set; } private FileSelectFileInfo? selectedFile { get; set; } private Workbook? workbook { get; set; } private async Task OnFileSelected ( FileSelectEventArgs args ) { if (args.Files !=null && args.Files.Any())
{
selectedFile=args.Files.First();
}
} public async Task LoadExcelFile () {
Guid submissionId=Guid.NewGuid(); if (selectedFile !=null )
{
Console.WriteLine( $"Processing file: {selectedFile.Name} - {selectedFile.Size} bytes" );

IWorkbookFormatProvider formatProvider=new XlsxFormatProvider();
@* var ms=new MemoryStream(); await selectedFile.Stream.CopyToAsync(ms);
workbook=formatProvider.Import(ms, TimeSpan.FromSeconds( 30 )); *@workbook=formatProvider.Import(selectedFile.Stream, TimeSpan.FromSeconds( 30 ));

}
}
}

### Response

**Chris** commented on 13 Feb 2025

It works if I use a local file instead of the file selected from the FileSelect component. using (Stream input=new FileStream( "test.xlsx", FileMode.Open))
{
workbook=formatProvider.Import(input, TimeSpan.FromSeconds( 30 ));
} Do I just need to save the selected file locally first instead of trying to use selectedFile.Stream?

## Answer

**Dimo** answered on 14 Feb 2025

Hi Chris, Copying our stream to another one is the way to go. Probably the max SignalR message size is too small for the file size and must be increased. Regards, Dimo Progress Telerik

### Response

**Chris** commented on 14 Feb 2025

Thank you! You're right, it was the max SignalR message size.
