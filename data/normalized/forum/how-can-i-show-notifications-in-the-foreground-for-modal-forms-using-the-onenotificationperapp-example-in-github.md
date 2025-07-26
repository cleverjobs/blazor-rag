# How can I show notifications in the foreground for modal forms using the "OneNotificationPerApp" example in Github?

## Question

**Geo** asked on 21 Dec 2022

Using the approach in the example code of "OneNotificationPerApp" works great for non-modal forms. However, modal forms that use this approach do show the notfication but its in the background, not easily visible. Is there a way to change that? I tried chaning the z order to a high number but that didn't work. Any suggestions would be great. Thanks in advance! Let me know if you need to see the code and I can zip it up and attach it. [https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app](https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app)

## Answer

**Dimo** answered on 26 Dec 2022

Hello George, I tested the GitHub project with a modal Dialog. The default z-index of its modal overlay is a little over 10,000. So I increased the Notification z-index: MainLayout.razor div.big-notification { z-index: 12345;
} As a result, the notifications displayed in the foreground as expected. Here are all changes I made. Is there anything else different in your case? Index.razor <OneNotificationPerApp.Components.FirstComponent></OneNotificationPerApp.Components.FirstComponent> <h3> Index Page </h3> <button @onclick="@ShowNotification"> Show Notification from Index Page </button> <TelerikButton OnClick="@ShowModal"> Show Modal Dialog </TelerikButton> <TelerikDialog Visible="@DialogVisible"> <DialogTitle> Modal Dialog </DialogTitle> <DialogContent> I am a modal dialog. <button @onclick="@ShowNotification"> Show Notification from Index Page </button> </DialogContent> </TelerikDialog> @code {
[CascadingParameter] protected Notification Notification { get; set; } bool DialogVisible { get; set; } async Task ShowModal ( ) {
DialogVisible=true;
} void ShowNotification ( ) {
Notification.Instance.Show( new NotificationModel ( ) {
Text="From Index Page. Go to the Counter Page and try the button there too",
ThemeColor=ThemeConstants.Notification.ThemeColor.Success,
CloseAfter=0,
Closable=true });
}
} Regards, Dimo

### Response

**George** commented on 29 Dec 2022

Increasing the z index over 10K worked, thanks!
