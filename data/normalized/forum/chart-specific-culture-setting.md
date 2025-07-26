# Chart-Specific Culture Setting

## Question

**Oma** asked on 26 Nov 2024

Hi, Is there a way to set the Y-axis culture directly within the chart? I prefer not to apply the culture globally. Thank you, Omar

### Response

**Omar** commented on 30 Nov 2024

Any one, is my question difficult for Telerik team.

## Answer

**Hristian Stefanov** answered on 02 Dec 2024

Hi Omar, I can confirm that every element of the Chart, including the Y-axis, adheres to the component's culture, which is determined by the app's culture settings. However, you can customize the Y-axis labels using the Format parameter to achieve the desired appearance. If the Format parameter alone does not provide the level of customization you need, the component also offers a label template for further styling and adjustments. Here is the relevant documentation: Label Template and Format. <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Data="@Series1Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 1"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Data="@Series2Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 2"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Area" Data="@Series3Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 3"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Max="1200"> <ChartValueAxisLabels Template="yAxisLabelTemplate" Format="c2" /> </ChartValueAxis> </ChartValueAxes> <ChartTitle Text="Revenue per Product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> <script suppress-error="BL9992" nonce="BL9992"> function yAxisLabelTemplate ( context ) { // use context.value or context.text return context.text.replace( ".", "," );
} </script> @code {
private List <SalesData> Series1Data { get; set; }=new();
private List <SalesData> Series2Data { get; set; }=new();
private List <SalesData> Series3Data { get; set; }=new();

protected override async Task OnInitializedAsync()
{
GenerateData();

await base.OnInitializedAsync();
}

private void GenerateData()
{
var now=DateTime.Today;
var monthsBack=12;

for (int i=1; i <=monthsBack; i++)
{
var dateTimeValue=now.AddMonths(-monthsBack + i);

Series1Data.Add(new SalesData()
{
Id=i,
Product="Product 1",
Revenue=Random.Shared.Next(1, 1000),
TimePeriod=dateTimeValue
});

Series2Data.Add(new SalesData()
{
Id=i,
Product="Product 2",
Revenue=Random.Shared.Next(1, 1000),
TimePeriod=dateTimeValue
});

Series3Data.Add(new SalesData()
{
Id=i,
Product="Product 3",
Revenue=Random.Shared.Next(1, 1000),
TimePeriod=dateTimeValue
});
}
}

public class SalesData
{
public int Id { get; set; }
public string Product { get; set; }=string.Empty;
public DateTime TimePeriod { get; set; }
public decimal Revenue { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik
