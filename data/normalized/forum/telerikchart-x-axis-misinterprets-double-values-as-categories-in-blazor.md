# TelerikChart X-Axis Misinterprets Double Values as Categories in Blazor

## Question

**Nuu** asked on 20 May 2025

Hello, I'm having trouble configuring a TelerikChart in Blazor to properly display a column series and a line series side-by-side on the same chart. My goal is to have the X-axis (CategoryAxis) reflect double values (e.g. 0, 5, 10, 15...) so that both series are aligned and spaced proportionally based on their actual numeric X values. However, what I'm observing is that the X-axis seems to treat these values as categories or strings, not real numbers. This results in incorrect spacing and ordering. What's going wrong: The columns are not placed in the correct positions on the X-axis — for instance, a column with X=6 appears at the far end if 6 doesn't also exist in the line series. The values on the X-axis are not sorted numerically — so the spacing between, say, 5 and 10 is the same as between 10 and 1024, which breaks the scale. Ideally, I want the chart to understand that X=1024 is far from X=50, and space it accordingly on a continuous numeric scale. You can see the visual chart below: The code for the chart: @page "/test" @using ChartLegendPosition=Telerik.Blazor.ChartLegendPosition
@using ChartSeriesType=Telerik.Blazor.ChartSeriesType
<TelerikChart>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Line" Name="Normal Distribution" Data="@series2Data" Field="Y" CategoryField="X" CategoryAxis="Category" Axis="Value" Style="@ChartSeriesStyle.Smooth" Color="blue">
<ChartSeriesMarkers Visible="false" />
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Histogram" Field="Y" CategoryField="X" CategoryAxis="Category" Axis="Value2" Data="@series1Data">
</ChartSeries>
</ChartSeriesItems>

<ChartValueAxes>
<ChartValueAxis Name="Value"></ChartValueAxis>
<ChartValueAxis Name="Value2"></ChartValueAxis>
</ChartValueAxes>

<ChartCategoryAxes>
<ChartCategoryAxis Name="Category">
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartTitle Text="Quarterly revenue per product"></ChartTitle>

<ChartLegend Position="ChartLegendPosition.Right">
</ChartLegend>
</TelerikChart>

@code { public List<Point> series1Data=new List<Point>()
{ new Point { X=0, Y=1 }, new Point { X=6, Y=2 }, new Point { X=12, Y=3 }, new Point { X=18, Y=4 }, new Point { X=24, Y=5 }, new Point { X=30, Y=6 }, new Point { X=36, Y=7 }, new Point { X=42, Y=8 }, new Point { X=48, Y=9 }, new Point { X=1024, Y=10 },
}; public List<Point> series2Data=new List<Point>()
{ new Point { X=0, Y=0.01 }, new Point { X=5, Y=0.02 }, new Point { X=10, Y=0.05 }, new Point { X=15, Y=0.1 }, new Point { X=20, Y=0.2 }, new Point { X=25, Y=0.35 }, new Point { X=30, Y=0.5 }, new Point { X=35, Y=0.7 }, new Point { X=40, Y=0.85 }, new Point { X=45, Y=0.95 }, new Point { X=50, Y=1.0 }, new Point { X=55, Y=0.95 }, new Point { X=60, Y=0.85 }, new Point { X=65, Y=0.7 }, new Point { X=70, Y=0.5 }, new Point { X=75, Y=0.35 }, new Point { X=80, Y=0.2 }, new Point { X=85, Y=0.1 }, new Point { X=90, Y=0.05 }, new Point { X=95, Y=0.02 }, new Point { X=100, Y=0.01 }
}; public class Point { public double X { get; set; } public double Y { get; set; }
} // protected override void OnInitialized() // { // var samples=new double[] {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93}; // var std=StatisticsHelper.StandardDeviation(samples); // var average=samples.Average(); // var yValues=StatisticsHelper.CalculateProbabilityDensityValues(samples.ToList(), std, average); // // series2Data=samples // .Zip(yValues, (x, y)=> new DistributionPoint { X=x, Y=y }) // .ToList(); // // base.OnInitialized(); // } } Does TelerikChart support a numeric X-axis instead of a CategoryAxis? If so, should I be using a ChartValueAxis for the X-axis instead of a ChartCategoryAxis? Is there a recommended way to configure a dual-axis chart where both the column and line series share a numeric X-axis? I'd like the spacing to be consistent and reflect the actual distance between values. PS: I also tried this with XAxes instead of CategoryAxes. But the same issue occurs. Also I tried to use ascatterline instead of line. with type numeric on the x-axis. But then I cant add the column on that axis. If you need more information, or if the issue is unclear, feel free to ask.

## Answer

**Dimo** answered on 21 May 2025

Hello Nuur,>> Does TelerikChart support a numeric X-axis instead of a CategoryAxis? Yes, the Chart can display category series and numeric series, but not both at the same time.>> If so, should I be using a ChartValueAxis for the X-axis instead of a ChartCategoryAxis? No, use a ChartXAxis like in the ScatterLine example.>> Is there a recommended way to configure a dual-axis chart where both the column and line series share a numeric X-axis? The Chart Column series is categorical one and cannot use a numeric axis. The Chart cannot display categorical and numerical series at the same time.>> I'd like the spacing to be consistent and reflect the actual distance between values. This is possible with numeric series and XAxis.>> I tried to use ascatterline instead of line with type numeric on the x-axis. But then I cant add the column on that axis. Yes, this is by design. Consider two separate Charts. Regards, Dimo Progress Telerik
