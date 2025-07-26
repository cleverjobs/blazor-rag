# Can the second level of a context menu ever pop up instead of down?

## Question

**Ste** asked on 30 Mar 2022

The second level of Context Menu never pops up, always down, even if there is no space to do so. It seems like the first level will pop up if there isn't enough room below the menu to show the items. However, the second level always appears below the menu that was expanded. Demo here: [https://demos.telerik.com/blazor-ui/contextmenu/overview](https://demos.telerik.com/blazor-ui/contextmenu/overview) Make your window not very tall, so the "clickable" part (that says "Right-click to open Context menu" is barely visible at the bottom of the screen"). Then right-click; and hover over "Style". The sub menu appears below the word "Style", and is cut off by the bottom of the window. It should know that there is no space down there, and pop "up". What can I do to fix this? Thanks!

## Answer

**Dimo** answered on 04 Apr 2022

Hello Steve, The ContextMenu and Menu will address such scenarios when we introduce screen boundary detection for these components. I recommend following these two items on our
