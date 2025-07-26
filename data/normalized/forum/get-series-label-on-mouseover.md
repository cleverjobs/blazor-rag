# Get Series Label on mouseover

## Question

**Jam** asked on 04 Aug 2019

Hey all, I have a Blazor chart which has about four series on it and each series has a hundred or so points. If I turn on the series labels, they all turn on and it makes my chart unreadable. Is there a way to have them only appear when you either mouse over a marker on the series or when you click on the marker in the series? This sounds easy to do but I can't seem to manage it with the Blazor chart. Any and all help will be appreciated. Thanks. Cheers, Jimmy

## Answer

**Marin Bratanov** answered on 05 Aug 2019

Hello Jimmy, Such a feature is not available yet. This is usually done by using a tooltip to show the data point value. You can Follow this page to get notifications when it gets implemented (I have already added your vote): [https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points.](https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points.) You may also want to vote and/or follow this request for a click event: [https://feedback.telerik.com/blazor/1412010-i-need-a-click-event-on-a-chart-element-such-as-a-specific-bar-in-a-bar-chart-or-a-slice-in-a-pie-chart.](https://feedback.telerik.com/blazor/1412010-i-need-a-click-event-on-a-chart-element-such-as-a-specific-bar-in-a-bar-chart-or-a-slice-in-a-pie-chart.) While it would not be suitable for toggling labels, you could use it to provide some details for the clicked item in a separate element (e.g, next to the chart), or to otherwise react to the user action. Regards, Marin Bratanov

### Response

**James** answered on 05 Aug 2019

Hey Marin, Thanks for your responce. I'll follow these two items as you suggested. Can you give a ballpark guess when we may see at least the tooltip one please? Thanks, Jimmy

### Response

**Marin Bratanov** answered on 05 Aug 2019

Hello Jimmy, At the moment, our short term priorities are adding features to the grid - the grid is the number one component an app needs, and so we must get that up to speed. After that, we will see - the interest (demand) we see in the

### Response

**James** answered on 08 Mar 2020

Hey Marin, Any progress on this feature? I still have customers needing this feature and charts haven't really improved since the initial release. I am hoping soon the grid will be where it needs to be to sustain customers expectations, so you can focus on other components, like the charts, which desperately need your companies attention. Sincerely, Jimmy

### Response

**Marin Bratanov** answered on 09 Mar 2020

Hello James, Since August we have released three new chart types - bubble, scatter and scatter line in 2.1.0. You can also follow your current plans here, we keep the roadmap page updated: [https://www.telerik.com/support/whats-new/blazor-ui/roadmap.](https://www.telerik.com/support/whats-new/blazor-ui/roadmap.) A couple of key things that we are working on right now are the grid state (which will let you save and load the grid layout, and also to set filtering, grouping, sorting and so on programmatically), a tooltip, recurring scheduler events and an async upload component. On the mouseover for the series - the closest feature is the tooltips and you can Follow their implementation here: [https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points.](https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points.) I cannot say at this point when they will become available - in our next release (2.9.0) we will be shipping a "regular" tooltip for standard elements, and there are still some framework limitations/difficulties for the charts because they are either a canvas, or svg, and neither of those has API from Blazor. Regards, Marin Bratanov
