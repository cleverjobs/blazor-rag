# Changing the color / opacity of the legend label for a hidden chart series

## Question

**IanIan** asked on 12 May 2024

I have a chart where clicking the legend for a series will toggle its visibility. However, when the series is hidden, the legend label gets becomes a very light grey, and some users struggle to see it I can't find any particular property on any of the chart related elements that seems to be able to change the font/colour/opacity settings in that scenario. Is there anything I've missed?

## Answer

**Tsvetomir** answered on 13 May 2024

Hi Ian, Thank you for the clear explanation of the scenario you are facing. To customize the legend items of a Chart, use the following CSS selector: .custom-legend-class svg> g> g:nth-last-child ( 2 )> g> g [transform] [aria-checked="false" ]> g:nth-child ( 2 )> text This CSS combinator targets the text of Chart legend items that are disabled (not clicked). With it, the color of the label can be changed through the " fill " CSS attribute. For your convenience, I have crafted an example for you that utilizes the above CSS approach: <style>.custom-legend svg> g> g:nth-last-child ( 2 )> g> g [transform] [aria-checked="false" ]> g:nth-child ( 2 )> text {
fill: red;
} </style> <TelerikChart OnLegendItemClick="@OnChartLegendClick" Transitions="false" Class="custom-legend"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Data="@Series1Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Smartphones" Visible="@( SeriesVisible(0) )"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Data="@Series2Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Tablets" Visible="@( SeriesVisible(1) )"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Data="@Series3Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Headphones" Visible="@( SeriesVisible(2) )"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Max="1000"> </ChartValueAxis> </ChartValueAxes> <ChartTitle Text="Revenue per Product Line"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> @code {
private List <SalesData> Series1Data { get; set; }=new List <SalesData> ();
private List <SalesData> Series2Data { get; set; }=new List <SalesData> ();
private List <SalesData> Series3Data { get; set; }=new List <SalesData> ();

private int? ChartLegendClickIndex { get; set; }

private bool SeriesVisible(int idx)
{
return ChartLegendClickIndex==null || ChartLegendClickIndex==idx;
}

private async Task OnChartLegendClick(ChartLegendItemClickEventArgs args)
{
Console.WriteLine($"Clicked legend item {args.Text} with series index {args.SeriesIndex}.");

if (ChartLegendClickIndex !=args.SeriesIndex)
{
ChartLegendClickIndex=args.SeriesIndex;
}
else
{
ChartLegendClickIndex=null;
}
}

protected override void OnInitialized()
{
var rnd=new Random();
var now=DateTime.Today;
var monthsBack=12;

for (int i=1; i <=monthsBack; i++)
{
var dateTimeValue=now.AddMonths(-monthsBack + i);

Series1Data.Add(new SalesData()
{
Id=i,
Product="Smartphones",
Revenue=rnd.Next(500, 900),
TimePeriod=dateTimeValue
});
Series2Data.Add(new SalesData()
{
Id=i,
Product="Tablets",
Revenue=rnd.Next(300, 700),
TimePeriod=dateTimeValue
});
Series3Data.Add(new SalesData()
{
Id=i,
Product="Headphones",
Revenue=rnd.Next(100, 400),
TimePeriod=dateTimeValue
});
}

base.OnInitialized();
}

public class SalesData
{
public int Id { get; set; }
public string Product { get; set; }
public DateTime TimePeriod { get; set; }
public decimal Revenue { get; set; }
}
} Regards, Tsvetomir Progress Telerik

### Response

**Ian** commented on 13 May 2024

That's perfect, thanks very much
