# Grid - persist row selection when changing pages.

## Question

**TimTim** asked on 06 Jul 2022

Hello, I have a grid which dynamically calls data for each page(uses OnRead). I can not figure out how I can keep the rows selected accross multiple pages. I see that the rows remain in the "selectedRows" list, but they are not selected in UI when I am changing pages. I have tried a bunch of approaches but nothing works. Is this even possible? <TelerikGrid @ref="@WOrderGrid" TItem="@WOrderAssignDto" SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="@selectedRows" Resizable="true" Reorderable="true" FilterMode="@GridFilterMode.FilterRow" Pageable="true" PageSize="15" Sortable="true" SortMode="@SortMode.Multiple" OnRead=@ReadItems>

## Answer

**Tim** answered on 06 Jul 2022

Solved it manually.
