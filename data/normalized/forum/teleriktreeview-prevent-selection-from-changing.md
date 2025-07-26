# TelerikTreeView prevent selection from changing

## Question

**JimJim** asked on 19 Jun 2024

I am using a TelerikTreeView in my component. When I click on a node (an expanded child node), I check whether the form for the currently selected node is dirty. If the form is dirty, I show a prompt asking the user to continue or not. When the user selects no/cancel, the clicked node should not be selected. I am using the event below. protected async Task OnItemClickedAsync(TreeViewItemClickEventArgs args) I can't find a way to cancel this event or to prevent the newly clicked item to be selected. Is there any way to prevent a clicked item to be selected? I have been experimenting with @bind-SelectedItems to no avail. I haven't been able to find a solution for this problem. Any help is appreciated.

## Answer

**Radko** answered on 21 Jun 2024

Hi Jim, Since the OnItemClick is really an informative event, it is not designed to be cancellable. What you are after should be possible by handling the SelectedItemsChanged event, as you have already attempted, thus I am curious as to what went wrong there. The SelectedItemsChanged event fires when an end user performs selection by clicking on an item. When handling the event, you receive an argument list containing a list of items the user is attempting to select - you can then execute any logic you see fit to decide whether the selection should indeed go through or not. An important note is that if you handle this event, you will then be responsible to correctly update the SelectedItems parameter, as you are essentially intercepting the two-way binding. Here is a simple example where selection is possible only for nodes with text containing index: [https://blazorrepl.telerik.com/QoOAQbaz43hQ5x9714](https://blazorrepl.telerik.com/QoOAQbaz43hQ5x9714) Regards, Radko Progress Telerik

### Response

**Jim** commented on 02 Jul 2024

Thanks for the reply. I think I am mixing two modes and I am not implementing ithemcorrectly. I will check out your example and I will take a lookt at this page in more detail: [https://docs.telerik.com/blazor-ui/components/treeview/events#selecteditemschanged](https://docs.telerik.com/blazor-ui/components/treeview/events#selecteditemschanged)

### Response

**Jim** commented on 02 Jul 2024

I got it to work!!! Thanks a lot.
