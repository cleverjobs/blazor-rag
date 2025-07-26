# Highlight row on rightclick in Treelist

## Question

**Fab** asked on 03 Feb 2025

We were using the TelerikTreeList with SelectionMode="TreeListSelectionMode. Single " SelectedItems=" @SelectedItems " with a ContextMenu. On Rightclick we wanted to open the ContextMenu but also set the row as Selected. If a row is selected and we rightclick on another one both will be selected. We don;t know exactly why and did not expect two rows to ever be selected after setting the SelectionMode to single. this is the code we use for selecting on right click. private async Task OnContextMenu (TreeListRowClickEventArgs args) { SelectedItems=[(TItem)args. Item ]; await InvokeAsync ( StateHasChanged ); Do you have any idea how to fix it?

### Response

**Hristian Stefanov** commented on 06 Feb 2025

Hi Fabian, I copied the provided code and attempted to reproduce the described behavior. In my testing, when a row is selected and I right-click another row, only the last clicked row remains selected. This outcome differs from what you're experiencing. For reference, here is the full runnable sample I used for testing: <TelerikTreeList Data="@Data" OnRowContextMenu="@OnRowContextMenuHandler" SelectionMode="TreeListSelectionMode.Single" SelectedItems="@SelectedItems" IdField="Id" ParentIdField="ParentId" Pageable="true"> <TreeListColumns> <TreeListColumn Field="Name" Expandable="true" Width="320px" /> <TreeListColumn Field="Id" Width="120px" /> <TreeListColumn Field="ParentId" Width="120px" /> <TreeListColumn Field="EmailAddress" Width="120px" /> <TreeListColumn Field="HireDate" Width="220px" /> </TreeListColumns> </TelerikTreeList> @code {
private IEnumerable <Employee> SelectedItems { get; set; }=Enumerable.Empty <Employee> ();

private async Task OnRowContextMenuHandler(TreeListRowClickEventArgs args)
{
SelectedItems=[(Employee)args.Item];
await InvokeAsync(StateHasChanged);
}

private List <Employee> Data { get; set; }

protected override async Task OnInitializedAsync()
{
Data=await GetTreeListData();
}

public class Employee
{
public int Id { get; set; }
public int? ParentId { get; set; }

public string Name { get; set; }
public string EmailAddress { get; set; }
public DateTime HireDate { get; set; }
}

private async Task<List <Employee>> GetTreeListData()
{
List <Employee> data=new List <Employee> ();

for (int i=1; i <15; i++)
{
data.Add(new Employee
{
Id=i,
ParentId=null,
Name=$"root: {i}",
EmailAddress=$"{i}@example.com",
HireDate=DateTime.Now.AddYears(-i)
}); ;

for (int j=1; j <4; j++)
{
int currId=i * 100 + j;
data.Add(new Employee
{
Id=currId,
ParentId=i,
Name=$"first level child {j} of {i}",
EmailAddress=$"{currId}@example.com",
HireDate=DateTime.Now.AddDays(-currId)
});

for (int k=1; k <3; k++)
{
int nestedId=currId * 1000 + k;
data.Add(new Employee
{
Id=nestedId,
ParentId=currId,
Name=$"second level child {k} of {i} and {currId}",
EmailAddress=$"{nestedId}@example.com",
HireDate=DateTime.Now.AddMinutes(-nestedId)
}); ;
}
}
}

return await Task.FromResult(data);
}
} Please run it and compare the results to see if they align with your expectations. Based on my observations, the selection appears to function as intended. Let me know if I'm missing something. Kind Regards, Hristian

### Response

**Sebastian** commented on 18 Feb 2025

Hi Hristian, Thanks for the example! While your code does work, it breaks once another asynchronous method is called within the `OnRowContextMenuHandler`, e.g. `await Task.Delay(1)`. Could this be a race condition within the TelerikTreeList component? The complete broken example: @page "/Test" <TelerikTreeList Data="@Data" OnRowContextMenu="@OnRowContextMenuHandler" SelectionMode="TreeListSelectionMode.Single" SelectedItems="@SelectedItems" IdField="Id" ParentIdField="ParentId" Pageable="true">
<TreeListColumns>
<TreeListColumn Field="Name" Expandable="true" Width="320px" />
<TreeListColumn Field="Id" Width="120px" />
<TreeListColumn Field="ParentId" Width="120px" />
<TreeListColumn Field="EmailAddress" Width="120px" />
<TreeListColumn Field="HireDate" Width="220px" />
</TreeListColumns>
</TelerikTreeList>

@code { private IEnumerable<Employee> SelectedItems { get; set; }=Enumerable.Empty<Employee>(); private async Task OnRowContextMenuHandler ( TreeListRowClickEventArgs args ) {
SelectedItems=[(Employee)args.Item]; await InvokeAsync(StateHasChanged); await Task.Delay( 1 );
} private List<Employee> Data { get; set; } protected override async Task OnInitializedAsync () {
Data=await GetTreeListData();
} public class Employee { public int Id { get; set; } public int? ParentId { get; set; } public string Name { get; set; } public string EmailAddress { get; set; } public DateTime HireDate { get; set; }
} private async Task<List<Employee>> GetTreeListData()
{
List<Employee> data=new List<Employee>(); for ( int i=1; i <15; i++)
{
data.Add( new Employee
{
Id=i,
ParentId=null,
Name=$"root: {i} ",
EmailAddress=$" {i} @example.com",
HireDate=DateTime.Now.AddYears(-i)
});
; for ( int j=1; j <4; j++)
{ int currId=i * 100 + j;
data.Add( new Employee
{
Id=currId,
ParentId=i,
Name=$"first level child {j} of {i} ",
EmailAddress=$" {currId} @example.com",
HireDate=DateTime.Now.AddDays(-currId)
}); for ( int k=1; k <3; k++)
{ int nestedId=currId * 1000 + k;
data.Add( new Employee
{
Id=nestedId,
ParentId=currId,
Name=$"second level child {k} of {i} and {currId} ",
EmailAddress=$" {nestedId} @example.com",
HireDate=DateTime.Now.AddMinutes(-nestedId)
});
;
}
}
} return await Task.FromResult(data);
}

}

### Response

**Hristian Stefanov** commented on 19 Feb 2025

Hi Sebastian, I tested the provided configuration with " await Task.Delay(1) ", and the selection appears to work correctly. When I right-click, the OnRowContextMenu event is triggered as expected, without any errors. Could you provide additional steps or details to help me reproduce the issue you’re experiencing? I want to ensure I’m not overlooking anything. Kind Regards, Hristian

### Response

**Sebastian** commented on 19 Feb 2025

Hi Hristian, I've attached a video showing the error. In the beginning, I left-click, later right-click. Left-clicking clears the selection correctly. Note that SelectedItems only contains a single item (as expected). I've tested this in both Firefox and Chromium, the issue occurs in both. I don't see anything outside of the file in my project that could affect it besides possible prerendering being enabled (but that is default in Blazor). Kind regards, Sebastian

### Response

**Hristian Stefanov** commented on 20 Feb 2025

Hi Sebastian, Thank you for sharing a screen recording. I investigated further and now I understand better what is causing the behavior in this scenario. The issue you're encountering seems to stem from how Blazor's state updates and UI rendering are being handled. Without await Task.Delay(1): When you assign a value to SelectedItems, Blazor processes the update immediately, and because of the event handler flow and how the component is rendered, only the selected item gets updated and rendered in the UI. With await Task.Delay(1): When you introduce the delay, the state changes and the UI is forced to render after the delay, but by that point, the SelectedItems is still in a "pending" state. The delay can cause Blazor to batch updates or render things at a later stage. The result is that the selection gets confused, and the UI shows all items selected when in fact only one item is in the collection. Blazor uses a single-threaded rendering model, so introducing a delay can lead to a situation where the UI is rendered before the state change has been fully processed. Additionally, the asynchronous call can cause the component to re-render unexpectedly, leading to undesired results. Kind Regards, Hristian

### Response

**Sebastian** commented on 24 Feb 2025

Hi Hristian, Thank you for the solution, the selection works as expected now. Nevertheless, this is quite unexpected. If Teleriks Tree List doesn't work correctly with an asynchronous event handler, shouldn't this be documented somewhere or even prevented on a type level? I couldn't find any documentation regarding this issue. Best regards, Sebastian

### Response

**Hristian Stefanov** commented on 25 Feb 2025

Hi Sebastian, I'm glad to hear that the selection works now as expected on your end. The reason we haven’t documented this is that it’s more of a general Blazor behavior rather than an issue specific to the OnRowContextMenu event. Such race conditions can occur in various scenarios with different events, including non-Telerik ones, but they might also work correctly in other contexts. This behavior isn’t exclusive to our component, which is why it’s not explicitly mentioned in our documentation. Kind Regards, Hristian
