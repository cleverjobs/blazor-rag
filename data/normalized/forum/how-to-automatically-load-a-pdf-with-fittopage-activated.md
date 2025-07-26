# How to automatically load a PDF with 'fitToPage' activated

## Question

**Mar** asked on 14 Aug 2023

The subject says it... <TelerikPdfViewer @ref="@PdfViewerRef" Width="100%" Height="100%" OnDownload="@OnPdfDownload" OnError="@OnPdfError" OnOpen="@OnPdfOpen" Zoom="@PdfZoom" ZoomChanged="@OnPdfZoomChanged" EnableLoaderContainer="true" Data="@PdfData"> <PdfViewerToolBar> <PdfViewerToolBarCustomTool> <TelerikButton OnClick="@PreviousPage"> Vorige pagina </TelerikButton> <TelerikButton OnClick="@NextPage"> Volgende pagina </TelerikButton> </PdfViewerToolBarCustomTool> <PdfViewerToolBarZoomTool /> <PdfViewerToolBarSelectionTool /> <PdfViewerToolBarSearchTool /> </PdfViewerToolBar> </TelerikPdfViewer>

## Answer

**Dimo** answered on 15 Aug 2023

Hi Marc, This will be possible when we implement this feature request - Change the default zoom level of PDF Viewer. I voted on your behalf and I encourage you to follow the item to receive status updates. Regards, Dimo Progress Telerik

### Response

**Marc** answered on 23 Nov 2023

A workaround for 'Fit to Width' can be accomplished by adding this JavaScript, but a regular setting would be better... As well as fixing the other major issue with the Blazor PDF Viewer regarding PDF degradation and it's inferior PDF quality in regard to the Kendo PDF Viewer.. But then, the Kendo UI for jQuery PDF Viewer has major zoom / scale issues... function setZoomOption(zoomOption) { var combo=$(".k-combobox-clearable").find("input").last().getKendoComboBox(); if (combo) { console.log("SetZoomOption: Zoomcombo found"); combo.select(zoomOption); combo.trigger("change"); } else { console.log("SetZoomOption: Zoomcombo not found"); } } And call it from HTML: <input type="button" value="Set ZoomOption" onclick="setZoomOption(2)" /> Or from Blazor: private async Task SetZoomFullWidth() { // Set scale does not work, we gonna push the button instead // await JsRuntime!.InvokeVoidAsync("setScale",PdfZoom); await JsRuntime!.InvokeVoidAsync("setZoomOption", 2); }

### Response

**Dimo** commented on 23 Nov 2023

Hi Marc, I agree with you that an initial "fit to page" will be quite useful. In the meantime, the JavaScript approach, which simulates user behavior is a possible workaround. The demonstrated code is for Kendo UI jQuery and here is an example for the pure Blazor PdfViewer.

### Response

**Marc** commented on 23 Nov 2023

Thanx, unfortunately the Blazor PDF viewer has a major problem since it significantly downgrades the PDF quality. Therefore the Blazor PDF Viewer is useless for us... See: [https://feedback.telerik.com/blazor/1611568?_ga=2.83551263.884795109.1700660517-738843539.1699372807&_gl=1*4kmd4a*_gcl_au*MTE1MjQyMDk4OC4xNjk5MzcyODA3*_ga*NzM4ODQzNTM5LjE2OTkzNzI4MDc.*_ga_9JSNBCSF54*MTcwMDc0NzAwMi40LjEuMTcwMDc0NzIzMy40MC4wLjA.](https://feedback.telerik.com/blazor/1611568?_ga=2.83551263.884795109.1700660517-738843539.1699372807&_gl=1*4kmd4a*_gcl_au*MTE1MjQyMDk4OC4xNjk5MzcyODA3*_ga*NzM4ODQzNTM5LjE2OTkzNzI4MDc.*_ga_9JSNBCSF54*MTcwMDc0NzAwMi40LjEuMTcwMDc0NzIzMy40MC4wLjA.) We had to switch to the Kendo UI for jQuery PDF Viewer... Which gave us other issues... We are still struggling to get the right PDF experience for our customers...

### Response

**David** commented on 07 Mar 2024

Here's a version using reflection: [https://blazorrepl.telerik.com/GoadYrPH17POYUdD18](https://blazorrepl.telerik.com/GoadYrPH17POYUdD18)
