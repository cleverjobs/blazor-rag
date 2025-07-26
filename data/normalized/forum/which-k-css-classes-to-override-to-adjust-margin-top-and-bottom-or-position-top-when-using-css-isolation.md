# Which .k css classes to override to adjust margin top and bottom or position top when using css isolation?

## Question

**Jam** asked on 21 Sep 2021

How to know while viewing styles in Chrome Dev tools which .k style classes to need to be overridden for margins using CSS isolation. Also if using properties of the TelerikNotification HorizontalPosition set to center and VerticalPosition set to top what is needed to override the top position when using CSS isolation

## Answer

**Eric R | Senior Technical Support Engineer** answered on 23 Sep 2021

Hi Jamy, The best approach for this is to use the Class property and set the css as desired. For the Top property, the!important rule may be required as well. Let me review an example below. Example Using the following Notification markup and the demo-notification class, I can then set the top property to 500px !important. I am using an exaggerated value here to illustrate the implementation in the output. See the following markup and code block for reference. Markup <style>.demo-notification { position: absolute; top: 500px!important; }.demo-notification.k-notification { width: 420px;
} #demo-runner { height: 400px;
}.notification-parent { position: relative; height: 250px;
}.k-badge { margin-left: 5px;
}.k-notification-container { margin: 6px 0;
} </style> <div class="notification-parent"> <TelerikButton Icon="notification" Enabled="@NotificationButtonEnabled" OnClick="@ShowUnreadNotifications"> Show unread notifications <span class="k-badge k-badge-solid k-badge-primary k-badge-md k-badge-rectangle k-badge-inline"> 2 </span> </TelerikButton> <TelerikNotification @ref="@Notification" Class="demo-notification" VerticalPosition="NotificationVerticalPosition.Top" HorizontalPosition="NotificationHorizontalPosition.Center"> </TelerikNotification> </div> Code Block Below is the code block for running the sample locally. public TelerikNotification Notification { get; set; } public bool NotificationButtonEnabled { get; set; }=true; public async Task ShowUnreadNotifications ( ) { var closeDelay=3000000;

NotificationButtonEnabled=false;

Notification.Show( new NotificationModel()
{
Text="Checkout! What's new in Telerik UI for Blazor.",
ThemeColor=ThemeColors.Info,
CloseAfter=closeDelay
});

Notification.Show( new NotificationModel()
{
Text="Trial version of Telerik UI for Blazor expires tomorrow.",
ThemeColor=ThemeColors.Warning,
CloseAfter=closeDelay
}); await Task.Delay(closeDelay);

NotificationButtonEnabled=true;
} Output Here is the output. Wrapping Up For additional reference, I have attached the above example and included a video for editing the Top property of the demo-notification class in the DevTools as well. Please let me know if you need any additional information. Thank you. Regards, Author nickname Progress Telerik
