# Is it possible to trigger Window Maximize/Minimize actions from code?

## Question

**Ale** asked on 31 Mar 2022

For example, when the user clicks on a button inside (or outside) the Window, I maximize or minimize the Window. Something like window.Maximize(); The specific use case here is when the user loads data, I want to automatically maximize the Window for them. It is difficult for the user to find the maximize button because the window width becomes greater than the browser window and they have to drag the window to find the maximize button and click it.

## Answer

**Alex** answered on 31 Mar 2022

I found out its possible to do by using the WindowState [https://docs.telerik.com/blazor-ui/components/window/size#maximize-and-minimize](https://docs.telerik.com/blazor-ui/components/window/size#maximize-and-minimize)
