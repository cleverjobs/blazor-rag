# Is it possible to specify the height of the labels on a chart category axis?

## Question

**Mar** asked on 14 Aug 2023

Hi We render a lot of charts with different sets of categories. We display the labels vertically and at an angle. Some have shorter names than others. This can make the charts appear differently and also move around as the label area expands and contracts. I will include an example picture. Is a parameter like the Height parameter of ChartLegend available? I have not been able to find it so far. If I have missed it could someone point me in the right direction. Just for context we have also: truncated long names to certain lengths. Attempted work arounds with padding vs label length but without a monospace font it is irregular Thanks

## Answer

**Svetoslav Dimitrov** answered on 17 Aug 2023

Hello Mark, Possibly the best way to achieve the desired behavior is by reducing the font size of the longer labels by utilizing the Font parameter. When text is concerned the "width" and "height" is controlled via font size. <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1 (bound to simple data)" Data="@simpleData"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Line" Name="Product 2 (bound to model)" Data="@modelData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesLabels Template="#=value# in #=dataItem.ExtraData# quarter" Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> <ChartCategoryAxisLabels Font="10px 'Times New Roman'"> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly sales trend"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> @code {
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
} Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Mark** commented on 17 Aug 2023

Thank you for your reply, Svetoslav. The font size does contribute to the size, that's correct. But we will not know which size to use to make a consistent visual. I'm going to include a REPL snippet to highlight the issue we have, I hope it is not too rough to see. How much of the chart is dynamically resized as we 'scroll' through a large dataset: [https://blazorrepl.telerik.com/mnEsPrFR015aV1Vj54](https://blazorrepl.telerik.com/mnEsPrFR015aV1Vj54) <TelerikChart Transitions="@false"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="Auction" Data="@visibleData" Field="@nameof(MyDataModel.FirstSeriesValue)"> <ChartSeriesStack Enabled="true"> </ChartSeriesStack> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Web Store" Data="@visibleData" Field="@nameof(MyDataModel.SecondSeriesValue)"> <ChartSeriesStack Enabled="true"> </ChartSeriesStack> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="red"> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Categories="@visibleXAxisItems"> <ChartCategoryAxisLabels Font="10px 'Times New Roman'"> <ChartCategoryAxisLabelsRotation Angle="45" Align="ChartAxisLabelsRotationAlignment.End" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Product Sales Per Storefront"> </ChartTitle> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart> <input style="display:block;width:100%;" id="scrollbar" type="range" min="0" max=@_scrollMaxValue value="1" class="slider" @oninput="(e)=> HandleScroll(e)" /> @code {
public class MyDataModel
{
public int FirstSeriesValue { get; set; }
public int SecondSeriesValue { get; set; }
public string ExtraData { get; set; }
}

private static List <MyDataModel> GenerateData(){
Random ran=new Random(2048);
return Enumerable.Repeat(1, 150)
.Select(i=> new MyDataModel{
FirstSeriesValue=ran.Next(10, 250),
SecondSeriesValue=ran.Next(10, 250)
}).ToList();
}

private static string[] GenerateLabels(){
Random ran=new Random(155);
return Enumerable.Repeat(string.Empty, 150)
.Select(i=> string.Join(
"-",
($"{Guid.NewGuid().ToString()}-{Guid.NewGuid().ToString()}".Split("-")).Take(ran.Next(1,9)))
)
.ToArray();
}

private List <MyDataModel> visibleData;
public List <MyDataModel> modelData;

public string[] xAxisItems;
public string[] visibleXAxisItems;

private int _scrollMaxValue=20;

protected override void OnInitialized()
{
modelData=GenerateData();
xAxisItems=GenerateLabels();

_scrollMaxValue=xAxisItems.Length - 20;

visibleData=modelData.Take(20).ToList();
visibleXAxisItems=xAxisItems.Take(20).ToArray();
}

private void HandleScroll(ChangeEventArgs e){
var value=Int32.Parse(e.Value!.ToString()!);
visibleData=modelData.Skip(value).Take(20).ToList();
visibleXAxisItems=xAxisItems.Skip(value).Take(20).ToArray();
}
}

### Response

**Svetoslav Dimitrov** commented on 22 Aug 2023

Hello Mark, We have an open feature request that once implemented can help you achieve the desired behavior - Custom rendering for Chart Series Labels - Visual Template. I can see that you have added your Vote for this feature and you can click the Follow button to receive email notifications on status updates, if you have not already. Once the feature is implemented, you will be able to take control of the labels in the Chart, understand their length, and take action accordingly.
