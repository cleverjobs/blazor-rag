# Charts: prevent no data template

## Question

**Tho** asked on 09 Jan 2025

Dear Telerik Support team, as of version 7.1.0 the No Data Template was introduced for Charts and I was wondering, if there's any chance to prevent the chart of rendering the no data template, when none is defined and needed. In my case I'd rather display an empty chart, instead of the no data template. Any way to accomplish that? Many thanks! Thomas

## Answer

**Tsvetomir** answered on 10 Jan 2025

Hello Thomas, Thank you for the clear explanation of the result you are looking for. Indeed, it is possible to display an empty Chart when there is no data. To achieve that, override the default theme styles with the following CSS approach: <TelerikButton OnClick="@UpdateData"> @ButtonContent </TelerikButton> <br /> <TelerikChart @ref="ChartRef" Width="800px" Height="400px"> <ChartTitle Text="Product Sales Over the Years" Position="@ChartTitlePosition.Bottom"> </ChartTitle> <ChartSettings> @* Define what should be shown when there's no data in the chart *@<NoDataTemplate> <p> No data available to display. Please add product data or check back later. </p> </NoDataTemplate> </ChartSettings> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Data="@ChartData" Name="Product Sales" Field="@nameof(ChartSeriesData.ProductSales)" CategoryField="@nameof(ChartSeriesData.Year)"> </ChartSeries> </ChartSeriesItems> </TelerikChart> <style>.k-chart-overlay { display: none;
} </style> @code {
private const string Add="Add Data";
private const string Remove="Remove Data";

private TelerikChart ChartRef { get; set; }
private List <ChartSeriesData> ChartData { get; set; }=new List <ChartSeriesData> ();
private string ButtonContent { get; set; }=Add;

private void UpdateData()
{
if (ChartData==null || ChartData?.Count()==0)
{
ChartData=ChartSeriesData.GenerateData();
ButtonContent=Remove;
}
else
{
// Clear the data
ChartData=new List <ChartSeriesData> ();
ButtonContent=Add;
}
ChartRef.Refresh(); // Refresh the Chart
}

public class ChartSeriesData
{
public int ProductSales { get; set; }
public int Year { get; set; }

public static List <ChartSeriesData> GenerateData()
{
List <ChartSeriesData> data=new List <ChartSeriesData> {
new ChartSeriesData { ProductSales=120, Year=2020 },
new ChartSeriesData { ProductSales=180, Year=2021 },
new ChartSeriesData { ProductSales=150, Year=2022 },
new ChartSeriesData { ProductSales=210, Year=2023 },
new ChartSeriesData { ProductSales=90, Year=2024 }
};

return data;
}
}
} I hope this serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik
