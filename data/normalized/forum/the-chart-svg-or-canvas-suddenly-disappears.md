# The chart SVG or canvas suddenly disappears.

## Question

**rob** asked on 15 May 2024

Issue: The chart SVG or canvas suddenly disappears. Reproduction of the Problem Use the Blazor UI from Telerik trial version. Perform actions such as hiding the chart line or adding values. Current Behavior At seemingly random intervals, the chart SVG or canvas disappears. This occurs when performing actions like hiding the chart line or adding values. The issue does not occur consistently or under obvious conditions. Expected/Desired Behavior The chart should behave as expected and not disappear unexpectedly. Environment Telerik UI for Blazor version: 5.1.1 (Trial) Browser: All App Type: Server Video: [https://www.veed.io/view/7782882d-6522-4fa6-a9df-8413695486ed?panel=share](https://www.veed.io/view/7782882d-6522-4fa6-a9df-8413695486ed?panel=share) <div style="width: 1100px; height: 500px;" class="graphBorder shadow">
<TelerikChart Height="95%" Transitions="false">
<ChartSeriesItems>
@foreach( var item in ChartData)
{
<ChartSeries
Visible="@item.ShowLine" Style="ChartSeriesStyle.Smooth" Type="ChartSeriesType.ScatterLine" Name="@item.LineName" Data="@item.Data" Color="@item.Color" XField="@nameof(Data.X)" YField="@nameof(Data.Y)">
<ChartSeriesMarkers Size="0" />
<ChartSeriesTooltip Visible="true" />
</ChartSeries>
}
</ChartSeriesItems>

<ChartTitle Text="TestChart"></ChartTitle>

<ChartXAxes>
<ChartXAxis Type="date" BaseUnit="minutes" MajorUnit="30" Min="@(new TimeOnly(0,0,0))" Max="@(new TimeOnly(3,0,0))">
<ChartXAxisTitle Text="TestChart"></ChartXAxisTitle>
<ChartXAxisLabels Format="{0:HH:mm}"></ChartXAxisLabels>
</ChartXAxis>
</ChartXAxes>

<ChartYAxes>
<ChartYAxis Max="@(100 + 5)" Min="0" MajorUnit="10">
<ChartYAxisLabels/>
<ChartYAxisTitle Text="TestChart"></ChartYAxisTitle>
</ChartYAxis>
</ChartYAxes>

<ChartLegend Visible="false" />

</TelerikChart>
<div class="Legend d-flex justify-content-sm-around flex-row">
@foreach( var item in ChartData)
{
<div>
<TelerikCheckBox Id="myCheckBox" @bind-Value="@item.ShowLine" />
<label for="myCheckBox">@item.LineName</label>
</div>
}
</div>
</div>

@code { public List<GraphData> ChartData=new ()
{ new GraphData
{
LineName="Stroom 1",
ShowLine=true,
Color="green",
MinDate=new TimeOnly( 0, 0 ),
TimeBetweenMinAndMax=new TimeSpan( 4, 0, 0 ),
Data=new List<Data>
{ new () { X=new TimeOnly( 0, 0 ), Y=10 }, new () { X=new TimeOnly( 0, 15 ), Y=20 }, new () { X=new TimeOnly( 0, 30 ), Y=12 }, new () { X=new TimeOnly( 0, 45 ), Y=3 }, new () { X=new TimeOnly( 1, 0 ), Y=10 }, new () { X=new TimeOnly( 1, 15 ), Y=12 }, new () { X=new TimeOnly( 1, 30 ), Y=14 }, new () { X=new TimeOnly( 1, 45 ), Y=15 }, new () { X=new TimeOnly( 2, 0 ), Y=16 }, new () { X=new TimeOnly( 2, 15 ), Y=40 }
}
}
};
}

## Answer

**Nansi** answered on 20 May 2024

Hello Robin, Thank you for the provided detailed explanation of the issue, that you are facing. Currently, we have no information for potential issues causing the Chart to behave like this. From the provided code I don't see a cause for the problem. I cannot load the video, that you sent, because it requires access. I don't reproduce the issue if I hide the Chart line. Here is a REPL example. Can you please send me an isolated sample that replicates the exact behavior you are hitting, so I can revise it in detail? Do you see any exceptions in the console? Regards, Nansi Progress Telerik

### Response

**robin** commented on 23 May 2024

Hello nansi, Thank you for replying. This exact code gives me the issue. The issue shows itself after (what i think) is showing the demo background image, Hereby a new link (it should work now) [https://www.veed.io/view/7782882d-6522-4fa6-a9df-8413695486ed?panel=share](https://www.veed.io/view/7782882d-6522-4fa6-a9df-8413695486ed?panel=share) Regards, Robin

### Response

**Nansi** answered on 28 May 2024

Hi Robin, Thank you for the provided video. I see how the Chart disappears on it. I also see that you are not testing it in the REPL. A possible cause in this case can be some custom CSS styling. The Chart in your example is in a <div> with a class attribute. Do you apply some CSS styles to the Chart elements via the graphBorder and shadow classes? Overall, it's hard to assume what might be the reason without an isolated example that replicates the behavior. Are you able to provide such an example, so I can move forward with the investigation? Regards, Nansi Progress Telerik

### Response

**robin** commented on 18 Jun 2024

Hi nansi, indeed wen i put it in repl i dont get the issue, what telerik version does it use? repl link: [https://blazorrepl.telerik.com/myaUFsOt56qw9ofb46](https://blazorrepl.telerik.com/myaUFsOt56qw9ofb46) Regards, Robin

### Response

**robin** commented on 18 Jun 2024

Hi nansi, the graphBorder and shadow only only add things tothe outer div WIth testing i think it is because i have the telerik trial version, every time the chart disapears the trial watermark shows up could this be a thing? Regards, Robin

### Response

**Nansi** answered on 21 Jun 2024

Hi Robin, The sidebar of the REPL provides Telerik UI Asset Manager. It allows you to change the Telerik.UI.for.Blazor package version. The version of the REPL, that I sent is using version 5.1.1. The one that you sent uses the latest version - 6.0.2. However, I tested the implementation with all available in the manager versions. Additionally, there shouldn't be any differences in the behavior if you use the trial version or a licensed one. I am sending a project, that uses the trial version and the Chart disappears on uncheck and appears on check the Checkbox. Can you share the styles, that you set via the graphBorder and shadow classes? Usually, the class attribute is used in a style sheet to apply styles to all elements with that class. Regards, Nansi Progress Telerik

### Response

**robin** commented on 25 Jun 2024

hi nansi, here are the classes: . shadow { box-shadow: 0 .5 rem 1 rem rgba ( 0, 0, 0,.15 )!important } . graphBorder { border: 1 px solid #000; padding: 10 px; margin: 10 px; border-radius: 5 px; } Regards, Robin

### Response

**Nansi** commented on 27 Jun 2024

Hi Robin, Thank you for the provided CSS styles. Indeed, they cannot cause the Chart to disappear. As a next step, you can modify my REPL example to reproduce the issue and send it back to me so I can investigate further. In general, the REPL provides an isolated environment. If something is working as expected in the REPL but not in a project, this suggests that something in the project could be the cause of the issue. Will you be able to send an example that reproduces the issue? You don't have to use your actual data source, you may generate some dummy data. You can also open a private ticket and send some sample project, where the issue is reproduced.
