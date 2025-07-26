# Will there be a MessageBox or a Toaster kind of notification

## Question

**SLSL** asked on 10 Jan 2020

I either need a Toaster to notify users of changes or even errors that automatically go away after a set time out. Will there be something like this in Blazor controls? If not do you have a general MessageBox modal dialog? Thanks.

## Answer

**Marin Bratanov** answered on 10 Jan 2020

Hi, You make one with the AnimationContainer at this very moment: [https://demos.telerik.com/blazor-ui/animationcontainer/notification.](https://demos.telerik.com/blazor-ui/animationcontainer/notification.) In fact, you can also use a Window component, as it is another popup (you just have to toggle its Visible parameter, like shown here: [https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly](https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly) ). You may also want to Vote for and Follow the implementation of a richer component for notifications: [https://feedback.telerik.com/blazor/1425097-notification-controls.](https://feedback.telerik.com/blazor/1425097-notification-controls.) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 10 Jan 2020

By the way, here is also another example of making a message box (it is a little different than a "toast" type of notification, but may be useful nonetheless): [https://github.com/telerik/blazor-ui/tree/master/common/message-box](https://github.com/telerik/blazor-ui/tree/master/common/message-box)

### Response

**SL** answered on 10 Jan 2020

Thank you.
