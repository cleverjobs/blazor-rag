# Delete method always receives null

## Question

**Dea** asked on 24 Sep 2021

Has anyone else had a problem with removing files using TelerikUpload? Upload works fine, but when attempting to remove it hits the Remove method, but the files parameter is null. I have tried changing the parameter type from string to string[], IFormFile and IEnumerable<IFormFile>. I've tried changing the parameter name (and corresponding RemoveField), and nothing makes any difference. I can add a second, custom parameter, and that works ok. I just can't get a value for files. Selected markup/code: <TelerikUpload SaveUrl="@(AddDocumentApi())" Multiple="true" RemoveUrl="@(RemoveDocumentApi())" OnUpload="OnUploadHandler" OnRemove="OnRemoveHandler" OnSuccess="OnSuccessHandler" WithCredentials="true" AllowedExtensions="@AllowedExtensions" /> public string RemoveDocumentApi()=> $"{AddDocumentApiBase}/deletedocument"; [HttpPost("deletedocument")] public async Task<IActionResult> DeleteDocument(string files) { // Hits a breakpoint here but files is null return new EmptyResult(); }

### Response

**Marin Bratanov** commented on 28 Sep 2021

This sounds like a routing problem. You can use the Network tab of the browser dev tools to see what goes out of the browser, what URL it goes to, what form fields it has, so you can investigate how such a request is handled by the server. You can even replay it with tools like Fiddler so you can easily debug the backend.

### Response

**Dean** commented on 04 Oct 2021

Thanks Martin but I don't think there is a problem with routing, because as I said, it hits a breakpoint in my controller, but the files parameter is null. I can see that the file name is being sent correctly. I've added two further images to clarify.

### Response

**Dean** commented on 04 Oct 2021

In the images I have an additional parameter of folder, but the problem is the same with or without it

### Response

**Dean** commented on 04 Oct 2021

Fixed this - I had to add [FromForm] before the parameter public async Task<IActionResult> DeleteDocument([FromForm] string files)

## Answer

**Dean** answered on 04 Oct 2021

Fixed this - I had to add [FromForm] before the parameter public async Task<IActionResult> DeleteDocument([FromForm] string files)
