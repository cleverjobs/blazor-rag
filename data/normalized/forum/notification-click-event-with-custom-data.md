# Notification click event with custom data

## Question

**Chr** asked on 15 Nov 2021

I'm utilizing the notification and trying to implement a click event similar to this example: [https://docs.telerik.com/blazor-ui/components/notification/templates#get-a-click-event-for-notification-body](https://docs.telerik.com/blazor-ui/components/notification/templates#get-a-click-event-for-notification-body) My problem is that I need to get a custom field to my click event (i.e. the ID of a database record) that will be different for each notification. Is there anyway to pass custom data to the notification other than what is in the NotificationModel?

### Response

**Chris** commented on 16 Nov 2021

To get around this, I ended up serializing an object into the NotificationModel.Text field and then deserializing it in the Notification template. It works, but it would be nice if there was a better way to do this.

## Answer

**Dimo** answered on 18 Nov 2021

Hi Chris, There is a better way that does not require (de)serialization. Implement a class that inherits from NotificationModel. For example, MyExtendedNotificationModel. Add the required properties to the new class. Pass a MyExtendedNotificationModel instance to the Notification Show method. This will allow you to set the custom properties. In the Notification <Template>, cast the context to MyExtendedNotificationModel. This will allow you to access and consume the additional data. If you use both overloads of Show(), make sure to check if the cast is successful, otherwise you may get a NullReferenceException. <TelerikNotification @ref="@NotificationReference" VerticalPosition="NotificationVerticalPosition.Top">
<Template>
@{ var myContext=context as MyExtendedNotificationModel; // This check is needed only if using both overloads of the Show() method. if (myContext !=null )
{
<span> @myContext.CustomID :</span>
<a style="color:inherit;" target="_blank" href="@( $" {myContext.CustomUrl}{myContext.CustomID} " )"> @myContext.Text
</a>
} else {
<span> @context.Text</span>
}
}

</Template>
</TelerikNotification> @code {
TelerikNotification NotificationReference { get; set; } protected override async Task OnAfterRenderAsync(bool firstRender)
{ if (firstRender)
{
ShowNotifications();
}
} void ShowNotifications()
{ // will use the default NotificationModel NotificationReference.Show( "plain notication", "tertiary" );

NotificationReference.Show( new MyExtendedNotificationModel()
{
Text="Completed tasks",
ThemeColor="secondary",
CustomID=2,
CustomUrl="[https://feedback.telerik.com/blazor?listMode=Popular&statusId=",](https://feedback.telerik.com/blazor?listMode=Popular&statusId=",)
CloseAfter=0 });

NotificationReference.Show( new MyExtendedNotificationModel()
{
Text="Tasks in development",
ThemeColor="primary",
CustomID=6,
CustomUrl="[https://feedback.telerik.com/blazor?listMode=Popular&statusId=",](https://feedback.telerik.com/blazor?listMode=Popular&statusId=",)
CloseAfter=0 });
} public class MyExtendedNotificationModel : NotificationModel
{ public int CustomID { get; set; } public string CustomUrl { get; set; }
}
} Regards, Dimo

### Response

**Chris** commented on 18 Nov 2021

Awesome. Thank you very much for the example. Exactly what I needed.
