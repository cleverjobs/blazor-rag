# Support for Sparklines or mini charts

## Question

**Joh** asked on 12 Sep 2021

I have just purchased Telerik Blazor UI and requires the use if the TelerikTreeList component to visualise heirachical data but also need a visualisation per row ie ideally there would be a sparkline but this isn't in the compoennts list nor is it in the Roadmap. I have tried using the standard chart but they seem too heavy and do not draw in the available space. In your chart page on the web site you show a chart in a grid in exactly the way I need. Can you please advise how this is done:

## Answer

**Marin Bratanov** answered on 12 Sep 2021

Hello John, In order of questions: You can Follow the implementation of dedicated sparkline charts here: [https://feedback.telerik.com/blazor/1483862-add-sparkline-charts.](https://feedback.telerik.com/blazor/1483862-add-sparkline-charts.) I've already added your Vote on your behalf. At the moment, you can achieve them by reducing the size of the "regular" charts and removing elements from them (such as axes, labels, grid lines, etc.) - sub-elements tend to have a Visible parameter you can set to false. You can read more about styling charts and working with their nested tags here: Customize Chart Elements - Nested Tags Settings. Lastly - where you can find the example from the screenshot (which contains configuration outlined above) - you find the full source of this app here: [https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-stocks.](https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-stocks.) Here is the particular sparkline component we made for that app (we even called it a sparkline, even if it is a regular chart with some settings): [https://github.com/telerik/blazor-ui/blob/master/sample-applications/blazor-stocks/Client/Components/StocksGrid/SparklineChart.razor.](https://github.com/telerik/blazor-ui/blob/master/sample-applications/blazor-stocks/Client/Components/StocksGrid/SparklineChart.razor.) On a side note - you may find interesting the entire repository where this project is - it shows a lot of sample scenarios and projects for UI for Blazor (I think the current count is about 60). Regards, Marin Bratanov

### Response

**John** commented on 12 Sep 2021

Excellent Marin ... thanks for answering on the weekend. I had decided to push ahead with shrinking the size of the regular charts before you answered so I am happy that this approach should be ok.

### Response

**Marin Bratanov** commented on 12 Sep 2021

It is perfectly OK, John :)
