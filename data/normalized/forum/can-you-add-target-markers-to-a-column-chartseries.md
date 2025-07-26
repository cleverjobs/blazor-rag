# Can you add target markers to a column ChartSeries?

## Question

**Mar** asked on 20 Oct 2023

Hi Can you add target markers to a column ChartSeries? Something a bit like this: We have been able to use a 0 width line series and their markers in some instances, REPL. But this can quickly breakdown with multiple columns per category or grouped series. We have been able to hijack a chart series label. But this breaks down on stacked series. Thanks Mark

### Response

**Mark** commented on 24 Oct 2023

Example of 0 width line series on a column chart (no stacking, no grouping), [https://blazorrepl.telerik.com/mnbkGSOs59XuBhe618.](https://blazorrepl.telerik.com/mnbkGSOs59XuBhe618.)

### Response

**Nadezhda Tacheva** commented on 25 Oct 2023

Hi Mark, Thank you for sharing the samples! I will revise other possible options to achieve such a result. I will get back to you with more details later today. Thank you for your patience in advance!

### Response

**Nadezhda Tacheva** commented on 26 Oct 2023

Hi Mark, Thank you once again for your patience! I've considered a couple of options that may help you achieve your desired result: Draw horizontal lines on the chart to serve as limits. See [https://feedback.telerik.com/blazor/1511761-easy-to-draw-horizontal-and-vertical-lines-in-the-charts.](https://feedback.telerik.com/blazor/1511761-easy-to-draw-horizontal-and-vertical-lines-in-the-charts.) This will most likely be achieved with a custom approach and we are planning to release such an example in the upcoming release. Use a visual template for the series once it is available. Similar to the approach listed here using the Kendo UI for jQuery Chart. Altering the configuration you could achieve something like this: [https://dojo.telerik.com/uMOZiFUD/2.](https://dojo.telerik.com/uMOZiFUD/2.) If you are interested in this option, you may vote for the feature request to bump its popularity and follow it to get status updates. For the time being, it is possible to use the jQuery Kendo Chart in your Blazor app. I hope you will find this information useful. Please let us know if additional questions appear.
