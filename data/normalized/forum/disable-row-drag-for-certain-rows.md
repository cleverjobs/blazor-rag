# Disable Row Drag for certain rows

## Question

**Arm** asked on 10 Feb 2023

Is it possible to disable or simply remove the icon for the drag action on a row in a treelist? I have a scenario where the children under specific parent should not be able to be dragged to another parent or change its position withing the parent group. Thanks

## Answer

**Dimo** answered on 15 Feb 2023

Hi Arman, Yes, it is possible to disable TreeList row dragging conditionally. Use the OnRowRender event and some custom CSS. Use the OnRowRender handler to determine whether the item ( args.Item ) should be draggable. If not, set some custom CSS class to args.Class. Use the CSS code below. tr.my-no-drag-class.k-drag-cell { pointer-events: none;
} tr.my-no-drag-class.k-drag-cell.k-icon { display: none;
} Regards, Dimo
