# Refreshing dynamically created charts

## Question

**Oma** asked on 20 Oct 2024

Hi, I have chart that is created dynamically. How to refresh all of the dynamically created charts. @foreach (var item in popData)
{ <TelerikChart Width="100%" Height="600px" @ref="PopChart"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Bar" Data="@item.chartData" Color="@item.borderColor" Field="@nameof(Classes.PopulationChartClass.count)" CategoryField="@nameof(Classes.PopulationChartClass.ageGroup)"> @* <ChartSeriesLabels Template="#=value# " Visible="@LabelVisable"> </ChartSeriesLabels> *@<ChartSeriesTooltip Visible="true"> <Template> </Template> </ChartSeriesTooltip> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="black"> <ChartValueAxisTitle Text="Population" /> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis> <ChartCategoryAxisLabels> <ChartCategoryAxisLabelsRotation Angle="315" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> }

## Answer

**Hristian Stefanov** answered on 21 Oct 2024

Hi Omar, To refresh all dynamically generated charts, assign a reference to each one and call the Refresh() method using that reference. Below is an example I’ve prepared to show you how to accomplish this: <TelerikButton OnClick="@RefreshCharts"> Refresh All Charts </TelerikButton> @foreach (var item in popData)
{ <TelerikChart Width="100%" Height="600px" @ref="@item.PopChart"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Bar" Data="@item.ChartData" Color="@item.BorderColor" Field="@nameof(PopulationChartClass.Count)" CategoryField="@nameof(PopulationChartClass.AgeGroup)"> <ChartSeriesTooltip Visible="true"> </ChartSeriesTooltip> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Color="black"> <ChartValueAxisTitle Text="Population" /> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis> <ChartCategoryAxisLabels> <ChartCategoryAxisLabelsRotation Angle="315" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> }

@code {
private List <PopulationChartData> popData; private void RefreshCharts()
{
foreach (var item in popData)
{ item.PopChart.Refresh(); }
} public class PopulationChartClass
{
public string AgeGroup { get; set; }
public int Count { get; set; }
}

public class PopulationChartData
{
public List <PopulationChartClass> ChartData { get; set; }
public string BorderColor { get; set; } public TelerikChart PopChart { get; set; } }

protected override void OnInitialized()
{
popData=new List <PopulationChartData> {
new PopulationChartData
{
ChartData=new List <PopulationChartClass> {
new PopulationChartClass { AgeGroup="0-18", Count=50000 },
new PopulationChartClass { AgeGroup="19-35", Count=75000 },
new PopulationChartClass { AgeGroup="36-55", Count=60000 },
new PopulationChartClass { AgeGroup="56-75", Count=40000 },
new PopulationChartClass { AgeGroup="75+", Count=20000 }
},
BorderColor="#3498db",
PopChart=new TelerikChart()
},
new PopulationChartData
{
ChartData=new List <PopulationChartClass> {
new PopulationChartClass { AgeGroup="0-18", Count=45000 },
new PopulationChartClass { AgeGroup="19-35", Count=82000 },
new PopulationChartClass { AgeGroup="36-55", Count=54000 },
new PopulationChartClass { AgeGroup="56-75", Count=30000 },
new PopulationChartClass { AgeGroup="75+", Count=15000 }
},
BorderColor="#2ecc71",
PopChart=new TelerikChart()
}
};
}
} Regards, Hristian Stefanov Progress Telerik
