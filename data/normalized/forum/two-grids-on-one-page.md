# Two Grids on one page

## Question

**And** asked on 15 Apr 2020

Hello, I have two grids on one page. The first one has SelectionMode="GridSelectionMode.Single" and the second one is re-reading the data (SQL) based on this selection. I am using Single Selection and handling the SelectedItemsChanged event. This works fine except the first grid is not unselecting the previously selected row so now it displays all previously selected rows. Click on first grid first row. First grid first row selected. Grid2 content refreshed. That's fine. Click on first grid second row. First grid second row selected. Grid2 content refreshed. But the grid1 first row is still selected. I am using UI Kendo 2.1. Thanks.

## Answer

**Andrey** answered on 15 Apr 2020

Here is the code: <div class="col-md-4"> <TelerikGrid Data="@Insurers" Height="400px" Sortable="true" FilterMode="GridFilterMode.FilterRow" SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<InsurerVM> insurerVMList)=> OnSelectInsurerAsync(insurerVMList))" Resizable="true" Reorderable="true" ScrollMode="@GridScrollMode.Virtual" Pageable="false" RowHeight="40"> <GridColumns> <GridColumn Field="@(nameof(InsurerVM.Name))" Title="Insurance Company" Width="200px" /> <GridColumn Field="@(nameof(InsurerVM.Counter))" Title="Counter" Filterable="false" Width="70px" /> <GridColumn Field="@(nameof(InsurerVM.Selected))" Title="Selected" Filterable="false" Width="75px" /> </GridColumns> </TelerikGrid> </div> <div class="col-md-4"> <TelerikGrid Data="@SubAccounts" Height="400px" Sortable="true" FilterMode="GridFilterMode.FilterRow" SelectionMode="GridSelectionMode.Single" Resizable="true" Reorderable="true" ScrollMode="@GridScrollMode.Virtual" Pageable="false" RowHeight="40"> <GridColumns> <GridColumn Field="@(nameof(SubAccountVM.Name))" Title="Product" Width="200px" /> <GridColumn Field="@(nameof(SubAccountVM.Counter))" Title="Counter" Filterable="false" Width="70px" /> <GridColumn Field="@(nameof(SubAccountVM.Selected))" Title="Selected" Filterable="false" Width="75px" /> </GridColumns> </TelerikGrid> </div>

### Response

**Marin Bratanov** answered on 15 Apr 2020

Hello Andrey, Could you compare against this example to see what is the difference causing the issue: [https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event?](https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event?) If this does not help you resolve it, can you post here a runnable version of the snippet that I can investigate? Also, please make sure that the upgrade to 2.10.0 went well and that any CDN references are also updated: [https://docs.telerik.com/blazor-ui/upgrade/overview](https://docs.telerik.com/blazor-ui/upgrade/overview) On a side note, in a Blazor scenario you should use Telerik UI for Blazor, the Kendo UI suite is not designed for Blazor. Regards, Marin Bratanov

### Response

**Andrey** answered on 15 Apr 2020

Hi Marin, Thank you for quick answer. I've found my problem. Grid2 getting data method should be sync. It was async Task. sync Task OnSelectFirstGrid(...) { SecondGridData=await GetDataAsync(...) //Error: multiple selection in first grid SecondGridData=GetData(...) //Works fine }
