# FileSelect Pdf Problems - not implemented

## Question

**Eri** asked on 09 Aug 2022

Hey, i am following the example listed here Blazor FileSelect - Events | Telerik UI for Blazor to use the FileSelect in my project to allow users to upload files in a blazor server all. I'm using the code below to save the files to a network location. private async Task UploadFile(FileSelectFileInfo file)
{
var path=Path.Combine(HostingEnvironment?.WebRootPath, file.Name);
await using FileStream fs=new FileStream(path, FileMode.Create);
await file.Stream.CopyToAsync(fs);
} This code works fine for .doc & .docx files, but when I tried to attempt to upload a .pdf file, the application crashes. I have also tried to use the on async method and it throws a not implemented exception. Any idea how to get around this? file.Stream.CopyTo(fs);

### Response

**Dimo** commented on 10 Aug 2022

Eric, the PDF file type should not be related in this case. I just tested the scenario from the linked documentation and it works. Seek the problem elsewhere, for example in the file size, file name, or anything that can cause an exception, because the code does not expect something to happen.
