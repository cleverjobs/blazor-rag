# Why such a bad implementation?

## Question

**Mar** asked on 22 Apr 2021

Please take a look at [https://github.com/Blazored/Toast](https://github.com/Blazored/Toast) this is how a toast should be implemented with default methods for ShowInfo ShowSuccess,,ShowWarning and ShowError Radzen and many other also have a similar implementation. Please be inspired and give us similar functionality in a upcoming release

## Answer

**Martin** answered on 22 Apr 2021

I created some extension methods to make live easier using Telerik.Blazor; namespace EmployeeTrading.Client.Pages { using Telerik.Blazor.Components; namespace OneNotificationPerApp.Shared { public class Notification { // set by blazor at runtime @ref component public TelerikNotification Instance { get; set; } public void Info( string msg) { var m=new NotificationModel { Text=msg, ThemeColor=ThemeColors.Info, Icon="info-circle", CloseAfter=5000 }; Instance.Show(m); } public void Success( string msg) { var m=new NotificationModel { Text=msg, ThemeColor=ThemeColors.Success, Icon="check-outline", CloseAfter=5000 }; Instance.Show(m); } public void Warning( string msg) { var m=new NotificationModel { Text=msg, ThemeColor=ThemeColors.Warning, Icon="exclamation-circle", CloseAfter=5000 }; Instance.Show(m); } public void Error( string msg) { var m=new NotificationModel { Text=msg, ThemeColor=ThemeColors.Error, Icon="x-outline", CloseAfter=0 }; Instance.Show(m); } } } } /*** Notification ***/ .bi-notification .k- icon { width: 2em; height: 2em; font-size: 32px; } .bi-notification .k-notification-content { font-size: large; align-self: center; } How to use if ( string.IsNullOrEmpty(filename)) { Notification.Error( "Failed to upload the attachment" ); } else { Notification.Success( "Attachment uploaded" ); }

### Response

**Hristian Stefanov** answered on 26 Apr 2021

Hello Martin, Great suggestions from you. Your feedback helped us a lot to improve our documentation. We now have examples there for implementing these common notification types. We have made changes to the Notification documentation, and you can follow them to see the difference here. Also, you can see the live preview of the page here: [https://github.com/telerik/blazor-docs/blob/master/components/notification/overview.md#success-info-warning-error-notifications.](https://github.com/telerik/blazor-docs/blob/master/components/notification/overview.md#success-info-warning-error-notifications.) It will be live with our next upload. We have chosen not to add explicit .Error(), .Info(), .Success() and .Warning() methods because our notifications have several additional settings, and combining all of them would make the API cumbersome. Nevertheless, making a facade like you have done is a perfectly valid approach for your project. If you have any other questions or cases, feel free to give us feedback again. Regards, Hristian Stefanov
