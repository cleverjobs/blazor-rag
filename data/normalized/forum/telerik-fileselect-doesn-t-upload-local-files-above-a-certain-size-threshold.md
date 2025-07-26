# Telerik FileSelect doesn't upload local files above a certain size threshold

## Question

**Ric** asked on 24 Feb 2023

Hello! I want to import .json files from my local machine using FileSelect: <TelerikFileSelect AllowedExtensions="@AllowedExtensions" MaxFileSize="@MaxFileSize" OnSelect="@OnFileSelectHandlerTest"> </TelerikFileSelect> The maximum file size is set to 4MB and the OnSelect function is as defined below, which is pretty much the example given at Blazor FileSelect - Events - Telerik UI for Blazor: async Task OnFileSelectHandler ( FileSelectEventArgs args ) { foreach ( var file in args.Files)
{ var byteArray=new byte [file.Size]; await using MemoryStream ms=new MemoryStream(byteArray); await file.Stream.CopyToAsync(ms);
}
} The method works fine for very small documents, below +- 26KB. Above this threshold, the app warns that it is attempting to reconnect to server and, after a couple of seconds, no document appears which suggests that the application gets stuck awaiting the CopyToAsync. The rest of the application (outside the FileSelect component) still works, but I can no longer add new files or remove the ones already selected. Has anyone been experiencing this problem and managed to solve it? (the same happens if I first create a local file and copy asynchronously into it) Thank you

## Answer

**Dimo** answered on 28 Feb 2023

Hi Ricardo, Our documentation discusses SignalR message size limitations. Adjust the app settings. Regards, Dimo
