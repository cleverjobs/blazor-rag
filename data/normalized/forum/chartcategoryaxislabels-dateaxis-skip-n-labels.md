# ChartCategoryAxisLabels DateAxis Skip n Labels

## Question

**ran** asked on 15 Feb 2020

I don't want to render fewer categories values on the chart itself. I just want to render the category axis label every n times so that you can read them when there are a lot of data points. I don't want to lose the granularity. See the date category axis in the attached screen shot please. Suggestions?

## Answer

**Marin Bratanov** answered on 15 Feb 2020

Hi Randy, If you are using a real Date axis ( ChartCategoryAxis="@ChartCategoryAxisType.Date" ), the chart will always perform some aggregation of the data based on the base units. If you don't want that - create string fields in the model that will hold the desired string representation of the dates and use them in a "regular" chart (that is, one that does not use ChartCategoryAxisType.Date). This will create one x-axis item per model data point and they will all be evenly spaced. That said, you can set that every n-th label will be rendered through the Step parameter of the x-axis labels. Here's an example I made for you: <TelerikChart>

<ChartCategoryAxes>
<ChartCategoryAxis Type="ChartCategoryAxisType.Date">
<ChartCategoryAxisLabels Step="7" />
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 1 (SUM)" Data="@chartData" Field="@nameof(MyDataModel.Product1)" CategoryField="@nameof(MyDataModel.MySharedCategories)" Aggregate="ChartSeriesAggregate.Sum">
<ChartSeriesLabels Visible="true"></ChartSeriesLabels>
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 2 (COUNT)" Data="@chartData" Field="@nameof(MyDataModel.Product2)" Aggregate="ChartSeriesAggregate.Count">
<ChartSeriesLabels Visible="true"></ChartSeriesLabels>
</ChartSeries>
</ChartSeriesItems>

</TelerikChart>

@code { public class MyDataModel { public DateTime MySharedCategories { get; set; } public int Product1 { get; set; } public int Product2 { get; set; }
} public List<MyDataModel> chartData=new List<MyDataModel>()
{ new MyDataModel() { MySharedCategories=new DateTime( 2019, 11, 11 ), Product1=1, Product2=2 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 15 ), Product1=2, Product2=3 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 19 ), Product1=3, Product2=4 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 28 ), Product1=4, Product2=5 },
};
} You may also want to rotate the labels vertically, especially if the Format you use is longer - this will make them narrower so you will be able to see more of them without overlap. Here's a basic example: <TelerikChart>

<ChartCategoryAxes>
<ChartCategoryAxis Type="ChartCategoryAxisType.Date">
<ChartCategoryAxisLabels Step="7"> <ChartCategoryAxisLabelsRotation Angle="-90" /> </ChartCategoryAxisLabels>
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 1 (SUM)" Data="@chartData" Field="@nameof(MyDataModel.Product1)" CategoryField="@nameof(MyDataModel.MySharedCategories)" Aggregate="ChartSeriesAggregate.Sum">
<ChartSeriesLabels Visible="true"></ChartSeriesLabels>
</ChartSeries>
<ChartSeries Type="ChartSeriesType.Column" Name="Product 2 (COUNT)" Data="@chartData" Field="@nameof(MyDataModel.Product2)" Aggregate="ChartSeriesAggregate.Count">
<ChartSeriesLabels Visible="true"></ChartSeriesLabels>
</ChartSeries>
</ChartSeriesItems>

</TelerikChart>

@code { public class MyDataModel { public DateTime MySharedCategories { get; set; } public int Product1 { get; set; } public int Product2 { get; set; }
} public List<MyDataModel> chartData=new List<MyDataModel>()
{ new MyDataModel() { MySharedCategories=new DateTime( 2019, 11, 11 ), Product1=1, Product2=2 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 15 ), Product1=2, Product2=3 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 19 ), Product1=3, Product2=4 }, new MyDataModel() { MySharedCategories=new DateTime( 2019, 12, 28 ), Product1=4, Product2=5 },
};
} Regards, Marin Bratanov

### Response

**randy** answered on 15 Feb 2020

Fantastic support! Thank you
