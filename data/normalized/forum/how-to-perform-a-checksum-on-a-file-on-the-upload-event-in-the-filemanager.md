# How to perform a checksum on a file on the upload event in the filemanager

## Question

**Emm** asked on 12 Sep 2024

Hello, i want to perform a checksum under a memorystream under the uploaded file on the upload event on the filemanager , i need to check if my file is already uploaded then check if the name is the same and so give the user some choice before uplod trully the file can you give me some docs ? sample

## Answer

**Dimo** answered on 12 Sep 2024

Hi Emmanuel, Such checks can happen in the controller, because the app doesn't have access to the uploaded file's content earlier. Then, use the OnSuccess event to notify the user for something, if necessary. Regards, Dimo Progress Telerik
