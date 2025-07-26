# TelerikGrid in a row of a TelerikGridLayout in a TelerikWindow exceeds TelerikWindow Height

## Question

**NiV** asked on 22 Jan 2023

I am trying to have a TelerikWindow with its content divided in 3 rows: in the first row a button (10% of the TelerikWindow Heigth), in the second row a scrollable TelerikGrid (80%) and in the third row another button (10%). To obtain this result I've created a TelerikWindow with a TelerikGridLayout in it, the TelerikGridLayout has 3 rows (10%, 80%, 10%) for button - grid - button. In my test the grid exceeds the height of the telerikwindow so a vertical scrollbar appears in the TelerikWindow, instead I would like all content in the TelerikWindow (without the TelerikWindow vertical scrollbar, only with the TelerikGrid scrollbar). My test is in repl at [https://blazorrepl.telerik.com/cdEbQQGu3019EWUB00.](https://blazorrepl.telerik.com/cdEbQQGu3019EWUB00.) May you kindly help me? Thank you.

### Response

**Nadezhda Tacheva** commented on 25 Jan 2023

Hi fpsoft, I revised the configuration and it generally looks correct. However, I do see that the Grid overflows the Window size. I will reach out to our front-end engineers to validate if something is missing and what may be causing this behavior. I will then get ack to you to suggest how to handle the scenario. Thank you for your patience in the meantime!

### Response

**Nadezhda Tacheva** commented on 27 Jan 2023

Hi fpsoft, Thank you for your patience! After further revising the scenario, I can say that the behavior seems expected due to the relative values of the elements' height. By design, the GridLayout component does not have Width and Height parameters and its size is controlled by the size of its children. In this case, however, they have relative Width and Height. Having this in mind, it looks like you are hitting the behavior listed here, in the Formal Definition> Percentages section: [https://developer.mozilla.org/en-US/docs/Web/CSS/height#formal_definition.](https://developer.mozilla.org/en-US/docs/Web/CSS/height#formal_definition.) To handle the scenario, you can either specify fixed height values or prevent the GridLayout from expanding by setting max-height. The second option will allow you to keep the relative height values, here is the modified example: [https://blazorrepl.telerik.com/mxYFGVPe43aMBfMc30.](https://blazorrepl.telerik.com/mxYFGVPe43aMBfMc30.) I hope you will find this information useful. Please let us know if any other questions appear.
