# Is is possible to generate a pdf from wasm?

## Question

**Dav** asked on 09 Jul 2021

I have the following code in a page. When it hits the first line an try's to execute it the app locks right up. I have breakpointed and as soon as you f10 the line it never comes back. protected void ExportList() { RadFixedDocument document=new RadFixedDocument(); RadFixedPage page=document.Pages.AddPage(); FixedContentEditor editor=new FixedContentEditor(page); editor.DrawText("Hello RadPdfProcessing!"); PdfFormatProvider provider=new PdfFormatProvider(); using (Stream output=File.OpenWrite("SPOTDemo.pdf")) { provider.Export(document, output); } }

## Answer

**Martin** answered on 12 Jul 2021

Hello David, I created a sample Blazor WebAssembly app using the provided code snippet in order to test the described behavior and on my side, it works as expected. Please, check the attached project and feel free to modify it in order to help us to reproduce the described behavior. Regards, Martin

### Response

**David** commented on 16 Jul 2021

Could it have anything to do with the pages being marked with the authorized attribute. I am now using your code and service files and it locks up on the first line. Locks out the hole wasm.

### Response

**David** commented on 16 Jul 2021

When I breakpoint and execute this line: RadFixedDocument document=new RadFixedDocument(); it never comes back to run the next line.

### Response

**Kezi** commented on 12 Sep 2022

Hi Martin, I'm trying to get the same demo code to work too, and after copying your sample app, I am getting a Microsoft.JSInterop.JSException: Could not find 'saveAsFile' ('saveAsFile' was undefined) error. Do you know why this would be?

### Response

**Martin** commented on 14 Sep 2022

Hi Kezi, I checked the method name in the provided sample project and it is declared as "saveFile" (not "saveAsFile") which could lead to this exception. You can check in the FileDownloader.cs and fileDownloader.js files. If this is not fixing the described behavior, I would like to ask you to send us a sample project that reproduces the exception in order to deeper investigate the case.

### Response

**David** answered on 15 Jul 2021

So I now have it setup like you injecting the filegenerator and it still locks up on the first line: RadFixedDocument document=new RadFixedDocument(); It just goes away and never comes back.

### Response

**David** answered on 16 Jul 2021

Ok I think this may be something. We r using .net core 5.0 and we are have the telerik.windows.documents.fixed package. The sample you sent me is using telerik.documents.fixed pacakage. Is that it. When I try to install the package your using it will not install.

### Response

**David** commented on 16 Jul 2021

ok we got it by installing the trial of telerik.documents.fixed.trial. Can't install the licensed version as it has a conflict with my licensed telerik.ui.for.blazor and the non-trial version of the docs. Something to to with telerik.zip

### Response

**Martin** answered on 19 Jul 2021

Hello David, In order to use the Telerik Document Processing Libraries in a Blazor environment, you will need to install the Document Processing`s.NET Standard NuGet packages. They don't include ' Windows ' in their names (e.g. Telerik.Documents.Core). For more information check the Cross-Platform Support article. What I could suggest is to remove all the packages installed, clean your project and install the correct one. As a side note, I would like to suggest unticking all the package sources in the NuGet Manager (if any) except the [https://nuget.telerik.com/nuget](https://nuget.telerik.com/nuget) in order to be sure the packages are installed from the right NuGet server: More information can be found in the NuGet Packages help article. Regards, Martin Progress Telerik

### Response

**David** commented on 19 Jul 2021

We have it working now but do not understand that while we own the Telerik Blazor UI license, we could not install the not trial version of Telerik Documents Fixed. I am running version 2.24.0 of the blazor ui package but the non trial version of the documents fixed has a conflict with Telerik Zip. in 2.24.0 and will not install. But the trial version of documents fixed does not. this is the error message we get when trying to install the telerik.documents.fixed non trial version: Severity Code Description Project File Line Suppression State Error NU1107 Version conflict detected for Telerik.Zip. Install/reference Telerik.Zip 2021.2.507 directly to project SpotDemo.Client to resolve this issue. SpotDemo.Client -> Telerik.UI.for.Blazor 2.24.0 -> Telerik.Documents.SpreadsheetStreaming 2021.2.507 -> Telerik.Zip (=2021.2.507) SpotDemo.Client -> Telerik.Documents.Fixed 2020.3.1019 -> Telerik.Zip (=2020.3.1019). SpotDemo.Client C:\Projects\VSWorkspace\SPOT_ES_AGILE_DEVTEAM\SPOTES_ARCHDEMOS\BlazerDemo\Client\SpotDemo.Client.csprojj

### Response

**Martin** answered on 20 Jul 2021

Hi David, From the provided additional information it seems that the version of the Telerik.Zip assembly from the Telerik.UI.for.Blazor package is different than the version of the Telerik.Documents.Fixed assembly, which seems to cause the problem. You will need to use the same version for all the Document Processing Libraries assemblies, so I could suggest installing the Telerik.Documents.Fixed version 2021.2.507 with the Telerik.UI.for.Blazor 2.24.0. Regards, Martin Progress Telerik
