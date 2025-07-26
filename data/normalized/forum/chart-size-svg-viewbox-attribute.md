# Chart Size (svg viewbox attribute)

## Question

**And** asked on 22 Jun 2021

Hi Do you plan to add the viewBox attribute to the svg tag to be able to scale charts? [https://css-tricks.com/scale-svg/#the-viewbox-attribute](https://css-tricks.com/scale-svg/#the-viewbox-attribute)

## Answer

**Nadezhda Tacheva** answered on 25 Jun 2021

Hello Andrey, At this stage there are no plans on exposing the viewBox attribute. The chart can render either with SVG elements, or with a <canvas> tag depending on the chosen rendering mode. As viewbox is not applicable for <canvas> an approach for including it cannot be used to cover both rendering modes for the chart. With that being said, as an alternative we have considered implementing a feature for ability to zoom on particular part of the chart. We have an opened request for that feature in our public
