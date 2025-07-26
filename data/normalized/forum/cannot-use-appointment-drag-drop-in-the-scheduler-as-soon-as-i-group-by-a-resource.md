# Cannot use appointment drag & drop in the Scheduler as soon as I group by a resource

## Question

**Rol** asked on 30 Jul 2021

If I comment out the <SchedulerGroupSettings> tag drag & drop works as expected. If I enable the tag the grouping by is displayed side by side correctly, but drag & drop no longer works. Dragging within the resource group no longer gives the usual visual feedback and does not call OnUpdate. Dragging to another resource group (and another time) sometimes calls OnUpdate, but always with the original values, not the "dropped" values.

### Response

**Dimo** commented on 04 Aug 2021

Hi Roland, I tested Scheduler grouping on our online demos and in a local app on my machine. In both cases drag & drop worked as expected when grouping was enabled, and OnUpdate was fired every time with the correct arguments. Perhaps there is something else in play here? Can you compare your implementation with the online demo? If you need further assistance with this, consider sending a runnable sample, so that we can take a look.
