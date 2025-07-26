# Hide or reduce width for hierarchy grid cells

## Question

**Iva** asked on 13 Jun 2021

Hello! It is possible to hide or reduce width for grid's hierarchy cells? On mobile devices, this place is very valuable and is not used effectively. When setting the value of a class property .k-hierarchy-cell { display=none } the nested table does not fill the full width of the container

## Answer

**Dimo** answered on 15 Jun 2021

Hi Ivan, Yes, it is possible to save some space in two ways: Reduce the width of the hierarchy column. Its width is controlled by the column class (.k-hierarchy-col), not by the cell class. Reduce or remove the paddings of the cell, which holds the nested table (.k-detail-cell) The styles below use the same specificity as our stylesheets. They will work if you add them after our stylesheet, otherwise you need to increase the selector specificity. .k-grid.k-hierarchy-col { width: 16px;
}.k-grid.k-detail-row.k-detail-cell { padding: 0;
} Regards, Dimo Progress Telerik
