# Notification Position

## Question

**Eri** asked on 25 Oct 2022

I have a notification component defined on my MasterLayout page like below. and then shared with all my other pages via a cascading parameter. <TelerikNotification @ref="@NotificationReference" AnimationType="@AnimationType.ZoomOut" Class="notification" HorizontalPosition="NotificationHorizontalPosition.Center" VerticalPosition="NotificationVerticalPosition.Top" /> Everything works fine, but I am noticing that if i am scrolled down on a child page, the notification stays at the top of the page (off the visible screen) instead of being relative to the top of the window. How can i make sure the notification is always visible to the end users regardless of how far down a page they might be scrolled too? Thanks in advance,

## Answer

**Eric** answered on 25 Oct 2022

I had some extra CSS in my style sheet that was causing the problem. Without it, the default behavior is what I expected.
