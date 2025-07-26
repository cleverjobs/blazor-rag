# Rowclick trigger OnStateChangeHanlder Prevent from calling function

## Question

**Arj** asked on 30 Jun 2025

I'm using the Blazor TelerikGrid component with SelectionMode="GridSelectionMode.Multiple". I have an OnRowClick handler to manually toggle selection (see below), and I bind the selected items via SelectedItems="@SearchState.SelectedItems". <TelerikGrid @ref="SearchGrid" TItem="@ChargeUIResult" SelectionMode="GridSelectionMode.Multiple" SelectedItems="@SearchState.SelectedItems" SelectedItemsChanged="@((IEnumerable<ChargeUIResult> args)=> SetSelectedItem(args))" OnRowClick="@OnRowClickHandler"...>
</TelerikGrid> void OnRowClickHandler ( GridRowClickEventArgs args ) { var currItem=args.Item as ChargeUIResult; if (SearchState.SelectedItems.Any(x=> x.Id==currItem?.Id))
{
SearchState.SelectedItems=SearchState.SelectedItems.Where(x=> x.Id !=currItem?.Id);
} else {
SearchState.SelectedItems=SearchState.SelectedItems.Concat( new [] { currItem });
}

SelectedItem=currItem;
ShouldRenderSelectedItem=true;
args.ShouldRender=false;
} What I want to achieve is: When a checkbox is clicked (i.e., selection happens), I want to get the first selected item from SearchState.SelectedItems and bind or use it immediately (e.g., assign it to SelectedItem or update the UI). 💬 My questions are: Is there a built-in event for detecting checkbox selection (apart from OnRowClick)? What's the recommended way to access the first selected item when selection changes via the checkbox — not just row clicks? Can SelectedItemsChanged help with this, and if so, how should I modify the SetSelectedItem logic?

## Answer

**Hristian Stefanov** answered on 30 Jun 2025

Hi Arjun, Detecting Checkbox Selection in TelerikGrid The SelectedItemsChanged event is the built-in event that fires whenever the selection changes, whether through a checkbox or a row click. There is no separate event specifically for checkbox selection; both actions trigger SelectedItemsChanged. Accessing the First Selected Item on Selection Change The recommended approach is to use the SelectedItemsChanged event. This event provides the current collection of selected items every time the selection changes, regardless of how the selection was made (checkbox or row click). In your handler (e.g., SetSelectedItem), you can immediately access the first selected item and update your UI accordingly. How to Use SelectedItemsChanged and Update SetSelectedItem You can modify your SetSelectedItem method to always update the SelectedItem with the first item from the new selection (or set it to null if no items are selected). This ensures your logic works for both checkbox and row selection. Example implementation: void SetSelectedItem ( IEnumerable<ChargeUIResult> selectedItems ) {
SearchState.SelectedItems=selectedItems.ToList();
SelectedItem=SearchState.SelectedItems.FirstOrDefault();
StateHasChanged(); // Trigger UI update if needed } This setup ensures that whenever a checkbox is clicked and the selection changes, SetSelectedItem runs, and you get the first selected item immediately. Summary and Best Practice Use only the SelectedItemsChanged event to handle all selection changes. This event covers both checkbox and row selection scenarios. Place your selection logic (such as updating the first selected item) in the SelectedItemsChanged handler. The OnRowClick event is optional and should be used for row-specific actions that are not related to selection (such as navigation or loading additional data). For more details, see: [https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event](https://docs.telerik.com/blazor-ui/components/grid/selection/single#selecteditemschanged-event) I hope this helps you move forward. Regards, Hristian Stefanov Progress Telerik

### Response

**Arjun** commented on 30 Jun 2025

Thank you for the clarification. I have a slightly different scenario. Your suggestion works well if I need to always show the FirstOrDefault value. However, in my case, I only want to show the FirstOrDefault value when the user selects an item using a checkbox. When the user clicks directly on a row, they expect to see the current (selected) value, not the first or default. How can I handle this scenario in the application?

### Response

**Arjun** commented on 01 Jul 2025

Hi Hristian Stefanov, Can we set different value for when user click directly from clicking row and different value if user click from checkbox, we have these two different scenarios in our application.

### Response

**Hristian Stefanov** commented on 03 Jul 2025

Hi Arjun, Thank you for clarifying what you’re looking to achieve. It sounds like you need a way to distinguish between a checkbox selection and a row click so you can implement the desired logic—whether to display the FirstOrDefault value or the currently selected value. To handle this, you can use both the OnRowClick and SelectedItemsChanged events together with a simple boolean flag to track the interaction type. Since OnRowClick only fires when a row is clicked, if SelectedItemsChanged triggers but OnRowClick does not, it indicates the selection was made via a checkbox. Best, Hris
