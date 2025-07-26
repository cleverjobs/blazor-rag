# Run function on mouse hover

## Question

**Oma** asked on 22 Apr 2025

Hi, Is there a way to trigger a method and pass data to it when hovering over a line in a line chart? Regards, Omar

## Answer

**Anislav** answered on 23 Apr 2025

Hi Omar, There isn't a built-in feature that supports triggering a method with data on hover for line charts. The available events are primarily click-based, as outlined in the documentation here: Chart Events - Telerik UI for Blazor. That said, you might be able to implement a similar behavior using JavaScript, but it would be quite complex. It would likely require reverse-engineering how the chart component is rendered and managed internally, which could be difficult to maintain. Best regards, Anislav Atanasov
