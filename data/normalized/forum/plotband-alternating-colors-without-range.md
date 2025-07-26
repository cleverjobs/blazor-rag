# Plotband alternating colors without range

## Question

**Nik** asked on 24 May 2022

Hello, I cannot get plotbands to work, could you please help me figure out what I'm doing wrong? <ChartCategoryAxisPlotBands> <ChartCategoryAxisPlotBand From="0" To="100000000" Color="red" Opacity="0.4" /> <ChartCategoryAxisPlotBand From="200000000" To="300000000" Color="red" Opacity="0.4" /> <ChartCategoryAxisPlotBand From="400000000" To="500000000" Color="red" Opacity="0.4" /> </ChartCategoryAxisPlotBands> Is there a oneliner for just alternating colors? Each even row number should be red and odd row number white. It makes it harder to make each plotband range, when the numbers are dynamic and change every single day. I do not control the min to max range, beacuse they are created automatically when the graph is rendered. Regards, Nikolas

### Response

**Nikolas** commented on 24 May 2022

My bad, my brain just stopped working today I guess. I used ChartCategoryAxisPlotBands when it should be ChartValueAxisPlotBands, the same goes for the specific ranges. But would still love to know about the oneliner :) Regards, Nikolas

## Answer

**Tsvetomir** answered on 26 May 2022

Hi, Nikolas, Currently, the ChartValueAxisPlotBands option accepts an array of items. Therefore, the ranges should be explicitly defined. We have a feature request in our feedback portal where alternating colors should be provided out-of-the-box. I encourage you to upvote and comment on the item with your specific scenario and desired outcome. This way, when the dev team starts working on the item, they will be able to cover all of the needs of the users. Kind regards, Tsvetomir Progress Telerik
