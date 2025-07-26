# Chart not displaying data

## Question

**Val** asked on 19 Sep 2019

Hi, Using: UI for Blazor 2.0 with .NET Core 3 RC1. We're trying to get data to show on our chart. However it seems this is not working. We're binding a single series like this: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Values" Data="@_dataPoints" Field="@nameof(DataPoint.Value)" CategoryField="@nameof(DataPoint.Category)" /> </ChartSeriesItems> <ChartLegend Position="Telerik.Blazor.ChartLegendPosition.Right" /> </TelerikChart> Our _dataPoints variable is set in OnInitializedAsync. We've tried invoking StateHasChanged after the variable has been set, but this does not seem to help. The "category" property on the DataPoint model was a DateTime but we changed this to string to check if that would work, but this also doesn't fix it. private IEnumerable<DataPoint> _dataPoints=new List<DataPoint>(); protected override async Task OnInitializedAsync() { _dataPoints=await CalculateDataPoints().ConfigureAwait(false); //await InvokeAsync(()=> StateHasChanged()).ConfigureAwait(false); } Are we missing something? Thank you in advance.

## Answer

**Marin Bratanov** answered on 20 Sep 2019

Hello, To follow up in this public thread with some info from the private ticket - it seems there was some issue in the actual data that was coming in and that was causing the problem. If new pertinent information comes up in the private ticket, we may update it here as well, to the benefit of anyone else experiencing similar problems. Regards, Marin Bratanov

### Response

**Datafyer** commented on 01 Aug 2021

What was the issue with the data? I think I have the same problem.

### Response

**Marin Bratanov** commented on 02 Aug 2021

All we know is that there had been unexpected duplicate values on categories. I hope OP will be able to chime in with some more details.
