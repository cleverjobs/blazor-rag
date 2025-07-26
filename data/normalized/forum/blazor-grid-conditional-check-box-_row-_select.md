# Blazor grid conditional check box (row )select

## Question

**Aud** asked on 01 Apr 2021

Iam using Telerik Blazor grid in one of my
application. The grid displays a list of items along with the itemType. I need to implement a feature where
users can select the items using a checkbox. I have done that using the GridCheckboxColumn.
Now I want to limit the user to only select one item of a specific itemType. Such
that the selected items will always belong to a distinct item type. No two
items of the same itemType can be selected. Is this possible in the current version? Could
you point me to any resource which will allow me to achieve this? I want to do this on the checkbox click
event or something similar.

## Answer

**Marin Bratanov** answered on 05 Apr 2021

Hi Audhut, You can use the SelectedItemsChanged event which will give you the current selection in the grid. You can then compare it with the current one, employ the desired business logic to determine what needs to remain selected, and set that to the SelectedItems collection of the grid. Regards, Marin Bratanov
