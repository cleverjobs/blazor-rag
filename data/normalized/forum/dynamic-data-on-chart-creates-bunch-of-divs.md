# Dynamic data on Chart creates bunch of divs

## Question

**mil** asked on 12 Jan 2022

Hello, I'm pushing data to chart from signalr every 1-2s and it's working fine but for each new entry, Telerik adds a DOM at the end of the document (<div style="display: none;">...</div> which overtime can generate thousands of those divs. Is there a way to eliminate those or at least to remove not used ones (as I'm showing max 10 latest records in the chart). Thanks <TelerikChart Transitions="false"> <ChartTooltip Visible="true" /> <ChartLegend Visible="false" /> <ChartChartArea Background="transparent" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Value" Data="@Data" Field="Value" CategoryField="Time"> </ChartSeries> </ChartSeriesItems> </TelerikChart>

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hi, This is a known bug in the component whos fix you can track here: [https://feedback.telerik.com/blazor/1424130-elements-remain-in-the-dom-after-updating-chart-data.](https://feedback.telerik.com/blazor/1424130-elements-remain-in-the-dom-after-updating-chart-data.) I've added your Vote to it to raise its popularity and thus priority. Regards, Marin Bratanov
