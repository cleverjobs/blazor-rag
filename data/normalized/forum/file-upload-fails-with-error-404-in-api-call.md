# File Upload fails with error 404 in API call

## Question

**Luy** asked on 25 Oct 2020

I have 2 projects inside the same solution. My first project is a client-side project that has the Upload .razor file. And my second project is a server-side project that has the API Controller. So when I want to upload a file, the file doesn't finish successfully cause the API Call fails with error 404. I would like to share both codes 1- .razor File: @page "/" @inject NavigationManager NavigationManager <TelerikUpload SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" SaveField="file" AllowedExtensions="@( new List<string>() { ".jpg", ".png", ".jpeg" } )" MaxFileSize="2048000" MinFileSize="1024" Multiple="false" /> @code { public string SaveUrl=> ToAbsoluteUrl("api/upload/save"); public string RemoveUrl=> ToAbsoluteUrl("api/upload/remove"); public string ToAbsoluteUrl(string url) { return $"{NavigationManager.BaseUri}{url}"; } } 2- APIController using System; using System.Collections.Generic; using System.IO; using System.Linq; using System.Net.Http.Headers; using System.Threading.Tasks; using Microsoft.AspNetCore.Hosting; using Microsoft.AspNetCore.Http; using Microsoft.AspNetCore.Mvc; namespace TelerikBlazorApp2.Server.Controllers { [Route("api/[controller]/[action]")] [ApiController] public class UploadController : Controller { public IWebHostEnvironment HostingEnvironment { get; set; } public UploadController(IWebHostEnvironment hostingEnvironment) { HostingEnvironment=hostingEnvironment; } [HttpPost] public async Task<IActionResult> Save(IFormFile file) // the form field name. See SaveField { if (file !=null) { try { //foreach (var file in files) //{ var fileContent=ContentDispositionHeaderValue.Parse(file.ContentDisposition); // Some browsers send file names with full path. // We are only interested in the file name. var fileName=Path.GetFileName(fileContent.FileName.ToString().Trim('"')); var physicalPath=Path.Combine(HostingEnvironment.ContentRootPath, fileName); // Implement security mechanisms here - prevent path traversals, // check for allowed extensions, types, size, content, viruses, etc. // this sample always saves the file to the root and is not sufficient for a real application using (var fileStream=new FileStream(physicalPath, FileMode.Create)) { await file.CopyToAsync(fileStream); } // } } catch (Exception ex) { // implement error handling here, this merely indicates a failure to the upload Response.StatusCode=500; await Response.WriteAsync("some error message"); // custom error message } } // Return an empty string message in this case return new EmptyResult(); } [HttpPost] public ActionResult Remove(string[] files) // the default field name. See RemoveField { if (files !=null) { try { foreach (var fullName in files) { var fileName=Path.GetFileName(fullName); var physicalPath=Path.Combine(HostingEnvironment.WebRootPath, fileName); if (System.IO.File.Exists(physicalPath)) { // Implement security mechanisms here - prevent path traversals, // check for allowed extensions, types, permissions, etc. // this sample always deletes the file from the root and is not sufficient for a real application System.IO.File.Delete(physicalPath); } } } catch { // implement error handling here, this merely indicates a failure to the upload Response.StatusCode=500; Response.WriteAsync("some error message"); // custom error message } } // Return an empty string message in this case return new EmptyResult(); } } }

## Answer

**Luyeye** answered on 25 Oct 2020

Adicional Note: Telerik version 2.15.0

### Response

**Marin Bratanov** answered on 26 Oct 2020

Hello Luyeye, The most likely reason for the problem is that the routing is wrong for this scenario. For example, the port is different on the WebAPI project, so the SaveUrl that the Upload component gets is 404. Regards, Marin Bratanov

### Response

**Luyeye** answered on 28 Oct 2020

Could you give an example of how to do this? please

### Response

**Marin Bratanov** answered on 28 Oct 2020

Hi Luyeye, I am not sure what example you need since my previous post did not offer steps for particular tasks. Nevertheless, I can suggest you use tools like FIddler to capture the network request for the file upload so you can modify and replay it to test your WebAPI back end. Regards, Marin Bratanov
