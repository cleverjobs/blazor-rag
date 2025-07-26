# Grid In-cell edit row selection and end of list new entry focus

## Question

**Ant** asked on 29 Nov 2023

I have 2 questions on how to do something with the grid component. Setup Here are the options I have set for the grid component. <TelerikGrid @ref="Grid" Data="Entries" TItem="ProductEntryModel" Class="font-size mb-1" Sortable="true" SortMode="@Telerik.Blazor.SortMode.Multiple" FilterMode="@GridFilterMode.FilterMenu" FilterMenuType="@FilterMenuType.CheckBoxList" ScrollMode="@GridScrollMode.Virtual" SelectionMode="@GridSelectionMode.Single" Height="570px" Width="100%" RowHeight="40" PageSize="@PageSize" EditMode="@GridEditMode.Incell" EnableLoaderContainer="@IsLoading" @bind-SelectedItems="SelectedItems" OnEdit="OnEditEventHandler" OnUpdate="OnUpdateEventHandler" Navigable="true" Size="sm"> For Context the first cell is a TemplateColumn with a TelerikCombobox Component in it. On Load It loads all the entries for the day selected. It adds a new line automatically at the bottom for adding more. But if the rows are longer than the height the new row will not fully show its whole height and I want it to start in edit of the first cell. The image shows that it is selected but not in edit. This image is right after load. You can see the row is selected but not in edit and half off-screen. If the rows are further than the height it will not bring it into view either. I would like it to start in view and the first cell in edit, how to accomplish that? In Edit This method below allows the user to keep adding rows to the grid after the PO NU... field loses focus. It works great as long as the grids next row is not out of view. Once it is out of view it will add the line, select it, and bring it to view, but the first cell is now out of edit and the user has to click in to the cell to start entry. Similar to above, how do I set the focus in the first cell? Some of this code is different attempts to get it to work. private async Task AddNewRecord ( ProductEntryModel? entry=null ) { if (Entries.Any(x=> x.ProductId==0 )) return; var newLine=new ProductEntryModel
{
EntryDate=EntryDate,
PoNumber=entry !=null? entry.PoNumber : "", // Carry down Sublet=entry !=null && ! string.IsNullOrWhiteSpace(entry.PoNumber) ? entry.Sublet : "", // Carry down };
Entries.Add(newLine); // Add A new line PageSize=Entries.Count> 15? Entries.Count : 15; // increase page size SelectedItems=new List<ProductEntryModel>() {newLine}; // Select new line await Task.Delay( 100 ); // Wait for the grid to update - Doesn't help select the next entry await ProjectCombobox.FocusAsync(); // New Attempt and doesn't work //Grid.Rebind(); }

### Response

**Hristian Stefanov** commented on 04 Dec 2023

Hi Anthony, As per my understanding, the desired functionality involves automatically adding a new row in edit mode upon the initial load. Subsequently, updating the last cell in that row should trigger the creation of a new row in edit mode by pressing Tab, and so forth. I have replicated the scenario in an example in this REPL link that seems to work without the new row being cut off at the end of the screen. Please run and test it by editing some rows to see the result. Let me know whether this is what you are looking for. Kind Regards, Hristian

### Response

**Anthony** commented on 04 Dec 2023

Your code does the same thing. It can only handle the 1st record after the height then next record loses focus after the add. See the GIF below.

### Response

**Anthony** commented on 04 Dec 2023

This GIF shows it better. It selects it then loses focus right after.

### Response

**Hristian Stefanov** commented on 07 Dec 2023

Hi Anthony, Thank you for providing additional details and videos of the behavior. Now I understand way better what the problem is. The videos clarified it for me. I confirm that this behavior is an actual bug in the Incell editing in combination with scroll. A public item for it has already been submitted on our Publick Feedback Portal: Triggering Incell or Inline Edit which causes the grid to scroll cancels the edit. I voted there and raised the priority. You can also subscribe to the item to receive email notifications for further status updates. Workaround A colleague of mine has provided possible workarounds in the comment section at the above link until we fix the bug. Kind Regards, Hristian
