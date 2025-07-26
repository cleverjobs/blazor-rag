# TelerikPopover show programmatically at correct location

## Question

**And** asked on 28 Aug 2024

Hello, I'm using a TelerikPopover with an AnchorSelector that references a class name. When the user clicks on an element with that class name the Popover show properly and to the right of that element. However, if I want to programmatically display the Popover using PopoverRef.Show(), the popover will display to the right of the first element with that selector. Is there a way for me to have to Popover display at a specific element? Thank You, -Andy

## Answer

**Dimo** answered on 02 Sep 2024

Hi Andy, In such scenarios, you can change the Popover AnchorSelector parameter at runtime to a unique value that points to a specific element. Here is an example: [https://blazorrepl.telerik.com/GeEinkvw42carE5f35](https://blazorrepl.telerik.com/GeEinkvw42carE5f35) The tricky part is that you need to recreate the Popover component for the change to take effect. This slows down the component display a little. Normally, component recreation should be not necessary and the AnchorSelector parameter should be reactive. That's why I am logging a public bug report on your behalf. Regards, Dimo Progress Telerik
