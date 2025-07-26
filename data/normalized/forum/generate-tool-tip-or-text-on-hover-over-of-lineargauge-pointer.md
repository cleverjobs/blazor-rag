# Generate tool tip or text on hover-over of LinearGauge pointer?

## Question

**Mic** asked on 15 Jul 2021

Is there a way to generate some kind of tool tip or text when hovering over the pointer in a linear gauge?

## Answer

**Radko** answered on 16 Jul 2021

Hi Michael, You can achieve this using our Tooltip component with a TargetSelector parameter targeting a path element with an exact attribute within the SVG. For example, a CSS selector targeting a pointer with a specific color. In this case, you can't use data- or title attributes, so the tooltip content itself can't be provided from the node itself. Instead, you can populate the content of the Tooltip from properties for example. I have attached a sample runnable application that demonstrates this approach. Please let me know if you need any additional information. Regards, Radko Stanev Progress Telerik

### Response

**Michael** commented on 16 Jul 2021

This worked great, thanks!
