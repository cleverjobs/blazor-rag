# Horizontal and Vertical lines

## Question

**Fai** asked on 04 Mar 2021

Is it possible to draw vertical or horizontal lines on the chart?, to display as limits? I could not find any examples of it. Its just for user to check if the series data are within the limits set. Thanks

## Answer

**Marin Bratanov** answered on 04 Mar 2021

Hi, The horizontal line is relatively easy - a line series with y-values that all have the same (desired) value, we have one such in the Date Axis demo. Vertical lines, however, are a more complex. Generally, if your first series is a Bar series, the chart will flip the x and y axes visually (it will rotate 90 degrees) and line charts will be vertical now. I am not sure this is what you are after, I expect you want some sort of marker in a certain place in the x-axis that goes up to denote a certain value or threshold. If so, keep reading for some more ideas. What could help a lot in this case is actually the ColorField feature some series have - it lets you change the color of the given bar/column per item in the series. So, you could evaluate the data and set the value of that field to a new color if it matches certain criteria (say, it is below a target value). In our Kendo charts, there are two features that might help in creating thresholds - Notes (see example here too that is closer to what I think you may be seeking) and plot bands. You can also find a few other ideas that are possible in our older suites that have some more features here (including the plot bands approach). If you like either of them, we can open a feature request so that it gets implemented in Blazor too, so you can know when it becomes available. Regards, Marin Bratanov

### Response

**Fairoz** answered on 18 Mar 2021

Hi Marin, Thanks for getting back with those suggestions. And yes, those horizontal and vertical lines were supposed to be markers, limits & threshold. Would be awesome if there was a way to simply draw a horizontal and vertical lines, bound to a collection of y and x data respectively. I think this would be a feature request and hoping for something like the below would be nice., <TelerikChart> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Line" Name="@P_Name1" Color="blue" Data="@P_Data1" Field="@P_Field1" CategoryField="@P_CategoryField1"> <ChartSeriesLabels Visible="true" Template="#=dataItem.P_Description#" /> <ChartSeriesMarkers Size="4" /> </ChartSeries> <ChartHorizontalLines Data="@YLinesData"/> <ChartVerticalLines Data="@XLinesData"/> </ChartSeriesItems> </TelerikChart> @code{ List<double> YLinesData, XLinesData; }

### Response

**Marin Bratanov** answered on 18 Mar 2021

Hi, I made this feature request page on your behalf so you can monitor the status of such a feature: [https://feedback.telerik.com/blazor/1511761-easy-to-draw-horizontal-and-vertical-lines-in-the-charts.](https://feedback.telerik.com/blazor/1511761-easy-to-draw-horizontal-and-vertical-lines-in-the-charts.) I also think it would be nice, and if there is interest in the community for it, management will consider its implementation. Regards, Marin Bratanov
