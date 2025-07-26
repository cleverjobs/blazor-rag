# Gridlines with multiple axes

## Question

**Emi** asked on 02 Nov 2021

Hello, I have a problem with gridlines not showing, when i use multiple axes. In the image below, the MajorGridLines of the axis to the right should be shown as red, and the MinorGridLines should also be visible. Is this a bug, intended or am i just doing something wrong. I have posted the code used for generating the chart at the bottom of this post. <TelerikChart>
<ChartTitle Text="Gross domestic product growth /GDP annual %/"></ChartTitle>
<ChartTooltip Visible="true"></ChartTooltip>
<ChartLegend Position="ChartLegendPosition.Top" Align="ChartLegendAlign.Start"></ChartLegend>

<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Line" Style="ChartSeriesStyle.Normal" Name="Chile" Data="@Data" Field="@nameof(ModelData.Series1)"></ChartSeries>
<ChartSeries Type="ChartSeriesType.Line" Style="ChartSeriesStyle.Step" Name="India" Data="@Data" Field="@nameof(ModelData.Series2)"></ChartSeries>
<ChartSeries Type="ChartSeriesType.Line" Style="ChartSeriesStyle.Smooth" Name="Haiti" Data="@Data" Axis="Secondary" Field="@nameof(ModelData.Series3)"></ChartSeries>
</ChartSeriesItems>

<ChartCategoryAxes>
<ChartCategoryAxis AxisCrossingValue="crossingValues" Categories="@Categories"></ChartCategoryAxis>
</ChartCategoryAxes>

<ChartValueAxes>
<ChartValueAxis ZIndex="1" Max="100">
<ChartValueAxisLabels Format="{0}%"></ChartValueAxisLabels>
<ChartValueAxisMajorGridLines Visible="true"></ChartValueAxisMajorGridLines>
</ChartValueAxis>
<ChartValueAxis Name="Secondary" ZIndex="12">
<ChartValueAxisLabels Format="{0}%"></ChartValueAxisLabels>
<ChartValueAxisMajorGridLines Color="Red" Visible="true" DashType="DashType.Solid"></ChartValueAxisMajorGridLines>
<ChartValueAxisMinorGridLines Visible="true" DashType="DashType.Dot"></ChartValueAxisMinorGridLines>
</ChartValueAxis>
</ChartValueAxes>
</TelerikChart> Best Regards, Emil

## Answer

**Nadezhda Tacheva** answered on 05 Nov 2021

Hello Emil, This behavior is expected and the reason behind it stems from the configuration of the Chart component itself. When working with multiple axes, such grid line settings should be defined under the first instance of ChartValueAxis as it is actually the main one and the multiple axes essentially share the grid lines. I've prepared a simple example to demonstrate how you can achieve the desired behavior. I am sharing if via the new Telerik REPL for Blazor tool we released recently. Here is a link and you can directly run and test it in the browser - [https://blazorrepl.telerik.com/mPPvaTla27z15Bpk38.](https://blazorrepl.telerik.com/mPPvaTla27z15Bpk38.) In addition, we will also consider improving the Chart component documentation and listing these specifics of the multiple axes. I hope you will find the above information and example useful. If you run across any other concerns, please let us know, we will be happy to step in and assist. Regards, Nadezhda Tacheva

### Response

**Emil** answered on 08 Nov 2021

Hello Nadezhda, Does this mean that there is no way to display major gridlines that align to the values on the secondary axis? Like show in the image below. Best Regards, Emil

### Response

**Nadezhda Tacheva** answered on 10 Nov 2021

Hi Emil, The grid lines are associated and controlled by the first instance of ChartValueAxis. The reason behind this is that one can declare multiple axes with various values and divisions settings, so we cannot render separate grid lines for all of them. We have, however, exposed parameters thorough which you can control the labels of the additional axes to align with the grid lines. Based on the max value of the secondary axis, you can change the major units through the MajorUnit parameter of the ChartValueAxis. Then, you can set the specific n-th labels to be rendered through the Step parameter of the ChartValueAxisLabels, to only render the labels aligning with the major grid lines. To better demonstrate the described approach, I have prepared another example where I've included some additional settings for the secondary ChartValueAxis - [https://blazorrepl.telerik.com/QblPbEbn44QQSbEQ55.](https://blazorrepl.telerik.com/QblPbEbn44QQSbEQ55.) I hope this will help you move forward with your application. Please let us know if any further questions appear. Regards, Nadezhda Tacheva Progress Telerik
