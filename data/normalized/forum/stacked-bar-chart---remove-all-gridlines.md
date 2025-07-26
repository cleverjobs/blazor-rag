# Stacked Bar Chart - Remove all GridLines

## Question

**Bec** asked on 10 May 2021

Hi I am trying to recreate the design below using stacked bar charts, I want to remove all gridlines. The red boxes are not part of the design but rather confidential info. As you can see I have been able to remove all the gridlines and values I don't want but the vertical ones. Here is my code, just playing at the moment. <TelerikChart Width="100%" Height="10%">
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Bar" Name="Product 1" Data="@series1Data">
<ChartSeriesStack Group="myStack" Type="Telerik.Blazor.ChartSeriesStackType.Stack100"></ChartSeriesStack>
</ChartSeries>

<ChartSeries Type="ChartSeriesType.Bar" Name="Product 2" Data="@series2Data">
<ChartSeriesStack Group="myStack"></ChartSeriesStack>
</ChartSeries>

</ChartSeriesItems>

<ChartCategoryAxes>
<ChartCategoryAxis>
<ChartCategoryAxisMajorGridLines Visible="false" />
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartValueAxes>
<ChartValueAxis>
<ChartValueAxes>
<ChartValueAxis Visible="false" />
</ChartValueAxes>
</ChartValueAxis>
</ChartValueAxes>


<ChartLegend Visible="false">
</ChartLegend>

</TelerikChart> I have tried hiding major and minor gridlines, in the Y, X, and value Axis to no avail. I would be so grateful if someone could point me in the right direction. Thank you Becca

## Answer

**Svetoslav Dimitrov** answered on 12 May 2021

Hello Becca, To remove all the Grid lines from the Chart you should remove both the MajorGridLines, as you did, and the MinorGridLines, together with the Major and MinorTicks for both axes. The code snippet below illustrates the concept: <TelerikChart Width="100%" Height="10%"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Bar" Name="Product 1" Data="@series1Data"> <ChartSeriesStack Group="myStack" Type="Telerik.Blazor.ChartSeriesStackType.Stack100"> </ChartSeriesStack> </ChartSeries> <ChartSeries Type="ChartSeriesType.Bar" Name="Product 2" Data="@series2Data"> <ChartSeriesStack Group="myStack"> </ChartSeriesStack> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis> <ChartCategoryAxisMajorGridLines Visible="false" /> <ChartCategoryAxisMinorGridLines Visible="false" /> <ChartCategoryAxisMajorTicks Visible="false" /> <ChartCategoryAxisMinorTicks Visible="false" /> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Visible="false"> <ChartValueAxisMajorGridLines Visible="false" /> <ChartValueAxisMinorGridLines Visible="false" /> <ChartValueAxisMajorTicks Visible="false" /> <ChartValueAxisMinorTicks Visible="false" /> </ChartValueAxis> </ChartValueAxes> <ChartLegend Visible="false"> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 5, 6 };
public List <object> series2Data=new List <object> () { 5, 8, 2, 7 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Becca** commented on 13 May 2021

Thank you very much, i will give it a go!

### Response

**Svetoslav Dimitrov** commented on 14 May 2021

Hello Becca, sure, you can take your time, if another question emerges let me know! Regards, Svetolsav Dimitrov
