# Upload control! Basic example ?

## Question

**Dea** asked on 26 Sep 2023

{ Note! I am a desktop dev, very little Web.. so bare with my dumb ?s } My issue is with the line: file.CopyToAsync I dont see that CopyToAsync. Guessing becuase my file=file in args.Files How can I get that CopyToAsync, so I can upload a file? Thanks in advance. I have on my razor page <div class="k-form-field"> <label class="k-label k-form-label">Files:</label> <div class="k-form-field-wrap"> <TelerikUpload Id="DuffUpLoader" SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" OnUpload="@OnUpload" AutoUpload="false"> </TelerikUpload> </div> </div> <style> .k-upload-files { max-height: 200px; overflow-y: auto; } </style> in my behind the code: public string SaveUrl=> ToAbsoluteUrl("Resources/upload/save"); public string RemoveUrl=> ToAbsoluteUrl("Resources/upload/remove"); private async Task OnUpload(UploadEventArgs args) { foreach (var file in args.Files) { using (var fileStream=new FileStream(SaveUrl, FileMode.Create)) { await file.CopyToAsync(fileStream); }; //await using FileStream fs=new(SaveUrl, FileMode.Create); //await file.OpenReadStream().CopyToAsync(fs); }; }

### Response

**Deasun** commented on 26 Sep 2023

tried: UpLoader.UploadFiles(); doesnt seem to do anything!

### Response

**Deasun** commented on 26 Sep 2023

also tried both of these: foreach (var file in args.Files) { //using (var fileStream=new FileStream(SaveUrl, FileMode.Create)) //{ // await file.CopyToAsync(fileStream); //}; await using FileStream fs=new(SaveUrl, FileMode.Create); await file.OpenReadStream().CopyToAsync(fs); };

### Response

**Nadezhda Tacheva** commented on 29 Sep 2023

Hi Deasun, I am not able to confirm why you do not see CopyToAsync based on just the provided information. At this stage, I am also not completely certain why you need to handle the OnUpload to copy the file stream. The Upload component will directly send the selected files to the configured endpoint and such operations are generally performed in the controller. The OnUpload event is often used to send additional custom data and request headers to the server and not for handling the upload. This is actually one major difference between the Upload and FileSelect components - the Upload directly uploads the selected files while the FileSelect provides you with the Stream of the selected file, so you can decide what to do with it. The more suitable component to use really depends on the specific case and the desired result. If you want to proceed with the Upload, my suggestion is to use the samples from here as a base to see how you can set up the Upload and the controller. Take a look at the Save() task inside the controller. The "files" it uses is of type IFormFile and CopyToAsync is invoked on that. Take your time to revise the sample and test the configuration on your end. Please let us know if you are still facing difficulties after that. If so, please send a runnable sample that replicates your configuration, so we can actually test it.

## Answer

**Deasun** answered on 06 Oct 2023

The controller part was my issue. Working grand now.
