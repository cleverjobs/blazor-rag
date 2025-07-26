# Add overlay side panel: what's the best component? Drawer has issue

## Question

**Cla** asked on 18 Dec 2024

Hi, my application layout has 2 default drawer (left one as Push and Right one as Overlay). To handle this layout i used the suggestion on: [https://www.telerik.com/forums/nested-drawer-for-menu-on-left-and-right](https://www.telerik.com/forums/nested-drawer-for-menu-on-left-and-right) The application is managed with this gerarchy: - Right drawer - Left drawer inside right drawer content - Application components inside Left drawer content Now i need a side panel inside of some application compoents: note who i don't need menu items, but only a side panel with a custom component on it, but i have not found a telerik component to handle it. There is a telerik component to handle an overlay side panel (other than TelerikDrawer)? I tried to add another TelerikDrawer with a custom template, but is seem not working. Adding a Drawer in one of my application components result in unexpected behaviour: the left drawer is rendered on the right side of the screen. Any suggestion? thanks

## Answer

**Dimo** answered on 20 Dec 2024

Hi Claudio, We are currently working on a Dock Manager component, which may be suitable for the complex layout with multiple overlay panels that you described. On the other hand, you can consider some other Telerik Blazor popup components if you think they can serve your purpose, for example, Popover or Popup. Regards, Dimo Progress Telerik
