# Render Custom Bar Chart axis tick labels

## Question

**Ric** asked on 09 Aug 2024

Blazor C# .Net I have a vertical bar chart. The bars represent colors so the labels are like "red", "blue"... Every time I do a search on the database the color count and values change. Like next time it will be "Yellow", "red"... I want to draw the labels my self and have the colors as little squares under the name of the color. Like get from where I am... to labels like I tried ChildContent on the ChartCategoryAxis but my function void CustomColorLabelDraw(RenderTreeBuilder builder) does not get the index of the tick, and does not get called as many times as there are bars, and the output if I return a AddMarkupContent of "My test string" ends up above the entire chart and outside the chart. How does on use a C# function to generate the HTML to render a tick label?

### Response

**Richard** commented on 12 Aug 2024

It's a Monday. Any comments on this? I'm kind of stuck here.
