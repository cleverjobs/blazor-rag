# Hide on click outside

## Question

**qwqw** asked on 29 Jan 2021

It is possible to hide AnimationContainer on click outside of it?

## Answer

**Marin Bratanov** answered on 29 Jan 2021

Hello, This is a feature we might implement for the Window, you can Vote for it and Follow it here if you find it useful: [https://feedback.telerik.com/blazor/1451714-window-modal-click-on-overlay-to-close.](https://feedback.telerik.com/blazor/1451714-window-modal-click-on-overlay-to-close.) For the animation container - you can add your own overlay to handle the click event (or handle it otherwise, e.g., with JS) in order to hide the animation container. You can find a similar example in this thread (see my post from 18 Aug 2020, just add the desired click handler to call the Cancel method in this sample). Regards, Marin Bratanov
