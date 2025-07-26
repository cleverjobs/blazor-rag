# Virtual mode and multiple select

## Question

**Joh** asked on 04 Mar 2021

Hi, I need to be able to use virtual mode and multiple select and be able to get the complete list of selected items when a user clicks a row, holds shift, scrolls the grid then clicks another row. Also with the usual, ctrl clicks, etc along the way. Virtual mode is needed as we must show up to 5000 rows without paging. And without virtual mode this grid simple cannot handle that much data. Is this possible, the docs suggest it is, but give no example code how to achieve this. We're looking at several grids to use, and Telerik is winning, but this is a showstopper if this cannot be done. TIA

## Answer

**John** answered on 05 Mar 2021

Figured this out. I had to turn off sorting and handle that myself, to properly detect start/stop indexes. And I bound to the RowClick event to do it. I also basically have to handle all selection myself. If theres a better way to do this than please let me know, if theres not. Please add this or something much better into the Telerik grid, because this must be a common use case. Seriously, lots of rows, multiple select, it needs to support it. It would be shocking if it doesnt. So I must be missing something. If anyone needs the code: <TelerikGrid @ref="TelerikGridInstance" Data="@GridItems" TotalCount="@GridItems.Count" @bind-SelectedItems="@SelectedItems" PageSize="30" Height="@Height" RowHeight="36" SelectionMode="@GridSelectionMode.Multiple" OnRowClick="OnRowClick" ScrollMode="@(VirtualMode ? GridScrollMode.Virtual : GridScrollMode.Scrollable)"> private ExpandoObject PreviousRow; private async Task OnRowClick(GridRowClickEventArgs args) { if (VirtualMode==false ) return; ExpandoObject item=args.Item as ExpandoObject ; if (item==null ) return; if (args.EventArgs is Microsoft.AspNetCore.Components.Web.MouseEventArgs mouse) { if (mouse.ShiftKey==false ) PreviousRow=item; else if (mouse.ShiftKey && PreviousRow !=null ) { // we're doing a shift selection int prevIndex=this.GridItems.IndexOf(PreviousRow); int curIndex=this.GridItems.IndexOf(item); int start=Math.Min(prevIndex, curIndex); int end=Math.Max(prevIndex, curIndex); var newSelection=this.SelectedItems.Union( this.GridItems.Skip(start).Take(end - start)).Union( new [] { item }).Distinct(); _=Task.Run(async ()=> { // we need this delay to override telerik from clearing the selection we want. this.SelectedItems=newSelection; this.StateHasChanged(); }); } } }

### Response

**Svetoslav Dimitrov** answered on 09 Mar 2021

Hello John, I am glad to read that you have figured it out and it is working in your application. Virtual scrolling is an alternative the paging. The user is able to select items from the current viewport (visible items). This behavior is documented under the Selection in Grid with virtualized rows section in the Selection Overview article. On the topic of improving the Grid with such a feature, how would you want to see it enabled, would you expect a parameter which controls that? That being said, the approach you have taken is the correct one. Regards, Svetoslav Dimitrov

### Response

**John** answered on 09 Mar 2021

Sure, a setting would be fine. But IMO this should be the default behaviour when using multiselect and virtual scrolling. The only reason to use virtual scrolling in this grid is due to the slowness in blazor with adding so many dom elements. When .net 6 comes out with the blazor performance improvements, I'm hoping this grid can handle 5000 rows easily without needing to use virtual scrolling. As a user, I may want to select everything for deletion, so I may click the first row, or thereabouts, scroll to the bottom (or there abouts) hold shift, and click the end row. Then hit the delete button. I would expect it to delete all the rows I selectetd, not the ones currently visible on the screen. Because as a user, virtual scrolling isnt the same as paging. I haven't navigated away, the same data should be selected. But I understand that making this the default may effect others, so a setting is fine. It just should be handled by the grid itself without this "hack". Thanks.

### Response

**Svetoslav Dimitrov** answered on 10 Mar 2021

Hello John, I have added a new Feature Request on your behalf - Improve the range selection (with Shift key) in Virtual Scrolling mode. Your Vote is already in and since I created the thread from your account you are automatically subscribed for email notifications on status updates. For the time being, the approach you have taken is the correct one. Regards, Svetoslav Dimitrov Progress Telerik
