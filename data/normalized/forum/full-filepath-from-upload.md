# Full FilePath from Upload

## Question

**Mat** asked on 11 Oct 2021

My customers currently have a tool where they identify documents used to support their conclusion. In it, they want to store a full file path. I am attempting to repurpose the Upload component, while I eagerly anticipate the FileSelect component in 2.30.0. I can get the file name. I have to assume that the component knows the original path, otherwise, how would it know where to grab the file from. Is there a way to get that full path?

## Answer

**Dimo** answered on 14 Oct 2021

Hi Matt, For security reasons, there is no way to obtain the full path of uploaded files.>> the component knows the original path, otherwise, how would it know where to grab the file from Actually, the file is not grabbed from the file system by the Upload component. The Upload uses internally a regular <input type="file" />, as there is no other way. The file selection and retrieval process is sandboxed in the browser. We only control the UI, when the upload starts and what the target endpoint is. Regards, Dimo

### Response

**Matt** commented on 15 Oct 2021

That's what I have read over several posts in other forums. Didn't see a way to cancel my post. So, I understand, but really wish there was some way to obtain that path...
