# Bug with OnRowRender and custom background colors

## Question

**Dan** asked on 25 Mar 2022

Hi, I'm using Blazor for UI 3.1.0 with a TelerikGrid. I want to implement a custom background color for certain rows in the grid. As a test I started with setting up a style for the row and attaching a OnRowRender event: <style>.PriorPeriodAdjustedRowFormatting { background-color: orange;
}.ApprovalForPaymentRowFormatting { background-color: lightgreen;
} </style> <TelerikGrid Data="@TransactionsGridData" EditMode="@GridEditMode.Popup" Height="450px" Pageable="true" PageSize="20" Sortable="false" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Resizable="true" Class="smallerFont" Reorderable="true" SelectionMode="@GridSelectionMode.Multiple" SelectedItems="@SelectedTransactions" SelectedItemsChanged="@((IEnumerable<MixedTransactions> list)=> OnTransactionsSelected(list))" OnStateInit="@((GridStateEventArgs<MixedTransactions> args)=> OnStateInitHandler(args))" OnRowRender="@OnTransactionsRowRender"> ... then in the OnTransactionsRowRender event I just forced every row to match one of the styles as a test, like so: void OnTransactionsRowRender(GridRowRenderEventArgs args)
{
args.Class="PriorPeriodAdjustedRowFormatting";
} This should turn the background color on every row orange but it doesn't, it only turns half of them orange: If I repeat the same test but ask for the color to be orange (instead of the background color) it turns all the text orange. So for example if the style is this: <style>.PriorPeriodAdjustedRowFormatting { color: orange;
}.ApprovalForPaymentRowFormatting { background-color: lightgreen;
} </style> then it does color the text in each row orange: It looks like the alternating row style is overwriting any custom settings for the background-color in OnRowRender but it respects the custom settings for color. Can it be fixed so it applies properly when set via OnRowRender?

## Answer

**Marin Bratanov** answered on 26 Mar 2022

Hi Daniel, The grid has some built-in CSS rules and alternating rows have a background color and/or gradient that can override your own rules. Thus, what you need is 1) heavier selector and 2) potentially to remove the linear-gradient rule (set it to none) to negate what comes from the built-in rules. You can find an example in the docs here: [https://docs.telerik.com/blazor-ui/components/grid/events#onrowrender](https://docs.telerik.com/blazor-ui/components/grid/events#onrowrender) and also another here [https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background#css-only-approach](https://docs.telerik.com/blazor-ui/knowledge-base/grid-conditional-cell-background#css-only-approach) Regards, Marin Bratanov
