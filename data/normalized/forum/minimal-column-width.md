# Minimal Column Width

## Question

**And** asked on 05 Sep 2019

Now I use constant or percentage values for column width settings. But for some columns I need constant width value after some threshold grid width. When my grid is set narrow, I need some columns set be constand width. May be will be usefull maximum column value also.

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hi Andriy, The problem with such a feature is that min-width and max-width are undefined for tables with fixed layout. You can read more about this in various places, like this thread: [https://www.sitepoint.com/community/t/fixed-layout-table-ignores-min-width-of-cells/110597/7.](https://www.sitepoint.com/community/t/fixed-layout-table-ignores-min-width-of-cells/110597/7.) Perhaps min/max width could be implemented when column resizing gets implemented and they could take effect for the user actions, but I am not sure what can be done for CSS rules. You could try using the auto table-layout and to add min-width and max-width to the td and th elements in the grid, but I am not sure whether that might not break something. Nevertheless, I would encourage you to post a feature request for such a feature in the

### Response

**Leland** answered on 08 Apr 2024

There is now a MinResizableWidth property for the GridColumn component.
