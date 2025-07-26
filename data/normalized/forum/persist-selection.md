# Persist selection

## Question

**Ron** asked on 01 Apr 2021

I have a grid that I added a column for a checkbox to select the row. I have multiple selection on. Now I want to respond to a button click and display the selected items in the grid. But I am finding that the act of clicking on the button deselects the selected items. How do I keep the keep the grid selection through a click on a button?

## Answer

**Marin Bratanov** answered on 01 Apr 2021

Hello Ronald, If the button is in the grid, you would need to prevent the click from getting to the grid row as shown here: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selection-in-template](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selection-in-template) If the button is outside of the grid, it should not affect the grid selection. If it does, please post here a sample that shows the problem. Regards, Marin Bratanov

### Response

**Ronald** answered on 01 Apr 2021

<TelerikGrid Data="@excludedOrganisms" Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true" SelectionMode="GridSelectionMode.Multiple" SelectedItems="@selectedExcludedOrganisms"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field="@(nameof(OrganismName.OrganismId))" Title="Group Id" Width="120px" /> <GridColumn Field="@(nameof(OrganismName.Name))" Title="Organism Name" Groupable="false" /> <GridColumn Field="@(nameof(OrganismName.CreatedBy))" Title="Created By" /> </GridColumns> </TelerikGrid> <div class="center"> <TelerikButton class="GroupingButton" OnClick="@OnForwardClick" Icon="caret-double-alt-right"></TelerikButton> <TelerikButton class="GroupingButton" OnClick="@OnReverseClick" Icon="caret-double-alt-left"></TelerikButton> </div> <TelerikGrid Data="@includedOrganisms" Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true" SelectionMode="GridSelectionMode.Multiple" SelectedItems="@selectedIncludedOrganisms"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field="@(nameof(OrganismName.OrganismId))" Title="Group Id" Width="120px" /> <GridColumn Field="@(nameof(OrganismName.Name))" Title="Organism Name" Groupable="false" /> <GridColumn Field="@(nameof(OrganismName.CreatedBy))" Title="Created By" /> </GridColumns> </TelerikGrid> The buttons are in between the grids. The button handlers right now are empty async Task OnForwardClick() { StateHasChanged(); } async Task OnReverseClick() { StateHasChanged(); } I would expect if I put a breakpoint in one of the handlers that the selected items list would have values in it. And after returning from the handler the items still show selected on the grid. Both of these things don't seem to be happening. private IEnumerable<OrganismName> selectedIncludedOrganisms { get; set; }=Enumerable.Empty<OrganismName>(); private IEnumerable<OrganismName> selectedExcludedOrganisms { get; set; }=Enumerable.Empty<OrganismName>(); Thank you for your prompt response.

### Response

**Marin Bratanov** answered on 01 Apr 2021

Hello Ronald, You should use the @bind-SelectedItems syntax so the grid can actually update the view-model with the selected items. The current syntax only provides an initial collection of selected items to the grid. You can find some examples here: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.) Without that, the grid does not update the view model, and the button click re-renders things with the state from the view-model that does not have the newly selected items. You can also read more on value binding here: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding) Regards, Marin Bratanov Progress Telerik
