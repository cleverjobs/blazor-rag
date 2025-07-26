# Notification is overflowing beneath other items

## Question

**Ale** asked on 21 Feb 2022

Code <TelerikNotification @ref="NotificationComponent" HorizontalPosition="@NotificationHorizontalPosition.Center" VerticalPosition="@NotificationVerticalPosition.Top" /> The attached photo shows how the notification gets rendered. Please let me know how can I fix it, so that it either: Comes on top of all the other items. That's fine with me, since the user can just close it. Or, be limited to a certain size and let the user scroll.

## Answer

**Marin Bratanov** answered on 21 Feb 2022

Hello Alex, You likely need to set a suitable z-index to it: [https://docs.telerik.com/blazor-ui/components/notification/appearance#z-index](https://docs.telerik.com/blazor-ui/components/notification/appearance#z-index) You may also find useful this article on choosing a position that is not part of the built-in options: [https://docs.telerik.com/blazor-ui/knowledge-base/notification-custom-position](https://docs.telerik.com/blazor-ui/knowledge-base/notification-custom-position) Regards, Marin Bratanov Progress Telerik

### Response

**Alex** commented on 23 Feb 2022

Hello, Marin, Setting z-index to high value only works if position is set to relative, but if we do it using Class attribute, it gets overridden by the position attribute in the k-notification-group. I fixed it in the end by adding position: relative !important to the class.
