# Tooltip Position

## Question

**BobBob** asked on 29 Jan 2021

Is there any way to control the tooltip position? In the Kendo UI Pie Chart the tooltip is always outside the pie when I hover over a slice, however the tooltips in the Blazor grid always appear wherever my mouse cursor is and many times it will block my ability to click on the slice to fire the series click event. Can we make the the tooltips appear outside the pie itself just like in the Kendo UI Pie Chart?

## Answer

**Stamo Gochev** answered on 03 Feb 2021

Hello Bob, There is a difference between how the tooltips are rendered in other suites compared to the way in blazor due to framework-specific features. Currently, there isn't a public API that allows configuration of the tooltip's position, but you can use CSS to customize the rendered element instead: <style>.k-chart-tooltip-wrapper { margin-left: - 50px; margin-top: 0px;
}
</style> Note that the exact values should be configured according to the specific case. Regards, Stamo Gochev
