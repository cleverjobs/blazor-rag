# PDF Viewer - Email

## Question

**cma** asked on 08 Mar 2023

Is there a way to enable an email button on the Viewer control? A client of ours was asking. Thank you!

## Answer

**Yanislav** answered on 13 Mar 2023

Hello Chris, If I understand you correctly you need to implement a button that sends emails with the PDF document attached. Is that correct? By design, the PDFViewer is a component whose purpose is to display a PDF document. Sending emails is a completely different functionality and it is up to the developer how to handle such a scenario. What I can recommend is to create a custom command that sends the email. The PdfViewerToolBarCustomTool configuration allows you to define a custom button. You can hook up for the click event of this button and execute a logic that sends the email. Although such implementation would fall beyond the support scope of the Telerik UI products, I've made research about how to implement an email-sender in a Blazor app, please review the following resources: [https://stackoverflow.com/questions/449887/sending-e-mail-using-c-sharp](https://stackoverflow.com/questions/449887/sending-e-mail-using-c-sharp) [https://learn.microsoft.com/en-us/dotnet/api/system.net.mail?view=net-7.0](https://learn.microsoft.com/en-us/dotnet/api/system.net.mail?view=net-7.0) [https://www.c-sharpcorner.com/UploadFile/sourabh_mishra1/sending-an-e-mail-with-attachment-using-Asp-Net/](https://www.c-sharpcorner.com/UploadFile/sourabh_mishra1/sending-an-e-mail-with-attachment-using-Asp-Net/) I hope this information helps. Regards, Yanislav
