# Gantt Tree and Timeline Height/Scroll Out of Sync

## Question

**Mat** asked on 15 Aug 2023

I have a Blazor server application that is displaying a Gantt control. For several of my users with smaller screen sizes they have noticed that the Tree and Timeline can get out of sync vertically. When scrolling the Tree stops and the Timeline keeps going: I have also observed that resizing the browser window can result in differences in height of the Tree and Timeline:

## Answer

**Svetoslav Dimitrov** answered on 18 Aug 2023

Hello Matt, It seems that you have stumbled upon the TreeList in a Gantt with 100% height that cannot dynamically get resized to fit its parent container. Can you try the workaround from the public item to see if this resolves the issue? If you are facing the same bug, I can encourage you to click the Vote and Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik
