# Screen reader not reading column name when the column header is sorted

## Question

**Mik** asked on 20 Jul 2022

When using either Jaws or NVDA screen readers with the grid, and the column header is being sorted (it doesn't matter whether ascending or descending), that column name is no longer read by the screen reader. Instead it reads out "sorted ascending (or descending)". I would expect that it should read out the column name and then the sort. For example: "Name sorted ascending". When the column is not sorted, then the column name is read out correctly. It should also be noted that this happens whether the focus is on the header cell or a regular cell for that column.

## Answer

**Nadezhda Tacheva** answered on 25 Jul 2022

Hi Mike, I am testing with NVDA version 2021.3.1. The reader indeed reads the sort operation - be that ascending, descending or no sorting. However, hovering over the column header text afterwards is still read correctly on my end. It seems that there is no issue with reading the content of the column cells as well. Please see video attached of the result I am getting. Regards, Nadezhda Tacheva

### Response

**Mike** commented on 25 Jul 2022

Hi Nadezha, Thanks for the response. Unfortunately, hovering with the mouse is not the same as navigating with the keyboard. Screen reader users are usually blind and are not able to use the mouse, so they rely on keyboard navigation. If you look at your Keyboard Navigation demo for the grid, and use NVDA with the keyboard, you will see that the column header is not read when that column is sorted. In the screenshot above you can see that the Unit Price is sorted ascending, but if you use NVDA with the keyboard, it doesn't get read. Here is what the NVDA Speech Viewer shows when I navigate the header row, and then navigate the first row of data. (Note: the Speech Viewer displays in text what is read by the screen reader. It's not on by default but you can enable it in NVDA's settings) Data table table Product Name Product Name column filter menu settings column header subMenu row 1 Product Name Product Name column filter menu settings column 2 Sorted in ascending order column header subMenu sorted ascending row 1 Sorted in ascending order column 3 Discontinued Discontinued column filter menu settings column header subMenu row 1 Discontinued Discontinued column filter menu settings column 4 False row 2 Discontinued Discontinued column filter menu settings column 4 2.50 row 2 Sorted in ascending order column 3 Geitost row 2 Product Name Product Name column filter menu settings column 2 I'm using the arrow keys to navigate, and as you can see above, I start with the Product Name, and it gets read. When I then arrow to the Unit Price, It just says Sorted in ascending order, but never actually reads the name. The same is true on the data row. Thanks, Mike

### Response

**Nadezhda Tacheva** answered on 28 Jul 2022

Hi Mike, Thank you for the additional details! Indeed, this behavior is reproducible using the keyboard navigation. In the meantime, another client has logged a bug report on the matter in our public portal: Grid Column Headers accessibility compliance I added your vote there to increase its popularity as we take the community demand into consideration when planning the bug fixes. You may follow the report, so you can receive email notifications on status updates. This is the best way to keep in track with the progress of the fix. Regards, Nadezhda Tacheva Progress Telerik
