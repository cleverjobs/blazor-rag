# TelerikGrid GridColumn TextAlign property not working for EditorTemplate

## Question

**Cla** asked on 01 Jun 2022

If i set the TextAlign property on GridColumn it work well for read Template, but not for EditorTemplate. It's a bug? There is a workaround? Thanks

## Answer

**Svetoslav Dimitrov** answered on 06 Jun 2022

Hello Claudio, The TextAlign property applies the text-align CSS rule and it is supposed to align the text in a container. In the EditorTemplate you have an editing component that is not supposed to be aligned with the text-align CSS rule. If you add a component, let's say a textbox, it would not be aligned even in the Template. To achieve the desired behavior you can take a look at the CSS Layout article of the W3 school. Regards, Svetoslav Dimitrov Progress Telerik
