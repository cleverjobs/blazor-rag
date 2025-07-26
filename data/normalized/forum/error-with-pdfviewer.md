# Error with PDFViewer

## Question

**Dou** asked on 16 Sep 2022

After updating to v3.6 I copied your demo code from here and pasted it into my blazor wasm project and I'm getting the error below. What do I need to do to resolve this? Unhandled exception rendering component: Could not find 'TelerikBlazor.initPdfViewer' ('initPdfViewer' was undefined).

## Answer

**Tsvetomir** answered on 21 Sep 2022

Hi, Doug, The initPdfViewer method is actually a JavaScript function that comes with the new 3.6.0 version of the product. I suspect that the NuGet of the project has been updated, but the client assets are pointing to an older version that does not have the function of interest. However, if you use a local copy of the client assets or a CDN, you need to update it. You can find more information in our documentation: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets) Let me know if the issue persists after the update. Regards, Tsvetomir Progress Telerik
