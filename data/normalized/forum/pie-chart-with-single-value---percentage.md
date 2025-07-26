# Pie Chart with Single Value - Percentage

## Question

**Jon** asked on 31 Mar 2020

Hi How do I create a chart. I want bind a single value / a percentage - like 66% (.66). For example disk space remaining. I have Drive object with PercentFree. When this renders I get a full blue pie chart. Enclosed is 8 percent <TelerikChart Width="100%" Height="100%" Transitions="false" RenderAs="@RenderingMode.SVG"> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Pie" Data="@DriveData" Field="@nameof(Drive.PercentFree)" CategoryField="@nameof(Drive.Name)" ExplodeField="@nameof(Drive.Explode)"> <ChartSeriesLabels Visible="true"></ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart>

## Answer

**Marin Bratanov** answered on 31 Mar 2020

Hi Jonathan, Generally, showing a single value is a job for a gauge not for a chart. The pie chart shows the values as their percentage of 100, so if you want to show one value as percentage of 100 you need to pad the data with another item that tops up the value to 100. Here follows an example of how something like that can be done with a pie chart. The key points of interest: The data is padded with a second item so you can achieve a pie chart. I show the drive name in the chart title because the categories from the data are shown in the legend, so they would probably both be the same letter. So I hide the legend <TelerikChart Width="100%" Height="100%" Transitions="false" RenderAs="@RenderingMode.SVG">
<ChartTitle Text="@TheDriveName"></ChartTitle>
<ChartLegend Visible="false"></ChartLegend>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Pie" Data="@DriveData" Field="@nameof(Drive.PercentFree)" CategoryField="@nameof(Drive.Name)" ExplodeField="@nameof(Drive.Explode)">
<ChartSeriesLabels Visible="true" Format="{0}%"></ChartSeriesLabels>
</ChartSeries>
</ChartSeriesItems>
</TelerikChart>

@code{
List<Drive> DriveData { get; set; }=new List<Drive>(); string TheDriveName { get; set; } protected override async Task OnInitializedAsync ( ) {
DriveData.Clear(); var drive=await GetDriveFreeSpace();
DriveData.Add(drive); var padding=new Drive { Name=DriveData[ 0 ].Name, PercentFree=100 - DriveData[ 0 ].PercentFree };
DriveData.Add(padding);
TheDriveName=DriveData[ 0 ].Name;
} async Task<Drive> GetDriveFreeSpace ( ) {
Drive data=new Drive
{
PercentFree=53,
Name="C:" }; return await Task.FromResult(data);
} public class Drive { public double PercentFree { get; set; } public string Name { get; set; } public bool Explode { get; set; }
}
} Or, you could keep the legend and show Free/Used in the categories, something like this: <TelerikChart Width="100%" Height="100%" Transitions="false" RenderAs="@RenderingMode.SVG">
<ChartTitle Text="@TheDriveName"></ChartTitle>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Pie" Data="@DriveData" Field="@nameof(Drive.PercentFree)" CategoryField="@nameof(Drive. Category )" ExplodeField="@nameof(Drive.Explode)">
<ChartSeriesLabels Visible="true" Format="{0}%"></ChartSeriesLabels>
</ChartSeries>
</ChartSeriesItems>
</TelerikChart>

@code{
List<Drive> DriveData { get; set; }=new List<Drive>(); string TheDriveName { get; set; } protected override async Task OnInitializedAsync ( ) {
DriveData.Clear(); var drive=await GetDriveFreeSpace();
DriveData.Add(drive); var padding=new Drive { Name=DriveData[ 0 ].Name, PercentFree=100 - DriveData[ 0 ].PercentFree, Category="Used" };
DriveData.Add(padding);
TheDriveName=DriveData[ 0 ].Name;
} async Task<Drive> GetDriveFreeSpace ( ) {
Drive data=new Drive
{
PercentFree=53,
Name="C:", Category="Free" }; return await Task.FromResult(data);
} public class Drive { public double PercentFree { get; set; } public string Name { get; set; } public string Category { get; set; } public bool Explode { get; set; }
}
} Regards, Marin Bratanov

### Response

**Jonathan** answered on 31 Mar 2020

thx again! Awesome How do I vote for a future Gauge Control?

### Response

**Marin Bratanov** answered on 31 Mar 2020

Hi Jonathan, There isn't a request for this yet, so I would encourage you to post a new one for such a component in our Feedback portal through the "Request a Feature" button. Just make sure to select the "make public" checkbox at the final step. This will let you explain your goals, requirements, even perhaps add a sample of what API and functionality you would expect it exposes. You can then Vote for it and Follow it to get updates on status changes. If it gets good traction with the community, we will consider its implementation. Regards, Marin Bratanov
