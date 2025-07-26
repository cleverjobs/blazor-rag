# Disable touch events on Telerik Chart

## Question

**Kev** asked on 10 Jun 2025

I am using a Column Chart component inside my Blazor application. When viewed on a mobile screen, the user is unable to pan the window, because i think the chart registers this as an event. If the user touches the chart, they cannot scroll the window anymore. I am not using any additional events on my chart, it does not need any interaction. How can I adjust the chart so that it can be touched and scrolled? Code snippet: <div style="@((DialogOpen) ? " visibility: hidden;": " visibility: visible;")"> <TelerikChart Height="200px"> <ChartZoomable Enabled="false"> </ChartZoomable> <ChartPannable Enabled="false"> </ChartPannable> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="min/100m" Data="@GraphData" Field="@nameof(GraphData)" Color="#9edfff"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@GraphX.ToArray()"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartLegend Position="ChartLegendPosition.Bottom"> </ChartLegend> <ChartTitle Text=""> </ChartTitle> </TelerikChart> </div>

### Response

**Hristian Stefanov** commented on 10 Jun 2025

Hi Kevin, You can disable the touch actions on the Chart by applying the CSS shown below. Please give it a try and let me know if it covers your needs. <style>.k-chart { pointer-events: none;
touch-action: none;
}
</style> Best regards, Hristian

### Response

**Kevin** commented on 10 Jun 2025

Hello Hristian, That indeed resolves my request, thank you! Is it also possible to disable touch actions on the entire chart, except for the bars that represent data? If I want to handle a touch or click event on a specific bar, do you have an example for that as well?

### Response

**Hristian Stefanov** commented on 11 Jun 2025

Hi Kevin, I can confirm that it's not possible to disable touch actions for the entire chart while keeping them enabled only for the bars. This is because the bars are rendered within the same element that receives the CSS styles for disabling touch actions. Additionally, since the chart uses SVG rendering, it's not feasible to selectively re-enable touch actions for just the bars using CSS alone. As for handling click events, you can use the OnSeriesClick event. Best regards, Hristian

### Response

**Kevin** commented on 11 Jun 2025

Hello Hristian, That is good to know, thank you very much for confirming my question and for your help.
