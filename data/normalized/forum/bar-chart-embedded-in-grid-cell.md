# Bar Chart Embedded in Grid Cell

## Question

**Kel** asked on 10 Feb 2020

I am trying to create a bar chart inside a grid cell that has labels on the left and values on the right. Is this possible with the Bar Chart component? (see attached file for what I am trying to have the cell look like.

## Answer

**Marin Bratanov** answered on 10 Feb 2020

Hi Kelly, You should be able to put a chart in a column template, we do that in our PWA sample app: the grid declaration: [https://github.com/telerik/blazor-stocks/blob/master/Client/Components/StocksGrid/StocksGrid.razor#L105](https://github.com/telerik/blazor-stocks/blob/master/Client/Components/StocksGrid/StocksGrid.razor#L105) the chart extracted to its own component: [https://github.com/telerik/blazor-stocks/blob/master/Client/Components/StocksGrid/SparklineChart.razor](https://github.com/telerik/blazor-stocks/blob/master/Client/Components/StocksGrid/SparklineChart.razor) On the chart itself: here's how to make a bar chart: [https://docs.telerik.com/blazor-ui/components/chart/types/bar](https://docs.telerik.com/blazor-ui/components/chart/types/bar) here's how to enable the bar labels: [https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format](https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format) Are you facing any issues when you try that? Regards, Marin Bratanov

### Response

**Kelly** answered on 15 Feb 2020

Got it, thank you! Links were very helpful.

### Response

**Kelly** answered on 16 Feb 2020

I now have a bar chart embedded in the cell, but cannot find a way to get to (or override) the path fill attribute. Setting .k-chart background-color does not solve it. Currently, the path fill is rgb(255,255,255). I want the grid row highlight color to apply. (see attached file) If I set the path fill to transparent manually, it will adopt the row highlight. How can I get the bar chart background to be transparent?

### Response

**Marin Bratanov** answered on 17 Feb 2020

Hi Kelly, You can Follow the implementation of a background feature in the following page: [https://feedback.telerik.com/blazor/1453987-expose-chart-background-setting.](https://feedback.telerik.com/blazor/1453987-expose-chart-background-setting.) At the moment, this setting is not available in the chart for configuration, I'm afraid. Regards, Marin Bratanov
