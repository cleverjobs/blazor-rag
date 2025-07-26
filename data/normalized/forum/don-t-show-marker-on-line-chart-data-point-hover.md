# Don't show marker on Line Chart data point hover

## Question

**IanIan** asked on 16 Mar 2024

I have a chart with two line series, one showing current values, and the other as a reference line. On the reference line I don't want any adornment or interaction, so I have made the markers invisible. However, the data points still appear if you hover over where they would be. Is there a property to prevent that? At the moment I'm just setting their size to zero to make them as least noticeable as possible

## Answer

**Svetoslav Dimitrov** answered on 20 Mar 2024

Hello Ian, For cases, where you need to show a threshold to the users we suggest using the Plot Bands feature. It does not provide any "interactive" elements such as markers. If plot bands do not fit your scenario, I can confirm that the approach you have taken is the best one possible. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Ian** commented on 22 Mar 2024

Thanks for the suggestion, but I'm already using plot bands for a different purpose on the chart, so they won't fit in this particular scenario. I'll continue with my current solution
