# File Select List

## Question

**Eri** asked on 05 Aug 2022

I am using a FileSelect to allow users to upload attachments with a request. Once the file is uploaded and it appears in he file list, there doesn't seem to be a way to allow the user to open in from an OnClick event or anything. Is there a way to either: 1. Capture and on click even when they click a file in the FileSelectFileList or 2. Hide the FileSelectFileList all together so that I can replace it with my own list and implement the functionality myself? Thanks in advance

## Answer

**Dimo** answered on 05 Aug 2022

Hello Eric, Point 1 will be possible when we implement file item templates. Point 2 is possible now - see the KB article that shows how to hide the built-in file list. Use the Upload events to create and manage your custom file list. Regards, Dimo
