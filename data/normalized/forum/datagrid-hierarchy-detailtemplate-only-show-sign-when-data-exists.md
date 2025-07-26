# DataGrid Hierarchy DetailTemplate Only Show + Sign When Data Exists

## Question

**Mik** asked on 15 Apr 2022

Is it possible to only show the + in a hierarchy data grid when data exists for that row? We want a visual indicator to only show to the user when there is actual detail rows that can be viewed.

## Answer

**Svetoslav Dimitrov** answered on 20 Apr 2022

Hello Mike, The DetailTemplate is of type RenderFragment. In Blazor, you can place any arbitrary HTML inside the RenderFragment -- from something as simple as ul/ol with list items to something as complex as a Grid. Unfortunately, there is no provision in Blazor to determine the content of the RenderFragment at runtime in order to notify the parent of what's in it. Currently, the parent Grid does not have the knowledge if the DetailTemplate has some plain text or a complex component. Having said the above, I am sorry to report that such functionality would not be possible at this point. Regards, Svetoslav Dimitrov
