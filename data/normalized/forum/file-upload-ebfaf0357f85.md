# File upload

## Question

**Ric** asked on 25 Sep 2019

Do you have a time table on a file upload component? I put together a working file uploader with a file type input and Blazor.FileReader but a built in component would be nice. Also a request from one of our staff here, they would prefer if the file upload was a drag and drop. A file upload that supports file browser and drag and drop would be nice.

## Answer

**Marin Bratanov** answered on 26 Sep 2019

Hello Rick, You can Follow this page for updates on it (I have added your Vote for your): [https://feedback.telerik.com/blazor/1397642-upload-async.](https://feedback.telerik.com/blazor/1397642-upload-async.) There are issues with handling files in Blazor yet, and we need to wait for a built-in solution to arrive, so we can step on it and enhance the UI and UX. The following blog explains those problems quite well, and offers a solution that can be used for the time being: [https://blog.stevensanderson.com/2019/09/13/blazor-inputfile/.](https://blog.stevensanderson.com/2019/09/13/blazor-inputfile/.) Regards, Marin Bratanov

### Response

**Ryan** answered on 18 Mar 2020

Any updates on the File Upload?

### Response

**Svetoslav Dimitrov** answered on 18 Mar 2020

Hello Ryan, The Upload component is live! You can check the demos here: [https://demos.telerik.com/blazor-ui/upload/overview](https://demos.telerik.com/blazor-ui/upload/overview) and the corresponding documentation here: [https://docs.telerik.com/blazor-ui/components/upload/overview.](https://docs.telerik.com/blazor-ui/components/upload/overview.) Regards, Svetoslav Dimitrov

### Response

**Ryan** answered on 18 Mar 2020

Thank you very much!

### Response

**Svetoslav Dimitrov** answered on 19 Mar 2020

Hello Ryan, I hope you had the chance to explore the feature of the new Upload component and you had great experience while using it! Regards, Svetoslav Dimitrov

### Response

**Gary** answered on 01 Apr 2020

Svetoslav, Is that your first name? I would not want to insult you. :-) I need to upload small text files into memory on my front end Blazor app, and pass the text to an API where I will drop it into Azure Keyvault. Is this the right tool to use?

### Response

**Marin Bratanov** answered on 01 Apr 2020

Hello Gary, Yes, that's his first name, but I'm jumping back on this thread as he is working on another task at the moment. The TelerikUpload component does something slightly different - it sends the files to an endpoint on a server (might not even be the same server that hosts the blazor app, might not even be your server at all). It does not give you the file stream in the Blazor app. We decided to do that async upload to an endpoint for two reasons: 1) it was what was requested more often and 2) it's the one that's harder to do (requires quite a bit more JS Interop). So, if this will serve you (e.g., you can add a controller in your app to handle the upload from client to server, and then save it to the vault), it can be the right tool for the job. To get the memory stream (or any stream, or a byte[]) into your Blazor app code, you need a FileSelect type of component which typically does not upload the file but just gives you an event with the stream/array. We don't have one as part of our component suite (you can post a feature request on our portal if you want to see one implemented), but you can find an example of making it in our demos - we use it on our Document Processing demos - at the moment it is ~/Shared/FileUpload.razor (it also has some JS Interop, so take a peek at the _Hosts.cshtml) and with our next release it will be called DemoFileSelector.razor to avoid confusion with a built-in component in the suite, but the code will be the same. Regards, Marin Bratanov

### Response

**Ryan** answered on 07 Apr 2020

Is there anyway to read a filestream instead of having to save the file to the server using the TelerikUpload component?

### Response

**Marin Bratanov** answered on 07 Apr 2020

Hello Ryan, You can Follow the implementation of such a component in this page: [https://feedback.telerik.com/blazor/1460649-fileselect-component.](https://feedback.telerik.com/blazor/1460649-fileselect-component.) It also offers a way to get it right now with a little bit of code based on our demos. Regards, Marin Bratanov
