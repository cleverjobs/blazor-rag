# Setting minimum value on the Y axis

## Question

**Mar** asked on 03 Feb 2022

How can I set the start value on the Y axis? The max value always look right

## Answer

**Apostolos** answered on 08 Feb 2022

Hi Martin, It is possible to set the Min and Max properties of the ChartValueAxis tag. This will define the minimum and maximum values of the respective Y-axis. Take a look at this REPL example that shows such a case. On a side note, there is a bug report regarding Min and Max properties of Date ChartCategoryAxis. The thread includes a workaround. I hope you find the above information useful. Regards, Apostolos

### Response

**Martin Herløv** commented on 08 Feb 2022

If I set the min/max then I got no output <TelerikChart Width="100%" Height="100%" RenderAs="RenderingMode.Canvas"> <ChartTitle Text="Prices" /> <ChartTooltip Visible="true" /> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Details.PriceGraphs" DashType="@DashType.Solid" CategoryField="@nameof(InstrumentPriceGraph.UpdateDateStr)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Min="0" Max="5"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Category"> <ChartCategoryAxisLabels Step="2"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart>

### Response

**Apostolos** commented on 11 Feb 2022

Hello Martin, Is it possible that the values Min="0" and Max="5" don't match the data? The data values on the previous screenshot are between 30 and 36, which would make them out-of-range. I created a REPL example using the provided code. See that I set the Min and Max properties dynamically based on the data. Apply a similar approach to solve the issue. If the problem seems different, please elaborate. Regards, Apostolos Progress Telerik

### Response

**Martin Herløv** commented on 11 Feb 2022

When I add the min/max y value the graph sometimes misses to draw the max value. Also I am still unable to format the dates on the x graph calculated Min/Max 115.5/123 Anyone knows about a smart way to calculate a tight fit for the y max/min value? <TelerikChart Width="100%" Height="100%" RenderAs="RenderingMode.Canvas"> <ChartTitle Text="Prices" /> <ChartTooltip Visible="true" /> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Details.PriceGraphs" DashType="@DashType.Solid" CategoryField="@nameof(InstrumentPriceGraph.UpdateDate)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Min="@_yMinValue" Max="@_yMaxValue" /> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Date" BaseUnit="ChartCategoryAxisBaseUnit.Days"> <ChartCategoryAxisLabels Step="2"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> When setting <ChartCategoryAxisLabels Step="2" Format="{0:d}"> I get this? works on the Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor.

### Response

**Apostolos** commented on 16 Feb 2022

Hello Martin, Please set Min and Max values, which are consistent the value axis label step. The step will depend on the range of data points and can be 5, 1, 0.5, 0.2, etc. In the provided example, Min is a decimal number and Max is integer. The step is 0.5, and the Max value does not match the next possible label, which would be 123.5. This is why the top line is not visible. So the following will always work: Max=Min + Step * [some integer] About the date format issue, unfortunately, I cannot reproduce this behavior. It will be helpful to provide a sample project with this behavior. This will help me take a look at the implementation and come to a solution. Regards, Apostolos Progress Telerik

### Response

**Martin Herløv** commented on 16 Feb 2022

First the min/max question. I think the build-in algoritme works really well for the max value but always has to many extra steps for the min value. If I want to set the step value should I then use BaseUnitStep? About the date format issue. If I take the exact code from this example [https://blazorrepl.telerik.com/QGkQFlbv07u4Se8x40](https://blazorrepl.telerik.com/QGkQFlbv07u4Se8x40) and use it on a new page. Adding format to the graph then it will fail when setting the culture to da-DK. When I don't set the culture then it will work. When you have dates crossing a year then it's not enough just showing day an month. I can only get it to work when binding to a string holding the date in the format I want (UpDateStr). <TelerikChart RenderAs="RenderingMode.Canvas"> <ChartTitle Text="Prices" /> <ChartTooltip Visible="true" /> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Details.PriceGraphs" DashType="@DashType.Solid" CategoryField="@nameof(InstrumentPriceGraph.UpdateDateStr)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Category" BaseUnitStep="" BaseUnit="ChartCategoryAxisBaseUnit.Days"> <ChartCategoryAxisLabels Step="2"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart>

### Response

**Apostolos** commented on 21 Feb 2022

Hi Martin, You can use the MajorUnit parameter of the ChartValueAxis to set its label step. This will help you control the number of displayed values of the axis. Let me know if my suggestion fits the scenario. It seems that the there is a separate discussion about the date format in this public post. I hope everything is resolved and work as expected. On a side note, it is a good practice to use a separate public post or
ticket for unrelated questions. It will be helpful to keep track of and
manage the flow of the conversation.
