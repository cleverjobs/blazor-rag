# Upload component reports 'File failed to upload'

## Question

**Jes** asked on 11 Oct 2020

Hi I am the Upload Blazor component (2.17) in my web application. I am using it in a cross-domain scenario. I have setup the headers to allow and respond as they should (I think :-) ). However, I am experience some problems. I have read what has been written about CORS on the Upload component page and added code accordingly. My site and API runs in Azure, so I have adjusted the controller code listen on the page of the component, to work in Azure. The issues I am facing are: 1. In the controller, I have added code to respond to the OPTIONS http verb. When I select a file to be uploaded, the OPTIONS method is called, the upload component states 'File failed to upload'. The http response from the API is 204 (NoContentResult). If I click on the retry icon, the upload component calls the actual upload method (post verb). 2. When the API receives the POST verb, the file is stored, and the API returns OkResult() (also tried with EmptyResult as some of your listings use that). However, the upload component write the error message 'File failed to upload' next to the file. In both cases, the parm in the 'OnError' event handler, shows that http status is '0'. Telerik Fiddler shows that the API server has returned http status 204 and 200. Do you have some idea why the component displayes 'File failed to upload' and how can I see what is wrong?

## Answer

**Marin Bratanov** answered on 12 Oct 2020

Hi Jesper, There should be no need to handle an OPTIONS verb explicitly for the upload itself - we don't use it to upload files, that might be something for the browser which fires prior to the POST itself, but it should not need to be handled explicitly as a file upload, and if it is handled - it should contain appropriate information for such a request, not just a blank a 204 status - the POST request must be indicated as allowed with the appropriate CORS headers (see here and the last paragraph here ). Ultimately, the Telerik Upload component only does an AJAX POST request to the designated endpoint and it is up to the networking and setup of that endpoint to handle that request successfully. If those articles don't help you get things running, I can suggest you try the following: Set up the upload to work with a local endpoint, for example like one from the docs ( link ). Ensure that this works first. Start moving that logic to a separate project to see where the failures start cropping up so you can fix them. For example, in Azure there might be some firewall rules or access rights, credentials or other similar logic/restrictions that are causing issues or truncating the requests. You can also try saving the POST request with a tool like Fiddler and replaying it against the endpoint until you can see it work. Regards, Marin Bratanov

### Response

**Jesper** answered on 12 Oct 2020

Hi Marin Thank you for your reply :-) And thanks for the links. I managed to find the solution to my problem :-) You write that the component does not issue a OPTIONS request explicit, however, it appears to do so implicitly. According to this article and this article browsers will issue a 'preflight' request (the http OPTIONS verb) when the conditions listed are not meet when doing cross domain calls. My guess is (please correct me if I am wrong) that the Upload component does insert a callback (see the second article) to provide the upload progress percentage shown on the component and therefore it triggers the browser to do the OPTIONS request. If someone else should end here with the same issue, below find the basic solution that made it work for me :-) My solution is to be run as a Azure Web application and as Azure Functions. In the Web Application I configured the Upload component as described in the documentation. The SAVEURL is set and is a cross domain url (e.g. 'MyUploadServer.dk/api/file'). No special code was applied to the Upload component. I wrote two Azure functions to handle the files to be uploaded. First, I wrote this function to handle the OPTIONS request: [FunctionName( "FileOptions" )] public static IActionResult FileOptions( [HttpTrigger(AuthorizationLevel.Anonymous, "options", Route="file" )] HttpRequest req, ILogger log) { string originSite=req.Headers[ "Origin" ]; req.HttpContext.Response.Headers.Add( "Access-Control-Allow-Origin", originSite); req.HttpContext.Response.Headers.Add( "Access-Control-Allow-Methods", "POST, GET, OPTIONS" ); req.HttpContext.Response.Headers.Add( "Access-Control-Allow-Credentials", "true" ); req.HttpContext.Response.Headers.Add( "Access-Control-Allow-Headers", "X-PINGOTHER, Content-Type" ); return new NoContentResult(); } Then, I modified the upload handler from the Upload component documentation: [FunctionName( "FileUpload" )] public static async Task<IActionResult> FileUpload( [HttpTrigger(AuthorizationLevel.System, "post", Route="file" )] HttpRequest req, ILogger log) { string originSite=req.Headers[ "Origin" ]; req.HttpContext.Response.Headers.Add( "Access-Control-Allow-Origin", originSite); if (req.Form.Files !=null ) { try { foreach (var file in req.Form.Files) { var fileContent=ContentDispositionHeaderValue.Parse(file.ContentDisposition); // Some browsers send file names with full path. // We are only interested in the file name. var fileName=Path.GetFileName(fileContent.FileName.ToString().Trim( '"' )); var physicalPath=Path.Combine(@"C:\Temp\UploadDir", fileName); // Implement security mechanisms here - prevent path traversals, // check for allowed extensions, types, size, content, viruses, etc. // this sample always saves the file to the root and is not sufficient for a real application using (var fileStream=new FileStream(physicalPath, FileMode.Create)) { await file.CopyToAsync(fileStream); } } } catch { // implement error handling here, this merely indicates a failure to the upload return new BadRequestResult(); } } // Return an empty string message in this case return new OkResult(); } And Voilá, it works :-) Best regards

### Response

**Marin Bratanov** answered on 12 Oct 2020

That's great news, Jesper, and thank you for sharing this with the community. I've actually linked your explanations from the docs, other people might benefit from them ( commit link ) and I marked your post as the answer to the thread. The preflight (OPTIONS) request is, indeed, something the browser does for a CORS request and, indeed, the expected result is the necessary headers that allow the access. Regards, Marin Bratanov

### Response

**Luca** answered on 26 Mar 2021

Hi Jesper Could you please give me a hint where and how you call/use your functions. Thanks Thomas

### Response

**Jesper** answered on 30 Mar 2021

Hi Thomas In order for the Telerik Upload component to work, the backend must have a web API that the upload component can call when one or more files are to be stored. Depending on the setup of the web application and the web API, it might result in a cross domain call. If this is the case, the web API must respond to the http verb 'OPTIONS'. When the browser discovers that the call to be made, is cross domain, a 'preflight' request is send. That 'preflight' request is a http request having the verb 'options'. The web API must respond to that verb with a reply that tells the browser from which domain the API will accept uploads. That is what I wrote the first method (with "options" parameter) to do. Do note, that this implementation is very simple and servers as a demo only. In a real-world application, you must return the correct site in the parameter 'Access-Control-Allow-Origin'. For further information, search the net. The method that receives the file(s), is the Telefik demo example with a slight adjustment. It is needed to add the setting of the response header with the originSite. This too, must return the real site in a real-world application. I hope this helps you.

### Response

**Luca** answered on 30 Mar 2021

Hi Jesper Thanks a lot for your answer. Meanwhile I use "FileInput" which transfers the files' content via SignalR to the server. Kind regards Thomas
