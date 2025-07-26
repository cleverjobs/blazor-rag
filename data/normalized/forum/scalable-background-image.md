# Scalable background image

## Question

**Ber** asked on 06 Jan 2023

Hi, We have to migrate and modernize an old application using new development tools and I try to find the tools which can reproduce the features we had so far. Having a background image in the chart is one of them. So my question is, can your Blazor chart component have a background in the chart area only as shown in the attached image? If yes, is it possible to get the position and the
size of the chart area in pixels? This is because the features in the image must fit to XY scales in the chart, so I need to resize the image accordingly. I would like to make a Blazor Hybrid application. Thank you Bertrand

### Response

**Dimo** commented on 11 Jan 2023

Bertrand - sorry, our Chart doesn't provide such a functionality. If possible, set the background to another element, which holds the Chart in it.
