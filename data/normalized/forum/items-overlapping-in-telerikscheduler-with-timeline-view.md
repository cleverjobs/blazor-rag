# Items overlapping in TelerikScheduler with Timeline View

## Question

**Ada** asked on 27 May 2025

Hey guys, I'm trying to setup my TelerikScheduler similar to this: Blazor Display Only All-Day Appointments in the Scheduler - Telerik UI for Blazor When I have multiple items for a single day, the items overlap, instead of stacking: REPL: Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. Which produces the overlapping items ("ABC" and "XYZ"): If you click "Next day" a couple times you'll see another example ("DEF" and "UVW" overlapping). Go one more day and it looks fine: If you click "Week" view at the top (which is also using the TimelineView), you can see an example of one of them overlapping (on the 27th): Is there any way to work around this issue? I would like to have multiple items listed per day (without time slots showing). Just stacked. Everything looks how it should in Month view. Everything looks how it should if they span more than one day generally. Thanks -Adam UPDATE: Forgot to mention - SlotDivisions="1" may have something to do with it. However, if I don't include this, it will have two columns per day which I don't want.

## Answer

**Stamo Gochev** answered on 30 May 2025

Hello Adam, I see that you have already found the relevant Knowledge Base articles that provide some workaround/customization ideas for some scenarios, but as you mentioned they are not directly applicable to the requirements you need to cover. Some other approaches including different values for "SlotDivisions" and CSS can be tested in order to hack the appearance of a slot, but they are not reliable. This being said, can you share where you have seen this being covered? There might be a room for a new feature request (something like "slot stacking"), but I will need more information to dive deep into the case in order to determine if we can generalize it and whether it can be implemented as a new feature request or if we need to dedicate time to make another Knowledge Base article that might help in some cases. Regards, Stamo Gochev Progress Telerik
