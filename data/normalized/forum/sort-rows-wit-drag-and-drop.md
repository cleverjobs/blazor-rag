# Sort rows wit drag and drop

## Question

**Eli** asked on 20 Apr 2020

Hi, Is it possible to sort rows in a grid dragging and dropping a row? I see there is support for the jquery version of telerik, but I can't find anything for the blazor version

## Answer

**Marin Bratanov** answered on 21 Apr 2020

Hi Elio, For the time being, you can add buttons to a grid column (or command column) and clicking them can let you have an event where you can alter the data as needed by your business logic. Once the data is updated, the grid will show its new order. A key aspect of this is that the grid can't know which field you want to change and to what value in such a case. That's assuming that there was drag-and-drop support in Blazor (which might be available around .NET 5, hopefully). In the Kendo grid this can be implemented through the separate Kendo Draggable widget where when an item is dropped, you have an event where you implement the desired logic for indexes and data, so it isn't an out-of-the-box solution either ( article link ). Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 06 Oct 2020

Hello again, There is a feature request for this now: [https://feedback.telerik.com/blazor/1488666-row-drag-and-drop-in-the-grid.](https://feedback.telerik.com/blazor/1488666-row-drag-and-drop-in-the-grid.) You can click the Follow button for status update notifications. The idea right now is that there will be an event when you drop a row that will give you the dropped row, the row over which it was dropped, and maybe whether it was above, below or on top of the row. This would let you alter the data as needed for the custom sorting logic. Regards, Marin Bratanov
