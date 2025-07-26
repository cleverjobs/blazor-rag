# Is it possible to remove successfully uploaded files from the TelerikUpload component

## Question

**Han** asked on 15 May 2025

Hi I have my own logic in the TelerikUpload OnSuccess Event that does some things to the uploaded files and therefore keep my own list of them. So the "File successfully uploaded" entries in the lower part of the component are useless for me. I tried to remove them somehow in the OnSuccess Event but the only thing I found was the ClearFiles method which removes all files, even those that are still uploading. Is there a way to remove specific files from the list or an option to remove them automatically?

## Answer

**Dimo** answered on 16 May 2025

Hi Hans, Currently your option is to hide the built-in Upload file list and use the Upload events to create a custom file list that you can fully control. You can check this KB article: Count selected and uploaded files. It's not about the same scenario, but it relies heavily on the component events, so you can use it as reference. Regards, Dimo Progress Telerik
