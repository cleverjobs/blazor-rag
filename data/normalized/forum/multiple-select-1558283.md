# multiple select

## Question

**n/an/a** asked on 18 Mar 2022

Hello, Any way possible that you can use GridCheckboxColumn multiple select and fire a custom method only for those selected items? I didn't see anywhere is the documentation if it's possible. Thank you

## Answer

**Marin Bratanov** answered on 18 Mar 2022

Hello, You can obtain the items that the user selected via the SelectedItems collection so that you can employ the desired business logic on them. If you need an event to know when selection happens - there is the SelectedItemsChanged event. You can find examples of both here: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple) Regards, Marin Bratanov
