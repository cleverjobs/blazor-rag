# Gradient color in chart series

## Question

**Ila** asked on 16 Aug 2022

I was able to make a gradient color Chart Area when RenderingMode is SVG. But it's not working on RenderingMode.Canvas. What do I need to change? What I use is: <ChartSeries Color="url(#svg-gradient)" where: <svg xmlns="[https://www.w3.org/2000/svg"](https://www.w3.org/2000/svg") version="1.1" width="0" height="0" style="visibility: hidden"> <defs> <linearGradient id="svg-gradient" x1="0%" y1="0%" x2="0%" y2="100%"> <stop offset="0%" style="stop-color: #c2dc8b; stop-opacity: 1.0"/> <stop offset="100%" style="stop-color: #c2dc8b; stop-opacity: 0.1"/> </linearGradient> </defs> </svg>

## Answer

**Joana** answered on 19 Aug 2022

Hello Ilan, We provide a built-in support for Series Gradient. You might observethe behavior in the following REPL snippet, or our API Reference: [https://blazorrepl.telerik.com/QmaWPXEI41Pt7Zjf32](https://blazorrepl.telerik.com/QmaWPXEI41Pt7Zjf32) [https://docs.telerik.com/blazor-ui/api/Telerik.Blazor.Components.ChartSeriesOverlay#collapsible-Telerik_Blazor_Components_ChartSeriesOverlay_Gradient](https://docs.telerik.com/blazor-ui/api/Telerik.Blazor.Components.ChartSeriesOverlay#collapsible-Telerik_Blazor_Components_ChartSeriesOverlay_Gradient) [https://docs.telerik.com/blazor-ui/api/Telerik.Blazor.ChartSeriesOverlayGradient](https://docs.telerik.com/blazor-ui/api/Telerik.Blazor.ChartSeriesOverlayGradient) In SVG RenderMode it is possible to apply external custom gradient. However, in Canvas mode it needs to be drawed by the chart engine. Regards, Joana Progress Telerik

### Response

**Paul** commented on 22 Sep 2022

Could you please provide an example of applying an external gradient using SVG RenderMode?

### Response

**Marin Bratanov** commented on 25 Sep 2022

The opener post by Ilan has one. It relies on the standard svg url() and <defs> features
