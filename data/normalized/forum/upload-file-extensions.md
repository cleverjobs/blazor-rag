# Upload: File extensions

## Question

**Joe** asked on 19 May 2025

Is there a way to filter which file extensions are allowed to be selected? I limit to PDF or PNG but it allows me to select XML. <div> <hr /> <h4 class="gsi-padding-tb0-lr12"> Upload File to Session... </h4> <TelerikUpload AllowedExtensions="@( new List<string>() { ".pdf ", ".png " } )" OnSelect="@OnUploadSelect" OnCancel="@OnUploadCancel" OnRemove="@OnUploadRemove"> </TelerikUpload> <div class="demo-hint gsi-padding-tb0-lr12"> <small> Upload <strong> PDF </strong> or <strong> PNG </strong> files with a maximum size of <strong> 6MB </strong>. </small> </div> </div>

## Answer

**Dimo** answered on 20 May 2025

Hi Joel, Please set the Upload Accept parameter to filter the selectable files in the browser's file dialog. Regards, Dimo Progress Telerik

### Response

**Joel** commented on 20 May 2025

We are closer... but, not quite there yet. First, the documentation on what that string is supposed to look like is not easily found. Secondly, with the AllowedExtensions attribute, this Accept property seems redundant in your design. But, this is what I have. I still need help to remove the "all files" option. Any ideas? <TelerikUpload Accept=".pdf,.png" AllowedExtensions="@( new List<string>() { ".pdf ", ".png " } )" OnSelect="@OnUploadSelect" OnCancel="@OnUploadCancel" OnRemove="@OnUploadRemove"> </TelerikUpload>

### Response

**Joel** commented on 20 May 2025

When a file is added to the upload control that doesn't meet the extension requirements I am provided an "X" to remove it from the list. When I do that I want to evaluate all the files in the control to determine if I should show an error. The args give me the file that is to be removed. Is there a way to capture all the files out of the control? protected void OnUploadRemove(UploadEventArgs args)
{
try
{
foreach (var file in args.Files)
{
if (file.Extension.ToLower() !=".pdf" &&
file.Extension.ToLower() !=".png")
{
throw new Exception("Invalid file selection. Only PDF or PNG files are accepted for upload.");
}
}
}
catch (Exception ex)
{
ProfileService.Exception=ex;
}
}

### Response

**Dimo** commented on 21 May 2025

Yes, you can keep track of all files that were selected, uploaded, and removed with the help of the Upload events. You can also check this KB article, which deals with a similar scenario: Count all selected and uploaded files in the Telerik Upload for Blazor
