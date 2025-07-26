# When Grid is InLine edit mode, get event when user leaves cell

## Question

**Ste** asked on 28 Dec 2023

Is it possible to have TelerikGrid for Blazor configured so when grid is using inline edit, as user tabs to next cell an event is triggered so that manual updates can be done to the row data, as simplest example, cells are quantity, unitcost, gst, total so that as unitcost is changed / exited the gst is calculated as quantity*unitcost*0.10 and total is calculated as quantity*unitcost+gst I've been searching for hours and I'm starting to arrive at conclusion it is not easily done. Cheers Steve Wark

## Answer

**Radko** answered on 01 Jan 2024

Hi Steve, If I understand correctly, what you are after is knowing when an editable cell has been blurred. What I can suggest is to either use Incell edit, which would then trigger the appropriate CUD events on each tab (as editing in fact occurs on each cell change), or introduce a custom JavaScript event handler attached to the Grid itself, listening for a focusout. Note that if you are to consider the latter approach, a JavaScript event is likely to be necessary rather than a Blazor one, as you may have to rely on the relatedTarget property, which is currently not present within the C# counterpart. Here is a very simple snippet that might serve as a foundation if you are to take this path. In it, I have defined a custom JS event that is triggered whenever an edit cell has lost focus: [https://blazorrepl.telerik.com/QoklYPkZ30JAxJCe23](https://blazorrepl.telerik.com/QoklYPkZ30JAxJCe23) I hope the above helps. Regards, Radko Progress Telerik
