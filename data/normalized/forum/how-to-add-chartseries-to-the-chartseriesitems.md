# How to add ChartSeries to the ChartSeriesItems

## Question

**Ber** asked on 04 May 2020

Hi, i would like to add ChartSeries to the ChartSeriesItems. I have a grid where I select some data. For each selected record, I would like to add a scatterline to a chart. Is this possible? Thanks

## Answer

**Marin Bratanov** answered on 04 May 2020

Hi Bert, You can use a series descriptor class and iterate over a collection of it in order to create many series at once: [https://docs.telerik.com/blazor-ui/knowledge-base/chart-dynamic-series.](https://docs.telerik.com/blazor-ui/knowledge-base/chart-dynamic-series.) You can even bind the grid to such a collection to get the selected items out of it automatically through two-way binding: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.) Regards, Marin Bratanov

### Response

**Bert** answered on 06 May 2020

Hi Marin, thanks for the answer. It works to add chartseries. I have 1 more problem, when I clear my list with datapoints (_RawSpectraList), the previous drawed lines are not removed. How can I clear the chart and remove all lines? @foreach (PointSerie item in _RawSpectraList) { <ChartSeries Type="ChartSeriesType.ScatterLine" Name="@item.name" Data="@item.data" Style="ChartSeriesStyle.Normal" XField="X" YField="Y"> <ChartSeriesMarkers Visible="false" /> </ChartSeries> }

### Response

**Marin Bratanov** answered on 06 May 2020

Hello Bert, You can Follow the fix for this and also find a workaround in this page: [https://feedback.telerik.com/blazor/1441685-cannot-clear-dynamically-created-series.](https://feedback.telerik.com/blazor/1441685-cannot-clear-dynamically-created-series.) Regards, Marin Bratanov
