# ChartTitle Position

## Question

**Ila** asked on 06 Mar 2021

Is there a way to change all the ChartTitle text alignment? I need it to be left: 0 i.e: Currently X=113.5 <text style="font:18.288px &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;white-space:pre;" x="113.5" y="32" stroke="none" fill="rgb(33, 37, 41)" fill-opacity="1">...</text> I have several charts in the page

## Answer

**Marin Bratanov** answered on 08 Mar 2021

Hi Ilan, The <ChartTitle> exposes the Align parameter that you can use for this. As a general rule of thumb, when customizing the charts, look for parameters and nested tags as described here: [https://docs.telerik.com/blazor-ui/components/chart/overview#customize-chart-elements---nested-tags-settings.](https://docs.telerik.com/blazor-ui/components/chart/overview#customize-chart-elements---nested-tags-settings.) <TelerikChart> <ChartTitle Text="Quarterly sales trend" Align="@ChartTitleAlign. Left "> </ChartTitle> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1 (bound to simple data)" Data="@simpleData"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2 (bound to model)" Data="@modelData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesLabels Template="#=value# in #=dataItem.ExtraData# quarter" Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> @code {
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
} Regards, Marin Bratanov
