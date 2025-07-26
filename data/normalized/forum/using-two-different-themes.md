# Using two different themes

## Question

**Han** asked on 02 Dec 2024

On the Telerik website, more specifically on Blazor Charts and Graphs - Overview, you can find a nice example of how to change the theme of the charts displayed. We would like to implement something like this in our project. However, a change in the theme affects the entire project. However, we would like the entire project not to be changed and the change in the theme only affects the Telerik chart. I would like to know if anyone has a good idea for us.

## Answer

**Hristian Stefanov** answered on 02 Dec 2024

Hi Hans, I can confirm that it is possible to apply a specific theme to an individual page without impacting the entire project by including the CDN link for the desired theme directly on that page. Here’s an example below for your reference. As a result, you can see that the chart on the " Home.razor " page is with the theme of the app and the chart on the " Counter.razor " page is with a dark theme. Home.razor @page "/" <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1 (bound to simple data)" Data="@simpleData"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2 (bound to model)" Data="@modelData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesLabels Template="#=value# in #=dataItem.ExtraData# quarter" Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly sales trend"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> @code {
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

private List <object> simpleData=new List <object> () { 10, 2, 7, 5 };

private string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Counter.razor @page "/counter" <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/7.0.0/kendo-theme-default/swatches/default-main-dark.css"](https://blazor.cdn.telerik.com/blazor/7.0.0/kendo-theme-default/swatches/default-main-dark.css") /> <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1 (bound to simple data)" Data="@simpleData"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2 (bound to model)" Data="@modelData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesLabels Template="#=value# in #=dataItem.ExtraData# quarter" Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly sales trend"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> @code {
public class MyDataModel
{
public int SecondSeriesValue { get; set; }
public string ExtraData { get; set; }
}

private List <MyDataModel> modelData=new List <MyDataModel> ()
{
new MyDataModel() { SecondSeriesValue=1, ExtraData="first" },
new MyDataModel() { SecondSeriesValue=5, ExtraData="second" },
new MyDataModel() { SecondSeriesValue=3, ExtraData="third" },
new MyDataModel() { SecondSeriesValue=2, ExtraData="fourth" },
};

private List <object> simpleData=new List <object> () { 10, 2, 7, 5 };

private string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Regards, Hristian Stefanov Progress Telerik

### Response

**Hans** commented on 03 Dec 2024

First of all, thank you very much for the quick reply. However, in your solution the whole page is changed, so the header, footer and menu have a dark theme. But I only want the chart to be with the dark theme and not the whole page.

### Response

**Hristian Stefanov** commented on 03 Dec 2024

Hi Hans, Apologies if the approach I shared earlier didn't fully address your specific scenario. The method we use on our demo page for theme switching is the same. I initially assumed you were aiming to change the theme for individual pages. Overall, the Chart component doesn't directly rely on the page's CSS; instead, it derives its styles from the active theme for the page. To update the Chart's theme, you'll need to either switch the theme for the entire current page using the previously shared approach or apply the theme change globally to the app. Modifying the theme for a single component is not supported. Still, for customizing the styles of individual components, such as Charts, you can use parameters like Color and ColorField to achieve tailored styling. Kind Regards, Hristian
