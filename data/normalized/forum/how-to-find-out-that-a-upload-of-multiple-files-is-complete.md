# How to Find out that a Upload of multiple Files is complete?

## Question

**Dom** asked on 27 Jun 2022

<TelerikUpload SaveUrl="api/v1.0/files/save" RemoveUrl="api/v1.0/files/remove" AllowedExtensions="@AllowedFileTypes" MinFileSize="@MinFileSize" MaxFileSize="@MaxFileSize" AutoUpload="true" Multiple="true" WithCredentials="false" OnUpload="@OnUploadHandler" OnProgress="@OnProgressHandler"/> I need an EventCallBack for "OnComplete" for a completion of all files or "OnProgress???" for all files. Or a complete different solution.

## Answer

**Dominik** answered on 27 Jun 2022

That's my solution for now. Maybe needs improvement for Error-Handling. private int count=0; protected async Task OnUploadHandler ( UploadEventArgs args ) {
count=args.Files.Count;
} protected void OnSuccessHandler ( UploadSuccessEventArgs args ) {
count -=args.Files.Count; if (count==0 )
{
OnUploadReady?.Invoke();
}
}

### Response

**Timothy J** answered on 27 Jun 2022

From the docs it appears OnSuccess fires for each file. I think you need to keep track of each file via OnSelect and keep track of the count in both events and when the counts match, you can fire your own OnAllFileSuccess event.

### Response

**Dominik** answered on 27 Jun 2022

I was afraid of it! Progress should improve it.
