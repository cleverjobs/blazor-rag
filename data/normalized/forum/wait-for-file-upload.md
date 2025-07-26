# Wait for file upload?

## Question

**Ric** asked on 15 Feb 2022

Hi, I have some backend API calls that I have to run before I TelerikUpload some files, namely I have to collect a ticketid to assign to the documents. Once I have my ticketid, I call UploadRef.UploadFiles() and add the ticketid to the request. I appreciate that UploadFiles runs asynchronously but in my case, I need to wait and make sure all of the files are accepted and take some actions based on if all were successful or if there were failures. I thought it was going to be really easy, but apparently I can't await for UploadRef.UploadFiles(): await UploadRef.UploadFiles() // nope Instead I'm currently doing this and it works but feels kludgy: private int UploadSuccessCount {get; set;} private int UploadFailureCount {get; set;} private async Task OnTelerikSuccessHandler(UploadSuccessEventArgs e)
{
UploadSuccessCount++;
}

private async Task OnTelerikErrorHandler(UploadErrorEventArgs e)
{
UploadFailureCount++;
}

private async Task <bool> WaitForFileUpload()
{
if(RequestModel.FileCount==0)
{
return true;
}

int count=RequestModel.FileCount;
UploadSuccessCount=0;
UploadFailureCount=0;
UploadRef.UploadFiles();

int processed=UploadSuccessCount + UploadFailureCount;
while( processed <count )
{
await Task.Delay(1000);
processed=UploadSuccessCount + UploadFailureCount;
}

return UploadSuccessCount==count ? true : false;
} I think UploadRef ought to be able to get at least the count of files that are ready to upload. In my case, there are some times that files are required. Currently, I have to track the file count via events: private async Task OnTelerikSelectHandler(UploadSelectEventArgs e)
{
RequestModel.FileCount +=e.Files.Count;
StateHasChanged();
}

private async Task OnTelerikRemoveHandler(UploadEventArgs e)
{
int count=RequestModel.FileCount - e.Files.Count;
if (count <0 ) count=0;
RequestModel.FileCount=count;
StateHasChanged();
} I would like to be able to wait for the uploads to complete, perhaps await UploadRef.UploadFilesAsync(); Thoughts?

### Response

**Rich** commented on 18 Feb 2022

Thanks for getting back with me. I took a look through the example and it's pretty close to what I'm already doing, so I feel pretty good about that. Rather than separately tracking the list of files to be uploaded and then syncing them via upload events, it would be easier if I could just look in on the list when I want to. In my case I don't want to autoupload - I have to do a few things before the upload starts, namely I have to call a backend service to get a ticketid to apply to each file upload. I'm envisioning more like this: if (UploadRef.Files.Count==0 ) // Can't seem to check on files through the uploadref?
{ await HideWindow(); // ticket doesn't have files, we're done.
ToastService.ShowSuccess( $"Service Request {TicketId} Successfully Added." );
} else {
var result=await UploadRef.UploadFilesAsync(); // Would be nice to be able to wait until finished. // do something on success // do something on failure } And then result would be something like a list of files with a 'success' boolean for each.

### Response

**Svetoslav Dimitrov** commented on 23 Feb 2022

Hello Rich, The best approach would be to use some custom logic as in the example. It would provide much greater flexibility. Other than that simply awaiting a file to complete would not guarantee that the validation has passed, in many cases, the server needs to execute some logic, like scanning for viruses.

## Answer

**Svetoslav Dimitrov** answered on 18 Feb 2022

Hello Rich, The best way to achieve the desired behavior is by using validation. We have an example on our public GitHub repository that showcases how to create validation for the TelerikUpload. Let me know if this example helps you move forward. Regards, Svetoslav Dimitrov Progress Telerik
