# Add/remove items to SelectedItems when clicking row or checkbox

## Question

**Arj** asked on 01 Jul 2025

I’m using the Telerik UI for Blazor <TelerikGrid> in a Razor Page. I’ve bound the grid to my view‐model like this: <TelerikGrid @ref="SearchGrid" TItem="ChargeUIResult" Class="cgt-tables__table border-radius-top-zero cgt-charge-preview-grid" Width="100%" Pageable="true" Sortable="false" ConfirmDelete="true" Resizable="true" Groupable="false" Navigable="false" Reorderable="true" EnableLoaderContainer="false" FilterMode="GridFilterMode.None" EditMode="GridEditMode.Popup" SelectionMode="GridSelectionMode.Multiple" ShowColumnMenu="true" OnRead="@ReadItems" SelectedItems="@SearchState.SelectedItems" @bind-Page="@SearchState.CurrentPage" @bind-PageSize="@SearchState.PageSize">
</TelerikGrid> What I have: SearchState.SelectedItems is an IList<ChargeUIResult> that tracks checkbox selection automatically. Clicking a row currently does nothing to that list. What I want: When the user clicks a row, add that item to SearchState.SelectedItems (if it isn’t already there). When clicking a row again (or unchecking its checkbox), remove it from the list. Keep the built‐in checkbox selector in sync with row clicks and vice versa.
