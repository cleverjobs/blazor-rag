# Problem with Selection in Grid

## Question

**Pet** asked on 19 Jan 2024

Hello, I have a grid with TelerikGrid Data="@lData" Height="200px" Width="auto" RowHeight="20" @ref="@GridRef" Sortable="true" Navigable="true" FilterMode="GetFilter()" Size="@ThemeConstants.Grid.Size.Small" Resizable="true" Reorderable="true" SelectionMode="@GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<NodeData> list)=> SelectRows(list))" OnRowClick="@OnRowClickHandler" OnRowDoubleClick="@OnRowDoubleClickHandler"> public async Task SelectRows(IEnumerable<NodeData> row) { List<FieldBase> fields=gridFields.Cast<FieldBase>().ToList(); SelectRowEventArgs selectRowrEventArgs=new SelectRowEventArgs(objectGrid, fields, row); await OnSelectRowCallback.InvokeAsync(selectRowrEventArgs); //this row maybe problem with selection } private async Task OnRowClickHandler(GridRowClickEventArgs args) { } Problem is with selection in grid with calling await OnSelectRowCallback.InvokeAsync(selectRowrEventArgs); I tried also OnRowClickHandler but seems the same problem. Could you help me, please, I don't know what is wrong Thanks Peter

### Response

**Hristian Stefanov** commented on 24 Jan 2024

Hi Peter, Thank you for sharing part of the configuration you use. Upon a thorough review of the code you've shared, I confirm that it seems OK. However, given the number of dependencies at play, I'm relegated to evaluating it without running the configuration. Thus, I've attempted to isolate the described issue using a standard Grid configuration. As a result, the selection seems to work correctly. In line with our goal of resolving the situation, as a next step, can you please send the whole configuration in a runnable sample with dummy data via the REPL platform to reproduce the issue? Having a runnable variant will enable me to gain firsthand exposure to the issue and consequently offer a suitable solution. I stand ready to provide prompt assistance once I hear back from you. Kind Regards, Hristian
