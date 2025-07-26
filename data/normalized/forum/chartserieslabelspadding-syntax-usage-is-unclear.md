# ChartSeriesLabelsPadding Syntax/Usage is unclear

## Question

**Hun** asked on 02 Nov 2023

How do I use ChartSeriesLabelsPadding, it seems to describe the exact behaviour I want in a chart, but I can't find any implementation details or examples of how it should be used anywhere. I have a series of charts where the largest data points are just at the top of the chart and the tooltip will appear just above the top and get cut off and only the bottom of the text is visible. Help would be greatly appreciated. Thanks, Hunter

## Answer

**Hristian Stefanov** answered on 07 Nov 2023

Hi Hunter, Here is a sample I have prepared for you that demonstrates the usage of "ChartSeriesLabelsPadding": <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="Product 3" Data="@series1Data"> <ChartSeriesStack Enabled="true" /> <ChartSeriesLabels Position="ChartSeriesLabelsPosition.OutsideEnd" Visible="true" Font="16px 'Times New Roman'" Background="transparent"> </ChartSeriesLabels> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Product 2" Data="@series2Data"> <ChartSeriesStack Enabled="true" /> <ChartSeriesLabels Position="ChartSeriesLabelsPosition.Top" Visible="true" Font="bold 14px 'Comic Sans MS'" Background="transparent" /> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Product 1" Data="@series3Data"> <ChartSeriesStack Enabled="true" /> <ChartSeriesLabels Position="ChartSeriesLabelsPosition.Above" Visible="true" Font="bold 22px Times New Roman" Background="rgba(0, 128, 0, 0.2)"> <ChartSeriesLabelsBorder Color="red" Width="5" DashType="@DashType.LongDashDotDot" /> <ChartSeriesLabelsMargin Left="50" /> <ChartSeriesLabelsPadding Top="50" /> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 5, 6 };
public List <object> series2Data=new List <object> () { 5, 8, 2, 7 };
public List <object> series3Data=new List <object> () { 15, 3, 8, 8 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Hristian Stefanov Progress Telerik
