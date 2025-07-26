# Grid: OnRowClicked is fired on load

## Question

**Hol** asked on 05 Apr 2022

Hello, I have a TelerikGrid like this: <TelerikGrid @ref="gridRef" Data="@MyData" Pageable="@pageable" PageSize="15" Sortable="true" SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<MyDataViewModel> itemList)=> OnRowClick(itemList))" SelectedItems="selectedRow" OnRowDoubleClick="@OnRowDbClick" OnRowContextMenu="@Menu" OnStateInit="@((GridStateEventArgs<MyDataViewModel> args)=> OnStateInitHandler(args))"> Works fine. But on page load, my OnRowClick-method will be fired with an empty [] as parameter. Is that working correctly? In my case, I can make a workaround for that, but maybe that is not the designed behaviour? :-) Runs on .net6.0.3. Testet on Firefox on Windows10. Telerik.UI.for.Blazor 3.1.0

## Answer

**Nadezhda Tacheva** answered on 07 Apr 2022

Hi Holger, Thank you for reaching out! You are correct, this behavior is not expected. As per your configuration, the OnRowClick method is an event handler of the SelectedItemsChanged event. It is supposed to fire when there is a change in the user selection. However, it looks like it is indeed currently fired on initialization when no items are even selected yet. If the user clicks once more on an already selected row, the SelectedItemsChanged event fires again although there is no change in the selection (this is not desired as well). I've logged a public bug report on your behalf, you can find it in our
