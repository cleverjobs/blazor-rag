# "Select all" on grouped grid with manual operations

## Question

**Ray** asked on 24 Apr 2025

Hi, I use grouping on a grid with manual operations and want to select all items in the grid. This works for the ungrouped data. But once the data are grouped the checkbox for selecting all items behaves strange. Is there a way around that? A sample can be found here: [https://blazorrepl.telerik.com/mJYeQIas44WKo5F346](https://blazorrepl.telerik.com/mJYeQIas44WKo5F346) Best regards, Rayko

## Answer

**Anislav** answered on 24 Apr 2025

I agree that the behavior seems odd, and it does look like a bug. However, if you change the value of the SelectAllMode parameter of the GridCheckboxColumn component from All to Current, it seems to work correctly. Here’s a an explanation from the documentation about SelectAllMode: Determines if the header cell checkbox selects all rows on the current page, or all rows in the Grid. Current selects the visible rows on the current page. All selects all the data items, including ones that may be currently filtered out. All requires the Grid to be data-bound via its Data parameter, and not OnRead. When using OnRead, the two SelectAllMode s behave identically, because the Grid controls only one page of items. So, if you’re using OnRead to load the Grid data, it's best to use SelectAllMode.Curren t. Regards, Anislav Atanasov
