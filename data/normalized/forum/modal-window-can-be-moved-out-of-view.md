# Modal window can be moved out of view

## Question

**Dou** asked on 09 Mar 2021

You can move a modal window past the bottom and out of view. At that point the only way to get back to it is to zoom out on the browser. Similarly, if you drag a window to the top, you can move it so high that the title bar is out of view. You can still see the bottom part of the window but even if you zoom out you can't get back to the title bar so the only thing you can do is to either escape out of the window or hope you have Ok/Cancel still visible. Is there a way to prevent this?

## Answer

**Marin Bratanov** answered on 10 Mar 2021

Hello Doug, I made the following enhancement idea on your behalf where you can Follow a built-in feature for this: [https://feedback.telerik.com/blazor/1510450-prevent-the-user-from-dragging-a-window-out-of-the-viewport.](https://feedback.telerik.com/blazor/1510450-prevent-the-user-from-dragging-a-window-out-of-the-viewport.) It also offers a solution you can start off from. Regards, Marin Bratanov Progress Telerik

### Response

**Doug** answered on 12 Mar 2021

Thanks Marin. Your solution works well for dragging windows above the top or below the bottom of the browser but where I'm having trouble is dragging it off the left. I have a modal TelerikWindow component in which I'm not setting the Width parameter as I want it to size based on the content (which it does nicely). But in the LeftChanged handler somehow I need to know what the width is so I can determine whether the entire window is off the left side of the browser (the right side is easy as the left value will be greater than the viewport width). I thought about assigning the TelerikWindow an Id intending to call JavaScript to get the width but alas, TelerikWindow doesn't expose an Id parameter. Any ideas on how to retrieve the width of a particlular TelerikWindow?

### Response

**Marin Bratanov** answered on 12 Mar 2021

Hi Doug, A Class can do. Or you can use some identifier from the content and go up the DOM until you reach the main element of the window. Regards, Marin Bratanov

### Response

**Doug** answered on 12 Mar 2021

How would you do that with a Class? Can you please elaborate a little more?

### Response

**Marin Bratanov** answered on 12 Mar 2021

Hello Doug, You can set the Class parameter of the Window and it renders in the DOM. So you can use document.querySelector(".the-window-class") to get the DOM element, just like you would with document.querySelector("#the-id-attribute") Regards, Marin Bratanov Progress Telerik

### Response

**Doug** answered on 12 Mar 2021

Oh, you mean reference the class name in the JavaScript. I'm with you now. Thanks.
