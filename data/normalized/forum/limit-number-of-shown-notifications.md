# Limit number of shown notifications

## Question

**Ton** asked on 22 Nov 2022

If I have multiple incoming notifications, how do I limit the number that are visible ? Is there a property to set or is there a way I can programmatically remove certain toasts? Thank you

## Answer

**Svetoslav Dimitrov** answered on 25 Nov 2022

Hello Tony, You can introduce a counter in your application and increase its value in the method that calls the notifications. I have prepared a basic example of the concept and you can use it as a base for your application. <TelerikButton OnClick="@AddNotification">Add a basic notification</TelerikButton>

<TelerikNotification @ref="@NotificationReference" Class="MyTelerikNotification"></TelerikNotification>

@code { public TelerikNotification NotificationReference { get; set; } public int NotificationCount=0; public void AddNotification ( ) { NotificationCount++; if (NotificationCount <=5 ) {
NotificationReference.Show( new NotificationModel()
{
Text="Auto Closable Notification",
ThemeColor=ThemeConstants.Notification.ThemeColor.Primary
});
}
}
}

<style>
.MyTelerikNotification .k-notification-container .k-notification-wrap {
width: 300 px;
height: 50 px;
font-size: 1.5 em;
text-align: center;
align-items: center;
}
</style> Regards, Svetoslav Dimitrov

### Response

**Tony** commented on 28 Nov 2022

Hello, Thank you for the suggestions on my previous question. The scenario that I am looking to solve is if there are more than 5 notifications, show only the latest 5. I currently am trying to add incoming notifications to a collection and then only show the last five. When the following code runs: I get the following error: I there a way I can set different Key values? Thanks, Tony

### Response

**Svetoslav Dimitrov** commented on 01 Dec 2022

Hello Tony, To be really honest I am not sure why this exception is thrown. I modified my previous snippet so that it takes the last 5 notifications. Snippet workflow: Click the Add a basic notification button. It will populate a collection of NotificaionModel with 25 notifications. Click the Show Notifications button. It will reverse the collection of notifications and render only the last 5 Can you compare the snippet against your own and see if any differences are causing the issue? If this does not help you move forward, can you modify the snippet and send it back to me for further investigation? <TelerikButton OnClick="@AddNotification">Add a basic notification</TelerikButton>

<TelerikButton OnClick="@ShowNotifications">Show Notifications</TelerikButton>

<TelerikNotification @ref="@NotificationReference" Class="MyTelerikNotification"></TelerikNotification>

@code { public TelerikNotification NotificationReference { get; set; } public int NotificationCount=0; public List<NotificationModel> NotificationsContainer { get; set; }=new (); public void AddNotification ( ) { for ( int i=0; i <=25; i++)
{
NotificationsContainer.Add( new NotificationModel()
{
Text=$"Auto Closable Notification {i} ",
ThemeColor=ThemeConstants.Notification.ThemeColor.Primary
});
}
} private void ShowNotifications ( ) { var reversedNotifications=NotificationsContainer.Reverse<NotificationModel>().Take( 5 ); //take last 5 notifications foreach ( var notification in reversedNotifications)
{
NotificationReference.Show(notification);
}
}
}

<style>
.MyTelerikNotification .k-notification-container .k-notification-wrap {
width: 300 px;
height: 50 px;
font-size: 1.5 em;
text-align: center;
align-items: center;
}
</style>

### Response

**Marcus** commented on 13 Jan 2025

Hello Tony, hello Svetoslav, the reason for the error seems to be the following: If you implement a kind of queue for your notifications, trigger the show event for each notification in the queue on a new enqueue event and one (or more) existing notifications are already shown, then the error is raised because the telerik notification tries to reredner an already shown notification with the same key. To avoid this you have to call NotificationReference.HideAll(); before showing all notifications in a loop again. Regards Marcus
