# Rename file on upload

## Question

**RobRob** asked on 16 Jun 2021

I'm having a problem changing the filename on upload. The control reports the file was uploaded with the new name, but the controller's file.ContentDisposition looks like this: form-data; name="file"; filename="Original.png" Here's my OnSelectHandler: private void OnSelectHandler ( UploadSelectEventArgs e ) { if (e.Files.Count> 1 )
{
e.IsCancelled=true;
} foreach ( var file in e.Files)
{
file.Name="New.png";
}
} I've also tried modifying the method to be private Task OnSelectHandler which returned Task.CompletedTask,

## Answer

**Dimo** answered on 17 Jun 2021

Hi Rob, In the described scenario, a file can be renamed at two places: In the OnSelect handler - this affects the client-side UI only In the remote endpoint - this affects the server side only So, to achieve consistency between the client and server, you need to do both. Here is the relevant documentation that explains this in more details: [https://docs.telerik.com/blazor-ui/components/upload/events#onselect](https://docs.telerik.com/blazor-ui/components/upload/events#onselect) See subsection "Changing the file name and checking for duplicate files on the server". You may ask why the component works like this and why changing the name in OnSelect does not affect the actual uploaded file. The answer is security - browsers do not allow programmatic tampering with file inputs. Regards, Dimo Progress Telerik
