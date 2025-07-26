# FileInfoStream throws NotImplementedException

## Question

**Joh** asked on 02 Nov 2022

Hi, I use the FileSelect component and when using the FileInfoStream object with another component that isn't asynchronous I get a NotImplementedException for the Read() method. Do you plan to implement these methods to ensure compatibility with synchronous components? Thanks! System.NotImplementedException: The method or operation is not implemented.
at Telerik.Blazor.Components.FileSelect.Stream.FileInfoStream.Read(Byte[] buffer, Int32 offset, Int32 count)
at System.IO.StreamReader.ReadBuffer()
at System.IO.StreamReader.ReadLine()

## Answer

**Dimo** answered on 04 Nov 2022

Hello Johannes, Blazor Server does not support synchronous IO reading of streams, that's why we have overridden some of the Stream methods in our code. The same limitation exists for the standard Blazor InputFile component. I also recommend this post and the pages it links. A possible workaround is to copy the FileSelect Stream to another one and work with that instead. @using System.IO

<TelerikFileSelect OnSelect="@ReadSelectedFiles" /> @code { private async Task ReadSelectedFiles ( FileSelectEventArgs args ) {
foreach ( var file in args.Files)
{ var ms=new MemoryStream(); await file.Stream.CopyToAsync(ms); var byteArray=new byte[file.Size];

ms.Seek( 0, SeekOrigin.Begin); // not possible with file.Stream ms.Read(byteArray); // not possible with file.Stream }
}
} Regards, Dimo Progress Telerik
