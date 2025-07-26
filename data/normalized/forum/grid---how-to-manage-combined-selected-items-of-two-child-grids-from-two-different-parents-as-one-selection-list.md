# Grid - How to manage combined selected items of two child grids from two different parents as one selection list.

## Question

**Jam** asked on 24 Oct 2024

I have a hierarchal grid of two entities, one the parent and one the child through a detail template. I would like to know how I can gather selected checkbox column items from a child grid of one parent and the selected checkbox column items from a child grid of a second parent in a "merged" collection. Currently the @bind-selected property of a detail template child grid definition only applies to one child grid of a parent row. How can I manage adding to the same collection, values of a child grid of the same type below a second parent row? Do you/anyone have any examples on how to develop this solution? Thanks, for any help!

## Answer

**Nadezhda Tacheva** answered on 29 Oct 2024

Hi James, You can handle the SelectedItemsChanged event of the child Grid declared in the DetailTemplate and add the newly selected children in a single collection. Take your time to implement the approach and let me know if you are facing any issues. If so, please send an isolated runnable version of your configuration, so I can revise it and validate what may be missing. Regards, Nadezhda Tacheva Progress Telerik

### Response

**James** commented on 30 Oct 2024

Nedezhda, thanks for the response. A question, does your solution apply when I am selecting using a GridCheckboxColumn too? Please note that I already have a row selection event in the detail template child grid which opens a drawer with the child grid row details. Then in each of the child rows I also have a GridCheckboxColumn, which I like to gather all selected items from ALL child grid rows even if they are inside a separate parent grid row. Does your SelectedItemsChanged event of the child Grid handle this scenario? Let me know, thanks!

### Response

**Nadezhda Tacheva** commented on 04 Nov 2024

Hi James, Yes, the suggested solution applies to the CheckBox selection, too. The SelectedItemsChanged event fires anytime when the user changes the selection - be that through clicking on the row or by checking the selection CheckBox. And to your second question - the answer is also yes. The idea is to handle the SelectedItemsChanged of the child Grid, so you can get the items that the user selected in the child Grid and add them to the desired collection. I hope this provides enough clarity on the matter.
