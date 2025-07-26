# PDF Viewer - Print format

## Question

**Dav** asked on 29 May 2024

Hello, We are using the PDF viewer to display a report that we made with Telerik Reporting. When we display it on the screen, everything work great, the format is correct (landscape) and the margin are correct (custom margin) When we click on the print button (made with <PdfViewerToolBarPrintTool />), the preview window show our report in "portrait" and with "default margin". Because of that, our report take 5 pages instead of 2. If we manually change the settings to "landscape" and "no margin" in the print preview, the print is correct. Is there a way to change that ? Change the default page orientation and the default margin so that our client doesn't have to do it themselve? We tried using the new release from may 2024 (blazor 6.0), the quality of the print went up, but I dont see any option which would let me do that. Thank you David

## Answer

**Svetoslav Dimitrov** answered on 03 Jun 2024

Hello David, I have consulted with our dev team and would like to ask for the specific PDF file you tested with so we can investigate the root cause. I am asking for this because it is not a known issue and we are unsure how to analyze it properly. If the report has sensitive information, you can open a private ticket where your information will never be publicly available. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**David** commented on 03 Jun 2024

I've joined some screenshots which show our settings (in telerik reporting), how it is display in TelerikPdfViewer, and how wrongly it will be print I know that I can manualy change the paper format, but I wished that the viewer would choose it correctly. How can I send you the PDF? Its not sensitive information, its some dummy data, but I cant add it to attachment (invalid format file) I've joined a dropbox link if that work [https://www.dropbox.com/scl/fi/61c9b1g0k72tbsmjzifis/Report.pdf?rlkey=5jzcsoptf2fuigopcppo00br1&st=ole5zccd&dl=0](https://www.dropbox.com/scl/fi/61c9b1g0k72tbsmjzifis/Report.pdf?rlkey=5jzcsoptf2fuigopcppo00br1&st=ole5zccd&dl=0)

### Response

**Svetoslav Dimitrov** commented on 06 Jun 2024

Hello David, Thank you for the screenshots and the PDF file. I successfully reproduced the behavior in the built-in browser print dialog. I am sorry to report that we cannot replace the browser's default print dialog with a custom one. The print dialog is a browser-controlled interface, and web applications cannot override it or create a custom print dialog that would replace the default one.

### Response

**David** commented on 06 Jun 2024

Alright, that what I thought, just wanted to be sure.
