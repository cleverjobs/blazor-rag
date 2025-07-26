# Heatmap chart

## Question

**Oma** asked on 30 Apr 2024

Hi, How can I rotate the angle of the Axis labels? I have tried everything but I might be missing something. <TelerikChart Width="100%" Height="100%"> <ChartTitle Text="Number of trips per day"> </ChartTitle> <ChartLegend Position="@ChartLegendPosition.Bottom"> </ChartLegend> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Heatmap" Name="" Data="@tripsListData" YField="@nameof(GetPublicTransportModified.tripsCountClass.trip_headsign)" XField="@nameof(GetPublicTransportModified.tripsCountClass.weekDayName)" Field="@nameof(GetPublicTransportModified.tripsCountClass.trips)"> <ChartSeriesTooltip Visible="true"> <Template> @{
var dataItem=context.DataItem as GetPublicTransportModified.tripsCountClass;
} <div> @($"{dataItem.weekDayName} contributions on {dataItem.trip_headsign}, week {dataItem.trips}") </div> </Template> </ChartSeriesTooltip> <ChartSeriesMarkers Type="@ChartSeriesMarkersType.RoundedRect" BorderRadius="5"> </ChartSeriesMarkers> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis> <ChartCategoryAxisLabels> <ChartCategoryAxisLabelsRotation Angle="315" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> </Content> </TabStripTab> </TelerikTabStrip> Many thanks, Omar

## Answer

**Hristian Stefanov** answered on 01 May 2024

Hi Omar, We have a knowledge base article that covers such cases: Prevent crowded labels in the Chart. Let me know if you are facing difficulties with any of the examples there. Regards, Hristian Stefanov Progress Telerik

### Response

**Omar** answered on 01 May 2024

Hi Hristian, I'm aware of the example you mentioned, and it seems to function well with all chart types except for the heatmap. I followed the example closely in the code I shared earlier, but it didn't work for the heatmap chart specifically. Could you possibly shed some light on why this might be happening and suggest any solutions? Best regards, Omar

### Response

**Hristian Stefanov** commented on 02 May 2024

Hi Omar, I have prepared an example with a Heatmap chart for you to use as a reference: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="@ChartSeriesType.Heatmap" Name="Commits Made per developer" Data="@HeatmapData" XField="@(nameof(MyHeatmapDataModel.Week))" YField="@(nameof(MyHeatmapDataModel.Day))" Field="@(nameof(MyHeatmapDataModel.CommitsNumber))"> </ChartSeries> </ChartSeriesItems> <ChartXAxes> <ChartXAxis> <ChartXAxisLabels> <ChartXAxisLabelsRotation Angle="-45"> </ChartXAxisLabelsRotation> </ChartXAxisLabels> </ChartXAxis> </ChartXAxes> <ChartYAxes> <ChartYAxis> <ChartYAxisLabels Visible="false"> </ChartYAxisLabels> </ChartYAxis> </ChartYAxes> </TelerikChart> @code {
public List <MyHeatmapDataModel> HeatmapData { get; set; }

protected override void OnInitialized()
{
HeatmapData=GetMyHeatmapData();
}

private List <MyHeatmapDataModel> GetMyHeatmapData()
{
List <MyHeatmapDataModel> data=new List <MyHeatmapDataModel> ()
{
new MyHeatmapDataModel("John", 14, 1, "Mon"),
new MyHeatmapDataModel("Idell", 8, 2, "Mon"),
new MyHeatmapDataModel("Ines", 13, 3, "Mon"),
new MyHeatmapDataModel("Stephen", 22, 4, "Mon"),
new MyHeatmapDataModel("John", 7, 1, "Tue"),
new MyHeatmapDataModel("Idell", 18, 2, "Tue"),
new MyHeatmapDataModel("Ines", 2, 3, "Tue"),
new MyHeatmapDataModel("Stephen", 5, 4, "Tue"),
new MyHeatmapDataModel("John", 10, 1, "Wed"),
new MyHeatmapDataModel("Idell", 11, 2, "Wed"),
new MyHeatmapDataModel("Ines", 20, 3, "Wed"),
new MyHeatmapDataModel("Stephen", 15, 4, "Wed")
};

return data;
}

public class MyHeatmapDataModel
{
public MyHeatmapDataModel() { }

public MyHeatmapDataModel(string devName, int commits, int week, string day)
{
DeveloperName=devName;
CommitsNumber=commits;
Week=week;
Day=day;
}

public string DeveloperName { get; set; }
public int CommitsNumber { get; set; }
public int Week { get; set; }
public string Day { get; set; }
}
} Kind Regards, Hristian

### Response

**Omar** commented on 02 May 2024

Hi, Nice, now it's working fine. Thanks, Omar
