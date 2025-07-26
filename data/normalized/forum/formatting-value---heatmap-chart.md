# Formatting value - Heatmap Chart

## Question

**Fil** asked on 13 Jan 2022

Hello, I am trying to format value (defined by Field="@nameof(HeatmapData.Value)" ) on a heatmap chart. The underlying Value is a double and I am trying to show it rounded to two decimal places ("0.##" format) with '%' appended. I've tried to use <ChartSeriesLabels Format="{0:0.##}%" />, but it prints value of the XField instead. Now I am trying <ChartSeriesLabels Template="#=value#%" />, but to my knowledge it doesn't support the "0.##" formatting option. Is there a way ho to do it? Thank you.

## Answer

**Svetoslav Dimitrov** answered on 18 Jan 2022

Hello Filip, As you rightfully mentioned, you should use the Template exposed on the <ChartSeriesLabels> tag. In the Template, you can use JavaScript to format the number into two decimals. To do that, you can use the toFixed() method and pass the desired number of decimal places in the brackets. <ChartSeriesLabels Template="#=value.toFixed(2)#% "> </ChartSeriesLabels> Regards, Svetoslav Dimitrov

### Response

**Filip** commented on 18 Jan 2022

That's working, thank you very much! Do you know why <ChartSeriesLabels Format="{0:0.##}%" /> doesn't work? It looks like it's exactly meant for that.

### Response

**Svetoslav Dimitrov** commented on 21 Jan 2022

Hello Filip, The Format attribute of the ChartSeriesLabels parameter supports the standard numeric format strings that Microsoft provides. The 0:0.## is part of the custom numeric format string which is not supported at the time of writing this.
