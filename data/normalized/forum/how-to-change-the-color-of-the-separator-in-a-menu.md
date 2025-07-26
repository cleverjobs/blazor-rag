# How to change the color of the separator in a menu

## Question

**Kev** asked on 23 Aug 2023

I have a menu I'd like to override the default style and am able to change the color of the text for the menu item but the separator between each text item doesn't change. How can I change the color of the separator.

## Answer

**Georgi** answered on 25 Aug 2023

Hi, Kevin, You can change separator color with CSS e.g: .k-menu-vertical>.k-separator { border-color: red;
} Note that this will change the separators for all vertical menus. If you prefer to change only a specific menu, create a custom CSS class selector: . customSeparator.k-menu-vertical>.k-separator { border-color: red;
} Then, set the class property of the chosen Menu: <TelerikContextMenu Class=" customSeparator " Data="@ContextMenuItems" Selector=".menuTarget" TextField="@nameof(ContextMenuItem.Section)" SeparatorField="@nameof(ContextMenuItem.IsItemSeparator)"> </TelerikContextMenu> Let me know if you need additional help. Kind Regards, Georgi Progress Telerik

### Response

**Kevin** commented on 11 Sep 2023

Thank you for your reply, Georgi. I used the information from your post and was able to successfully change the color of the separator on a test page but in my application it does not work. The separators are not displaying but I can highlight them as if they are there. Could this be a visibility issue? Could the theme I'm using be setting the separator to not visible? I appreciate your help!

### Response

**Georgi** commented on 14 Sep 2023

Hi, Kevin, This can be caused by CSS isolation, a .NET feature which scopes styles to specific Razor components. More information can be found in these two articles: Override Theme Styles Knowledge base for CSS Isolation It would be very helpful if you create a runnable sample or modify this REPL example and send it back to me so I can observe the issue locally. This way, I will be able to investigate it locally and come up with suggestions accordingly.

### Response

**Kevin** commented on 20 Sep 2023

Hi Georgi, Where can I send you a runnable sample? Thank you, Kevin

### Response

**Kevin** commented on 20 Sep 2023

Hi Georgi, I re-read the knowledge base for CSS isolation and was able to resolve the issue. I appreciate your help! Thank you, Kevin
