# Can you stack series in a Range Column Chart?

## Question

**Mar** asked on 24 Aug 2023

Is it possible to stack a series in a Range Column Chart? We have created a chart using an invisible baseline series to shunt our series upward. But the hover state of the invisible series cannot be configured. [https://blazorrepl.telerik.com/GxkiGIvF15qirZPe20.](https://blazorrepl.telerik.com/GxkiGIvF15qirZPe20.) Does anyone have any other ideas of chart types that may be more suitable?

## Answer

**Svetoslav Dimitrov** answered on 29 Aug 2023

Hello Mark, I can confirm that you have taken the best approach to achieve the desired behavior. The issue with the hover style is not easy to resolve as the Chart is rendered as an SVG. Targeting SVGs with CSS is possible, but not straightforward. You can use the browser's Inspect to gain a better understanding of how the Chart renders and build the appropriate CSS selectors to remove the hover effects. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Mark** commented on 31 Aug 2023

Our selectors are at the mercy of each Telerik UI for Blazor release. Any change in rendering patterns could break them without warning. I hope this feature is added soon.
