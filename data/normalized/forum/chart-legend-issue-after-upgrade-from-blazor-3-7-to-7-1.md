# Chart Legend issue after Upgrade from Blazor 3.7 to 7.1

## Question

**Pet** asked on 20 Jan 2025

Hi, I upgrades a Blazor Projekt from net 6, Blazor 3.7 to net 8, Blazor 7.1. I handled all breaking changes, so it works now. There is only an issue with the legend style : in 3.7 only the line is shown. But in 7.1 a dot with line. The code of my chart control was not changed from 3.7 to 7.1. <TelerikChart Height="200px"> <ChartPlotArea Background="#FAFAFA"> </ChartPlotArea> <ChartTooltip Visible="true"> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Scatter" Name="@($" { AxleNumber }: { right_text }")" Data="@chartRight" Color="#ff8400" XField="@nameof(ChartDataViewModel.start)" YField="@nameof(ChartDataViewModel.Indicator)" Visible="@right_visible"> <ChartSeriesMarkers Type="ChartSeriesMarkersType.Circle" Size="4" Background="#ff8400" /> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Name="@($" { AxleNumber }: { left_text }")" Data="@chartLeft" Color="#0071ff" XField="@nameof(ChartDataViewModel.start)" YField="@nameof(ChartDataViewModel.Indicator)" Visible="@left_visible"> <ChartSeriesMarkers Type="ChartSeriesMarkersType.Circle" Size="4" Background="#0071ff" /> </ChartSeries> </ChartSeriesItems> <ChartYAxes> <ChartYAxis Max="YAxis_Max" Min="YAxis_Min" /> </ChartYAxes> <ChartXAxes> <ChartXAxis Type="date" BaseUnit="days"> <ChartXAxisLabels Format="{0:dd.MM.yy}"> </ChartXAxisLabels> </ChartXAxis> </ChartXAxes> <ChartLegend Position="ChartLegendPosition.Custom" OffsetX="50" OffsetY="10" Height="10" Visible="@(right_visible && left_visible)" /> </TelerikChart> How can I get back to old Legend style? Peter

## Answer

**Tsvetomir** answered on 21 Jan 2025

Hi Peter, Thank you for the provided information about the encountered behavior. To achieve the same layout of the markers as the one shown in the first screenshot is required to hide the default LegendItem markers. For your convenience, I've prepared an example for you that achieves the desired outcome: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1" Data="@series1Data"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2" Data="@series2Data"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Bottom"> <ChartLegendItem> <ChartLegendItemMarkers Visible="false"> </ChartLegendItemMarkers> </ChartLegendItem> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 5, 6 };
public List <object> series2Data=new List <object> () { 5, 8, 2, 7 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} I hope this serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik
