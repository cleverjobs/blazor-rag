# Series label tooltip

## Question

**Ila** asked on 23 Mar 2023

When Y is 0 there's no place to hover in order to get the current tooltip. Is there a way to add a tooltip when hovering on charts category series label as well?

## Answer

**Dimo** answered on 28 Mar 2023

The Chart series tooltip requires a non-zero value and a visible data point to display. Otherwise there is nothing to hover, as you correctly say. Why do you need a tooltip for a missing / zero value? Isn't the situation intuitive and clear for your users? If needed, I can suggest adding some note outside the Chart that provides additional information. If you really must provide a tooltip in the Chart, then the only option is to render a fake data point and use a Chart tooltip template to provide the correct information to the user: <TelerikChart Height="480px" Width="640px"> <ChartSeriesItems> <ChartTooltip Visible="true"> <Template> @{ var dataItem=(StockDataPoint)context.DataItem; }

@if (dataItem.EmptyPoint)
{ <text> zero value here </text> }
else
{ <div> Open: @dataItem.Open.ToString("c2") <br /> Close: @dataItem.Close.ToString("c2") <br /> High: @dataItem.High.ToString("c2") <br /> Low: @dataItem.Low.ToString("c2") <br /> Volume: @dataItem.Volume.ToString("c2") <br /> </div> } </Template> </ChartTooltip> <ChartSeries Type="@ChartSeriesType.Candlestick" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Date))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date" BaseUnit="@ChartCategoryAxisBaseUnit.Months"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:C4}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @code {
List<StockDataPoint> ChartProduct1Data { get; set; } protected override async Task OnInitializedAsync ( ) { await GenerateChartData();
} async Task GenerateChartData ( ) {
ChartProduct1Data=new List<StockDataPoint>()
{ new StockDataPoint( new DateTime( 2019, 1, 1 ), 39. 88m, 40. 12m, 41. 12m, 39. 75m, 3584700 ), // Close is lower than Open, so the Down color is used, see later in the article for more details new StockDataPoint( new DateTime( 2019, 2, 1 ), 41. 62m, 40. 12m, 41. 69m, 39. 81m, 2632000 ), new StockDataPoint( new DateTime( 2019, 3, 1 ), 40m, 40m, 41m, 39m, 0, true ), new StockDataPoint( new DateTime( 2019, 4, 1 ), 42. 25m, 43. 06m, 43. 31m, 41. 12m, 4922200 ),
}; await Task.FromResult(ChartProduct1Data);
} public class StockDataPoint { public StockDataPoint ( ) { } public StockDataPoint ( DateTime date, decimal open, decimal close, decimal high, decimal low, int volume, bool empty=false ) { Date=date;
Open=open;
Close=close;
High=high;
Low=low;
Volume=volume;
EmptyPoint=empty;
} public DateTime Date { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; } public bool EmptyPoint { get; set; }
}
}

### Response

**Ilan** commented on 28 Mar 2023

Doesn't the ChartTooltip needs to be inside ChartSeries?

### Response

**Dimo** commented on 29 Mar 2023

Both options are valid and it depends on what you need - see the Chart Tooltip documentation.
