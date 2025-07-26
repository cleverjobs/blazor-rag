# Chart drag, context menu and actions

## Question

**Nik** asked on 05 Jul 2022

Hello, I have some questions regarding the different TelerikCharts. 1. Is there a way to enable drag on a series, to change the value? I have attached some example code, on how I could like it to work. 2. Is there a way to disable series click when right clicking? I still would like to use series click, but only on leftclick. 3. Is there a way to open a context menu on a series, when right clicking? Regards, Nikolas

## Answer

**Dimo** answered on 08 Jul 2022

Hello Nikolas, I have to admit that all three behaviors are currently not supported. Sorry about that. Dragging to change the series value is theoretically possible, but implies that Charts should adopt CRUD operations. That is a huge change in the component paradigm. We can consider it if there is enough demand. Currently I don't see previous such requests in our archive - probably due to the fact that Charts are often used for aggregated or analytical data that is not subject to changes. The SeriesClick event may expose the mouse button in the event arguments in future product versions. The Context Menu integrates with HTML elements, while the Chart renders as SVG. Regards, Dimo

### Response

**Nikolas** commented on 08 Jul 2022

Hello Dimo, Thanks for the answer. Regards, Nikolas

### Response

**Nikolas** commented on 14 Jul 2022

Hello Dimo, Is there any estimate on "future product verions" with the SeriesClick event arguments, or should I create a feature request on the different things and let people vote? Regards, Nikolas

### Response

**Dimo** commented on 15 Jul 2022

Hi Nikolas, It's best to submit a feature request for better visibility. Here is one that I created on your behalf.
