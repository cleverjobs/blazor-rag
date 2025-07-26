# PDFProcessing Example not working

## Question

**Nik** asked on 16 Sep 2021

Anyone that got this example about PDF Processing to work? [https://demos.telerik.com/blazor-ui/pdfprocessing/overview](https://demos.telerik.com/blazor-ui/pdfprocessing/overview) It keeps giving me errors. First error is without Telerik.Documents.Core nuget: Second is with Telerik.Documents.Core nuget: Didn't change any code, just added the following nuget as listed: Telerik.Windows.Documents.Core Telerik.Windows.Documents.Fixed Telerik.Windows.Zip Telerik.Windows.Documents.CMapUtils Thx Best regards, Nikolas

## Answer

**Radko** answered on 20 Sep 2021

Hi Nikolas, The package you need to install to get this running is Telerik.Documents.Fixed, instead of the Telerik.Windows.Documents.Fixed package you currently have (note the lack of the 'Windows' word). The difference between the two packages is that the first one targets .NET Standard while the second one targets .NET Framework. This is covered in the following article - Pdf Processing - Getting Started. I hope you find the above useful. If you run across any other concerns, please let us know, we will be happy to step in and assist. Regards, Radko Stanev
