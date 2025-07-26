# Aligned chart with different column sizes

## Question

**Dat** asked on 10 Jun 2020

I have 2 different concepts which are displayed together with a shared category axis. Currently there is a 1 to 1 mapping between each. Is it possible to align each in every category so that they are vertically aligned? Currently they seem to display side by side. This might be because the bottom column can be vary large and in the worst case go all the way to the top. In addition can the bottom column be made to be larger and a different z-index then the top chart? For instance in the image the bottom column would grow from top to bottom and be visually larger than the top column. Therefore any overlap would be visually easy to distinguish.

## Answer

**Marin Bratanov** answered on 11 Jun 2020

Hello Patrick, I am not sure I understand the question and the need, but something similar to what I see on the screenshot can be achieved in two ways: use two x-axes, populate them with the same categories, set the crossing point of the second to be high enough (e.g., by examining the maximum value of the orange series). Here's docs on multiple axes so you can see examples and configuration options: entire article and direct link to categorical series section. If the values of the "lower" series are large enough, they can go above the other series. The series that is defined later in the chart markup is at the top. By default, two series can be bound to the same category axis and can be shown side by side, which is usually easier for comparison, you can see similar examples here. I'd also encourage you to review the data binding article to see how you can fix series data points to categories, combine or separate categories. We are also working on a financial type of chart that shows several dimensions of a single data point, similar to this one, so you may find this useful (it is planned for this summer). That said, here's an example based on the docs above that puts one series above the other: <TelerikChart>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 2" Data="@chartData" CategoryAxis="secondAxis" Color="blue" Field="@nameof(MyDataModel.Product2)" CategoryField="@nameof(MyDataModel.SecondSeriesCategories)">
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 1" Data="@chartData" CategoryAxis="firstAxis" Color="red" Field="@nameof(MyDataModel. Product1 )" CategoryField="@nameof(MyDataModel.FirstSeriesCategories)" Opacity="0.5">
</ChartSeries>
</ChartSeriesItems>

<ChartCategoryAxes>
<ChartCategoryAxis Name="firstAxis" Color="red"></ChartCategoryAxis>
<ChartCategoryAxis Name="secondAxis" Color="blue"></ChartCategoryAxis>
</ChartCategoryAxes>

<ChartValueAxes>
<ChartValueAxis AxisCrossingValue="@crossingPoints"></ChartValueAxis>
</ChartValueAxes>
</TelerikChart>

@code { public class MyDataModel { public string FirstSeriesCategories { get; set; } public string SecondSeriesCategories { get; set; } public int Product1 { get; set; } public int Product2 { get; set; }
} public List<MyDataModel> chartData=new List<MyDataModel>()
{ new MyDataModel() { FirstSeriesCategories="a", SecondSeriesCategories="e", Product1=1, Product2=20 }, new MyDataModel() { FirstSeriesCategories="match", SecondSeriesCategories="match", Product1=2, Product2=30 }, new MyDataModel() { FirstSeriesCategories="c", SecondSeriesCategories="g", Product1=100, Product2=40 }, new MyDataModel() { FirstSeriesCategories="d", SecondSeriesCategories="h", Product1=4, Product2=50 },
}; public object [] crossingPoints=new object [] { -9999999, 20 };
} Regards, Marin Bratanov
