# TelerikUpload Files parameter inaccessible due to its protection level (Blazor server-side)

## Question

**Bil** asked on 14 Aug 2023

Hello, I'm using the (excellent) TelerikUpload component in our Blazor app and I'm trying to set the initial files list for previously-uploaded files as specified here: [https://docs.telerik.com/blazor-ui/components/upload/initial-files.](https://docs.telerik.com/blazor-ui/components/upload/initial-files.) When I try to do something like Uploader.Files=new List<UploadFileInfo>(); I get the error that 'TelerikUploadBase<UploadFileInfo>.Files' is inaccessible due to its protection level. If I try to set it as a parameter on the component declaration on my page, I get the error that Files isn't set a a ParameterAttribute or CascadingParameter. Am I missing something?

## Answer

**Dimo** answered on 15 Aug 2023

Hello Bill, Please upgrade to version 4.4.0, which introduced the Files parameter: Initial Files feature request Release Notes for 4.4.0 Direct parameter mutation (Uploader.Files=...) should not be used in Blazor. Regards, Dimo Progress Telerik

### Response

**Bill** commented on 15 Aug 2023

Ah, I see- thanks!
