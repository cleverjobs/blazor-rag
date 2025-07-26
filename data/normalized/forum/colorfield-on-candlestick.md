# ColorField on Candlestick

## Question

**Emi** asked on 08 Oct 2021

Hello, Is there a way to make the candlestick chart always use the colorfield even if the value is down? In my solution it dont matter if the value is up or down, if the colorfield is defined it should always us that. I can't use the Color and DownColor, since the colorfield can be different throughout the series. As displayed below all the "Down" values are displayed as black, when it should be pink. Best Regards, Emil

## Answer

**Marin Bratanov** answered on 13 Oct 2021

Hi Emil, If you will be using the ColorField, you must also use the DownColorField. If you use only Color for the series, then you can use only DownColor for the series. The ColorField and DownColorField values take priority over their respective feature - either color, or down-color. I've also logged an issue for enhancing the docs with this info: [https://github.com/telerik/blazor-docs/issues/525](https://github.com/telerik/blazor-docs/issues/525) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 10 Oct 2021

Hello Emil, The easiest way is to set the series Color and DownColor to the same value: <TelerikChart Height="480px" Width="640px"> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Candlestick" Color=" purple " DownColor=" purple " Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Date))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date" BaseUnit="@ChartCategoryAxisBaseUnit.Months"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:C4}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @code {
List <StockDataPoint> ChartProduct1Data { get; set; }

protected override async Task OnInitializedAsync()
{
await GenerateChartData();
}

async Task GenerateChartData()
{
ChartProduct1Data=new List <StockDataPoint> ()
{
new StockDataPoint(new DateTime(2019, 1, 1), 39.88m, 40.12m, 41.12m, 39.75m, 3584700),

// Close is lower than Open, so the Down color is used, see later in the article for more details
new StockDataPoint(new DateTime(2019, 2, 1), 41.62m, 40.12m, 41.69m, 39.81m, 2632000),

new StockDataPoint(new DateTime(2019, 3, 1), 42m, 42.62m, 43.31m, 41.38m, 7631700),
new StockDataPoint(new DateTime(2019, 4, 1), 42.25m, 43.06m, 43.31m, 41.12m, 4922200),
};

await Task.FromResult(ChartProduct1Data);
}

public class StockDataPoint
{
public StockDataPoint() { }

public StockDataPoint(DateTime date, decimal open, decimal close, decimal high, decimal low, int volume)
{
Date=date;
Open=open;
Close=close;
High=high;
Low=low;
Volume=volume;
}
public DateTime Date { get; set; }

public decimal Open { get; set; }

public decimal Close { get; set; }

public decimal High { get; set; }

public decimal Low { get; set; }

public int Volume { get; set; }
}
} Differentiating between "regular" and "down" items is an important feature of this chart type, and if you want to make them use the same colors, you must do so in the application logic - either by using the series features, or by supplying suitable data that contains the same color for both cases. Regards, Marin Bratanov

### Response

**Emil** answered on 11 Oct 2021

Hello Marin, Thank you for the response. Yes, setting both the downcolor and the color, would fix the issue if the entire chart should be the same color. But in the solution I have, there is defined a color field on the data, that should be used as the color of a specific part of the series. The problem is that the downcolor overwrites the "ColorField" property, it works if the Close is higher than the Open value. <TelerikChart Height="480px" Width="640px"> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Candlestick" Color="purple" DownColor="purple" ColorField="@nameof(StockDataPoint.Color)" Name="Product 1" Data="@ChartProduct1Data" CategoryField="@(nameof(StockDataPoint.Date))" OpenField="@nameof(StockDataPoint.Open)" CloseField="@nameof(StockDataPoint.Close)" HighField="@nameof(StockDataPoint.High)" LowField="@nameof(StockDataPoint.Low)"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date" BaseUnit="@ChartCategoryAxisBaseUnit.Months"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:C4}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @code {
List <StockDataPoint> ChartProduct1Data { get; set; }

protected override async Task OnInitializedAsync()
{
await GenerateChartData();
}

async Task GenerateChartData()
{
ChartProduct1Data=new List <StockDataPoint> ()
{
new StockDataPoint(new DateTime(2019, 1, 1), 39.88m, 40.12m, 41.12m, 39.75m, 3584700, "Red"),

// Close is lower than Open, so the Down color is used, see later in the article for more details
new StockDataPoint(new DateTime(2019, 2, 1), 41.62m, 40.12m, 41.69m, 39.81m, 2632000, "Green"),

new StockDataPoint(new DateTime(2019, 3, 1), 42m, 42.62m, 43.31m, 41.38m, 7631700, "Blue"),
new StockDataPoint(new DateTime(2019, 4, 1), 42.25m, 43.06m, 43.31m, 41.12m, 4922200, "Yellow"),
};

await Task.FromResult(ChartProduct1Data);
}

public class StockDataPoint
{
public StockDataPoint() { }

public StockDataPoint(DateTime date, decimal open, decimal close, decimal high, decimal low, int volume, string color)
{
Date=date;
Open=open;
Close=close;
High=high;
Low=low;
Volume=volume;
Color=color;
}
public DateTime Date { get; set; }

public decimal Open { get; set; }

public decimal Close { get; set; }

public decimal High { get; set; }

public decimal Low { get; set; }

public int Volume { get; set; } public string Color {get; set; } }
} I would expect the purple part to be green, given the color defined in the data source. Best Regards, Emil

### Response

**Emil** answered on 13 Oct 2021

Hello Marin, That did it, I was missing the DownColorField. Thanks for the help. Best Regards, Emil
