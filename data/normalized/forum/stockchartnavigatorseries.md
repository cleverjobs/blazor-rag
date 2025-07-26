# StockChartNavigatorSeries

## Question

**Far** asked on 23 Aug 2024

Hi, I am using StockChartNavigator, Have 2 questions 1) How to change the area chart background color 2) How to call a function when user change the range selection using handles. I want to change some label values on my component based on date range

## Answer

**Hristian Stefanov** answered on 26 Aug 2024

Hi Farukh, I noticed that my colleague Nadezhda has already addressed these two questions in a private ticket. To ensure others who may have similar questions can benefit, I'll provide a quick summary below. 1) How to change the area chart background color: The chart's background color is controlled by the selected theme. For example, you can check out our Stock Chart demo and switch the theme to "Main Dark" to see how it affects the background color. Alternatively, you can use custom CSS to change the color. Here's an example I prepared for you: <style>.k-stockchart svg g path [d="M0 0 L 700 0 700 450 0 450Z" ] {
fill: aquamarine;
} </style> <TelerikStockChart Height="450px" Width="700px"> <StockChartCategoryAxes> <StockChartCategoryAxis BaseUnit="@ChartCategoryAxisBaseUnit.Years"> </StockChartCategoryAxis> </StockChartCategoryAxes> <StockChartSeriesItems> <StockChartSeries Type="StockChartSeriesType.Area" Name="Product 1" Data="@Data" Field="@nameof(ChartSeriesData.Product1Sales)" CategoryField="@nameof(ChartSeriesData.Year)"> </StockChartSeries> <StockChartSeries Type="StockChartSeriesType.Area" Name="Product 1" Data="@Data" Field="@nameof(ChartSeriesData.Product2Sales)" CategoryField="@nameof(ChartSeriesData.Year)"> </StockChartSeries> <StockChartNavigator> <StockChartNavigatorSeriesItems> <StockChartNavigatorSeries Type="StockChartSeriesType.Line" Name="Product 1" Data="@Data" Field="@(nameof(ChartSeriesData.Product1Sales))" CategoryField="@(nameof(ChartSeriesData.Year))"> </StockChartNavigatorSeries> </StockChartNavigatorSeriesItems> </StockChartNavigator> </StockChartSeriesItems> </TelerikStockChart> @code {
public List <ChartSeriesData> Data { get; set; }

protected override void OnInitialized()
{
Data=ChartSeriesData.GenerateData();
}

public class ChartSeriesData
{
public int Product1Sales { get; set; }
public double Product2Sales { get; set; }
public DateTime Year { get; set; }
public string SegmentName { get; set; }

public static List <ChartSeriesData> GenerateData()
{
List <ChartSeriesData> data=new List <ChartSeriesData> ();

for (int i=1; i <=3; i++)
{
var dataItem=new ChartSeriesData
{
Product1Sales=i,
Product2Sales=i + 1.123,
Year=new DateTime(2000 + i, 3, i),
SegmentName=$"{i * 100}"
};

data.Add(dataItem);
}

return data;
}
}
} 2) How to call a function when the user changes the range selection using handles (e.g., updating label values based on a date range): A feature request has been submitted for a Range Selection Change event. Regards, Hristian Stefanov
