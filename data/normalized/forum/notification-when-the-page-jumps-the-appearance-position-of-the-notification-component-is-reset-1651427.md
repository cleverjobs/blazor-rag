# [Notification] When the page jumps, the appearance position of the Notification component is reset.

## Question

**Jac** asked on 09 May 2024

Hi, When the page jumps, the appearance position of the Notification component is reset. Calling code: await AlertController.ShowSuccessNotification( "[Complete Work Task]:Success" );
NavigationController.Navigate( new WorkViewParam()); Controller code: public static class AlertController { private static Notification NotificationReference { get; set; } public static async Task ShowSuccessNotification ( string message="Success", int closeAfter=60000, object icon=null,AnimationType animationType=AnimationType.Fade,NotificationHorizontalPosition horizontalPosition=NotificationHorizontalPosition.Center, NotificationVerticalPosition verticalPosition=NotificationVerticalPosition.Top ) { if (NotificationReference !=null )
{
NotificationReference.Animation=animationType;
NotificationReference.HorizontalPosition=horizontalPosition;
NotificationReference.VerticalPosition=verticalPosition;
NotificationReference.Text=message;
NotificationReference.CloseAfter=closeAfter;
NotificationReference.Icon=icon; await NotificationReference.ShowSuccess();
}
} internal static void SetNotificationReference ( Notification notificationReference ) {
NotificationReference=notificationReference;
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
} protected override async Task OnInitializedAsync () { await base.OnInitializedAsync();
AlertController.SetNotificationReference( this );
}
}

### Response

**Jackson** commented on 10 May 2024

this is screen cut

### Response

**Hristian Stefanov** commented on 13 May 2024

Hi Jackson, Thank you for providing such detailed information on the scenario, including a screenshot. I have tried to reproduce the described issue within this REPL link by copying the Notification configuration from your message. As a result, the notification position persists as expected, no matter the action I'm performing inside the button that triggers it. As a next step, could you modify the above REPL sample to reproduce the issue and send it back to me for inspection? That will allow me to see the behavior firsthand and offer suitable solutions. I eagerly anticipate hearing back from you. Your cooperation is highly valued. Kind Regards, Hristian

### Response

**Jackson** commented on 14 May 2024

this issue only occurs in the local development and does not happen in the production environment. thank you for your answer.

## Answer

**Jackson** answered on 14 May 2024

this issue only occurs in the local development and does not happen in the production environment.

### Response

**Hristian Stefanov** commented on 14 May 2024

Hi Jackson, Thank you for updating me on the situation. I'm glad to hear that it works correctly in production. Kind Regards, Hristian
