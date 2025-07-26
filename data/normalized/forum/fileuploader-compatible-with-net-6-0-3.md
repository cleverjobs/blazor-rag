# Fileuploader compatible with .net 6.0.3

## Question

**Hol** asked on 24 Mar 2022

Hi, I had to update to .net 6.0.3. The Fileuploader don't work anymore. I can choose a file from the OS-Select Popup, but then nothing happens. The popup closes, no preview (the row with icon, filename, progress) and no error-message and no upload. The same in Firefox and Edge.

### Response

**Hristian Stefanov** commented on 28 Mar 2022

Hi Holger, I'm ready to help out here. We have two components that are working with files - FileSelect and Upload. I wasn't completely sure which one you are using in this scenario. That being said, I tried to reproduce the described issue with both on my machine. As a result, it seems the components are working as expected on my side. There can be different reasons for the reported problem. Could you please share if the problem is on WebAssembly or Server Blazor project? Also, are there any errors in the Visual Studio console, not in the browser? Is the debugging working while running the app? This additional information will help us investigate further and suggest next steps. Thank you. I look forward to your reply.

### Response

**Holger** commented on 29 Mar 2022

Hi, It is the TelerikUpload component. It is in a WebAssembly project. There are no errors in the browser and in the VS console. Is not working with debugging or without debugging. Thanks.

### Response

**Hristian Stefanov** commented on 31 Mar 2022

Hi Holger, Thank you for providing additional information. Most likely, there is something wrongly cached in the browser, so I can suggest you clean the project - delete the obj and bin folders or hard reload the browser page. I'm attaching a project created on .NET 6.0.3 with an Upload working as expected. Please run and test it to see if the result you get is the same. I would be happy to keep me updated on the situation.

### Response

**Holger** commented on 04 Apr 2022

So, I stripped down the Uploader to: <TelerikUpload
SaveUrl="@SaveUrl" AutoUpload="false">
</TelerikUpload> And it worked (the row with the icon, Filename, Filesize and Remove-Handle will be generated). If I added: OnSelect="@OnSelect" My OnSelect-Handler will be fired: public async Task OnSelect ( UploadSelectEventArgs args ) {
Console.WriteLine( "OnSelect" );
Console.WriteLine(JsonConvert.SerializeObject(args, Formatting.Indented));
} and I get the args in the browser-console: Onselect
{ "IsCancelled": false, "Files": [
{ "Progress": 0, "Status": 0, "Id": "db10e0ac-ace0-4162-befb-1d1d5153dcb5", "Name": "skype.png", "Size": 2865, "Extension": ".png", "InvalidExtension": false, "InvalidMinFileSize": false, "InvalidMaxFileSize": false }
]
} But the row with icon, Filename, filesize and remove-Handler will NOT be generated (anymore). I don't know if .net6.0.3 is the cause for that behaviour, but before 6.0.3 it works... I need the working OnSelect-Handler for custom validations and calculation of image width and height (via javascript) and generating an custom preview image.

### Response

**Hristian Stefanov** commented on 07 Apr 2022

Hi Holger, Thank you for keeping me updated on the situation. I modified the previously attached sample project and added the OnSelect event. Still, it seems to work as expected on my side. There might be needed some additional code from the actual project to reproduce the problem. That being said, could I kindly ask you to modify the attached project to show the issue? This will help us investigate further and suggest next steps. In the meantime, to not miss our latest features/fixes, make sure to upgrade to our latest 3.1.0 version. I look forward to your reply.
