# How to upload FileSelect Results from Blazor WASM app

## Question

**Chr** asked on 06 Jun 2022

I am trying to use the File Select component in a Blazor WASM app to upload a file. However, when I try to read the stream in the FileSelectEventArgs object, it's coming out empty. I do get a value for the stream length but reading it into a byte array is producing an array of 0's. Here's my code: @code {
List<string> CpmAllowedExtensions { get; set; }=new List<string> { ".pdf" }; async Task HandleFiles ( FileSelectEventArgs args ) { foreach ( var file in args.Files)
{ if (!file.InvalidExtension)
{ var b=new byte [file.Stream.Length]; await file.Stream.ReadAsync(b, 0, b.Length); //b is blank here }
}
}
}

<TelerikFileSelect OnSelect=@HandleFiles AllowedExtensions="@CpmAllowedExtensions"></TelerikFileSelect> How do I get to the byte array in the file so that I can upload it? The example I see in the Docs doesn't seem to be for uploading a file and trying to use a filestream as it does is producing the same result as my code above. Also, I tried uploading the file.Stream using a SteamContent object but nothing is getting sent in the request payload.

### Response

**Hristian Stefanov** commented on 09 Jun 2022

Hi Chris, The provided part of the code looks OK. It is similar to the first example in our documentation. Currently, in the sample, the file is getting selected only. As a next step, to upload the selected file, there is a need for manual coding in the OnSelect handler. Here is an example that has upload functionality implemented: FileSelect upload. You can use it as a starting point. Let me know if I can help with anything further.

### Response

**Chris** commented on 10 Jun 2022

Stephan, I tried the code in the second example that you linked but I think that's for a Blazor Server app. It didn't work for my Blazor WASM app. The line await file.Stream.CopyToAsync(fs, Tokens[file.Id].Token); is just producing an empty FileStream. Do you have an example from a Blazor WASM app?

## Answer

**Christopher** answered on 13 Jun 2022

This seems like the same question but it doesn't specify if it's WASM or not: [https://www.telerik.com/forums/how-to-use-the-fileselect-component-to-actually-upload-files](https://www.telerik.com/forums/how-to-use-the-fileselect-component-to-actually-upload-files)

### Response

**Nadezhda Tacheva** answered on 14 Jun 2022

Hi Christopher, I am stepping in the discussion to provide some more details. The other forum thread you linked targets Blazor Server apps only. The discussion there is for SignalR specifics regarding its MaximumReceiveMessageSize. You can read more details in the Large File Support section. In Blazor WASM you cannot experience such an issue as this hosting model does not use SignalR. Based on the testing I performed on my end, the problem here is not that the stream cannot be copied to the fs FIleStream, but rather that the fs object is not successfully created. In WASM you cannot create FileStream on the client because the app cannot directly access the client file system. Instead, you can use a MemoryStream and copy the Stream of the selected file there. You can find more details on that in the ASP.NET Core Blazor file uploads article. Here is a runnable sample that you can test, I am printing the stream length in the console as confirmation that the stream is successfully copied: [https://blazorrepl.telerik.com/GmOgFePe54pXfanW21.](https://blazorrepl.telerik.com/GmOgFePe54pXfanW21.) I hope this information and example will help you move forward with your application. Please let us know if any further questions are raised. Regards, Nadezhda Tacheva
