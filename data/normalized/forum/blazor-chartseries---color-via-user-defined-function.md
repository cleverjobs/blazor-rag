# Blazor ChartSeries - Color via user-defined function

## Question

**opu** asked on 04 Nov 2022

Hi all I've got a question related to chart layout. In Blazor on the ChartSeries there is a property "Color". Per intellisense a function(point) can be used that will evaluate the series color on point-by-point basis. But how do you exactly do that ? Any help is very much appreciated. FYI I'm trying this on an Area chart.

### Response

**Hristian Stefanov** commented on 09 Nov 2022

Hi Opus Numeri, I confirm that the " Color " parameter accepts any valid CSS color by name or by HEX. This color covers the whole area from that specific series along with all points inside. The "Color" parameter applies per series, not per point in the series. Here is an example that shows both ways to set the " Color " parameter: <TelerikChart> <ChartSeriesItems> @*Color set by Name ("red")*@<ChartSeries Type="ChartSeriesType.Area" Name="Product 1" Color="red" Data="@series1Data"> </ChartSeries> @*Color set by HEX ("#abcdef")*@<ChartSeries Type="ChartSeriesType.Area" Name="Product 2" Color="#abcdef" Data="@series2Data"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 7, 5 };
public List <object> series2Data=new List <object> () { 5, 12, 8, 2 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Let me know if that covers the question and if the IntelliSense description is confusing so we can improve it.

### Response

**opusnumeri** commented on 01 Dec 2022

Hi Hristian Thank you for the example and for the clarification. Gr Steven
