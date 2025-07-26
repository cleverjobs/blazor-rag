# Telerik.Blazor.Components.FileSelect.Stream Invalid operation exception

## Question

**bim** asked on 01 Apr 2025

Hi folks, I am trying to upload a file to a state container using the FileSelect component. private async Task OnFileSelected(FileSelectEventArgs e) { try { foreach (var file in e.Files) { using var memoryStream=new MemoryStream(); byte[] buffer=new byte[81920]; // 80 KB buffer size int bytesRead; while ((bytesRead=await file.Stream.ReadAsync(buffer, 0, buffer.Length))> 0) { await memoryStream.WriteAsync(buffer, 0, bytesRead); } byte[] fileBytes=memoryStream.ToArray(); // Store file in state container await FileState.AddFileContentAsync(file.Name, fileBytes); } } catch(Exception ex) { Console.WriteLine("Error uploading files " + ex.Message); } StateHasChanged(); } Here file.Stream.ReadAsync is not working. In Visual studio for the file.Steam property I am getting the following error message. SYNCHRONOUS_FILESTREAM_READ_ERROR property Synchronous actions on the file stream is not supported by the Blazor framework in Blazor Server-side apps due to the SignalR communication between the client and the host. Use the 'ReadAsync' method instead. and the code does not continue to execute after the line while ((bytesRead=await file.Stream.ReadAsync(buffer, 0, buffer.Length))> 0)

## Answer

**bimal** answered on 03 Apr 2025

Hi Anislav , Issue fixed. In Program.cs had to increase the SignalR MaximumMessageReceiveSize to about 1 mb from default 32 kb. builder.Services.AddServerSideBlazor() .AddHubOptions(options=> { options.MaximumReceiveMessageSize=1 * 1024 * 1024; });

### Response

**Anislav** answered on 01 Apr 2025

Did you try using CopyToAsync instead of ReadAsync? Here's an example specifically for Blazor Server apps: [https://www.telerik.com/blazor-ui/documentation/components/fileselect/events#example.](https://www.telerik.com/blazor-ui/documentation/components/fileselect/events#example.) Regards, Anislav Atanasov

### Response

**bimal** commented on 02 Apr 2025

Yes Anislav, I tried the standard code first as shown below, since it was not working. I tried a workaround with ReadAsync . it was also giving the same error private async Task OnFileSelected(FileSelectEventArgs e) { foreach (var file in e.Files) { using var stream=new MemoryStream(); await file.Stream.CopyToAsync(stream); byte[] fileBytes=stream.ToArray(); // Store file in state container await FileState.AddFileContentAsync(file.Name, fileBytes); } StateHasChanged(); }
