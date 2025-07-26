# DragClueField shows null when dragging multiple objects

## Question

**Fab** asked on 03 Aug 2023

Hi, the DragClueField always shows 'null' when dragging multiple objects instead of just one. When only one item is dragged it shows the specified attribute but when it's two or more objects from a grid it salways shows 'null'. Are you aware of this bug?

## Answer

**Svetoslav Dimitrov** answered on 08 Aug 2023

Hello Fabian, Can you reproduce the same behavior with the code snippet from our Drag and Drop documentation article (the Drag and Drop multiple rows section)? I have tested it multiple times and the correct Drag Clue is always rendered (N items selected). I would appreciate it if you modify the code snippet and send it back to us for further investigation. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Fabian** commented on 08 Aug 2023

Hey Svetoslav, no I can not reproduce the bug. Our implemenatiton of the grid is huge. I have the inkling that it might be caused by us using the "SelectedItems" attribute from your grid - thats the only difference I can spot that might cause somethign like that. Here is a screenshot from our code where I marked the two relevant spots. Also I have to clarify the clue shows what it is supposed to when only dragging one item. But when dragging multiples it only shows the correct amount and then 'null' - like this:

### Response

**Dimo** answered on 11 Aug 2023

Hi Fabian, The null label indicates a missing localization key, specifically Grid_DragItems. Please update the Telerik . resx files in your app. Regards, Dimo Progress Telerik

### Response

**Fabian** commented on 11 Aug 2023

Hey Dimo, thank you very much! That was the issue. Problme solved. Thanks!
