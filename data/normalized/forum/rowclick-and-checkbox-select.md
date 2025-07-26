# RowClick AND Checkbox select

## Question

**Ron** asked on 01 Apr 2021

I like the ability to select a row by clicking on a checkbox. But the handler for clicking on the row supplies the contents of the row where as putting a GridCheckbox like <GridColumns> <GridCheckboxColumn ValueChanged="@((bool value)=> ValueChanged(value))"/> only gives me the state of the checkbox. Is there anyway to have the row click handler also respond to the checkbox? Or how can I get the contents of the row that the checkbox that was clicked is on?

## Answer

**Marin Bratanov** answered on 05 Apr 2021

Hi Ronald, To handle selection you should use the dedicated event the grid exposes for that - OnSelectedItemsChanged. You can find some more details in your other thread with a similar case. Regards, Marin Bratanov

### Response

**Ronald** answered on 05 Apr 2021

Forgive me for not understanding. Right now to respond to the OnSelectedItemsChanged event I set a handler. This would handle the case where a check-box was used to select the row. But if I disable (prevent default) the row click event, doesn't that make it so that OnRowClick is not handled? I want OnSelectedItemsChanged AND OnRowClick to be handled by the same handler.

### Response

**Marin Bratanov** answered on 05 Apr 2021

Hello Ronald, Item selection and row click events are two separate events that are not tied together. You can handle or not the row click event, but it is not a "cancellable" event that stops event propagation (doing that conditionally is not possible in Blazor). Moreover, the two events have distinctly different signatures due to the different nature of metadata they need to expose. As such, you can't handle them with the same event handler. You need to choose to which action you want to respond: OnRowClick fires when the row is clicked SelectedItemsChanged fires when the selection changes - that can be a row click, a checkbox click, or the keyboard navigation So, if you want to customize the selection behavior, you should work only with the SelectedItemsChanged event - it will fire when you click the row too - it covers all selection scenarios and options. Then, if you want to do something if the user clicks the row - you can do that in OnRowClick - such as load data on demand for something else on the page. Business logic related to selection needs to go in the SelectedItemsChanged handler, though, the two are separate. Regards, Marin Bratanov Progress Telerik

### Response

**Ronald** answered on 05 Apr 2021

I hope I am not exasperating you. Let me recap the way I am understanding it. If the user clicks on a checkbox thus selecting the row I can get the effect of selecting the row (all of the UI stuff that the component offers) and can prevent the default behavior of clicking on a row since that will be handled by the act of clicking on the checkbox. Now if the user clicks on the row on a column other than the column containing the checkbox that is considered a "RowClick" event and can be wired up appropriately so that it is handled. What do I need to do so that when handling the "RowClick" it looks to the user as if they have clicked on the checkbox and the whole row is highlighted and selected?

### Response

**Marin Bratanov** answered on 05 Apr 2021

Hello Ronald, Clicking the checkbox the GridCheckboxColumn provides for selection will fire the SelectedItemsChanged event. It will not fire the OnRowClick event. This lets you handle selection alone through the dedicated event for selection. When selection is enabled, the user can click a row and it will get selected automatically. You do not have to handle the RowClick event. The row click will fire the SelectedItemsChanged event that lets you populate the SelectedItems collection which is what controls which rows are highlighted in the grid. You can try the examples from the documentation articles I've linked and add a few breakpoints in the event handlers to see when they fire and how the component behaves. Regards, Marin Bratanov

### Response

**Tobias** answered on 19 May 2022

Hi Marin, you told: Business logic related to selection needs to go in the SelectedItemsChanged handler, though, the two are separate. Documentation of the selectedItemsChanged-event says: [https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event](https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event) If you want to load that data on demand, you should use the OnRowClick event. Now, if I want to load data from backend service based on selection, how should that be done? Doc says in OnRowClick, but there selection is not available? Thanks, Tobias

### Response

**Marin Bratanov** commented on 22 May 2022

The correct statement is in the documentation. Loading on demand (basically, an async event handler) should be done via RowClick. Other logic that is synchronous (such as avoiding the selection for a certain row based on some condition, or adding more selected rows) can be done in SelectedItemsChanged. In the RowClick event, you know the current row from the event arguments, and so you can use that. Or, you can combine it with the previous selection data to check if it was selected already (ergo, you have a deselection), or not.
