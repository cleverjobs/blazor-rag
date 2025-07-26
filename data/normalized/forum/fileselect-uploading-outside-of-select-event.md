# FileSelect uploading outside of select event

## Question

**Bil** asked on 15 Aug 2023

Hello, I'm trying to use the FileSelect control in my Blazor server-side app to allow users to upload one or more files to an S3 bucket. I don't want to upload them individually upon select, the requirement is they can select multiple files several times. As such I have a separate "Upload" button that calls an event which will kick off the upload. My goal is to send the file streams to a javascript function so that I can upload them through the user's browser to S3 (using generated pre-signed URLs that DO get created on select). The problem I'm running into is that the Streams are already disposed of after the Select event is done. I was originally trying to do this with the TelerikUpload control, but that seems geared to sending to an API, and I'm trying to avoid proxying the files internally so I don't have to have the user send files to an internal API and then the API sending them on to S3. Are there any examples of what I'm trying to accomplish? Does it even seem possible? Thanks! Bill

## Answer

**Dimo** answered on 18 Aug 2023

Hi Bill, In Blazor Server apps, the FileSelect sends immediately each selected file to the server's .NET runtime via SignalR. To upload all files at the same time with JavaScript, you need to obtain the file content in OnSelect and then send this content back to the browser via JSInterop, which will create a full loop of client-server-client file transmission. That's why I believe the following suggestions are more optimal: Use the Upload with AutoUpload="false" and proxy the upload process with your own endpoint. In the future, we will probably support uploading multiple files with the same request. OR Use the FileSelect, but give up the JavaScript upload mechanism. Instead, store the content of all selected files in the Razor component that holds the FileSelect. Then, when the user is ready, upload the files to S3 from the .NET runtime. The first option relies on HTTP uploading to your app server, which is better and faster, compared to SignalR transfer, but you will need to save the files temporarily. The second option doesn't require temporary file saving. Regards, Dimo Progress Telerik
