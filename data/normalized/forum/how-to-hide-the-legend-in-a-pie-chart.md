# How to hide the legend in a Pie Chart?

## Question

**TedTed** asked on 24 May 2024

Hi, I'm not adding a ChartLegend element to a pie chart, but the legend is still showing up to the right of the pie chart? How can I remove the legend entirely from the Pie chart? See here for demo: [https://blazorrepl.telerik.com/cSupwSbA500BPvKK06](https://blazorrepl.telerik.com/cSupwSbA500BPvKK06)

## Answer

**Tsvetomir** answered on 29 May 2024

Hi Ted, Thank you for the provided screenshot and runnable sample! The visibility of the Chart legend can be managed through the Visible parameter of the ChartLegend tag. By design, the Pie Chart displays a legend, with the default value of the parameter set to " true ". To change this behavior, define a ChartLegend tag and set the Visible parameter to " false ". To assist you further, I'm sending you back the modified REPL demo with the removed legend. Regards, Tsvetomir Progress Telerik
