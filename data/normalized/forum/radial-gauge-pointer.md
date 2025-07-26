# Radial Gauge Pointer

## Question

**Evg** asked on 01 Aug 2022

Hello! I want to add a radial gauge in my web application. I set the "From" and "To" properties for the Scale Range and when the desired value is increased I can see the changes. But I want to change the pointer according to the "From" and "To" properties of the Scale Range. I can set the "Value" property equal to "To" but when it changes the pointer seems to reset and not to increase. I want the pointer start from the last "To" value and end to its "Value" property which is equal to the new "To" property. Any ideas about this? My demo code: <TelerikButton OnClick=@IncrementRange>Add Range</TelerikButton> <TelerikRadialGauge> <RadialGaugeScales> <RadialGaugeScale> <RadialGaugeScaleRanges> <RadialGaugeScaleRange From="@FromRadialGauge" To="ToRadialGauge" Color="red"></RadialGaugeScaleRange> </RadialGaugeScaleRanges> </RadialGaugeScale> </RadialGaugeScales> <RadialGaugePointers> <RadialGaugePointer @ref="@RadialGaugePointerRef" Value="@ToRadialGauge"> </RadialGaugePointer> </RadialGaugePointers> </TelerikRadialGauge> My code: private int FromRadialGauge=0; private int ToRadialGauge=0; private void IncrementRange() { ToRadialGauge=ToRadialGauge + 10; RadialGaugePointerRef.Value=ToRadialGauge; } Thanks in advance!

### Response

**Dimo** commented on 03 Aug 2022

Hi Evgenia, If I understand correctly, you are talking about this behavior, which affects all gauges and is a confirmed bug in our backlog: LinearGauge always restarting from 0 ArcGauge flickers when updating the value If this is the case, I am sorry it's causing you trouble. Please vote and follow these items to get status updates when we fix them.
