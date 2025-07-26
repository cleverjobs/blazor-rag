# Showing Notification only to first visit to page?

## Question

**Jst** asked on 13 Jul 2021

I would like to only display a notification the first time a user visits a page. When the notification is closed I would like to set a Boolean value in local storage that I can check before displaying the notifications again. Is there a mechanism or event for the Notifications that would assist me in doing this? I've read thru the examples and Docs but have not found anything.

## Answer

**Dimo** answered on 16 Jul 2021

Hello John, Indeed, the Notification component does not expose events at this point. If you require to set the boolean flag only after the user closes the popup, you can use a Window with an OnClick handler for its Close action. Alternatively, you can show the notification just once, make it bigger and more prominent (even position it at the center of the screen ), and assume the user has seen it. Regards, Dimo
