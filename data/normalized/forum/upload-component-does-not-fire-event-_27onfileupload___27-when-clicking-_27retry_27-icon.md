# Upload component does not fire event 'OnFileUpload()' when clicking 'retry' icon

## Question

**Jes** asked on 12 Oct 2020

Hi I have defined an OnUpload handler like this on the TelerikUpload: <TelerikUpload AutoUpload="false" ... OnUpload="@OnUploadHandler"></TelerikUpload> It turns out that the handler is only called when I click on the 'Upload' button. If the upload fails, the retry icon is shown. However when clicking on the Retry icon, the OnUpload handler is not called. In my case that is a problem, because I add headers and request in this event: async Task OnUploadHandler(UploadEventArgs e) { e.RequestData.Add("SomeFormField", "Hello world!"); // for example, user name e.RequestHeaders.Add("Authorization", "Bearer " + Token); // for example, authentication token } It does not matter if the request is to same host or cross-domain. Best regards

## Answer

**Marin Bratanov** answered on 13 Oct 2020

Hi Jesper, You can Follow the fix for that here: [https://feedback.telerik.com/blazor/1465957-the-retry-button-does-not-fire-onupload-and-you-can-t-attach-auth-tokens.](https://feedback.telerik.com/blazor/1465957-the-retry-button-does-not-fire-onupload-and-you-can-t-attach-auth-tokens.) I'm afraid there is no workaround I can offer. Regards, Marin Bratanov

### Response

**Jesper** answered on 13 Oct 2020

Hi Marin Thanks :-)

### Response

**Edward** answered on 24 Nov 2020

Just ran into this issue. Is there a fix planned for this?

### Response

**Marin Bratanov** answered on 25 Nov 2020

Hello Edward, The best way to know when this gets fixed is to click the Follow button on its portal page. Once we know the release it will be in, that information will be added to the page and you will receive an email. I've also added your Vote on your behalf to raise its priority (you can do that yourself by clicking the Vote button on items that interest you). Regards, Marin Bratanov
