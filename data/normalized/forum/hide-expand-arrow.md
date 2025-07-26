# Hide Expand Arrow

## Question

**EliEli** asked on 14 May 2020

Is there a way to hide the expand arrow on just the top level items? They do have children. A second option would be suggestion on how to expand a background to include the arrow, so it is not off to the side without effecting sub items. Picture attached with icon off to side. I echo the need to apply custom styling up higher in the element like this thread references would be helpful as well. [https://www.telerik.com/forums/styling-issue](https://www.telerik.com/forums/styling-issue) Thank you.

## Answer

**Svetoslav Dimitrov** answered on 15 May 2020

Hello Eli, There are two possible approaches to handle this: Use a CSS selector that targets the <span> element that has the icon (k-menu-expand-arrow) and set the display attribute to none. Below, you can see a code snippet to illustrate the CSS rule. You could remove them by using a JavaScript function, because Blazor, as a framework, has some limitations regarding DOM manipulations. Basically what I did was to select the <span> items that contain the arrow down icon and used element.classList.remove() to remove the icon. As attached file you can see a demo project I built to showcase the things I explained above. <style>.k-menu-expand-arrow { display: none;
}
</style> Regards, Svetoslav Dimitrov
