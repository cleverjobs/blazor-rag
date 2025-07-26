# Work with Blazor Upload in Offline mode.

## Question

**Zei** asked on 12 Sep 2022

I need to take photos and videos and save their path in IndexedDB from our web app so, when user decides to go to another page or reload it ..I can be able to retrieve the photos or video that user took through files' path and all of this should work in offline mode and from a tablet(Android's system) the user will submit the information later. So, what our team thought to do is using File system Access API. Here is demo: [https://filehandle-indexeddb.glitch.me/.](https://filehandle-indexeddb.glitch.me/.) But, I tested this demo from my mobile browser(chrome) and did not work out correctly because android is not supported and that's why cannot access android file system:( . So, we thought that we can mix storing files handles in IndexedDB from File System Access API* and Blazor Upload from telerik but, We need to know if we can do it offline. Thanks in advance,

## Answer

**Dimo** answered on 13 Sep 2022

Hi Zeina, The Upload needs a remote endpoint to send the selected file. This can't work in offline mode. If you have a WebAssembly app, you can consider the FileSelect component instead. It will provide the content of the selected file to the .NET runtime on the user's device, so that you can store it in the browser's localStorage and reuse it later. Regards, Dimo Progress Telerik
