# open menu

## Question

**kha** asked on 12 Jul 2020

Hello i was looking for a way to keep menu open if its clicked not like staying open as long as its hovered i need it to stay open as long as its focused

## Answer

**Marin Bratanov** answered on 13 Jul 2020

Hi Khashayar, If the menu does not get disposed when you navigate to a new page (that is, it is outside of the @Body), it will not close. I am attaching our CRUD project template here, modified to nest the pages in a child menu, and a short video that demonstrates this behavior. Regards, Marin Bratanov

### Response

**khashayar** answered on 14 Jul 2020

thank you marin this is exactly how my menu works but my issue is menu gets opened when its hovered and if you stop hovering it gets closed what i want is that when i click on it, it should be open and doesnt matter if its hovered or not like the popup of drop down when you click on arrow it gets open and when dropdown looses focus popup gets closed

### Response

**Marin Bratanov** answered on 14 Jul 2020

Hi, I made this page where you can Follow the implementation of such a feature: [https://feedback.telerik.com/blazor/1476204-hide-event-for-the-menu-not-hide-on-mouseout](https://feedback.telerik.com/blazor/1476204-hide-event-for-the-menu-not-hide-on-mouseout) Regards, Marin Bratanov
