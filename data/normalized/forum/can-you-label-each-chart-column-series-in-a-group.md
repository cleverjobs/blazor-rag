# Can you label each Chart Column Series in a group?

## Question

**Mar** asked on 16 Oct 2023

With ChartCategoryAxes, is it possible to label the group and then each column within it? For example, [https://blazorrepl.telerik.com/QdbaPgbU17q4epgO21:](https://blazorrepl.telerik.com/QdbaPgbU17q4epgO21:) We have tried to use ChartCategoryAxisLabel templates. But without HTML to enable styling it is difficult to space the elements evenly. We have tried adding an invisible series at the top of the stacked series with a label, but on dark backgrounds the invisible series is revealed on hover. We can use brittle CSS selectors to hide the hover but ideally our label would be beneath the chart, within the axis.

## Answer

**Dimo** answered on 19 Oct 2023

Hi Mark, Your approach is smart and it's suitable for a fixed-width Chart. I can suggest you a series label template for the topmost series in each category: Blazor Chart stacked series with a category label Regards, Dimo Progress Telerik

### Response

**Mark** commented on 19 Oct 2023

Hi Dimo, Thank you for your answer. Do you know if there is any way I can get the group and column labels into the axis while being correctly aligned? I am able to achieve this in Kendo UI in this dojo Untitled | Kendo UI Dojo (telerik.com) Thanks again Mark

### Response

**Dimo** commented on 19 Oct 2023

(Post updated) I revisited the Chart parameters and tags, and it turns out the Kendo UI jQuery approach is possible with the Blazor Chart too. <ChartSeries Type="ChartSeriesType.Column" Data="@Series1Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 1"> <ChartSeriesLabels Visible="true" Rotation="-90" Position="@ChartSeriesLabelsPosition.InsideBase" Template="seriesLabelTemplate"> <ChartSeriesLabelsMargin Top="110" /> </ChartSeriesLabels> </ChartSeries> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date"> <ChartCategoryAxisLabels> <ChartCategoryAxisLabelsMargin Top="110" /> </ChartCategoryAxisLabels> </ChartCategoryAxis>
