# Right Align a TelerikNumericTextBox

## Question

**Bre** asked on 24 Jun 2025

I have tried and tried to get a TelerikNumericTextBox aligned right. Honestly, for a numeric text box, this should just be a property on the component. Crazy. Anyway, here is what I've tried and have been through all the forums, etc. CSS /* Right-align input in TelerikNumericTextBox for this component */ .p21-numerictextbox-right .k-numerictextbox .k-input-inner { text-align: right !important; } Markup <TelerikNumericTextBox @ref="P21NumericTextEditorRef" Class=" p21-numerictextbox-right" @bind-Value="_value" Arrows="false"/> This does not work. Any thoughts? Thank you!

## Answer

**Dimo** answered on 25 Jun 2025

Brett - there should be no space between.p21-numerictextbox-right and.k-numerictextbox. A space is a descendant combinator, while these two classes render on the same element. [https://blazorrepl.telerik.com/cJkqmpEU174tgAIe05](https://blazorrepl.telerik.com/cJkqmpEU174tgAIe05) Regards, Dimo Progress Telerik

### Response

**Brett Parkhurst** commented on 28 Jun 2025

Thank you so much! This did the trick. I appreciate it.
