# Set Chart Position

## Question

**Cam** asked on 14 Jun 2019

I have been playing around with the pie chart example within the documentation. I have my chart within a card view and I noticed there is a position property on both the Title and Legend of the chart but not for the Chart or SeriesItems. I was wondering if it is possible to set the position of the chart within the HTML or if this is something that is going to be added later? Thanks, Cameron

## Answer

**Marin Bratanov** answered on 14 Jun 2019

Hello Cameron, Said simply, to position the chart on the page, you should position its container. The title and legend positions are relative to the chart itself, and are enums. For example, the legend can be at the top, right, bottom or left of the chart. It is not a pixel position as in CSS positioning. Thus, these properties are not applicable in the context of the entire chart or of series items - the items' positions are defined by the data and how they should be plotted, and the entire chart is just a component that the developer can place in the page like any other component. I hope this explains the situation. If I am misunderstanding something, let me know. Regards, Marin Bratanov

### Response

**Cameron** answered on 14 Jun 2019

Hi Marin, Would this mean that I could wrap th component in say a div and simply align the div in whatever alignment I need? Kind Regards, Cameron

### Response

**Marin Bratanov** answered on 14 Jun 2019

Hi Cameron, That's what I mean, yes. Just keep in mind that, by default, the chart is rendered through an <svg> element and some CSS rules may be inherited by its element (text-align is perhaps the most common). If adding some special positioning causes issues with the chart rendering, consider that possibility, and that you can also set the chart's RenderAs to Canvas so it uses a <canvas> context and not <svg>. Regards, Marin Bratanov
