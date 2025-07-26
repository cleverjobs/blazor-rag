# Clipboard service not able to copy the text when you select folder path and it throws exception.

## Question

**Lak** asked on 26 Aug 2021

Hi Team, As i'm not able to copy the text when you select folder path and it is showing as exception. Could not find 'clipboard' in 'window.navigator'. Error: Could not find 'clipboard' in 'window.navigator'. at Please check below code snippet. public class ClipBoardService { private readonly IJSRuntime _jsRuntime; public ClipBoardService(IJSRuntime jsRuntime) { _jsRuntime=jsRuntime; } public ValueTask WriteTextAsync(string text) { return _jsRuntime.InvokeVoidAsync("navigator.clipboard.writeText", text); } } <GridCommandButton Command="View" OnClick="@CopySelectedItemClicked" Title="Click to view folder containing this file">View</GridCommandButton> if(clipBoardService !=null) { await clipBoardService.WriteTextAsync(selectedItem.IsolationFolderPath); }
