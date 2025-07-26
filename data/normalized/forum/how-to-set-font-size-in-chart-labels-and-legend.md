# How to Set Font Size in Chart Labels and Legend?

## Question

**TedTed** asked on 24 May 2024

How can the font size used in Chart Labels and Legends be set? I don't see any configuration for that, and overriding the CSS has no effect on the SVG generated for the charts.

## Answer

**Tsvetomir** answered on 29 May 2024

Hi Ted, To change the font size of the Chart series and Chart legend labels, use the Font parameter. The only specific to this parameter is that the expected value is a valid CSS font string (e.g., " 20px Sans-serif "). To assist you further, I crafted an example that demonstrates the desired outcome: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="Product 1" Data="@series1Data"> <ChartSeriesLegendItem> <ChartSeriesLegendItemMarkers Background="blue"> </ChartSeriesLegendItemMarkers> </ChartSeriesLegendItem> <ChartSeriesLabels Visible="true" Font="15px Sans-serif" /> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Product 2" Data="@series2Data"> <ChartSeriesLegendItem Type="@ChartLegendItemType.Area"> <ChartSeriesLegendItemMarkers Background="#00ff00"> </ChartSeriesLegendItemMarkers> </ChartSeriesLegendItem> <ChartSeriesLabels Visible="true" Font="30px Sans-serif" /> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right" Visible="true"> <ChartLegendTitle Text="Revenue per product" Background="lightblue" Color="black" Font="15px Sans-serif"> </ChartLegendTitle> <ChartLegendItem> <ChartLegendItemMarkers Type="@ChartSeriesMarkersType.Cross" Background="#00ff00"> </ChartLegendItemMarkers> </ChartLegendItem> <ChartLegendLabels Font="15px Sans-serif"> </ChartLegendLabels> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 5, 6 };
public List <object> series2Data=new List <object> () { 5, 8, 2, 7 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Tsvetomir Progress Telerik
