# Using the TelerikMenu component, is it possible to always keep the menu visible as long as the cursor is somewhere over the menu.

## Question

**Bra** asked on 06 Nov 2024

Hi I'm using the TelerikMenu component with multiple nested levels of menu items. When moving the cursor from inside a nested level, to a parent level that is not in the currently selected path, the menu disappears. View this example on REPL: [https://blazorrepl.telerik.com/mIvFOglY481u2hRG05](https://blazorrepl.telerik.com/mIvFOglY481u2hRG05) When moving the cursor from "Item A1 - 1" to "Item A2", the menu disappears. Because I have a large menu with multiple levels, it would improve user experience to keep the menu visible as long as the cursor hovers it. Is there any way to make this happen? Best regards Bram

## Answer

**Nadezhda Tacheva** answered on 08 Nov 2024

Hi Bram, If you want to easily browse through the various child items without the Menu disappearing, I recommend configuring the Menu, so it opens and closes on click instead of on mouse enter and leave. I've updated your sample to better showcase the idea: [https://blazorrepl.telerik.com/mIvFksFq30vuyq4e14.](https://blazorrepl.telerik.com/mIvFksFq30vuyq4e14.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Bram** commented on 12 Nov 2024

Hi Nadezhda This is not an option. Clicking an item needs to execute a different action, so if I configure the menu to open on click, that other action is lost. Best regards Bram

### Response

**Nadezhda Tacheva** commented on 13 Nov 2024

Hi Bram, I'm afraid that configuring the Menu to open and close on click is the only option to keep the child Menu open when moving the cursor from inside a nested level, to a parent level that is not in the currently selected path. By design, of the MouseLeave hide mode, the child Menu items will disappear when the mouse cursor leaves the child item group and their parent. Apart from that, even if you set the ShowOn and/or HideOn to "Click", the Menu will still fire its OnClick event, so you may perform your desired action.

### Response

**Bram** answered on 17 Feb 2025

This seems to be fixed in the latest release: Telerik UI for Blazor 8.0.0 (2025 Q1) I updated the REPL sample to 8.0.0 and the Menu now stays visible when hovering any item.
