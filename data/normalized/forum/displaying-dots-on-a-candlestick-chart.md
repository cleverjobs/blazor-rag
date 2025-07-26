# Displaying dots on a candlestick chart

## Question

**Iva** asked on 12 Oct 2020

Hello! I am trying to implement a box and whisker chart using a candlestick chart. Everything looks good, but I can not display outliers in the form of points. The problem is that you can't mix categorical candlestick chart type and numeric type. Using a categorical type of line chart also does not produce the desired result. Can anyone tell me how to display a scatter chart on a candlestick chart?

## Answer

**Marin Bratanov** answered on 12 Oct 2020

Hello Ivan, The OHLC types of charts rely on a date x-axis (distinct categories), while numerical charts rely on a numerical x-axis, so they cannot be mixed together. You can read more on what you can mix here. Another important bit is that neither the OHLC, nor the Candlestick chart types show outliers. That said, I can suggest a line series bound to the same data where you can control the markers and make the series itself transparent. Here's a basic example (this does not have a field for outliers, I used the High field, but you can alter that as needed): <TelerikChart Height="480px" Width="640px">

<ChartSeriesItems>
<ChartSeries Type="@ChartSeriesType.Candlestick" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Date))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)">
</ChartSeries>

<ChartSeries Type="@ChartSeriesType.Line" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Date))" Field="@(nameof(StockDataPoint.High))" Color="transparent" VisibleInLegend="false"> <ChartSeriesMarkers>
<ChartSeriesMarkersBorder Color="red" Width="3"></ChartSeriesMarkersBorder>
</ChartSeriesMarkers> </ChartSeries>
</ChartSeriesItems>

<ChartCategoryAxes>
<ChartCategoryAxis Type="@ChartCategoryAxisType.Date" BaseUnit="@ChartCategoryAxisBaseUnit.Months">
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartValueAxes>
<ChartValueAxis>
<ChartValueAxisLabels Format="{0:C4}"></ChartValueAxisLabels>
</ChartValueAxis>
</ChartValueAxes>

</TelerikChart>

@code {
List<StockDataPoint> ChartProduct1Data { get; set; } protected override async Task OnInitializedAsync ( ) { await GenerateChartData();
} async Task GenerateChartData ( ) {
ChartProduct1Data=new List<StockDataPoint>()
{ new StockDataPoint( new DateTime( 2019, 1, 1 ), 39.88 m, 40.12 m, 41.12 m, 39.75 m, 3584700 ), // Close is lower than Open, so the Down color is used, see later in the article for more details new StockDataPoint( new DateTime( 2019, 2, 1 ), 41.62 m, 40.12 m, 41.69 m, 39.81 m, 2632000 ), new StockDataPoint( new DateTime( 2019, 3, 1 ), 42 m, 42.62 m, 43.31 m, 41.38 m, 7631700 ), new StockDataPoint( new DateTime( 2019, 4, 1 ), 42.25 m, 43.06 m, 43.31 m, 41.12 m, 4922200 ),
}; await Task.FromResult(ChartProduct1Data);
} public class StockDataPoint { public StockDataPoint ( ) { } public StockDataPoint ( DateTime date, decimal open, decimal close, decimal high, decimal low, int volume ) {
Date=date;
Open=open;
Close=close;
High=high;
Low=low;
Volume=volume;
} public DateTime Date { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; }
}
} Regards, Marin Bratanov

### Response

**Ivan** answered on 12 Oct 2020

Thanks for your feedback! I tried this option, but it doesn't work as there can be many outliers for each category (many high property values for the new DateTime (2019, 1, 1) category) The line chart displays only one point for each category unfortunately.

### Response

**Marin Bratanov** answered on 12 Oct 2020

Hi Ivan, You can add as many series as needed to display more data points in the same category. Have you seen a charting solution that can achieve this without such additional logic, and do you have such an example from a different place? Something similar is done by BoxPlot charts, see an example here: [https://demos.telerik.com/kendo-ui/box-plot-charts/index.](https://demos.telerik.com/kendo-ui/box-plot-charts/index.) They represent statistical data and they have collections for outlier data that they display, yet they are not OHLC by nature but you could use the lower, q1, q3 and upper in a similar fashion (see an example here that shows how using the same values can reduce the "clutter" of such a chart in the first item and make it look more like a candlestick chart). If a box plot is what you seek and/or would serve your purpose, you can make a new feature request for it, or I can do that for you (just confirm for me whether it's what you seek). That said, you may also want to Vote for and Follow this feature that would let you implement custom rendering for the series data point so you could render what you want: [https://feedback.telerik.com/blazor/1441979-custom-rendering-for-series-element-visual-template](https://feedback.telerik.com/blazor/1441979-custom-rendering-for-series-element-visual-template) in case that would help. Another thing you can consider is the opposite - using a Scatter Chart with dates on the x-axis and adding more series to display the relevant fields (such as open, close, high, low). You can see how you can work around a scatter series with a datetime axis here: [https://feedback.telerik.com/blazor/1441432-scatter-chart-with-date-axis.](https://feedback.telerik.com/blazor/1441432-scatter-chart-with-date-axis.) If that would suit your needs, Vote for and Follow that too. Note that this would not enable a candle stick and scatter chart to mix, they use different x-axis types and you can have one of them - the categorical date-time axis aggregates, while the numerical date-time axis is linear. Regards, Marin Bratanov

### Response

**Ivan** answered on 12 Oct 2020

Of course, an ideal solution would be to implement the kendo ui box plot diagram on blazor. At the moment, only one developer has such a solution on blazor, but I really don't want to include an entire new framework for the sake of one component. Thanks for the hint, while I'm implementing a box plot diagram using a scatter diagram

### Response

**Marin Bratanov** answered on 12 Oct 2020

Hello Ivan, I made this feature request on your behalf so you can Follow the implementation of a box plot chart: [https://feedback.telerik.com/blazor/1489452-box-plot-chart-type](https://feedback.telerik.com/blazor/1489452-box-plot-chart-type) In the meantime, you can consider using the Kendo chart jQuery widget (see here ) if that can be an option for you. Regards, Marin Bratanov

### Response

**Ivan** answered on 12 Oct 2020

The solution is as follows, but there is a problem: context.DataItem is null for the second line chart series and no tooltips are displayed. The problem arises if you use the categorical data type ChartCategoryAxis Type="@ChartCategoryAxisType.Category" @page "/" <TelerikChart Height="480px" Width="640px"> <ChartTooltip Visible="true"> <Template> @{ var item=context.DataItem; if (item is StockDataPoint candle) { <span>@($"{candle.Volume}")</span> } else if (item is Outlier outlier) { <span>@($"{outlier.Value}")</span> } } </Template> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Candlestick" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Type))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)"> </ChartSeries> @foreach (var outs in outs.Select(x=> x.Outs)) { <ChartSeries Type="@ChartSeriesType.Line" Data="@outs" CategoryField="@(nameof(Outlier.Type))" Field="@(nameof(Outlier.Value))" Color="red" VisibleInLegend="false"> <ChartSeriesMarkers> <ChartSeriesMarkersBorder Color="red" Width="3"></ChartSeriesMarkersBorder> </ChartSeriesMarkers> </ChartSeries> } </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Category"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:C4}" /> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @code { List<StockDataPoint> ChartProduct1Data { get; set; } List<Outliers> outs; protected override async Task OnInitializedAsync() { outs=new List<Outliers>() { new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type1, Value=50m } } }, new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type1, Value=60m } } }, new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type1, Value=62m } } }, new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type2, Value=20m } } }, new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type2, Value=21m } } }, new Outliers{Outs=new List<Outlier>{new Outlier(){Type=Types.Type2, Value=22m } } } }; await GenerateChartData(); } async Task GenerateChartData() { ChartProduct1Data=new List<StockDataPoint>() { new StockDataPoint(Types.Type1, 31m, 45m, 48m, 24m, 3584700, outs), new StockDataPoint(Types.Type2, 31m, 45m, 48m, 24m, 3584700, outs) }; await Task.FromResult(ChartProduct1Data); } public class Outliers { public List<Outlier> Outs { get; set; } } public class Outlier { public Types Type { get; set; } public decimal Value { get; set; } } public class StockDataPoint { public StockDataPoint() { } public StockDataPoint(Types type, decimal open, decimal close, decimal high, decimal low, int volume, List<Outliers> outliers) { Type=type; Open=open; Close=close; High=high; Low=low; Volume=volume; Outliers=outliers; } public Types Type { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; } public List<Outliers> Outliers { get; set; } } public enum Types { Type1, Type2 } }

### Response

**Marin Bratanov** answered on 13 Oct 2020

Hello Ivan, In the provided code, the line series only get one data item in their data, and not two. So, effectively, there is data only for the first category. I am attaching a screenshot that illustrates this. You need to have the two data points in the Data collection you provide to the series. I made the following example for you that shows the proper data structure for a chart with several series, based on the provided code: <TelerikChart Height="480px" Width="640px">
<ChartTooltip Visible="true" Background="red">
<Template>
@{ var item=context.DataItem; if (item is StockDataPoint candle)
{
<span>@( $" {candle.Volume} " )</span>
} else if (item is Outlier outlier)
{
<span>@( $" {outlier.Value} " )</span>
}
}
</Template>
</ChartTooltip>
<ChartSeriesItems>
<ChartSeries Type="@ChartSeriesType.Candlestick" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Type))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)">
</ChartSeries>
@foreach (List<Outlier> currSeriesData in outs)
{
<ChartSeries Type="@ChartSeriesType.Line" Data="@currSeriesData" CategoryField="@(nameof(Outlier.Type))" Field="@(nameof(Outlier.Value))" Color="transparent" VisibleInLegend="false">
<ChartSeriesMarkers>
<ChartSeriesMarkersBorder Color="red" Width="3"></ChartSeriesMarkersBorder>
</ChartSeriesMarkers>
</ChartSeries>
}

</ChartSeriesItems>
<ChartCategoryAxes>
<ChartCategoryAxis Type="@ChartCategoryAxisType.Category">
</ChartCategoryAxis>
</ChartCategoryAxes>
<ChartValueAxes>
<ChartValueAxis>
<ChartValueAxisLabels Format="{0:C4}" />
</ChartValueAxis>
</ChartValueAxes>

</TelerikChart>

@code {
List<StockDataPoint> ChartProduct1Data { get; set; }
List<List<Outlier>> outs { get; set; }=new List<List<Outlier>>(); protected override async Task OnInitializedAsync ( ) {

outs.Add( new List<Outlier>
{ new Outlier() { Type=Types.Type1, Value=50 m }, new Outlier() { Type=Types.Type2, Value=20 m }
});

outs.Add( new List<Outlier>
{ new Outlier(){Type=Types.Type1, Value=60 m }, new Outlier() { Type=Types.Type2, Value=21 m }
});

outs.Add( new List<Outlier>
{ new Outlier(){Type=Types.Type1, Value=62 m }, new Outlier(){Type=Types.Type2, Value=22 m }
}); await GenerateChartData();
} async Task GenerateChartData ( ) {
ChartProduct1Data=new List<StockDataPoint>()
{ new StockDataPoint(Types.Type1, 31 m, 45 m, 48 m, 24 m, 3584700 ), new StockDataPoint(Types.Type2, 31 m, 45 m, 48 m, 24 m, 3584700 )
}; await Task.FromResult(ChartProduct1Data);
} //public class Outliers //{ // public List<Outlier> Outs { get; set; } //} public class Outlier { public Types Type { get; set; } public decimal Value { get; set; }
} public class StockDataPoint { public StockDataPoint ( ) { } public StockDataPoint ( Types type, decimal open, decimal close, decimal high, decimal low, int volume ) {
Type=type;
Open=open;
Close=close;
High=high;
Low=low;
Volume=volume;
} public Types Type { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; }
} public enum Types
{
Type1,
Type2
}
} Regards, Marin Bratanov

### Response

**Ivan** answered on 13 Oct 2020

In a real-life situation, we cannot know if there will be outliers in the results for a particular data series. If there will be no outliers for the Type1 series, but there will be outliers for Type2 (comment out the addition of objects of the Outlier class with type1) and the context for this series will be null.

### Response

**Ivan** answered on 13 Oct 2020

@page "/" <TelerikChart Height="480px" Width="640px"> <ChartTooltip Visible="true" Background="red"> <Template> @{ var item=context.DataItem; if (item is StockDataPoint candle) { <span>@($"{candle.Volume}")</span> } else if (item is Outlier outlier) { <span>@($"{outlier.Value}")</span> } } </Template> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Candlestick" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Type))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)"> </ChartSeries> @foreach (List<Outlier> currSeriesData in outs) { <ChartSeries Type="@ChartSeriesType.Line" Data="@currSeriesData" CategoryField="@(nameof(Outlier.Type))" Field="@(nameof(Outlier.Value))" Color="transparent" VisibleInLegend="false"> <ChartSeriesMarkers> <ChartSeriesMarkersBorder Color="red" Width="3"></ChartSeriesMarkersBorder> </ChartSeriesMarkers> </ChartSeries> } </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Category"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:C4}" /> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @code { List<StockDataPoint> ChartProduct1Data { get; set; } List<List <Outlier>> outs { get; set; }=new List<List <Outlier>>(); protected override async Task OnInitializedAsync() { outs.Add(new List<Outlier> { //new Outlier() { Type=Types.Type1, Value=50m }, new Outlier() { Type=Types.Type2, Value=20m } }); outs.Add(new List<Outlier> { //new Outlier(){Type=Types.Type1, Value=60m }, new Outlier() { Type=Types.Type2, Value=21m } }); outs.Add(new List<Outlier> { //new Outlier(){Type=Types.Type1, Value=62m }, new Outlier(){Type=Types.Type2, Value=22m } }); await GenerateChartData(); } async Task GenerateChartData() { ChartProduct1Data=new List<StockDataPoint>() { new StockDataPoint(Types.Type1, 31m, 45m, 48m, 24m, 3584700), new StockDataPoint(Types.Type2, 31m, 45m, 48m, 24m, 3584700) }; await Task.FromResult(ChartProduct1Data); } //public class Outliers //{ // public List<Outlier> Outs { get; set; } //} public class Outlier { public Types Type { get; set; } public decimal Value { get; set; } } public class StockDataPoint { public StockDataPoint() { } public StockDataPoint(Types type, decimal open, decimal close, decimal high, decimal low, int volume) { Type=type; Open=open; Close=close; High=high; Low=low; Volume=volume; } public Types Type { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; } } public enum Types { Type1, Type2 } }

### Response

**Ivan** answered on 13 Oct 2020

Сurious that normal tooltips are rendered ok but context.DataItem is null

### Response

**Svetoslav Dimitrov** answered on 15 Oct 2020

Hello Ivan, After further investigation of the sample, you have provided the issue seems to be the same as the one we discussed in your other forum thread. The context.DataItem is not received correctly and again is connected to this Bug Report from our Feedback Portal. Regards, Svetoslav Dimitrov
