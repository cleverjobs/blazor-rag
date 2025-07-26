# How do I include a bearer/access token?

## Question

**SLSL** asked on 13 May 2020

I'm testing the Upload component and I'm using bearer tokens on my APIs. How do I include the bearer token in the TelerikUpload component? Thanks.

## Answer

**SL** answered on 13 May 2020

Oops, I found the events doc so I'm going to try it first. [https://docs.telerik.com/blazor-ui/components/upload/events](https://docs.telerik.com/blazor-ui/components/upload/events)

### Response

**SL** answered on 13 May 2020

Okay, this warrants a question. The UploadHandler works when attaching auth tokens. Howerver, clicking the retry icon when the upload fails does not fire the UploadHandler so no auth tokens is getting sent to the server. Is there another event where the retry should be handled?

### Response

**Marin Bratanov** answered on 13 May 2020

Hi, I made the following public page where you can Follow a fix for this issue: [https://feedback.telerik.com/blazor/1465957-the-retry-button-does-not-fire-onupload-and-you-can-t-attach-auth-tokens.](https://feedback.telerik.com/blazor/1465957-the-retry-button-does-not-fire-onupload-and-you-can-t-attach-auth-tokens.) Regards, Marin Bratanov
