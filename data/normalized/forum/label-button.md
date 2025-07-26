# Label / Button

## Question

**Ala** asked on 02 Jul 2020

I would like to have the upload component but change the text on the button or, even better, create a Telerik button and call the upload functionality. That way, the button could have theming, etc. and only the upload would need to be called. Any pointers on how I can accomplish either task (especially calling from a button)?

## Answer

**Marin Bratanov** answered on 03 Jul 2020

Hi Alan, The button is already themed, and you can change its text through localization (including the default string): [https://demos.telerik.com/blazor-ui/upload/globalization.](https://demos.telerik.com/blazor-ui/upload/globalization.) In the demo you can also change the theme to see how it looks. As for invoking the upload manually - there is a built-in feature for that - setting the AutoUpload parameter to false will give your users an explicit Upload button they must click before the actual request to the server is sent. This property defaults to true, as we believe it provides better UX that way for the majority of cases. Regards, Marin Bratanov

### Response

**khashayar** answered on 06 Jul 2020

hello, yes the localization works but i also need to change the whole text to another one how can i do it ?

### Response

**Marin Bratanov** answered on 06 Jul 2020

Hello Khashayar, I am attaching a video from the demo that shows how localization changes the entire text of the button. I'd suggest you download our demos (you can find them in the "demos" folder in your local installation) with our latest version and see how that works on the demos so you can emulate that. You can also see the Globalization article for details and examples. If you have issues with that, please open a support ticket and send us a simple runnable example that showcases the problem so we can have a look. Regards, Marin Bratanov

### Response

**khashayar** answered on 07 Jul 2020

yes this is how localization works but i need to change the button text to a completely diferent text like i want to change Select files... to Upload image

### Response

**Daniel** answered on 07 Jul 2020

Hi Khashayar, I also wanted to use a custom button to trigger the file upload from elsewhere on my form. I have my custom button trigger a JavaScript interop call, which in turn triggers the "Select files" button on the TelerikUpload control. The trick is to trigger the click event on the input element inside the button div, not the button div itself. Here is a simple example of the javascript. This assumes you only have one upload control on the form...if not you can get creative and pass container classes or other identifiers. Hope this helps. window.customUploadClick=function () { $( '.k-upload-button input' ).trigger( 'click' ); }

### Response

**Alan** answered on 08 Jul 2020

Ok, I finally had a chance to see what Marin is describing. Check out this file in the git repo: [https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Shared/Resources/TelerikMessages.resx](https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Shared/Resources/TelerikMessages.resx) ~Line 598 shows you where to change the text. Makes sense but I think it would be good to have a simpler way to handle it. That is my personal opinion. Perhaps a Text property or label or Content tag. Telerik devs know better than I do on how to handle it but simpler usage would be helpful.

### Response

**Marin Bratanov** answered on 08 Jul 2020

Hi all, I made these Feature Request pages in the Feedback Portal so you can Follow the implementation status of such ideas. I have added the Votes of the people who participated in this discussion, and anyone else can also Vote for an item to raise its priority. Text parameter for the button: [https://feedback.telerik.com/blazor/1475229-button-text-content-parameter](https://feedback.telerik.com/blazor/1475229-button-text-content-parameter) Method to start uploads: [https://feedback.telerik.com/blazor/1475230-trigger-file-upload-from-my-own-button](https://feedback.telerik.com/blazor/1475230-trigger-file-upload-from-my-own-button) Metod to trigger file select dialog: [https://feedback.telerik.com/blazor/1475231-trigger-file-select-dialog-from-my-own-button](https://feedback.telerik.com/blazor/1475231-trigger-file-select-dialog-from-my-own-button) You may also find interesting this one for a custom area to drop files into: [https://feedback.telerik.com/blazor/1471026-custom-droptarget-for-telerikupload.](https://feedback.telerik.com/blazor/1471026-custom-droptarget-for-telerikupload.) If so, Vote for, and Follow it. Regards, Marin Bratanov

### Response

**Alan** answered on 08 Jul 2020

Awesome. Thank you.
