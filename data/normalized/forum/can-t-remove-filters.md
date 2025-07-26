# Can't Remove Filters

## Question

**Mat** asked on 28 Mar 2024

On the Filter component I have observed that when it is added to a Dialog component it no longer functions correctly. You can add filters but can't remove any of them without generating an exception. Here is a working Filter: [https://blazorrepl.telerik.com/cyOdQMGY430AGXlV24](https://blazorrepl.telerik.com/cyOdQMGY430AGXlV24) The exact code on the documentation page Here is a non-working Filter [https://blazorrepl.telerik.com/QyaHmCcY52sOsyto41](https://blazorrepl.telerik.com/QyaHmCcY52sOsyto41) A Dialog component has been added The Filter component will allow you to add filters but if you click the 'x' to remove a filter it will not remove. Clicking the 'x' again results in an error: Unhandled exception rendering component: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index') Exception: System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index') at System.Collections.ObjectModel.Collection`1.RemoveAt(Int32 index) at Telerik.Blazor.Components.Filter.FilterGroup.OnFilterRemove(Int32 index, String removedFilterId) at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) I also noticed that if you remove the binding from the Filter it fails the same way: [https://blazorrepl.telerik.com/weEHQCQa49xsfTxF28](https://blazorrepl.telerik.com/weEHQCQa49xsfTxF28)

## Answer

**Nansi** answered on 01 Apr 2024

Hello Matt, Thank you for providing examples and different scenarios. Two-way binding for the Filter Value won't work inside a Dialog, because you need to Refresh() the Dialog to reflect UI changes. You can use one-way binding and call the Refresh method of the Dialog in the Filter ValueChanged event. I have updated your example to demonstrate this approach. The Filter requires to have a Value otherwise it won't work, as you have already tested when removing the binding. Regards, Nansi Progress Telerik

### Response

**IT** commented on 01 Apr 2024

Thanks! That worked.
