# How to prevent row selection change

## Question

**Chr** asked on 25 Jan 2023

I need to be able to cancel row selection and there is no SelectedItemsChanging event that proceeds the SelectedItemsChanged event. I am trying to handle it in the OnRowClick event handler, but while I can prevent other changes, the row selection change still happens. I have a grid, and if the user clicks on a row it opens and loads a detail component below the grid. If the detail component is visible and the user clicks in the grid on a different record I show a confirmation dialog to let them know about potentially lost changes since they have not saved. I do this in the onrowclick handler, and if the clicked row does not equal the selected row (and the selected row is not empty then I show the confirmation after saving the selected row in a new variable If they opt to lose the changes I proceed with the change and update the SelectedItems to the newly clicked on row. If they opt to not proceed, then I set the SelectedItems to a new list and add the <TelerikGrid @ref="RolesGrid" TItem="@GetRoles.Response" Pageable="true" Sortable="true" OnRead="@ReadRoles" EnableLoaderContainer="@IsGridLoading" SelectionMode="GridSelectionMode.Single" OnRowClick="@HandleRolesGridRowClick" SelectedItems="SelectedItems"> private async Task HandleRolesGridRowClick(GridRowClickEventArgs args) { var clickedRole=args.Item as GetRoles.Response; var selectedRole=SelectedItems.FirstOrDefault(); bool allowSelection=selectedRole==null || await Dialogs.ConfirmAsync($"Switching roles will lose unsaved changes in the {selectedRole.Name} role", "Lose Unsaved Changes?"); if (allowSelection) { DisplayRole(clickedRole.RoleId, clickedRole.Name); SelectedItems=new List<GetRoles.Response>(){clickedRole}; } else { SelectedItems=new List<GetRoles.Response>() { selectedRole }; } args.ShouldRender=allowSelection; } Based on another suggestion elsewhere, I tried adding the following to the Grid's definition and and empty method to handle it and it still makes the selection change. SelectedItemsChanged="@((IEnumerable<GetRoles.Response> selectedRecords)=> HandleRoleSelection(selectedRecords)) Any help would be appreciated.

## Answer

**Hristian Stefanov** answered on 30 Jan 2023

Hi Chris, I'm pasting here the answer I gave you in the private ticket so the community can benefit from it.==As far as I understand, the main goal is to conditionally select/deselect specific rows based on logic in the OnRowClick handler. I confirm that this is possible by using the SelectedItems list and "if" blocks. I have prepared a sample for you in this REPL link that allows selecting only the 2nd, 3rd, and 4th rows. You can copy and use the same approach to the actual project. Use the REPL sample as a comparison. I have also left comments on the code for explanation. Additionally, here is one knowledge base article we have that gives more information about controlling the row selection with the OnRowClick event.==Regards, Hristian Stefanov

### Response

**Stefan** commented on 29 Mar 2023

Please, add link to this solution to the Grid documentation. This is a very common scenario and should be readily available.

### Response

**Hristian Stefanov** commented on 03 Apr 2023

Hi Stefan, Thank you for your suggestion. Your feedback is highly appreciated. We will for sure explore possibilities for improving our Grid documentation. If we can help with anything else here, I would be glad. Kind Regards, Hristian

### Response

**Marco** answered on 03 Jul 2024

Hello, I re-open this thread to ask a simple question. What I was doing right now was the following: //Handle the SelectedItemsChanged event and do not execute any logic in it, so you can override the built-in selection. private void SelectedItemsChanged(IEnumerable<FormatDataVM> data) { } private IEnumerable<FormatDataVM> _previousSelectedItems=[]; //Handle the OnRowClick event to programmatically update the SelectedItems collection. Check if an item exists in the collection (is selected). Add it to the collection to select it. Remove it from the collection to deselect it. private async Task OnRowClickHandler(GridRowClickEventArgs args) { var currItem=args.Item as FormatDataVM; var previousSelectedItems=_previousSelectedItems.ToList(); var newSelectedItems=SelectedItems.ToList(); bool confirm=true; if (_inEditMode && IsDataChanged()) { confirm=await Dialogs.ConfirmAsync(Translations.WarningChangesNotSaved, Translations.ChangesNotSaved); } if (confirm) { DiscardChanges(); if (newSelectedItems.Any(x=> x==currItem)) { newSelectedItems=newSelectedItems.Where(x=> x !=currItem).ToList(); } else { newSelectedItems.Add(currItem); } SelectedItems=new List<FormatDataVM>(newSelectedItems); _previousSelectedItems=new List<FormatDataVM>(SelectedItems); } else { SelectedItems=new List<FormatDataVM>(_previousSelectedItems); } args.ShouldRender=true; StateHasChanged(); } I need to have the same behaviour of row selection applied to GridCheckboxColumn selection, actually that's not working (entering the SelectionChanged event I already have the grid modified and the item de-selected). Is there any way to achive this? Thanks! P.s. before trying to fit inside this logic, what I was doing was the following: private async Task SelectedItemsChanged(IEnumerable<FormatDataVM> selectedItems) { if (!_inEditMode || (_inEditMode && !IsDataChanged()) || (_inEditMode && IsDataChanged() && await Dialogs.ConfirmAsync(Translations.WarningChangesNotSaved, Translations.ChangesNotSaved))) { DiscardChanges(); SelectedItems=selectedItems; } } The result I was having was pretty what I was looking, except the fact that pressing cancel on the dialog was keeping the item unselected in graphic but selected inside SelectedItemList...

### Response

**Hristian Stefanov** commented on 05 Jul 2024

Hi Marco, Thank you for sharing parts of your code. However, I'm still not completely sure what specific issue you're dealing with based on the provided information. Could you please provide more details on the exact problem you're facing and what aspect of the " Select or Deselect Grid Items on Row Click " knowledge base article doesn't cover your scenario? I eagerly anticipate your response. Kind Regards, Hristian
