# InputElement.files is empty in Google Chrome with TelerikUpload

## Question

**Hol** asked on 21 Apr 2022

Hi, at the OnUpload event I call a Javasrcipt to do some stuff before uploading. I generate a random string and set it as classname to the upload element to identify it in Javascript. In Javascript: var files=$( '. + uploaderClass)[0].querySelector(' input ').files; this works in Firefox but not in Chrome (official version, I installed today). So I set an pure HTML FileInput below the TelerikUpload like: <input type="file" id="testFileUpload" /> (I choose first in the testFileUpload a file, then in the TelerikUpload which fires my Javascript) I logged both elements to the browser console: var telerikUploadElement=$( '.' + uploadClass)[ 0 ].querySelector( 'input' ); var testInput=document.querySelector( '#testFileUpload' ); console.log(telerikUploadElement); console.log(testInput); The console output for the telerikUploadElement: input
.....
- files: FileList { length: 0 }
.... the console ouptut for the testInput: input#testFileUpload
....
- files: FileList {0: File, length: 1}
...... In Firefox, the console output is the same for both upload elements. Tested on: Windows10 Telerik.UI.for.Blazor 3.2.0.net6.0 Google Chrome 100.0.4896.127 Firefox 99.0.1

## Answer

**Marin Bratanov** answered on 23 Apr 2022

Hello Holger, This is not something we support in Blazor - DOM manipulations are not supported and they can cause a variety of issues (e.g., if the component re-renders, anything you touched in the DOM is likely to be lost, or anything you touch may break the components inner workings). If you need to attach information to files, you should do it when you get them for saving in the C# event. If you want to customize the appearance, you should upvote and follow the template feature: [https://feedback.telerik.com/blazor/1524852-upload-template-for-the-file-items.](https://feedback.telerik.com/blazor/1524852-upload-template-for-the-file-items.) Regards, Marin Bratanov

### Response

**Holger** commented on 25 Apr 2022

I do not want to add informations to the files, I want to read the files with the filereader in Javascript before sending them to the server. But I can't do that, because the file array is empty in Google Chrome.

### Response

**Marin Bratanov** commented on 25 Apr 2022

It seems to me that the FileSelect component will be a better fit to you than the Upload component - the File Select gives you the file as a stream in C# in the event so that you can do with it as you please. Here are its demo so you can see it in action: [https://demos.telerik.com/blazor-ui/fileselect/overview](https://demos.telerik.com/blazor-ui/fileselect/overview)
