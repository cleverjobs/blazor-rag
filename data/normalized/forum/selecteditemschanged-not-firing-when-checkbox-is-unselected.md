# SelectedItemsChanged not firing when checkbox is unselected.

## Question

**BobBob** asked on 18 Aug 2021

I have a grid using checkbox selection and when I un-check a row, it is not firing the SelectedItemsChanged event. The event adds filters to another grid I have on the page. <TelerikGrid Data="strategicLevelItems" SelectedItems="selectedStrategic" Width="100%" Height="500px" ScrollMode="GridScrollMode.Scrollable" SelectionMode="GridSelectionMode.Multiple" SelectedItemsChanged="@((IEnumerable<GetNavigationNodesModel> strategicItems)=> OnStrategicSelectAsync(strategicItems))" FilterMode="GridFilterMode.FilterRow"> <GridColumns> <GridCheckboxColumn SelectAll="true" Width="40px" OnCellRender="@GridHelpers.CenterAlign" /> <GridColumn Field="@(nameof(GetNavigationNodesModel.Name))" /> </GridColumns> </TelerikGrid> private async Task OnStrategicSelectAsync(IEnumerable <GetNavigationNodesModel> selectedItems)
{
selectedStrategic=selectedItems;

var state=tacticalGrid.GetState();

var compositeFilter=new CompositeFilterDescriptor() { LogicalOperator=FilterCompositionLogicalOperator.Or };
foreach (var item in selectedItems)
{
compositeFilter.FilterDescriptors.Add(new FilterDescriptor()
{
Member="ParentId",
Operator=FilterOperator.IsEqualTo,
Value=item.Id
});
}

state.FilterDescriptors.Clear();
state.FilterDescriptors.Add(compositeFilter);

await tacticalGrid.SetState(state);
}

### Response

**Bob** commented on 19 Aug 2021

The problem appears to happen when you select an item and then un-select it. The event fires when it is selected, but doesn't fire when it is un-selected.

## Answer

**Hristian Stefanov** answered on 23 Aug 2021

Hi Bob, I see that you already have logged a bug report on our Public Feedback Portal - SelectedItemsChanged event not firing upon unchecking a row. Thank you for that. The status is set to "Unplanned", which means that this is a verified/confirmed bug, but with no scheduled date for implementation yet. Since you are the creator of this bug report, you are automatically subscribed to receive email notifications on status updates. We prioritize bug reports depending on interest. With your vote already added there, the item popularity is increased. I'm sorry to confirm that using a void handler remains the only option to avoid the problem in the meantime. Let me know if you have any other questions. Regards, Hristian Stefanov Progress Telerik
