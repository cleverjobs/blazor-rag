# Series click on aggregated chart

## Question

**Ila** asked on 07 Jun 2023

I'm using a chart with BaseUnit="ChartCategoryAxisBaseUnit.Fit" Aggregate="ChartSeriesAggregate.Sum", Type="ChartCategoryAxisType.Date" When clicking on a series it returns a single date (day) and not the date range that were used for the aggregation. I need the range in order to show the full result list in a grid. How can it be done?

### Response

**Yanislav** commented on 12 Jun 2023

Hello Ilan, Correct me if I misunderstood something, but based on the description, I understand that you are trying to display the aggregate value for a specific range instead of for a certain date. Is that correct? In general, the purpose of an aggregate is to convert a collection of values into a single value for a specific point. Since there are multiple values for the same category, one of them needs to be plotted (and the choice is determined by the aggregate function). The chart then continues to work with that point, not the range. However, since the chart is currently not functioning in this way and the click event only returns the category it is working with, I suggest logging a feature request in our

## Answer

**Ilan** answered on 12 Jun 2023

1. In that case, is there a way to know how the aggregate function works? or create a custom one? 2. There's no way to know the original points or at least get the current base unit ? (days, month etc)

### Response

**Yanislav** commented on 14 Jun 2023

Hello Ilan, Given that the click handler currently returns the plotted category, a possible solution would be to prepare the data in advance and directly pass it to the Chart. This way, you can perform the necessary aggregate operations and preserve the ranges for each category. Here is a simple example that demonstrates this approach: [https://blazorrepl.telerik.com/mHugFovH38sIS5Cb53](https://blazorrepl.telerik.com/mHugFovH38sIS5Cb53)
