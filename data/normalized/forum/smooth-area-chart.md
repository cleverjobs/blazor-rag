# Smooth Area chart

## Question

**Ila** asked on 27 Mar 2022

Is the ChartSeriesStyle.Smooth property supposed to work on Area chart as well? seems like it's working on a line chart only for me

## Answer

**Marin Bratanov** answered on 27 Mar 2022

Hi Ilan, Per the docs (direct link here: Area Chart - Line Style ), you need to use the ChartSeriesLine nested tag: [https://blazorrepl.telerik.com/QwEdcrkj34RcD5Xq04.](https://blazorrepl.telerik.com/QwEdcrkj34RcD5Xq04.) <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Area" Name="Product 1" Data="@series1Data"> <ChartSeriesLine Style="@ChartSeriesLineStyle.Smooth"> </ChartSeriesLine> </ChartSeries> <ChartSeries Type="ChartSeriesType.Area" Name="Product 2" Data="@series2Data"> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 7, 5 };
public List <object> series2Data=new List <object> () { 5, 12, 8, 2 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Marin Bratanov
