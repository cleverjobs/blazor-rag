# Trend line

## Question

**Lau** asked on 23 Nov 2020

Is is possible to add a trend line / linear regression to the Blazor charts like Excel? See it is available in the kendo charts ([https://docs.telerik.com/kendo-ui/knowledge-base/chart-add-trend-line).](https://docs.telerik.com/kendo-ui/knowledge-base/chart-add-trend-line).) Also found the old 2015 knowledge base article ([https://www.telerik.com/blogs/how-to-plot-a-simple-linear-regression-in-telerik-asp.net-web-form-chart)](https://www.telerik.com/blogs/how-to-plot-a-simple-linear-regression-in-telerik-asp.net-web-form-chart))

## Answer

**Marin Bratanov** answered on 24 Nov 2020

Hello Steve, Both approaches rely on the application supplying the data for a series that shows the trend - whether it is a hardcoded example like in the Kendo KB article, or a more detailed approach on using statistical methods to calculate it at runtime (like in the AJAX blog) - in both cases it is up to the app to provide that data. Then, you only need to add a series that shows it. Regards, Marin Bratanov
