# Clear chart

## Question

**Oma** asked on 30 Nov 2024

Hi, I have chart within child component, the chart is create dynamically. After populating the chart, I would like to clear it. How to clear the chart? Thanks, Omar <TelerikChart @ref="GNChart"> <ChartSeriesItems> @{
var swedishCulture=new CultureInfo("sv-SE");
}
@foreach(var group in ChartData.Select(c=>c.text).Distinct().ToList())
{ <ChartSeries Type="ChartSeriesType.Line" Data="@ChartData.Where(c=>c.text==group)" Name="@group" Field="@nameof(ChartDataClass.value)" CategoryField="@nameof(ChartDataClass.month)"> <ChartSeriesTooltip Visible="true"> <Template> <TelerikSvgIcon Icon="SvgIcon.InfoCircle" /> @((context.DataItem as ChartDataClass).value.ToString("N0", swedishCulture)) | @((context.DataItem as ChartDataClass).text) </Template> </ChartSeriesTooltip> </ChartSeries> } <ChartValueAxes> <ChartValueAxis Color="purple"> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> </ChartSeriesItems> <ChartTitle Text="Quarterly revenue per product" Visible="false"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Bottom"> </ChartLegend> </TelerikChart>

## Answer

**Hristian Stefanov** answered on 02 Dec 2024

Hi Omar, To clear the dynamically created chart in your child component, you can use a combination of updating the data source and triggering a re-render of the component. Here are some methods you can try: Using StateHasChanged(): After you update your data source, call StateHasChanged() to refresh the component. This method triggers a re-render of the component and should help clear the chart. void UpdateChartData ( ) { // Update your ChartData here StateHasChanged(); // This will trigger a re-render } Using Refresh() method: If StateHasChanged() alone doesn't clear the chart as expected, you can use the chart's Refresh() method. This method forces the chart to refresh and should be called on the chart reference. You might want to add a small delay before calling Refresh() to ensure the chart clears and re-renders properly. TelerikChart GNChart; async Task ClearAndRefreshChart ( ) { // Update your ChartData here // Optionally, add a small delay await Task.Delay( 100 );
GNChart.Refresh(); // This will force the chart to refresh } Ensure DataSource is Empty: Before updating the chart with new data, make sure to clear the existing data source. This step is crucial to prevent old data from mixing with new data. void ClearChartData ( ) {
ChartData.Clear(); // Clear existing data StateHasChanged(); // Trigger re-render } Regards, Hristian Stefanov Progress Telerik

### Response

**Omar** commented on 05 Dec 2024

the Delay did the trick. Many thanks await Task.Delay( 100 );
