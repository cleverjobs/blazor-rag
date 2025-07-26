# Telerik Line Chart - Price development graph

## Question

**Mar** asked on 02 Feb 2022

Hi how can I make a graph like this one? What I have now <TelerikChart> <ChartTitle Text="Prices"> </ChartTitle> <ChartTooltip Visible="true"> </ChartTooltip> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Prices" Data="@Details.PriceGraphs" DashType="@DashType.Solid" XField="@nameof(InstrumentPriceGraph.UpdateDate)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> </TelerikChart> Model public class InstrumentPriceGraph { public string CiInstrument { get; set; } public DateTime UpdateDate { get; set; } public decimal Price { get; set; }
}

## Answer

**Martin Herløv** answered on 03 Feb 2022

I now have this. Only need to fix the date formatting and setting the min value on the Y axis. If I use the format. Then the dates will be replaced with the format string. So "1/12" will become {0:yy MM dddd}. In this example I would like to set the Y min value to 105. <TelerikChart Width="100%" Height="100%" RenderAs="RenderingMode.Canvas"> <ChartTitle Text="Prices" /> <ChartTooltip Visible="true" /> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Details.PriceGraphs" DashType="@DashType.Solid" CategoryField="@nameof(InstrumentPriceGraph.UpdateDate)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Date" BaseUnit="ChartCategoryAxisBaseUnit.Days"> <ChartCategoryAxisLabels Step="2" Format="{0:dd-MM-YY}"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> This is how it looks if I use the format option

### Response

**Hristian Stefanov** answered on 07 Feb 2022

Hi Martin, You are on the right path. It is possible to have a date type of axis. We have the following article in our documentation that shows how to configure date type axis. Date Axis article Please follow the steps from there to cover your app requirements. You can take a look at our date axis demo as well. Additionally, we have an open bug report regarding the Min/Max properties of the Chart. Chart not displayed if I set Min and Max properties of a Date ChartCategoryAxis You can also check it out to see how to avoid it. If there is still a problem, I would be glad to help. Regards, Hristian Stefanov Progress Telerik
