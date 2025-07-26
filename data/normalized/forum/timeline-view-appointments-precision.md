# Timeline view appointments precision

## Question

**Ale** asked on 05 Oct 2022

Hi, is there a way to achive appointment precision like in the asp.net scheduler? Let's say I add 2 appointments. Starting at 8:30 and finishing at 9:15, and another one starting at 9:20. The blazor scheduler result is going to be like this: The asp.net scheduler result is going to be like this: Thanks.

## Answer

**Nadezhda Tacheva** answered on 07 Oct 2022

Hi Alessio, Indeed, by current design the appointments start and end time is rounded up. It will be useful to render them with higher precision. We currently have an opened feature request for that: More precise representation of start/end times on scheduler - Exact Time Rendering I voted for it on your behalf as we keep track on the gathered community votes in order to prioritize the component enhancements. You may subscribe for the item to get status updates. This is the easiest way to follow the progress of the feature. Regards, Nadezhda Tacheva
