# Removing borders on Stacked Chart

## Question

**Jac** asked on 01 May 2023

Hello I have a stacked chart: [https://blazorrepl.telerik.com/mdapkbvq40X63oHt59](https://blazorrepl.telerik.com/mdapkbvq40X63oHt59) Is it possible to remove the strokes on the colored boxes in the chart so it looks more like the image attached? I can remove them with a css selector, but it looks like this and obviously isn't a great selector svg g> g> g> g> g> g> g path { stroke: none; } Also, is it possible to put a border-radius around the whole column?

## Answer

**Mark** answered on 25 Oct 2023

Hi Jacob, Sorry to revive the thread if you have moved on. But I have the same issue and I agree that the CSS selector is brittle and difficult to maintain. This feature request to allow configuration of `ChartSeries` borders could resolve our issues: Border settings for series in Chart (telerik.com) Thanks Mark
