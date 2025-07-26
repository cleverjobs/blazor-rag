# Get stream from UploadFileInfo

## Question

**Joe** asked on 23 May 2025

I can now list my files in the upload control. Now, how do I get the stream from the collection of files? I need to have the stream in order to upload to Azure. foreach (UploadFileInfo file in args.Files)
{
var fileName=Path.GetFileName(file.Name);

//await using (var fileStream=new FileStream(fileName, FileMode.Create))

### Response

**Joel** commented on 23 May 2025

Your demo is very confusing and needs more explanation: [https://demos.telerik.com/blazor-ui/upload/chunk-upload](https://demos.telerik.com/blazor-ui/upload/chunk-upload) [https://www.telerik.com/blazor-ui/documentation/components/upload/overview](https://www.telerik.com/blazor-ui/documentation/components/upload/overview) This is using asp.net core methods from a controller with blazor... which I've never seen before. Where does the 2nd example tie the controller into the Blazor code? What am I missing?

### Response

**Yanislav** commented on 28 May 2025

Hi Joel, As we discussed, the Upload component sends the files via HTTP requests. If you need access to the file stream, the FileSelect component might be more suitable. To keep the communication organized, let's continue in the private ticket so we can provide more focused support.

## Answer

**Joel** answered on 23 May 2025

AI gave method solution... but, it doesn't work because there is no filestream. T foreach (UploadFileInfo file in args.Files)
{
using var content=new MultipartFormDataContent();
// file.Stream is the file content, file.Name is the file name
content.Add(new StreamC ontent(file.FileStream), "file", file.Name);

// Adjust the URL to match your UploadController route
var response=await HttpClient.PostAsync("/api/upload/save", content);

if (!response.IsSuccessStatusCode)
{
// Handle error
var error=await response.Content.ReadAsStringAsync();
throw new Exception($"Upload failed: {error}");
}
}
