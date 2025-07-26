# Upload large files

## Question

**JayJay** asked on 02 Sep 2020

Do you have any plans on modifying the component to upload large video files over 1GB in size? From your documentation it looks like the upload component will only handle the max request size of IIS.

## Answer

**Marin Bratanov** answered on 02 Sep 2020

Hi Jay, I made this page on your behalf where you can Follow the chunk upload implementation: [https://feedback.telerik.com/blazor/1483101-upload-file-in-chunks-large-file-upload.](https://feedback.telerik.com/blazor/1483101-upload-file-in-chunks-large-file-upload.) Regards, Marin Bratanov

### Response

**Renier Pretorius** commented on 17 Nov 2023

@Marin, Is there a working example of a large file upload implementation for Balzor WebAssembly hosted with ASP.NET Core? As soon as I try and upload too large a file, the IFormFile attribute hitting the controller method is null. I have added the following to my server program.cs builder.Services.Configure<FormOptions>(options=>
{
options.MultipartBodyLengthLimit=128 * 1024 * 1024; // 128MB });

builder.Services.Configure<IISServerOptions>(options=>
{
options.MaxRequestBodySize=128 * 1024 * 1024; // 128MB }); but still get null

### Response

**Renier Pretorius** answered on 17 Nov 2023

For anyone still struggling with this, the solution turned out to be exceedingly simple. I decorated my UploadController with [ApiController] attribute and the specific upload method with [DisableRequestSizeLimit] attribute.
