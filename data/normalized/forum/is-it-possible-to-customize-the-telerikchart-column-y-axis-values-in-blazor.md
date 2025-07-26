# Is it possible to customize the telerikchart column y-axis values in blazor

## Question

**Ano** asked on 11 Nov 2024

I have a column chart with the x-axis representing whole month dates and each data point ranging in value from 0 to 86000. The y-axis now has a default range of 0 to 86000, with intervals of 10,000 each. I need to set the y-axis values to 0, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 17000, 22000, 26000, 30000, 34000, 43000, 60000, and 86000. There are a total of 16 iterations. Is it possible using TelerikChart in Blazor to adjust the y-axis values as shown above?

## Answer

**Dimo** answered on 13 Nov 2024

Hello Anoop, The described scenario requires the following configuration: Set Min, Max and MajorUnit to the ChartValueAxis in such a way that the Chart can render all desired label templates automatically. For example, the MajorUnit can be 1000. The Max parameter value must be greater than 86000. Use a ChartValueAxisLabels Template to render only some of the value (Y) axis labels conditionally, because they follow a custom step / skip logic. A logarithmic axis cannot be used together with MajorUnit, because the axis generates predefined units based on Min and Max. This means that the Chart may need to be very high to prevent overlapping of the large number of axis labels that are close to one another. <TelerikChart Height="1200px"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Data="@Series1Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 1"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Data="@Series2Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 2"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Area" Data="@Series3Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 3"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Max="86001" Min="0" MajorUnit="1000"> <ChartValueAxisLabels Template="chartValueAxisLabelTemplate" /> </ChartValueAxis> </ChartValueAxes> <ChartTitle Text="Revenue per Product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> <script suppress-error="BL9992"> function chartValueAxisLabelTemplate ( context ) { var visibleValues=[ 0, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 17000, 22000, 26000, 30000, 34000, 43000, 60000, 86000 ]; if (visibleValues.includes(context.value)) { return context.value;
} else { return "";
}
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
var monthsBack=6;

for (int i=1; i <=monthsBack; i++)
{
var dateTimeValue=now.AddMonths(-monthsBack + i);

Series1Data.Add(new SalesData()
{
Id=i,
Product="Product 1",
Revenue=Random.Shared.Next(0, 86000),
TimePeriod=dateTimeValue
});

Series2Data.Add(new SalesData()
{
Id=i,
Product="Product 2",
Revenue=Random.Shared.Next(0, 86000),
TimePeriod=dateTimeValue
});

Series3Data.Add(new SalesData()
{
Id=i,
Product="Product 3",
Revenue=Random.Shared.Next(0, 86000),
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
} If you prefer a logarithmic axis and a smaller Chart Height, then the setup can be similar to the one below. Note that logarithmic axes cannot have a Min value of zero. <TelerikChart Height="600px"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Data="@Series1Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 1"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Data="@Series2Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 2"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Area" Data="@Series3Data" Field="@nameof(SalesData.Revenue)" CategoryField="@nameof(SalesData.TimePeriod)" Name="Product 3"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Type="@ChartCategoryAxisType.Date"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis Max="100000" Type="@ChartValueAxisType.Logarithmic"> </ChartValueAxis> </ChartValueAxes> <ChartTitle Text="Revenue per Product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
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
var monthsBack=6;

for (int i=1; i <=monthsBack; i++)
{
var dateTimeValue=now.AddMonths(-monthsBack + i);

Series1Data.Add(new SalesData()
{
Id=i,
Product="Product 1",
Revenue=Random.Shared.Next(0, 86000),
TimePeriod=dateTimeValue
});

Series2Data.Add(new SalesData()
{
Id=i,
Product="Product 2",
Revenue=Random.Shared.Next(0, 86000),
TimePeriod=dateTimeValue
});

Series3Data.Add(new SalesData()
{
Id=i,
Product="Product 3",
Revenue=Random.Shared.Next(0, 86000),
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
} Regards, Dimo Progress Telerik
