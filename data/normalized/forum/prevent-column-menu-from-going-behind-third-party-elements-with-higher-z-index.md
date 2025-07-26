# Prevent column menu from going behind third party elements with higher z-index.

## Question

**Stu** asked on 01 Jul 2024

The Telerik animation containers get placed on the body using position:absolute and have a z-index that is set based on other animation containers. ( [https://feedback.telerik.com/blazor/1548718-showing-the-context-menu-via-its-api-method-does-not-set-its-z-index?_](https://feedback.telerik.com/blazor/1548718-showing-the-context-menu-via-its-api-method-does-not-set-its-z-index?_) ) So they seem to get set to be a value like 2. I am using a ui framework that has some elements on the body with z-indexes> 1000. Eg a side menu. I am using the Telerik grid. The column menu's use the animation container, and because the animation containers get placed directly on the body with a z-index of 2, they always appear behind this side menu. I do not want to set a blanket CSS rule like `.k-animation-container { z-index: 2000 !important; }` because it will break any other behaviour that Telerik animation containers have. When i don't use `!important`, eg like here ( [https://feedback.telerik.com/blazor/1514877-css-class-does-not-render-on-the-topmost-element](https://feedback.telerik.com/blazor/1514877-css-class-does-not-render-on-the-topmost-element) ) the inline style overrides it anyway. Could this be solved by any of these: 1. Set a default z-index value for animation containers, and have all subsequent animation containers base themselves off of that value? Eg a config setting, or a CSS variable, or a dummy animation container being placed into the dom with a set z-index value so that all others are based on it Or, 2. A parameter as part of the grid column menu that lets me pass an extra class to the animation container, I can then use this class to specifically set the z-index for only column menu instances of the animation container.

## Answer

**Nadezhda Tacheva** answered on 03 Jul 2024

Hi Stuart, Thank you for the detailed explanation about the issue you are facing! The second option seems more optimal to me as it will allow one to specify their preferred z-index plus it will open the door for other potential visual customizations of the menu. I opened a feature request on your behalf: Allow setting CSS class to the topmost element of the Column Menu. I already added your vote there and as a creator, you are automatically subscribed to get email status updates. Regards, Nadezhda Tacheva Progress Telerik
