# Value Axis Label Rotation auto

## Question

**Nik** asked on 13 Oct 2021

How do I set the ChartValueAxisLabelsRotation Angle to auto? It has the same description as the ChartCategoryAxisLabelsRotation Angle, but instead of taking " @object" the ValueAxis takes "D ouble?"? Description for both ChartCategoryAxisLabelsRotation and ChartValueAxisLabelsRotation Angle: The rotation angle of the labels. By default the labels are not rotated. Can be set to "auto" if the axis is horizontal in which case the labels will be rotated only if the slot size is not sufficient for the entire labels. Error: Cannot convert string to double? Code: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="Product 1" Data="@series1Data"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Product 2" Data="@series2Data"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels> <ChartValueAxisLabelsRotation Angle="@AutoLabelsRotation" /> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes AxisCrossingValue="crossingPoints"> <ChartCategoryAxis Categories="@xAxisItems"> <ChartCategoryAxisLabels> <ChartCategoryAxisLabelsRotation Angle="@AutoLabelsRotation" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> </TelerikChart> @code { string AutoLabelsRotation="auto"; public List <object> series1Data=new List<object>() { 10, 2, 5, 6, 8 }; public List <object> series2Data=new List<object>() { 5, 8, 2, 7, 6 }; public string [] xAxisItems=new string [ 5 ]; protected override void OnInitialized ( ) { for ( int i=0; i <5; i++)
{
xAxisItems[i]=$"looooong label {i + 1 } ";
} base.OnInitialized();
}
} Thanks Regards, Nikolas

## Answer

**Stamo Gochev** answered on 15 Oct 2021

Hello, This option is not currently available (the description is incorrect and should be updated accordingly) as the backing C# property cannot be of type double (accepting a number for the angle) as well as a string. This being said I would suggest testing different numeric values for the angle and choosing the one that best fits your scenario. Regards, Stamo Gochev Progress Telerik

### Response

**Nikolas** commented on 15 Oct 2021

Hello Stamo, Will this be added in some upcomming release? My content is created dynamically, so I cannot just pick a value for the angle, because I have no idea how much space the chart has, nor how much data will be displayed. But the auto angle on category axis is working great, so nicely done :) Thanks Regards, Nikolas

### Response

**Stamo Gochev** commented on 20 Oct 2021

Hello, We will be making a revision of the chart properties after .NET 6.0 ships officially and are considering a dedicated release later (note: changes to the schedule and the decision might apply) that can affect a set of parameters that are currently incompatible - in the concrete case, there is no way to set the exceptional "auto" value to a double property. We want to avoid "monkey patching" properties here and there, but rather make a broader improvement. The exact way of fixing the case is yet to be decided, e.g. the type can be "relaxed" to object, new properties can be exposed to better differentiate the separate configurations, etc. Regards, Stamo Gochev

### Response

**Nikolas** commented on 20 Oct 2021

Hello Stamo, Makes sense, thanks :) Regards, Nikolas
