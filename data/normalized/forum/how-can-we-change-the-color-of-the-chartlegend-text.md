# How can we change the color of the ChartLegend text?

## Question

**Dav** asked on 08 Apr 2022

ChartTitle has a Color property, but ChartLegend does not. How can I change the text to white?

## Answer

**Svetoslav Dimitrov** answered on 11 Apr 2022

Hello David, You can use the ChartLegendLabels tag and the exposed Color attribute to change the text color. Below, I have added a basic code snippet where you can see the configuration. <TelerikChart Class="custom-legend-color"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1 (bound to simple data)" Data="@simpleData"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2 (bound to model)" Data="@modelData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesLabels Template="#=value# in #=dataItem.ExtraData# quarter" Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly sales trend"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> <ChartLegendLabels Color="yellow"> </ChartLegendLabels> </ChartLegend> </TelerikChart> @code {
public class MyDataModel
{
public int SecondSeriesValue { get; set; }
public string ExtraData { get; set; }

}

public List <MyDataModel> modelData=new List <MyDataModel> ()
{
new MyDataModel() { SecondSeriesValue=1, ExtraData="first" },
new MyDataModel() { SecondSeriesValue=5, ExtraData="second" },
new MyDataModel() { SecondSeriesValue=3, ExtraData="third" },
new MyDataModel() { SecondSeriesValue=2, ExtraData="fourth" },
};

public List <object> simpleData=new List <object> () { 10, 2, 7, 5 };

public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Svetoslav Dimitrov
