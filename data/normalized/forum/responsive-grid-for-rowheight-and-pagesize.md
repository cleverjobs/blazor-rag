# Responsive Grid for RowHeight and PageSize

## Question

**Jer** asked on 25 Oct 2021

The blazor-ui samples blazor-ui/ResponsiveGrid.razor at master · telerik/blazor-ui · GitHub show using a windows hook to make a responsive GRID. I've had pushback on this saying that BootStrap using CSS can do this instead. Is there another approach using CSS that can make the GRID responsive to window resizing and changes in media sizes?

## Answer

**Marin Bratanov** answered on 26 Oct 2021

Hi Jerdobi, The grid is already responsive - you can set its Width and Height to 100%, and it will fill up its container. Then, it is up to the container and the application to define the desired behavior and sizes. As for changing the page size - that is not something that should or could be controller with plain CSS, as it is an application behavior rather than appearance. Regards, Marin Bratanov
