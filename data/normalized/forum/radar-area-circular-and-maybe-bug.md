# Radar Area circular and maybe bug?

## Question

**Nik** asked on 05 Oct 2021

"Circular" Is it possible to make the Radar Area circular? How it looks now: How it should look: "Bug" I also have a problem with the ChartValueAxis, I need to set the ZIndex to 1. If I don't, then the numbers disappear underneath the chart if I change the opacity on the series to 1. Is this normal behaviour, or? Normal: ZIndex 1: Code: <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> --------------------------------- <ChartValueAxes> <ChartValueAxis ZIndex="1"> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> Thanks Regards, Nikolas

## Answer

**Marin Bratanov** answered on 06 Oct 2021

Hello Nikolas, The type of chart you are looking for is something we call a Polar Area Chart, and it is not yet available in Blazor. So, I made this enhancement request on your behalf so you can Follow its implementation: [https://feedback.telerik.com/blazor/1538233.](https://feedback.telerik.com/blazor/1538233.) The situation with the z-index for the axis is the same, here is the request for that: [https://feedback.telerik.com/blazor/1538234.](https://feedback.telerik.com/blazor/1538234.) Since I made them on your behalf, you are automatically following them, and I have added your Vote for them on your behalf as well. Regards, Marin Bratanov

### Response

**Nikolas** commented on 07 Oct 2021

Hello Marin, Thanks for the Polar Area Chart request. Just to be clear regarding the Z-Index, the option is available, and I'm using it. The question was: Is it the right behaviour, that if you dont use the Z-Index, when the opacity is set to 1, then the numbers go behind the drawing? Or is it a bug? Regards, Nikolas

### Response

**Marin Bratanov** commented on 07 Oct 2021

Ooops, my bad on somehow missing the z-index feature. I've deleted the portal page for it to avoid confusion for anyone else. Indeed, it is expected - by default the data has priority (that is the series).
