# Change grid page size does not refresh data

## Question

**Cla** asked on 04 Sep 2023

I use a grid with PageSizes settings and OnRead event to load data. When i change the selected page size combobox value, the grid does not reload. It update only the pager, but grid does not update the records. You can reproduce with this code: [https://blazorrepl.telerik.com/mHkjEoOV17OVmZ9u30](https://blazorrepl.telerik.com/mHkjEoOV17OVmZ9u30) How to solve? Thanks

### Response

**Claudio** commented on 04 Sep 2023

Solved, found PageSizeChanged event.

### Response

**Hristian Stefanov** commented on 06 Sep 2023

Hi Claudio, Thank you for sharing your outcome. I'm happy to see you quickly found the solution on your own. If we can assist with more information, I would be glad. Kind Regards, Hristian

### Response

**Tools SVI** commented on 06 May 2024

Having found this answer, I would have liked to see how you actually refresh the list following a pageSize changed event... But that's a good pointer, thanks! EDIT: I found this method, not sure it is the optimal one though. Also it seems odd that we have to manually set the new value on the grid and rebind to update the data. 🤔 void GridPageSizeChangedHandler ( int pageSize ) {
GridRef.PageSize=pageSize;
GridRef.Rebind();
}
