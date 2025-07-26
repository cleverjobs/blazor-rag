# GRID Filter for decimal numbers without arrows

## Question

**Pet** asked on 08 Nov 2022

Hi, I need GridFilterMode.FilterRow for decimal or real numbers without arrows . Perhaps, TelerikNumericTextBox can be used, but without arrows or common TextBox. Could you help me with it. Are there any parameters or templates for it? Thanks Peter

## Answer

**Nadezhda Tacheva** answered on 10 Nov 2022

Hi Peter, By design of the built-in filtering functionality, the Grid will use an integrated NumericTextBox as a filter editor of numeric fields. If you need to somehow customize the behavior of the built-in filtering, you may use a Filter Row Template. You can indeed add a Numeric Textbox component and adjust its Arrows parameter - it controls whether the arrows will be visible and it is true by default. When Filter Template is used, the built-in filtering is essentially overridden and one should manually handle the filtering by creating the necessary filter descriptions based on the value changes in the corresponding filter editor. If the only customization you need to make is hiding the arrows, you may also consider a CSS approach. This will allow you to keep the default filtering but still hide the arrows. For example: [https://blazorrepl.telerik.com/QmvPPavl41tRFUue51](https://blazorrepl.telerik.com/QmvPPavl41tRFUue51) - the Age column is a numeric one. I hope the above-listed information and materials will help you move forward with your application. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva
