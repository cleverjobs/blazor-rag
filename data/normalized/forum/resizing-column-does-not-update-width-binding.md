# Resizing column does not update Width binding

## Question

**Ser** asked on 30 Jun 2021

I have multiple grids in one view and would like to sync the columns widths. That is, if a user resizes a column, I want that column to be resized in all the grids in the view. I bound the Width property to a field and while it sets the initial width, however, resizing the column does not change the bound value. Is this not supported? There also doesn't seem to be a Resize event either, so no way to workaround the problem. Any suggestions? Thanks in advance.

## Answer

**Jeffrey** answered on 30 Jun 2021

An alternate approach could be to use the OnStateChanged event in the main grid and then interrogate the GridState to propagate the column widths to the other grids. This is a rather brute-force way of doing things because the OnStateChanged event isn't going to tell you which column was updated so you would have to set every column's width each time the event fires.

### Response

**Sergio** commented on 30 Jun 2021

Yes, that is still going to be problematic since the GridColumnState only returns an index. My grid has nested columns, so I'd have to hard-code all the indices I'm interested in. The class does have a Column property, but they're always null...

### Response

**Marin Bratanov** commented on 03 Jul 2021

Jeffrey is correct that this is the approach. You will have to re-render the grid anyway if you want to resize a column, so the state is the current tool to tell the grid to do something. In the state you have all the column widths too. You can Vote for and Follow the addition of more metadata in the column state here: [https://feedback.telerik.com/blazor/1489571-add-field-property-in-grid-s-columnstate.](https://feedback.telerik.com/blazor/1489571-add-field-property-in-grid-s-columnstate.) Perhaps in a future version an Id would also be added if set for the column.
