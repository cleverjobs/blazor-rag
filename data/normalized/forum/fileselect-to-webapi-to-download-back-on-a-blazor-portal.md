# FileSelect to WebApi to download back on a blazor portal

## Question

**Doo** asked on 21 May 2021

With my original queston, I got to know about FileSelect here. I'm now able to send files to my internal unexposed Api. How do I download these files? I want to have an Api that sends file back to Blazor Portal. My files are saved as byte[] in a SQL table. I'm also triyng to figure out a way to show preview of common files on the portal as well. Any helpers?

## Answer

**Marin Bratanov** answered on 21 May 2021

Hello Hassan, There are three ways to download a file: navigate the user agent (browser) to an URL that will download the file. You'd either need JS, or perhaps the NavigationManager.NavigateTo() with a forced reload and a full URL might work (I have not tested whether it can do this). It is important that this endpoint must be secured accordingly and send the file correctly (e.g., with the desired content-disposition header). make an XHR request from the browser to such an endpoint You can do this with JS and you can even attach bearer tokens and other auth info. The content-disposition header value is also important - if it is an attachment the browser is more likely to open the Save dialog, but an inline file is likely to replace the current page. generate a download link with a blob made of the byte[] you have. You can find one example of such an approach in our demos (you can find the solution in the "demos" folder of your local installation), see the DemoFileExporter.cs file to see how to call the JS interop in the download-upload-files.js file. Regards, Marin Bratanov
