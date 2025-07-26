# Window is blurry

## Question

**kha** asked on 17 Aug 2020

Hello, i found a very strange problem with all of windows that i have used (around 10 ) and they all are blurry and when i change their position it get's fixed

## Answer

**Svetoslav Dimitrov** answered on 17 Aug 2020

Hello Khashayar, Could you replicate the issue on our demos? As attached file I have created demo application which has a Telerik Window. You could change its top and left position through numeric input and center it. Could you make some changes so we can investigate what changes of the position would make the Window blurry? Regards, Svetoslav Dimitrov

### Response

**James** commented on 03 Aug 2021

I am also experiencing blurriness blurred in normal view not blurred in full screen mode: Any idea when we could expect a fix or someone to look into this?

### Response

**Svetoslav Dimitrov** answered on 06 Aug 2021

Hello James, This issue seems to stem from the Chrome browser if the component has odd values for the Width and Height of the component. Below, I will provide some additional information on the case. There is a problem with the fixed positioning of the window in a combination with the transform(-50%, -50%) CSS property and if the height of the window. If this specific style combination is present, the transformed element is blurred in chrome because the 50% calculation on an odd height/width results in half pixels computations. A solution for the demo would be to set a default height and width (even values). Regards, Svetoslav Dimitrov Progress Telerik
