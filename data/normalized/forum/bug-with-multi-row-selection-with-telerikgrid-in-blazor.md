# Bug with multi-row selection with TelerikGrid in Blazor

## Question

**Dan** asked on 22 Mar 2022

Hi, I'm using UI for Blazor version 3.1.0. I have a grid with multi-row selection turned on that triggers an OnEmployeesSelected event when the selected items change. I also have a GridCheckboxColumn as well. The code looks like so: <TelerikGrid Data="@EmployeeGridData" EditMode="@GridEditMode.Popup" Height="240px" Pageable="true" PageSize="20" Sortable="true" Groupable="false" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Resizable="true" Class="smallerFont" Reorderable="true" SelectionMode="@GridSelectionMode.Multiple" SelectedItems="@SelectedEmployees" SelectedItemsChanged="@((IEnumerable<EmployeeList> list)=> OnEmployeesSelected(list))"> <GridColumns> <GridCheckboxColumn SelectAll="true" SelectAllMode="GridSelectAllMode.All"> The issue is the @SelectedEmployees variable holding the selected items for the grid gets out of sync with what it displayed. Part of that may be due to this behavior: If I click on the GridCheckboxColumn to check a row that was previously unchecked the OnEmployeesSelected event triggers immediately, the checkbox is displayed in the column, and the @SelectedItems collection appears to be accurate. If I click on the GridCheckboxColumn to uncheck a row that was previously checked the OnEmployeesSelected event does not trigger. The checkbox is removed from the displayed column however the @SelectedItems collection still has it. Selecting other rows in the grid by clicking somewhere else in the row (i.e. by not clicking on the GridCheckboxColumn), after the @SelectedItems is out of sync from the 2nd note above, gets the @SelectedItems collection even further out of sync.

### Response

**Nadezhda Tacheva** commented on 25 Mar 2022

Hi Daniel, I have tried to replicate your scenario in order to reproduce the issue but to no avail. The selection seems to be working correctly on my end - SelectedItemsChanged is fired accordingly and the SelectedItems collection is updated properly. I've been testing with latest Telerik UI for Blazor as well (3.1.0). You may check the behavior yourself in this REPL - [https://blazorrepl.telerik.com/mmOxwflJ23nD9nj256.](https://blazorrepl.telerik.com/mmOxwflJ23nD9nj256.) The only thing coming to my mind which might be causing an issue is if you have some asynchronous operation in the SelectedItemsChanged event. We generally recommend that such operations are handled in the OnRowClick or OnRowDoubleClick events. Could you please send us a runnable reproduction of the issue, so we can debug on our end and find what might be causing it? You may use the sample I provided as a base and modify it to reproduce the problem. Thank you in advance! I will be looking forward to hearing from you!

## Answer

**Daniel** answered on 25 Mar 2022

Hi, Thank you for the reply. I didn't realize that I shouldn't call asynchronous events inside the SelectedItemsChanged event. When I switched them to synchronous events things seem to be working properly.
