# Is it possible to use a Drawer Component to display an edit form (or other content)?

## Question

**Jes** asked on 02 Jun 2021

I am attempting to use a drawer component to slide in from the right and present the user with a form to edit various items from a grid. Is there a way to display content (form, text, etc) in a drawer other than menu-type items? Thanks, Jesse

## Answer

**Dimo** answered on 04 Jun 2021

Hi Jesse, Theoretically, it is possible to place a custom Grid edit form inside a Drawer via its ItemTemplate. However, the component is designed to be used in a different way and side effects will occur: the edit form will inherit flexbox Drawer styles which can break its layout the Drawer is designed to collapse as soon as you click anywhere on the fly-out portion, because it is assumed that navigation will occur Isn't the built-in Grid popup editing a feasible option for you? Regards, Dimo

### Response

**Jesse** answered on 04 Jun 2021

Hi, Dimo. Thanks for your reply. I don't think the grid popup editing feature will work; fields not in the grid need editing, and some fields require complex controls. E.g., combo box, switch, etc. The slide-in pane for editing also is a style used in related sites (using other technologies.) It sounds like the drawer will be problematic due to it being designed for another purpose. I've tried using an animation container, and I can get close to the behavior I want. However, if the browser is resized while the container is visible, it does not stay anchored to the right side of the window. Can you offer any guidance here? Thank you, Jesse

### Response

**Dimo** commented on 08 Jun 2021

It is possible to configure the AnimationContainer in such a way, so that it moves or resizes together with the browser window. Just use dynamic size and position CSS values, for example: <TelerikAnimationContainer @ref="@AnimationContainer" Top="50px" Left="calc(100vw - 350px)" Width="300px" Height="300px" AnimationType="@AnimationType.SlideLeft"> More information on calc() is available at: [https://developer.mozilla.org/en-US/docs/Web/CSS/calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/calc()) For a JS-based alternative, also check [https://www.telerik.com/forums/is-it-possible-to-animate-a-blazor-animationcontainer-to-that-is-appears-to-slide-in-from-the-right-hand-side-of-the-browser-window](https://www.telerik.com/forums/is-it-possible-to-animate-a-blazor-animationcontainer-to-that-is-appears-to-slide-in-from-the-right-hand-side-of-the-browser-window)
