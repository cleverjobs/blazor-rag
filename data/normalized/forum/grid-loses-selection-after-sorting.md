# Grid loses selection after sorting

## Question

**Bri** asked on 25 Apr 2022

The Telerik Blazor Grid doesn't seem to retain the currently selected items when sorting. I've got a simple single select grid and have bound the SelectedItems property to a similarly named field in code behind. The SelectedItems field definitely contains a single entry ok and selecting items in the grid updates this as expected. However, when sorting, the grid no longer highlights the selected item as selected, and the check box column is not selected, even though the SelectedItems field still contains a single entry. Is this the intended behaviour? And, if so, how can I get the grid to highlight the selected item after sorting? I'm using Telerik Blazor UI 3.2.0.

### Response

**Brian** commented on 25 Apr 2022

Managed to resolve. Problem was resolved by calling ToList when instantiating my data source for the grid.

## Answer

**Brian** answered on 25 Apr 2022

Managed to resolve. Problem was resolved by calling ToList when instantiating my data source for the grid.
