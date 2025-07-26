# Identify which grid cells are "dirty"/have been changed

## Question

**Cla** asked on 07 Nov 2023

In an editable grid, is there some way to identify cells that have been edited from their original values? In this case, I'm looking to style them differently to make it visibly apparent that they are "dirty". We have a solution that is functional but cumbersome. Within each record, we maintain a list of dirty fields it contains (updated in the OnUpdate handler). Then we assign an OnCellRender handler to every column which adds a "changed-cell" class conditionally if that field on that record is dirty. It's a pain adding this OnCellRender handler to everything; I would rather it be automatic. Does something exist that would allow me to easily accomplish this? If not, would a feature request be possible to automatically add a class to a cell when it is changed? Thanks.

### Response

**Hristian Stefanov** commented on 09 Nov 2023

Hi Clark, The Batch Editing functionality in our Grid seems to align with what you are describing. We have a runnable demo that demonstrates it: Grid - Custom Batch Editing. Could you check if this is what you are searching for by taking a look? I look forward to hearing from you. I remain at your disposal to assist further if needed. Kind Regards, Hristian

### Response

**Clark** commented on 09 Nov 2023

Thanks for your reply, Hristian. That example is using OnCellRender="@((GridCellRenderEventArgs args)=> OnCellRenderHandler(args, "ColumnName"))" on each column, which is exactly what we're doing. In fact, I suspect our original developer who incorporated this copied it from the example you linked. My goal is to not repeat that on every editable column. I feel that this functionality should automatically be applied on any column that's editable; I shouldn't have to add OnCellRender to apply "k-changed-cell" myself on every column. As far as I know, it seems like this needs to be a feature request?

### Response

**Hristian Stefanov** commented on 10 Nov 2023

Hi Clark, Thank you for getting back to me with feedback. I confirm that the demo I linked is a custom implementation of batch editing, created to get as close as possible to such a built-in feature for the time being. That said, it can have some slight differences from built-in Batch Editing. Here is the public item for implementing a built-in batch editing feature: Batch Editing. I voted there on your behalf and raised the priority. Once the built-in feature is implemented, this functionality will automatically be applied to any column that's editable. If we can assist with more information, I would be glad. Kind Regards, Hristian
