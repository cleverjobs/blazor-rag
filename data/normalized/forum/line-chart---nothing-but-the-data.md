# Line Chart - Nothing but the data

## Question

**Ric** asked on 15 Oct 2020

Hi All, I'd like to make certain that I'm just showing one data line and no legends, tick marks, axes, padding and so on. I would also like the first data point to be the center of the graph vertically. Here's my chart markup, please let me know if you have any suggestions. Thank you so much. <TelerikChart Width="100%" Height="100%" Transitions="false" RenderAs="Telerik.Blazor.RenderingMode.Canvas"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Data" Color="@LineColor"> <ChartSeriesMarkers Visible="false" /> <ChartSeriesLabels Visible="false" Background="transparent" /> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Visible="false"><ChartCategoryAxisMajorGridLines Visible="false" /></ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Visible="false"><ChartValueAxisMajorGridLines Visible="false" /></ChartValueAxis> </ChartValueAxes> <ChartTitle Visible="false" /> <ChartLegend Visible="false" /> </TelerikChart>

## Answer

**Marin Bratanov** answered on 16 Oct 2020

Hi Rich, You seem to have hidden all the chart elements but the series, so that will yield a blank white space with just the line on it. As for starting the line at the middle of the chart - you'd have to pad the data accordingly, a chart starts on the left always. Here's a basic example that pads the data so the center point (number 4 of 7) is the first with meaningful data <TelerikChart Width="100%" Height="100%" Transitions="false" RenderAs="Telerik.Blazor.RenderingMode.Canvas">
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Data" Color="@LineColor">
<ChartSeriesMarkers Visible="false" />
<ChartSeriesLabels Visible="false" Background="transparent" />
</ChartSeries>
</ChartSeriesItems>
<ChartCategoryAxes>
<ChartCategoryAxis Visible="false"><ChartCategoryAxisMajorGridLines Visible="false" /></ChartCategoryAxis>
</ChartCategoryAxes>
<ChartValueAxes>
<ChartValueAxis Visible="false"><ChartValueAxisMajorGridLines Visible="false" /></ChartValueAxis>
</ChartValueAxes>
<ChartTitle Visible="false" />
<ChartLegend Visible="false" />
</TelerikChart>

@code{ public List <object> Data=new List<object>() { null, null, null, 5, 8, 2, 7 }; string LineColor="cyan";
} Regards, Marin Bratanov
