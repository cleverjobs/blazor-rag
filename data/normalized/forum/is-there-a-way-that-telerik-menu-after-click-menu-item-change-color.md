# is there a way that telerik menu after click menu item change color?

## Question

**DeDe** asked on 13 Apr 2024

Hi, is there a way to use css to change the telerik menu item border or color when user click on it. After user click on other menu item, the existing old menu item color will remove and the new selected menu item will change the color.

## Answer

**Justin** answered on 15 Apr 2024

Hello De, This question was also asked in a support ticket so I will share the answerer here as well for the community. Yes, it is possible to change the style of the last selected item in the menu and keep the new style after loosing focus. This can be achieved through the use of an Item Template and the OnClick event. The event will allow you to get the ID of the clicked item. You can then use the template in combination with the ID to conditionally apply a custom CSS selector to the item. Please take a moment to look over this example I created in our REPL. Regards, Justin Progress Telerik
