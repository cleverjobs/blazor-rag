# Pie chart labels: can they be configured to overlay the chart itself

## Question

**Kyl** asked on 16 Dec 2024

I want to show a series of pie charts but with the series labels on top of each section like so: I haven't found anything that suggests the labels can be anywhere except attached by lines. Is this possible?

## Answer

**Hristian Stefanov** answered on 17 Dec 2024

Hi Kyle, To display the labels on top of each section in a pie chart, you can configure the ChartSeriesLabels to position the labels inside the pie sections. Here's how you can achieve this: Set the Position of Labels: Use the Position property of ChartSeriesLabels and set it to ChartSeriesLabelsPosition.Center to place the labels inside the pie sections. Enable the Labels: Ensure that the labels are enabled by setting the Visible property of ChartSeriesLabels to true. Here's a code snippet to illustrate this configuration: <TelerikChart Width="600px" Height="600px"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Donut" Data="@donutData" Field="@nameof(MyDonutChartModel.SegmentValue)" CategoryField="@nameof(MyDonutChartModel.SegmentName)"> <ChartSeriesLabels Visible="true" Position="ChartSeriesLabelsPosition.Center" Template="@labelTemplate"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartTitle Text="Revenue per product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
private string labelTemplate="#=dataItem.SegmentCategory#";

public class MyDonutChartModel
{
public string SegmentName { get; set; }
public double SegmentValue { get; set; }
public bool ShouldShowInLegend { get; set; }=true;
public string SegmentCategory { get; set; }
}

private List <MyDonutChartModel> donutData=new List <MyDonutChartModel> {
new MyDonutChartModel
{
SegmentName="Product 1",
SegmentValue=2,
SegmentCategory="Category 1"
},
new MyDonutChartModel
{
SegmentName="Product 2",
SegmentValue=3,
SegmentCategory="Category 2"
},
new MyDonutChartModel
{
SegmentName="Product 3",
SegmentValue=4,
SegmentCategory="Category 3"
}
};
} Regards, Hristian Stefanov Progress Telerik

### Response

**Kyle** commented on 17 Dec 2024

Oh bother, I should have read the docs more closely. I thought all of the position options related to the label's position relative to the line. Thank you. That works for me.
