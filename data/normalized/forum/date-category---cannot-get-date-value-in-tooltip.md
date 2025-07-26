# Date category - cannot get date value in tooltip

## Question

**Nic** asked on 13 Nov 2020

Hi, This is a bit weird, and it might even be a framework problem. I have a date series line chart which has a date category axis and a numeric value axis. It's all working fine. I wanted to add a tooltip template so that when the user hovers over a point it shows the date and the value. I can display the value fine, but the date is always set to DateTime.MinValue for some odd reason. My class is called UiVami and looking at my code, I can see the list of values is being created OK. Nowhere else do I ever change the Date value. In an attempt to debug it, I changed my class to have immutable properties with a constructor that throws an exception when the DateTime passed in is equal to DateTime.MinValue. This exception is being hit when I hover the mouse over a point - suggesting that something in the grid/framework is creating a new UIVami and setting the DateTime to null! public class UiVami { public DateTime Date { get; } public decimal Value { get; } public UiVami(DateTime date, decimal value) { if (date==DateTime.MinValue) { throw new Exception( "arrgh" ); } Date=date; Value=value; } } I'm actually binding via this type which contains a list of of VAMIs: public class UiVamiSet { public string InstrumentName { get; set; } public List<UiVami> Vamis { get; set; } } Here's my code for the chart: <TelerikChart @ref="@_vamiChart" Width="100%" Height="100%"> <ChartSeriesItems> @foreach (var vamiSet in _uiVamiSets) { <ChartSeries Type="ChartSeriesType.Line" Name="@vamiSet.InstrumentName" Field="@nameof(UiVami.Value)" CategoryField="@nameof(UiVami.Date)" Data="@vamiSet.Vamis"> <ChartSeriesMarkers Visible="false"></ChartSeriesMarkers> <ChartSeriesTooltip Visible="true"> <Template> @{ var dataItem=context.DataItem as UiVami; } <div> <strong>@vamiSet.InstrumentName</strong> </div> <div> @dataItem.Date - @dataItem.Value </div> </Template> </ChartSeriesTooltip> </ChartSeries> } </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis NarrowRange="true"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Date"> <ChartCategoryAxisLabels Step="3"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Fund Performance"></ChartTitle> <ChartLegend Position="ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> Any help appreciated! Thanks.

## Answer

**Svetoslav Dimitrov** answered on 18 Nov 2020

Hello Nick, When you use a Date axis chart the DataItem will contain only the aggregated value in the corresponding y-value field, because it is a collection of more than one item. Instead, you can use the Category to filter the data source and obtain the actual data items from the data source in case you want to provide extra information about them. More information on what fields the context provides can be found here. Below, I have created a quick example of how I have achieved it: <TelerikChart>

<ChartCategoryAxes>
<ChartCategoryAxis BaseUnit="ChartCategoryAxisBaseUnit.Minutes" Type="ChartCategoryAxisType.Date">
<ChartCategoryAxisLabels Step="60"></ChartCategoryAxisLabels>
</ChartCategoryAxis>
</ChartCategoryAxes>

<ChartSeriesItems>
<ChartSeries Type="Telerik.Blazor.ChartSeriesType.Column" Name="Product 1 (SUM)" Data="@chartData" Field="@nameof(MyDataModel.Product1)" CategoryField="@nameof(MyDataModel.MySharedCategories)" Aggregate="ChartSeriesAggregate.Sum">
<ChartSeriesLabels Visible="false"></ChartSeriesLabels>
<ChartSeriesTooltip Visible="true">
<Template>
@{
DateTime dateCategory=DateTime.Parse(context.Category.ToString()); var dataItems=GetDataPointsFromCategory(dateCategory); var currentItem=dataItems.Where(x=>
x.MySharedCategories.Date==dateCategory.Date
&& x.MySharedCategories.Hour==dateCategory.Hour &&
x.MySharedCategories.Minute==dateCategory.Minute).FirstOrDefault();

<div>
@currentItem.TooltipText
</div>
}
</Template>
</ChartSeriesTooltip>
<ChartSeriesStack Group="Stack1"></ChartSeriesStack>
</ChartSeries>
<ChartSeries Type="Telerik.Blazor.ChartSeriesType.Column" Name="Product 2 (SUM)" Data="@chartData" Field="@nameof(MyDataModel.Product2)" CategoryField="@nameof(MyDataModel.MySharedCategories)" Aggregate="ChartSeriesAggregate.Sum">
<ChartSeriesLabels Visible="false"></ChartSeriesLabels>
<ChartSeriesTooltip Visible="true">
<Template>
@{
DateTime dateCategory=DateTime.Parse(context.Category.ToString()); var dataItems=GetDataPointsFromCategory(dateCategory); var currentItem=dataItems.Where(x=>
x.MySharedCategories.Date==dateCategory.Date
&& x.MySharedCategories.Hour==dateCategory.Hour &&
x.MySharedCategories.Minute==dateCategory.Minute).FirstOrDefault();

<div>
@currentItem.TooltipText
</div>
}
</Template>
</ChartSeriesTooltip>
<ChartSeriesStack Group="Stack1"></ChartSeriesStack>
</ChartSeries>
</ChartSeriesItems>

</TelerikChart>

@code { public class MyDataModel { public DateTime MySharedCategories { get; set; } public decimal Product1 { get; set; } public decimal Product2 { get; set; } public string TooltipText { get; set; }
} List<MyDataModel> GetDataPointsFromCategory ( DateTime category ) { return chartData.Where(x=>
x.MySharedCategories.Year==category.Year && x.MySharedCategories.Month==category.Month).ToList();
} public List <MyDataModel> chartData=new List<MyDataModel>(); protected override void OnInitialized ( ) { var random=new Random(); for ( var i=0; i <20; i++)
{ var dateTime=new DateTime( 2019, 1, 1 ); var value1=Convert.ToDecimal(random.NextDouble() * 10 ); var value2=Convert.ToDecimal(random.NextDouble() * 10 ); this.chartData.Add( new MyDataModel { MySharedCategories=dateTime.AddMinutes(i * 15 ), Product1=value1, Product2=value2, TooltipText="00:15: 0,04 kWh" });
}
}
} Regards, Svetoslav Dimitrov

### Response

**Nick** answered on 19 Nov 2020

Thanks Svetoslav, I'll take a look at this!
