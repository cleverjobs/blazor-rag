# ChartLegend Issues

## Question

**Zac** asked on 19 Aug 2020

Once you have more than about 4-5 categories in your legend, the legend starts reusing colors. Is there some way to provide the legend with more colors than that so you don't sometimes have 2-3 categories with the same color. Also, if you pass in data and use the FieldCategory, I take it does not group by the category value and creates duplicate keys with different colors, further complicating the first issue above. Plus, making the 2 issues above even worse, even if the results in the chart do not have values (and are not visible) the legend still generates keys that are not present in the results? See attachment shows all 3 things in action at once. I think I could make this mostly (beside the reused colors) better by creating a helper to group/merge by category into a smaller dataset and then create subsets of that filtered where No>0. Having to do that in a larger dashboard scenario adds a ton of plumbing for what I would assume should be groupable based on configuration settings with a shared data collection used by many charts on the same view.

## Answer

**Marin Bratanov** answered on 19 Aug 2020

Hi Zack, I must start by explaining two core concepts of the charts: They render the data as it is provided by the app. The only exception is the date axis when aggregation is performed, but it does not affect pie charts, as they don't have axes. The charts cannot know the business need and implement grouping or filtering, this is something the app must do. Often times simple .Where() query on the data will let you, for example, remove items with small/zero/negative values from display in donut charts. The charts come with a predefined set of colors from our themes, but that set of colors cannot be endless. This is why you can set the color to each series, and individual series have the ColorField where you can set the color for each individual series item (like a pie/donut chart segment). The docs for each series showcases key concepts (like here - for the donut chart we link to the pie chart to avoid repetition - here's how the ColorField works for pie/donut types of charts). So, with that in mind, the solution to your situation is to use the ColorField to define colors for the segments, and if you want to remove certain segments from the rendering, you mush shape the data accordingly before providing it to the chart - whether you will combine several data points into one or remove them altogether is up to you to decide depending on the presentation you want to get. Regards, Marin Bratanov

### Response

**Zack** answered on 19 Aug 2020

I see. Thanks. We will create some group/where/color sets to provide the charts with more than 6 colors and remove duplicates.

### Response

**Zack** answered on 19 Aug 2020

I found that you cannot add series to pie charts, and if you add series to donut charts, it adds inner rings that are not what we would want. So basically I think you are stuck with 6 colors if you want a pie-like donut.

### Response

**Zack** answered on 19 Aug 2020

Oops, never mind :) I see ColorField now.
