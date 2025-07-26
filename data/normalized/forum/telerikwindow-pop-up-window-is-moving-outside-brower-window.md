# TelerikWindow pop-up window is moving outside brower window

## Question

**Vin** asked on 01 Jul 2022

Team, Currently I am using TelerikWindow (3.4.0) Pop-up window which is centered while opening, i see while dragging it is moving outside browser window attached screen-shot and causing to unable to close the window. Here i don't want to use CloseOnOverlayClick property. Tried with Left & Top Property along with LeftChanged or TopChanged but if i use Left/Top Window is not being Centered while window is loading. Attached test snippet code and need your assistance with sample code or inputs to avoid Pop-Window moving out of browser window (top/left/right/browser)

## Answer

**Svetoslav Dimitrov** answered on 06 Jul 2022

Hello Vinod, We have an open feature request for built-in boundary detection in multiple of our components (the Window included). I have added your Vote for it and I would encourage you to click on the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov

### Response

**Jon** commented on 09 Jan 2024

Hello Svetoslav, I looked at the linked feature request for this. Although it's similar, in my humble opinion, this request needs its own feature request. The Window can be "lost" by dragging or scrolling. If the Window is modal, this is quite an issue for the user. If the user drags a modal Window to where the title bar cannot be seen and then releases it there, they are stuck. If we set Draggable to false, it can still be scrolled out of view. Hopefully the user would realize what happened, but, you know, they're not always going to understand. Thanks, Jon

### Response

**Svetoslav Dimitrov** commented on 12 Jan 2024

Hello Jon, The built-in boundary detection will not allow users to drag the Window/Scroll it out of the viewport. This should solve the issue at hand here. I am curious as to what is your suggested approach to deal with this issue.
