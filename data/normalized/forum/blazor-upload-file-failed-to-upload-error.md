# Blazor Upload "File failed to upload error"

## Question

**And** asked on 26 Feb 2025

I have a Blazor server solution with separate projects for the UI and API. When the Upload component is configured to use a controller in the API project to handle the save function I get the error seen in the attached file 'Screenshot 2025-02-26 132709' but the file is successfully uploaded. If I copy the same controller to the UI project the error goes away see 'Screenshot 2025-02-26 132538'. to get the save function to work with the API at all I had to add the below HTTP options section to the API program.cs app.Use(async (context, next)=>
{
if (context.Request.Method==HttpMethods.Options)
{
context.Response.Headers.Add("Allow", "GET, POST, PUT, OPTIONS");
context.Response.Headers.Add("Access-Control-Allow-Origin", "[https://localhost:7053");](https://localhost:7053");)
context.Response.StatusCode=(int)HttpStatusCode.OK;
return;
}
await next.Invoke();
}); Upload component: <TelerikUpload SaveUrl="@saveURL" RemoveUrl="[https://localhost:7121/api/DocumentUpload/remove"](https://localhost:7121/api/DocumentUpload/remove") MaxFileSize="@MaxFileSize" /> Controller: using DocumentFormat.OpenXml.Drawing;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace API.Controllers
{
[Route("api/[controller]")]
[ApiController]
public class DocumentUploadController : ControllerBase
{
public IWebHostEnvironment HostingEnvironment { get; set; }

public DocumentUploadController(IWebHostEnvironment hostingEnvironment)
{
HostingEnvironment=hostingEnvironment;
}



[HttpPost("save")]
public async Task <IActionResult> Save(IFormFile files) // "files" matches the Upload SaveField value
{
if (files !=null)
{
try
{
// save to wwwroot - Blazor Server only
//var rootPath=HostingEnvironment.WebRootPath;
// save to Server project root - Blazor Server or WebAssembly
var rootPath=HostingEnvironment.ContentRootPath;
var newFolder=Guid.NewGuid().ToString();
System.IO.Directory.CreateDirectory(rootPath + newFolder);
var saveLocation=System.IO.Path.Combine(rootPath + newFolder, files.FileName);

using (var fileStream=new FileStream(saveLocation, FileMode.Create))
{
await files.CopyToAsync(fileStream);
}
}
catch (Exception ex)
{
Response.StatusCode=500;
await Response.WriteAsync($"Upload failed.");
}
}

return new OkResult();
}

[HttpPost("remove")]
public async Task <IActionResult> Remove([FromForm] string files) // "files" matches the Upload RemoveField value
{
if (files !=null)
{
try
{
// delete from wwwroot - Blazor Server only
var rootPath=HostingEnvironment.WebRootPath;
// delete from Server project root - Blazor Server or WebAssembly
//var rootPath=HostingEnvironment.ContentRootPath;
var fileLocation=System.IO.Path.Combine(rootPath, files);

if (System.IO.File.Exists(fileLocation))
{
System.IO.File.Delete(fileLocation);
}
}
catch (Exception ex)
{
Response.StatusCode=500;
await Response.WriteAsync($"Delete failed.");
}
}

return new EmptyResult();
}
}
} Any ideas? Have I missed something I need to setup in the API program.cs?

## Answer

**Nadezhda Tacheva** answered on 28 Feb 2025

Hi Andrew, By design of the Upload, the error message is rendered if the status that the component receives from the controller when uploading the file is "Failed". You may track this status by handling the Upload events. I can suggest the following two options to try: Check the browser's network tab for the HTTP status code from the controller and any error messages. Use WithCredentials due to the CORS scenario. I hope these steps will help you resolve the issue on your end. Regards, Nadezhda Tacheva

### Response

**Andrew** commented on 28 Feb 2025

if I add with Credentials=true then the file fails to get uploaded. The HTTP repones from the API controller is 201 but there is response body so that could be the problem? Is there anyway to override the error message or hide it? <TelerikUpload SaveUrl="@saveURL" RemoveUrl="@removeURL" MaxFileSize="@MaxFileSize" OnUpload="OnUploadHandler" OnRemove="OnUploadRemoveHandler" WithCredentials=true Files="@InitialFiles" />

### Response

**Tsvetomir** commented on 03 Mar 2025

Hello Andrew, I'm joining the conversation, because Nadezhda currently is out of the office. After reviewing the discussion, I assume the following points are relevant to the issue: Upload Security - make sure to check this section in our documentation. To troubleshoot further the issue, track the status of the upload file with the Upload component events like - OnError, OnSuccess, OnSelect, OnUpload. Observing these events in more detail will give you the information where the request fail, or is there at all a request to the external API controller. If the status code of your request is 201 means that it is successful, so the OnSuccess method should be triggered. Another possible reason is wrong setup in the Program.cs file. Based on the information in your initial reply it seems the UI project might be missing the preconfigured HttpClient registered in the Program.cs file and declared service. To ensure everything is setup correctly refer to the Microsoft documentation on how to call a web API from ASP.NET Core Blazor and follow the steps. I hope the provided information helps you resolve the matter. Regards, Tsvetomir Hristov
