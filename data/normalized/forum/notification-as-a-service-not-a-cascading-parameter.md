# Notification as a service not a cascading parameter

## Question

**Mar** asked on 31 Aug 2021

Is there an example where the TelerikNotification component is used more like a service, similar to the MessageBox callback example? I would like to be able to raise notifications from my view models and not have to either raise an event for the view to handle, or pass the TelerikNotification instance down to the view model. thanks -marc

## Answer

**Marc Simkin** answered on 31 Aug 2021

Nevermind. Below is what I was able to put together. This will allow for the notifications to be raised from anywhere in the code, since the notification service can be injected into any object. NotificationService.cs using System; using Telerik.Blazor; using Telerik.Blazor.Components; namespace Demo.Controls.Notification { public class NotificationService { public event Action<NotificationModel> OnShowNotification; public void Info ( string msg, int closeAfter=5000 ) {
OnShowNotification?.Invoke( new NotificationModel
{
Text=msg,
ThemeColor=ThemeColors.Info,
Icon="info-circle",
CloseAfter=closeAfter
});
} public void Success ( string msg, int closeAfter=5000 ) {
OnShowNotification?.Invoke( new NotificationModel
{
Text=msg,
ThemeColor=ThemeColors.Success,
Icon="check-outline",
CloseAfter=closeAfter
});
} public void Warning ( string msg, int closeAfter=5000 ) {
OnShowNotification?.Invoke( new NotificationModel
{
Text=msg,
ThemeColor=ThemeColors.Warning,
Icon="exclamation-circle",
CloseAfter=closeAfter
});
} public void Error ( string msg, int closeAfter=5000 ) {
OnShowNotification?.Invoke( new NotificationModel
{
Text=msg,
ThemeColor=ThemeColors.Error,
Icon="x-outline",
CloseAfter=closeAfter
});
}
}
} NotificationContainer.razor <TelerikNotification @ref="_notification" HorizontalPosition="NotificationHorizontalPosition.Right" VerticalPosition="NotificationVerticalPosition.Top" Class="big-notification"> <Template> @RawText(Message) </Template> </TelerikNotification> NotificationContainer.razor.cs using Microsoft.AspNetCore.Components; using Telerik.Blazor.Components; namespace Demo.Controls.Notification { public partial class NotificationContainer { # region Services [ Inject ] public NotificationService NotificationService { get; set; } # endregion Services protected override void OnInitialized ( ) {
NotificationService.OnShowNotification +=(NotificationModel notificationModel)=>
{
InvokeAsync(()=>
{
Message=notificationModel.Text;

_notification.Show(notificationModel);
});
};
} private MarkupString RawText ( string text ) { return new MarkupString(text);
} # region Properties public string Message { get; set; } private TelerikNotification _notification { get; set; } # endregion Properties }
} Someplace in your application, maybe MainLayout.razor add the <NotificationContainer> component. Then register the NotificationService with DI in the Startup.cs. It needs to be registered ServiceLifetime.Scoped.

### Response

**Hristian Stefanov** answered on 03 Sep 2021

Hi Marc, Great job! This seems like a good sample project for our public blazor-ui GitHub repository. You can go and create a pull request there. Making public such an example can be very beneficial for other interested developers. As a small gesture of gratitude, I added Telerik points to your account. Regards, Hristian Stefanov Progress Telerik
