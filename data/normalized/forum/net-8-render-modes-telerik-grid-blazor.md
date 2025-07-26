# >.net 8 render modes Telerik Grid Blazor

## Question

**Aja** asked on 20 Mar 2024

Hello I have a grid which has a "Add" button which is defined in a GridBarToolBarTemplate which opens a pop up used for adding a new record displaying in the Grid. With Blazor .Net 8 I am using Stream rendering to show the grid. I now want to put the add button in a different component so I can use another "Interactive" rendering mode just for adding a new record I have tried during this but it doesnt seem to work. Is this possible? and how do Iget it to work? Thanks Aj

## Answer

**Dimo** answered on 21 Mar 2024

Hi Aj, You need interactive render mode in all . razor files, which contain our components. Stream rendering more is not enough. See section Interactive render mode in new .NET 8 apps. If you already have interactive render mode wherever there are Telerik Blazor components, then please open a private ticket and send a small runnable app for inspection. Regards, Dimo Progress Telerik
