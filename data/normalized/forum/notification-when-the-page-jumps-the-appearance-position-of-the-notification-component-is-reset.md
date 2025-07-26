# [Notification] When the page jumps, the appearance position of the Notification component is reset.

## Question

**Jac** asked on 09 May 2024

Hi, When the page jumps, the appearance position of the Notification component is reset. My project code: public static async Task ShowSuccessNotification ( string message="Success", int closeAfter=60000, object icon=null,AnimationType animationType=AnimationType.Fade,NotificationHorizontalPosition horizontalPosition=NotificationHorizontalPosition.Center, NotificationVerticalPosition verticalPosition=NotificationVerticalPosition.Top ) { if (NotificationReference !=null )
{
NotificationReference.Animation=animationType;
NotificationReference.HorizontalPosition=horizontalPosition;
NotificationReference.VerticalPosition=verticalPosition;
NotificationReference.Text=message;
NotificationReference.CloseAfter=closeAfter;
NotificationReference.Icon=icon; await NotificationReference.ShowSuccess();
}
} Notification Component Code(.razor): @using Telerik.Blazor
@using Telerik.Blazor.Components

<style>
.custom-notification-parent {
position: fixed;
left: 50 %;
top: 20 px;
transform: translateX( -50 %);
z-index: 99999999;
}

.custom-positioned-notifications {
position: relative;
flex-wrap: nowrap !important;
}

.k-notification {
box-shadow: var (--kendo-elevation -4, 0 8 px 10 px rgba ( 0, 0, 0, 0.12 ), 0 4px 16px rgba ( 0, 0, 0, 0.12 ));
font-size: 16 px;
}
</style>

<div class="custom-notification-parent">
<TelerikNotification @ref="@notification" AnimationType="@Animation" Class="custom-positioned-notifications" VerticalPosition="@VerticalPosition" HorizontalPosition="@HorizontalPosition">
</TelerikNotification>
</div>

@code {

} Notification Component Code(.razor.cs): public partial class Notification { private TelerikNotification notification { get; set; } public NotificationHorizontalPosition HorizontalPosition { get; set; }=NotificationHorizontalPosition.Center; public NotificationVerticalPosition VerticalPosition { get; set; }=NotificationVerticalPosition.Top; public AnimationType Animation { get; set; } public string Text { get; set; } public int CloseAfter { get; set; } public object Icon { get; set; }=null; public async Task ShowSuccess () {
notification.Show( new NotificationModel
{
Text=Text,
ThemeColor=ThemeConstants.Notification.ThemeColor.Success,
CloseAfter=CloseAfter,
Icon=Icon
});
} public async Task ShowError () {
notification.Show( new NotificationModel
{
Text=Text,
ThemeColor=ThemeConstants.Notification.ThemeColor.Error,
CloseAfter=CloseAfter,
Icon=Icon
});
} public async Task ShowWarning () {
notification.Show( new NotificationModel
{
Text=Text,
ThemeColor=ThemeConstants.Notification.ThemeColor.Warning,
CloseAfter=CloseAfter,
Icon=Icon
});
} public async Task ShowInfo () {
notification.Show( new NotificationModel
{
Text=Text,
ThemeColor=ThemeConstants.Notification.ThemeColor.Info,
CloseAfter=CloseAfter,
Icon=Icon
});
} protected override async Task OnInitializedAsync () { await base.OnInitializedAsync();
AlertController.SetNotificationReference( this );
}
} Calling code: try
{
var response=await CoreDataSource.Request(bulkRequest);

await AlertController.ShowSuccessNotification("[Complete Work Task]:Success");
NavigationController.Navigate(new WorkViewParam());
}
catch (Exception e)
{
await AlertController.ShowWarningNotification("[Complete Work Task]:" + e.Message);
}

### Response

**Hristian Stefanov** commented on 13 May 2024

Hi Jackson, This public post is a duplicate of this one: [https://www.telerik.com/forums/notification-when-the-page-jumps-the-appearance-position-of-the-notification-component-is-reset-1651427.](https://www.telerik.com/forums/notification-when-the-page-jumps-the-appearance-position-of-the-notification-component-is-reset-1651427.) Let's continue the conversation there to keep everything in one place. Kind Regards, Hristian
