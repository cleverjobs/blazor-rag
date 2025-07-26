# Transitions on Blazor Gauges drops to min then to new value

## Question

**KenKen** asked on 17 Mar 2023

When transition is true the gauge operates in a visually unappealing way by default and I'm wondering if there is a setting or method to make it work better. Basically if the gauge (linear or radial) has a value of 20 then jumps to 30, the needle drops to 0 then transitions to 30. When really it should transition from 20 to 30. To reproduce use the Telerik demo page @: [https://demos.telerik.com/blazor-ui/radialgauge/overview](https://demos.telerik.com/blazor-ui/radialgauge/overview) Paste in 35 into the Change Pointer Value box and watch what happens. Note : Don't type in 35 because it will jump to 0 then to 3 before you type the 5 so it makes it harder to see. Is there a way to stop this and have the gauge go from the last value to the new value??

## Answer

**Nadezhda Tacheva** answered on 21 Mar 2023

Hi Ken, Indeed, this behavior can be improved. We have a bug report logged on the matter: ArcGauge animation flickers when updating the value The item is opened for the ArcGauge but applies to other Gauge types as well. I voted for it on your behalf and you may follow it to get status updates. Regards, Nadezhda Tacheva Progress Telerik
