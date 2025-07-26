# How to refresh chart

## Question

**Bry** asked on 25 Oct 2019

I have a parent component when contains a child component with a TelerikChart. Using cascading parameters, when I change a value in the parent component it cascades to the child and I rerun queries to create the proper data for the chart. Often times, but no all the time, a chart will rerender with some of the old data mixed in with some of the new data, even though the data model only contains the new data. Is there a way to force the chart to totally clear out before rerendering?

## Answer

**Marin Bratanov** answered on 28 Oct 2019

Hi Bryon, Calling .StateHasChanged() after you change the data should re-render the charts and have them use the new data. Something like: chartData=await GetTheNewChartData();

StateHasChanged() If this does not help, you can also call the chart's .Refesh() method (perhaps after a small timeout). Something like: chartData=await GetTheNewChartData(); await Task.Delay( 20 ); //redraw the chart theChart.Refresh(); If neither of these helps, please post a simple example of what breaks so I can debug. Regards, Marin Bratanov

### Response

**Kevin** commented on 22 Jan 2022

hi, this doesn't solve for when you are using the chart as a child component and passing values through CascadingValue.

### Response

**Marin Bratanov** commented on 23 Jan 2022

Make sure the Data parameter of the chart gets a new references, not just a modified collection. If this does not help, I recommend opening a ticket or a new thread to show the exact issue with an example, as I am not aware of such issues at the moment.
