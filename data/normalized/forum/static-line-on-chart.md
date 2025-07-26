# Static Line on Chart

## Question

**Har** asked on 09 Jun 2021

I am wanting to display a static line on a line chart to show a target the is hoping to be reached. the screenshot is an example of the current graph and what we need is a solid line to be shown at a set value for example 2250 that goes all the way across so that you can see which points are hitting the target needed.

## Answer

**Svetoslav Dimitrov** answered on 14 Jun 2021

Hello Harry, We have an open Feature Request regarding the ability to easily draw horizontal and vertical lines in the Charts. I have added your Vote for it and you can follow it to receive email notifications on status updates. In the public thread, opening post, you can see some options for a workaround. Regards, Svetoslav Dimitrov

### Response

**Peter** answered on 28 Jan 2022

Hi Harry, as workaround for vertical lines I use a Scatterline with missing values and ChartSeriesMissingValues.Gap. Regards, Peter @page "/Testchart" <TelerikChart>
<ChartSeriesItems>
<ChartSeries Type="ChartSeriesType.Scatter" Data="@serie" XField="@nameof(DataModel.x)" YField="@nameof(DataModel.y)">
<ChartSeriesMarkers Type="ChartSeriesMarkersType.Circle" Size="4" />
</ChartSeries>
<ChartSeries Type="ChartSeriesType.ScatterLine" Data="@verticalLines" XField="@nameof(DataModel.x)" YField="@nameof(DataModel.y)" MissingValues="ChartSeriesMissingValues.Gap" Color="Green">
<ChartSeriesMarkers Size="0" />
</ChartSeries>
</ChartSeriesItems>
<ChartYAxes>
<ChartYAxis Min="ymin" Max="ymax" />
</ChartYAxes>
<ChartXAxes>
<ChartXAxis Type="date" BaseUnit="days">
<ChartXAxisLabels Format="{0:dd.MM.yy}"></ChartXAxisLabels>
</ChartXAxis>
</ChartXAxes>
</TelerikChart>

@code { class DataModel { public DateTime x { get; set; } public double y { get; set; }
} int ymin=0; int ymax=100;

List<DataModel> serie { get; set; }=new List<DataModel>();
List<DataModel> verticalLines { get; set; }=new List<DataModel>(); protected override async Task OnInitializedAsync ( ) { var start=new DateTime( 2021, 10, 1 ); for ( var i=0; i <100; i++)
serie.Add(( new DataModel { x=start.AddDays(i), y=i })); for ( var i=0; i <100; i+=10 )
{
verticalLines.Add( new DataModel { x=start.AddDays(i) , y=ymin });
verticalLines.Add( new DataModel { x=start.AddDays(i) , y=ymax });
verticalLines.Add( null );
}
}
}
