# FileSelect accepts more than one file through drag and drop.

## Question

**Twa** asked on 06 Jul 2023

Hello. I am using the FileSelect component to upload a single file. For this, I configured the property Multiple=false, and everything works as expected. The problem is that regardless of the Multiple state, more than one file can be uploaded through Drag and Drop. I believe this is an inconsistency in the component's logic since both file selection options should be limited. How can this be achieved in a simple way? Another question: Is it possible to deactivate the drop zone? Greetings. Twain.

## Answer

**Yanislav** answered on 11 Jul 2023

Hello Twain, Thank you for reporting this issue. It does indeed seem incorrect that when the user drops multiple files, the FileSelect selects all of them. Therefore, I have logged a Bug Report item on your behalf: [https://feedback.telerik.com/blazor/1615763-the-restriction-of-selecting-only-one-file-when-multiple-false-is-bypassed-when-files-are-dragged](https://feedback.telerik.com/blazor/1615763-the-restriction-of-selecting-only-one-file-when-multiple-false-is-bypassed-when-files-are-dragged) As a creator, you are automatically subscribed to receive email notifications about status changes. I have added your vote there to increase its popularity, as we prioritize fixes based on community demand and severity. In the meantime, as a workaround, you can check the ` args.Files ` count in the OnSelect event and cancel the event if there are multiple files, preventing the selection of multiple files. async Task OnSelectHandler ( FileSelectEventArgs args ) { if (args.Files.Count()> 1 )
{
args.IsCancelled=true; return;

} As a token of gratitude for helping us identify this issue, I have updated your Telerik points.===Regarding your question - currently, the API does not expose a configuration/parameter that allows you to deactivate the drop zone. If you think that such a configuration would be helpful and will enhance the FileSelect component, you can log a feature request in our

### Response

**Twain** commented on 11 Jul 2023

Hello Yanislav, Thank you for your prompt response and for logging a bug report on my behalf. I appreciate the workaround you provided and will use it until the issue is resolved. I also appreciate the update to my Telerik points. Regarding the drop zone configuration, I understand that it is not currently available in the API. However, I will log a feature request in your

### Response

**Yanislav** commented on 14 Jul 2023

Hello Twain, You're welcome! I'm glad I was able to help. In case you have other questions, please do not hesitate to contact us.
