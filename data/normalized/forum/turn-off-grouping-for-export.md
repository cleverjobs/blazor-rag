# Turn off Grouping for Export

## Question

**BobBob** asked on 23 Feb 2022

Is there any way to turn off grouping before exporting to excel and then turn it back on. I have tried utilizing the before and after export events but it does not seem to work. private async Task OnExcelAfterExportAsync(GridAfterExcelExportEventArgs args)
{
await ticketGrid.SetState(currentGridState);
}

private async Task OnExcelBeforeExportAsync(GridBeforeExcelExportEventArgs args)
{
currentGridState=ticketGrid.GetState();

GridState <TicketListModel> tempState=new()
{
SortDescriptors=currentGridState.SortDescriptors,
FilterDescriptors=currentGridState.FilterDescriptors,
GroupDescriptors=new List <GroupDescriptor> ()
};

await ticketGrid.SetState(tempState);

args.Columns=args.Columns.Except(args.Columns.Where(c=> c.Field=="HasAttachments")).ToList();

var statusColumn=args.Columns.First(c=> c.Field=="StatusId");
statusColumn.Field="Status";

var priorityColumn=args.Columns.First(c=> c.Field=="PriorityId");
priorityColumn.Field="Priority";

var areaColumn=args.Columns.First(c=> c.Field=="Area");
areaColumn.Width="150px";

args.IsCancelled=false;
}

## Answer

**Svetoslav Dimitrov** answered on 28 Feb 2022

Hello Bob, Toggling the Grouping before and after the excel would not be possible as it would require a re-render or a data rebind of the Grid. Both of these (re-render or a data rebind) would worsen the performance of the Grid. To achieve the desired behavior, you can use some custom login as in the following examples on our public GitHub repository: PDF export server Export Hierarchy to XLSX Let me know if these sample apps helped you move forward. Regards, Svetoslav Dimitrov Progress Telerik
