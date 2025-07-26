# Notification doesn't work

## Question

**Mau** asked on 14 Sep 2022

Probably I do something very simple wrong but I try to follow the single instance per app example and if I debug my code I can see the cascading variable getting the instance. I can send the following code without any error in the code or in the console of my browser Notification. Instance. Show ( new NotificationModel { Text="TEST", ThemeColor=ThemeConstants. Notification. ThemeColor. Error, CloseAfter=30000, Closable=true }); But I will not see the notification on screen. It doesn't matter if this is somewhere in the code or in the protected override async Task OnAfterRenderAsync ( bool firstRender ) or protected override void OnInitialized ()

## Answer

**Radko** answered on 15 Sep 2022

Hi Maurice, Given you are correctly passing the Notification object as a Cascading parameter and are invoking the Show method, I see no reason why the notification will not appear. A possible issue that comes to mind is related to the notification's z-index, as in, it might be in fact appearing, just being hidden by the page content already present there. Could you have a look at the following article which might help, if this is the case: Notification - Z-Index. If this is not the issue, could you please see if our example works as expected for you? The example has been updated to run on .NET 6 and use our latest package version, so it should be runnable without the need for any changes. Here is a link to it: [https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app](https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app) If you are still having issues, would it be possible for you to prepare a small project that reproduces the behavior, so we can have a look? Regards, Radko Stanev

### Response

**Maurice** commented on 15 Sep 2022

It was the Z-INDEX. Now it works
