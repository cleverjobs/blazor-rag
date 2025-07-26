# How do I add a Clear button to a DropDownList?

## Question

**Sea** asked on 11 Jun 2023

How do I add a Clear button to a DropDownList? The docs say that it can be done, but don't give any examples that I can find.

## Answer

**Nadezhda Tacheva** answered on 14 Jun 2023

Hi Sean, I see a colleague of mine already answered in your private ticket. I will post the information here as well for visibility and in case any other community member is interested in this scenario. In general, the DropDownList component does not provide a built-in clear button as in the ComboBox component, for example. Thank you once again for identifying this discrepancy in our documentation. I've already updated it and the changes are pending approval. The desired result can be achieved with a custom approach by adding a button and handling its onclick to clear the DropDownList value. Here is a runnable sample: [https://blazorrepl.telerik.com/wHaqvwPe19zqGzQp45.](https://blazorrepl.telerik.com/wHaqvwPe19zqGzQp45.) In addition, if you want to display the button inside the main element of the DropDownList, you can use this approach: [https://blazorrepl.telerik.com/cdYAbylu04u4fslu34.](https://blazorrepl.telerik.com/cdYAbylu04u4fslu34.) Regards, Nadezhda Tacheva
