# Prepopulate Upload component

## Question

**Way** asked on 12 May 2021

Is there anyway to prepopulate the Upload control? Basically access the Files property to initialize with existing files. I am able to do this in the Kendo UI Upload.

## Answer

**Marin Bratanov** answered on 12 May 2021

Hello Wayne, You can Follow the implementation of such functionality here: [https://feedback.telerik.com/blazor/1485660-initial-files-in-blazor-upload.](https://feedback.telerik.com/blazor/1485660-initial-files-in-blazor-upload.) I added your Vote to it on your behalf to raise its priority. Regards, Marin Bratanov

### Response

**Irfan** commented on 09 Sep 2021

@Marin, Is there any workaround for this functionality to work?

### Response

**Marin Bratanov** commented on 09 Sep 2021

Unfortunately there is no workaround possible, it is a pretty serious feature even it if has a relatively small public api surface. In the meantime you can consider showing info to your users about related files they have on record in a grid or listview near (or next to, or above, or below) the upload so they can see what they have already. You can also return info for errors (say, duplicate files) in the OnSuccess event (see the second snippet) and show them a message (maybe through the Dialog component ).
