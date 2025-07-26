# Stacked Bar Chart Legend

## Question

**Chr** asked on 03 Dec 2020

I am trying to build a stacked bar chart with a cumulative total split to two values per bar, with the data source coming from multiple items that the cumulative counts are derived. My problem is the legend shows the multiple items and the stack breaks out into multiple color sections rather than the two desired, yet I am not able to locate where this is happening in the code. I used the Stacked Bar Chart demo example to create the chart. Can anyone provide their thoughts or suggestions?

## Answer

**Marin Bratanov** answered on 03 Dec 2020

Hello Chris, The chart legend shows all the series that the chart has. Stacking several series on top of one another still keeps them as separate series and so they should show up in the legend. If you don't want many series, you can aggregate the chart data yourself and avoid using stacked series but reduce the series count to the count of the stacks you want and put all the data into one series per stack. Another approach is to hide some series from the legend by setting their VisibleInLegend parameter to false. Here's a basic example of that: <TelerikChart>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 1" Data="@series1Data">
<ChartSeriesStack Enabled="true"></ChartSeriesStack>
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 2" Data="@series2Data" VisibleInLegend="false">
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 3" Data="@series3Data">
</ChartSeries>
</ChartSeriesItems>

<ChartCategoryAxes>
<ChartCategoryAxis Categories="@xAxisItems"></ChartCategoryAxis>
</ChartCategoryAxes>

<ChartTitle Text="Quarterly revenue per product"></ChartTitle>

<ChartLegend Position="ChartLegendPosition.Right">
</ChartLegend>
</TelerikChart>

@code { public List <object> series1Data=new List<object>() { 10, 2, 5, 6 }; public List <object> series2Data=new List<object>() { 5, 8, 2, 7 }; public List <object> series3Data=new List<object>() { 15, 3, 8, 8 }; public string [] xAxisItems=new string [] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Marin Bratanov
