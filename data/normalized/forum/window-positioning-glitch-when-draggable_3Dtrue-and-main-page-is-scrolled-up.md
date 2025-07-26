# Window positioning glitch when Draggable=true and main page is scrolled up

## Question

**Jef** asked on 09 Mar 2021

I'm noticing that the window will shift down when I click on the window title (e.g. when I want to move the window). It only happens if I have scrolled my main page up. As a matter of fact, the window will shift down exactly the same distance that I've scrolled my main page. The shifting will occur repeatedly as well. Each time I click on the window title, it shifts down until it's completely disappeared. At that point I'm stuck because I can't close the window. Looks like the calculation that is computing the top coordinate of the window isn't correctly accommodating the scroll position of the main page.

## Answer

**Nadezhda Tacheva** answered on 12 Mar 2021

Hi Jeffrey, In the attached project you will find a simple example that I made in order to test the Window, however I was not able to reproduce the described behavior - no issues appear when dragging and closing the Window regardless of the position of the main page (see the video attached). The example covers two scenarios - there are buttons to toggle the window from the top and the bottom of the page but still no issues in dragging and closing the Window in both cases. Could you run that project locally and see how it works for you? Then you can compare it against your project to see if any differences cause the described behavior. If this doesn't help, could you modify the project I sent to reproduce the issue, so we can investigate further and provide a solution? Regards, Nadezhda Tacheva Progress Telerik

### Response

**Don** commented on 29 Apr 2021

I am also seeing this issue. (or at least similar) Whenever I make my Window component Draggable and I drag it partially off the bottom of my screen, click away from the window, then click the window header it centers my view on the window vertically and shifts the entire web page behind it. It is a rather jarring experience but the behind view is shifted back to the correct position once the window is dragged back towards the top of the screen.

### Response

**Marin Bratanov** commented on 30 Apr 2021

Hi Don, I have posted an answer at the root level of this thread that might be useful to you: [https://www.telerik.com/forums/window-positioning-glitch-when-draggable%3Dtrue-and-main-page-is-scrolled-up#5302832](https://www.telerik.com/forums/window-positioning-glitch-when-draggable%3Dtrue-and-main-page-is-scrolled-up#5302832) If this is not the scenario you have, I recommend opening a new thread or ticket to discuss the particular case you have so we can keep each thread concise so it can deal with one problem - from the OP.

### Response

**Marin Bratanov** answered on 30 Apr 2021

Hi all, This also targets Don's comment from 30 April 2021. Clicking outside of the window will focus the element that you just clicked. Clicking again in the window will focus the window element (its main <div> element, in the common case). Browsers tend to bring into view (which include scrolling) focusable elements, and so the expected behavior is that the browser will try to scroll the page to make the entire window visible. The catch here is that the element that actually can have a scrollbar can vary greatly from one layout to the other and the browser may have a hard time doing that scrolling. I am attaching here a short video from our demos that shows this expected behavior as a reference point in case it helps someone else. At this point I am not sure if this is the behavior and issue Jeffrey observed in the opener post, so I am adding this information here for anyone who might find it useful. Regards, Marin Bratanov

### Response

**Don** commented on 30 Apr 2021

So that is expected behavior? In my use case the background page is not scrollable and when the browser brings the window back into view, the positioned background gets shifted up until the window is in view. You can kind of reproduce this behavior on the Draggable Demo ([https://demos.telerik.com/blazor-ui/window/draggable)](https://demos.telerik.com/blazor-ui/window/draggable)) by dragging the window to the bottom of the section it is in off of the screen, click to bring focus away from it, and re focus the window it will shift the page content up with the scroll bar. This isn't as big of a deal if the element behind it is scrollable.

### Response

**Marin Bratanov** commented on 30 Apr 2021

That behavior is expected, indeed, because it is the browser that does it and we can't avoid it - the window must be focusable for accessibility reasons. The same behavior is visible in the video I attached above. What could alleviate this would be a feature that prevents the user from dragging the window out of the viewport in the first place: [https://feedback.telerik.com/blazor/1510450-prevent-the-user-from-dragging-a-window-out-of-the-viewport.](https://feedback.telerik.com/blazor/1510450-prevent-the-user-from-dragging-a-window-out-of-the-viewport.) If you think this would suit your needs, Vote for it and Follow it. You can also try the workaround it offers.
