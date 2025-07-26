# OnSuccess not being called when response body is large

## Question

**BobBob** asked on 04 Nov 2020

I have implemented the upload control to allow user's to upload a new avatar to their profile. In my SaveUrl I convert their uploaded file to a base64 string and return that string as the body of the Request's response. The problem is that the OnSuccess action is never called when I come back. If i simply return a blank string (or something short like "Hello World", it is called just fine, so the problem appears to be that the base64 string is rather long. I have not figured out why this is happening. Any help would be appreciated. [HttpPost("saveavatar")] [DisableRequestSizeLimit] public async Task<IActionResult> SaveAvatar(IFormFile avatar) { string returnString=null; if (avatar !=null) { using var stream=new MemoryStream(); await avatar.CopyToAsync(stream); byte[] croppedImageBytes=imageHelper.ScaleImage(stream, 80, 100, ImageFormat.Png); string avatarBase64=Convert.ToBase64String(croppedImageBytes); returnString=$"data:image/png;{avatarBase64}"; } return Content(returnString); } private void OnAvatarSuccess(UploadSuccessEventArgs e) { string content=e.Request.ResponseText; if (e.Operation==UploadOperationType.Upload) { staffMember.Avatar=content; } }

## Answer

**Stamo Gochev** answered on 09 Nov 2020

Hi Bob, Indeed, the problem is most probably connected with the size of the base64-encoded image. What I can suggest is to return the URL of the uploaded image instead of encoding the image itself, which will reduce the total bytes transferred to the browser. If this doesn't work, can you send me a runable project that demonstrates the issue, so I can investigate it? Regards, Stamo Gochev

### Response

**Bob** answered on 09 Nov 2020

I am trying to avoid saving the file to disk, so I am just using the stream to get the base64 bytes. I will create a project for you but how I send it to you? I am only allowed to attach images to these posts?

### Response

**Stamo Gochev** answered on 10 Nov 2020

Hello Bob, You can attach files other than images using the "Attach files" button after the project folder is archived as a .zip/.rar. More information can be found in: [https://www.telerik.com/blogs/how-to-submit-a-support-ticket](https://www.telerik.com/blogs/how-to-submit-a-support-ticket) [https://docs.telerik.com/teststudio/knowledge-base/best-practices-kb/submit-support-ticket#new-tickets](https://docs.telerik.com/teststudio/knowledge-base/best-practices-kb/submit-support-ticket#new-tickets) If saving the file on the disk is not applicable in your case, then what I can suggest is to read the file in the browser (e.g. using FileReader API ). A feature request for a component that does this has already been logged in the Feedback Portal, so you can vote for it at: [https://feedback.telerik.com/blazor/1460649](https://feedback.telerik.com/blazor/1460649) Regards, Stamo Gochev

### Response

**Bob** answered on 10 Nov 2020

It does not let me attach my zip file here. I get: The selected file(s) cannot be attached because it may exceed the maximum attachment size (2 MB) or is from not allowed type (allowed: .jpg, .jpeg, .gif, .png).

### Response

**Stamo Gochev** answered on 11 Nov 2020

Hello, Can you try to split the project into parts and attach them separately, if the file size is too big? Removing any unnecessary folders/files like "bin" and "obj" is also applicable. Regards, Stamo Gochev

### Response

**Bob** answered on 11 Nov 2020

The problem is NOT the size the of attachment (it's only 219KB). The problem is you are ONLY allow jpg, jpeg, gif, or png attachments! I have renamed the attachment to a .jpg file so that I can send it but you will have to change it to a .zip file to use it.

### Response

**Stamo Gochev** answered on 11 Nov 2020

Hello Bob, There is currently a problem with attaching .zip files in a forum thread (like this one), so in the future, you can open a standard support ticket, which does allow uploading .zip files. I am sorry for the inconvenience. I was able to run your project, but the "OnSuccess" handler is called as shown below: I tried this with various images (including images with different files extensions), but the handler is working OK. Can you send me the file you are testing with and a video that demonstrates this on your side, so I can replicate the exact steps to reproduce the problem? Regards, Stamo Gochev

### Response

**Bob** answered on 11 Nov 2020

Here is the file. I don't know how to make a video showing you what I am doing, but all I am doing is choosing this file in your upload control.

### Response

**Stamo Gochev** answered on 13 Nov 2020

Hi Bob, I tested with the image that you sent (me5.jpg) and I can confirm that the "OnSucess" handler is indeed not being hit (although I tested with various other images and they are working OK). What I've found out though is that the custom logic in the "SaveAvatar" method (in "UploadController.cs" file) is causing the problem: public async Task<IActionResult> SaveAvatar ( IFormFile avatar ) { string returnString=null; if (avatar !=null )
{ using var stream=new MemoryStream(); await avatar.CopyToAsync(stream); byte[] croppedImageBytes=imageHelper.ScaleImage(stream, 80, 100, ImageFormat.Png); string avatarBase64=Convert.ToBase64String(croppedImageBytes);

returnString=$"data:image/png; {avatarBase64} ";
} return Content(returnString);
} If the line: byte [] croppedImageBytes=imageHelper.ScaleImage(stream, 80, 100, ImageFormat.Png ); is changed to use a JPEG extension: byte [] croppedImageBytes=imageHelper.ScaleImage(stream, 80, 100, ImageFormat.Jpeg ); the "OnSuccess" handler is called. I am attaching a GIF that shows the result on my side (upload-image.gif). The "ImageHelper.ScaleImage" contains some custom code that is causing the problem, so you can check it out. Regards, Stamo Gochev

### Response

**Bob** answered on 13 Nov 2020

That worked, I think because the jpeg creates a smaller base64 string. The issue still remains that when the base64 string is too large (and if I specifically need a png) it still doesn't work. I guess I will have to figure out if there is any way to increase the maximum size allowed to be returned, but for now changing it to jpeg worked, so thanks for the help.

### Response

**Stamo Gochev** answered on 18 Nov 2020

Hello Bob, You are correct that the size of the encoded data is problematic and the same issue might be encountered without the Upload component by making a request to the controller action that returns a long base64 string. Handling such scenarios is more suitable for a component like FileSelect: [https://feedback.telerik.com/blazor/1460649](https://feedback.telerik.com/blazor/1460649) What I can suggest as an alternative is to implement logic that leverages the FIleReader API and read the image in the browser's memory or try the new InputFile component. Regards, Stamo Gochev
