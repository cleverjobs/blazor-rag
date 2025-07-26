# Padding chart line area

## Question

**Iva** asked on 14 Feb 2021

Hello! Please help with border padding for chart area. Min and Max for X-axe getting automatically by code. Need some padding to correct display first and last x-values

## Answer

**Eric R | Senior Technical Support Engineer** answered on 16 Feb 2021

Hi Ivan, Thank you for providing the screenshot. I was able to produce similar behavior when using the Min/Max values of a Scatter chart series dataset. From what I understand, since the value is retrieved from code, it may be possible to decrease/increase the Min/Max values on the X-Axis. Let me provide an example of what that would look like below. Example Using the scatter sample, I was able to reproduce a similar output from the provided screenshot. Note the GetMin and GetMax functions is where the value is increased or decreased accordingly. <TelerikChart> <ChartTitle Text="Unrecoverable Errors Per Minute vs. Signal Level"> </ChartTitle> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series1Data" Name="APSK modulation" XField="@nameof(ModelData.Strength)" YField="@nameof(ModelData.Errors)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series2Data" Name="QAM modulation" XField="@nameof(ModelData.Strength)" YField="@nameof(ModelData.Errors)"> </ChartSeries> </ChartSeriesItems> <ChartXAxes> <ChartXAxis Max="@GetMax()" Min="@GetMin()" AxisCrossingValue="@(new object[] { -100 })"> <ChartXAxisTitle Text="Signal Strength, dBm"> </ChartXAxisTitle> </ChartXAxis> </ChartXAxes> <ChartYAxes> <ChartYAxis> <ChartYAxisTitle Text="Error count"> </ChartYAxisTitle> </ChartYAxis> </ChartYAxes> </TelerikChart> @code {
#region scatter example
public class ModelData
{
public double Strength { get; set; }
public double Errors { get; set; }
}

double GetMax()
{
double max1=Series1Data.Max(p=> p.Strength);
double max2=Series2Data.Max(p=> p.Strength); return max1> max2 ? max1 + 1 : max2 + 1; }

double GetMin()
{
double min1=Series1Data.Min(p=> p.Strength);
double min2=Series2Data.Min(p=> p.Strength); return min1 <min2? min1 - 1: min2 - 1; } public List <ModelData> Series1Data=new List <ModelData> ()
{
new ModelData { Strength=-82, Errors=15 },
new ModelData { Strength=-79, Errors=13 },
new ModelData { Strength=-77, Errors=10 },
new ModelData { Strength=-74, Errors=7 },
new ModelData { Strength=-70, Errors=3 },
new ModelData { Strength=-65, Errors=1 }
};

public List <ModelData> Series2Data=new List <ModelData> ()
{
new ModelData { Strength=-80, Errors=25 },
new ModelData { Strength=-76, Errors=22 },
new ModelData { Strength=-73, Errors=17 },
new ModelData { Strength=-70, Errors=15 },
new ModelData { Strength=-65, Errors=12 },
new ModelData { Strength=-61, Errors=10 },
new ModelData { Strength=-55, Errors=7 },
new ModelData { Strength=-50, Errors=3 }
};
#endregion

} Before and After Output The following screenshot is taken when using the GetMin/GetMax values of the series data. The next screenshot is the output after increasing or decreasing the GetMax and GetMin values. Wrapping Up Ultimately, the above workaround may or may not work with your scenario as I am unable to see the chart markup or code-behind from the provided screenshot. If the above fix doesn't work for your scenario, I ask that you provide more information about how the chart is declared and how the Min/Max values are calculated. In the meantime, please let me know if you need any additional information. Thank you for using the Blazor Forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Ivan** answered on 17 Feb 2021

Hi Eric! Thanks for your quick reply. Of course, i'm used this workround with decrease/increase the Min/Max values on the X-Axis But this not suitable for my chart, because all values on the x-axis must correspond to a certain number (serial number of the laboratory) In a dataset, for example, there are 1-10 laboratories. I cannot extend the x-axis to values 0 - 11 and show lab numbers 0 and 11 since they do not exist.

### Response

**Eric R | Senior Technical Support Engineer** answered on 18 Feb 2021

Hi Ivan, Thank you for providing more specifics about your scenario. Unfortunately, it still is not enough information to completely understand the exact issue as I am unable to see how the chart is declared and configured. For example, in this case, it is important to know what chart type is in use and whether the X-Axis is categorical or numerical. If the axis is numerical I can see no reason why its min and max cannot be extended to provide the desired space - values on a numerical axis are not discreet anyway. If you do need discreet values, you should use a categorical chart (like a line chart) rather than a numerical chart (scatterline) to clearly denote those items on the x-axis with their descriptions instead of arbitrary numbers. So, it may be that the Justified configuration chart feature is what you are looking for. This would provide the ability to add/remove space at the beginning and end of the series for categorical charts. If this is the case, this feature is currently unavailable. We do have an existing public feature request that I have gone ahead and cast a vote on your behalf. I also encourage following the item to receive notifications of status updates. Please let me know if you need any additional information. Thank you. Regards, Eric R | Senior Technical Support Engineer
