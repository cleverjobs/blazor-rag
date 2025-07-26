# Can I get the X/Y Position of a mouse click on the chart area?

## Question

**Jer** asked on 15 May 2024

I am using a DateTime ChartSeries (ScatterLine). I would like to be able to click on the chart area at any point and get a XY position. Is there any way to do this?

## Answer

**Mark** answered on 20 May 2024

To get the X/Y position of a mouse click on a DateTime ChartSeries (ScatterLine), you can use the HitTest method to find the coordinates. Alternatively, you can convert the click position to axis values using the PixelPositionToValue method. Both methods will give you the X and Y values where the mouse was clicked on the chart.

### Response

**Tsvetomir** answered on 20 May 2024

Hello Jeremy, To achieve the desired functionality, you can use an approach with a JavaScript function that attaches an on-click event to the targeted Chart area. I have prepared an example for you below with the described approach. Here are also the steps: Within the JS function, attach an on-click event to the targeted area that takes the X and Y in pixels and converts them to the actual values from the Chart. Pass the result of the JS function to the Chart Component method OnPathClick(). @using Microsoft.JSInterop

@inject IJSRuntime JSRuntime <TelerikChart Class="custom-chart"> <ChartTitle Text="Charge current vs. charge time"> </ChartTitle> <ChartLegend Visible="true"> </ChartLegend> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.ScatterLine" Data="@Series1Data" Name="0.8C" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.ScatterLine" Data="@Series2Data" Name="1.6C" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.ScatterLine" Data="@Series3Data" Name="3.1C" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> </ChartSeriesItems> <ChartXAxes> <ChartXAxis Max="100"> <ChartXAxisTitle Text="Time"> </ChartXAxisTitle> <ChartXAxisLabels Format="{0}m"> </ChartXAxisLabels> </ChartXAxis> </ChartXAxes> <ChartYAxes> <ChartYAxis Max="100"> <ChartYAxisTitle Text="Charge"> </ChartYAxisTitle> <ChartYAxisLabels Format="{0}%"> </ChartYAxisLabels> </ChartYAxis> </ChartYAxes> </TelerikChart> <h3> @ValuesXY </h3> <script suppress-error="BL9992"> window.addChartClickEvent=( dotNetHelper )=> { setTimeout ( ()=> { // Get the Chart area const chartElement=document.querySelector( '.custom-chart svg> g> path:nth-child(2)' ); const chartBoundingRect=chartElement.getBoundingClientRect(); const xDataRange={ min: 0, max: 100 }; // Example x-axis data range const yDataRange={ min: 0, max: 100 }; // Example y-axis data range document.querySelectorAll( '.custom-chart svg> g> path:nth-child(2)' ).forEach( path=> {
path.addEventListener( 'click', ( event )=> { const xPixel=event.clientX - chartBoundingRect.left; const yPixel=event.clientY - chartBoundingRect.top; //Convert the pixels from the area to the actial Chart data const xDataValue=xDataRange.min + (xPixel / chartBoundingRect.width) * (xDataRange.max - xDataRange.min); const yDataValue=yDataRange.max - (yPixel / chartBoundingRect.height) * (yDataRange.max - yDataRange.min); // Pass the data values back to the Blazor component dotNetHelper.invokeMethodAsync( 'OnPathClick', xDataValue, yDataValue);
});
});
}, 500 ); // Adjust the delay as necessary }; </script> @code {
public string ValuesXY { get; set; } protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
await JSRuntime.InvokeVoidAsync("addChartClickEvent", DotNetObjectReference.Create(this));
}
} [JSInvokable]
public void OnPathClick(double x, double y)
{
ValuesXY=$"X position: {x:F2} Y position: {y:F2}";

InvokeAsync(StateHasChanged);
} public class ModelData
{
public int X { get; set; }
public int Y { get; set; }
}

public List <ModelData> Series1Data=new List <ModelData> ()
{
new ModelData() { X=10, Y=10 },
new ModelData() { X=15, Y=20 },
new ModelData() { X=20, Y=25 },
new ModelData() { X=32, Y=40 },
new ModelData() { X=43, Y=50 },
new ModelData() { X=55, Y=60 },
new ModelData() { X=60, Y=70 },
new ModelData() { X=70, Y=80 },
new ModelData() { X=90, Y=100 },
};

public List <ModelData> Series2Data=new List <ModelData> ()
{
new ModelData() { X=10, Y=40 },
new ModelData() { X=17, Y=50 },
new ModelData() { X=18, Y=70 },
new ModelData() { X=35, Y=90 },
new ModelData() { X=47, Y=95 },
new ModelData() { X=60, Y=100 },
};

public List <ModelData> Series3Data=new List <ModelData> ()
{
new ModelData() { X=10, Y=70 },
new ModelData() { X=13, Y=90 },
new ModelData() { X=25, Y=100 },
};
} Regards, Tsvetomir Progress Telerik

### Response

**Jeremy** commented on 20 May 2024

Thanks! Is there any chance that these functions will be brought into the C# / Blazor side natively rather than via JSInterop, so they can be called much like the WPF or MAUI variant?

### Response

**Tsvetomir** answered on 22 May 2024

Hi Jeremy, Thank you for the provided feedback. I am glad I was able to assist. Indeed, a feature request for adding an event for clicking on the Chart area has already been logged on our public feedback portal: Add the OnPlotAreaClick event. I voted for it on your behalf and raised its priority. Currently, its status is Unplanned. You can also subscribe to the item to get notified of any status updates via email. Regards, Tsvetomir Progress Telerik
