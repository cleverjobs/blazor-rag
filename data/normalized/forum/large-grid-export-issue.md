# Large Grid Export Issue

## Question

**Dea** asked on 27 Feb 2023

Well large for me. :) 360K+ records to excel. Works on the Dev PC but when published to web server it does nothing. No errors either. I tried setting MaximumReceiveMessageSize but that didnt seem to do much. Anyone any ideas on fixing this? Thanks Deasun.

### Response

**Deasun** commented on 27 Feb 2023

Some more info: 1] file size after export , on the dev PC, is 75mb. 2] Code I tried in the program.cs file is: builder.Services.AddServerSideBlazor().AddHubOptions(hub=> hub.MaximumReceiveMessageSize=100 * 1024 * 1024); // 100 MB 3] 100K records seems to work.

### Response

**Deasun** commented on 27 Feb 2023

on the servers it will do 105K records. 23mb file. No bigger it seems.

### Response

**Deasun** commented on 27 Feb 2023

Also tried: builder.Services.AddSignalR(e=> { e.MaximumReceiveMessageSize=100 * 1024 * 1024; }); In the program.cs file. Still wont work.

## Answer

**Svetoslav Dimitrov** answered on 02 Mar 2023

Hello, IIS limits the upload file size by default to 30000000 bytes which are approximately 28.6 MB. This can also be caused by a size restriction by the SMTP server configuration. To resolve: 1. Install Request Filtering role to your Web Server IIS. 2. Open Internet Information Services (IIS) Manager. 3. In the Connections pane click on Default Web Site. 4. In the Home pane, double-click Request Filtering. 5. Click Edit Feature Settings... in the Actions pane. 6. Increase Maximum allowed content length (Bytes) Click Ok. The default value is 30000000 which is approximately 28.6MB. 7. In the Connections pane click on ProcessManager application and verify that the settings are the same as in Default Web Site (steps 5-7). 8. It is recommended to Restart IIS. Regards, Svetoslav Dimitrov Progress Telerik
