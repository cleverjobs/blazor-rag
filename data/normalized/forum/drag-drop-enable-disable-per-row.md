# Drag & Drop enable/disable per row

## Question

**Con** asked on 11 Apr 2023

Is it possible to enable or disable the drag & drop feature per row? I have two or more grids that display products with a quantity field. Dragging from the master grid will move the product and quantity from one grid to an other. When this happens, the secondary grid will get the total quantity from the master grid, leaving the original row with 0 quantity. When the quantity is 0, I want to disable the dragging feature for this particular row. When part or all of the quantity is returned to the original master row, the dragging feature should once again be enabled. I also want to disable drag & drop on the same grid. It seems to me that there is no drag start event to trigger a possible cancel of drag drop or a drag over event to disable droping an item.

## Answer

**Tsvetomir** answered on 14 Apr 2023

Hello, Currently, the Grid does not expose a suitable event that can be leveraged to cancel the drag. We have a pending item in our feedback portal regarding the same: [https://feedback.telerik.com/blazor/1522561-onrowdrag](https://feedback.telerik.com/blazor/1522561-onrowdrag) I encourage you to cast your vote and subscribe to the item whenever a change in the status is present. Once available, you would be able to conditionally disable the drag of certain rows. Regards, Tsvetomir Progress Telerik
