# How to remove padding around HeatMap chart?

## Question

**Fed** asked on 30 Nov 2023

I have a heatmap chart where I'm showing the X axis' labels on top of the chart. In the attached screenshot, you can see that the padding below the chart is bigger than the padding on the sides, how can I remove this extra padding?

## Answer

**Dimo** answered on 04 Dec 2023

Hi Federico, The Chart may render some empty space around its elements and I am afraid there is no way to remove it. However, the screenshot shows more empty space at the bottom of the Chart than I am able to produce on my test page. Can you compare the two Chart setups? Regards, Dimo Progress Telerik

### Response

**Federico** commented on 05 Dec 2023

Hi Dimo, thanks for your feedback. There is just one thing from your test page that I'm not sure I understand, regarding the X axis labels positioned above the chart In my code, I need to explicitly set <ChartXAxisLabels Position=ChartAxisLabelsPosition.End /> to do that, while in yours it seems to be the result of this parameter: AxisCrossingValue="@( new object[] { 10 })" on the Y axis, but I can't see why that is happening. Can you please explain that?

### Response

**Dimo** commented on 05 Dec 2023

Yes, see this help section - Choose Axis Position (update: I should probably confirm that your approach is simpler, while AxisCrossingValue can be useful in more complex scenarios with multiple horizontal or vertical axes.)
