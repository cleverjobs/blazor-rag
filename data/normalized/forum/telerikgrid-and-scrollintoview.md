# TelerikGrid and scrollIntoView

## Question

**Lou** asked on 21 Feb 2023

Hello, I try to scroll to the selected item in grid and w/o success. I use this : <TelerikGrid Data=@infosEmplacementSource Class="@theGridClass" @bind-SelectedItems="@SelectedItems_".... string theGridClass { get; set; }="theSpecialGrid";

public async Task EmplacementSubmitHandler()
{
emplacementMessageStore?.Clear();
infosEmplacementsTelerikDialog.FicheEspaceClosId=ficheEspaceClosId;

var (success, added, error)=await AdditionalInformationDataService.AjoutertlkpEmplacementAsync(infosEmplacementsTelerikDialog, CultureInfo.DefaultThreadCurrentCulture.Name.ToString());
if (success)
{
infosEmplacementSource.Insert(0, new treltlkpEmplacementViewModel
{
tlkpEmplacementId=added.tlkpEmplacementId

});
CloseTelerikDialogAddEmplacementSource();
SelectedItems_=infosEmplacementSource.Where(item=> item.tlkpEmplacementId==added.tlkpEmplacementId).ToList();
await Task.Delay(20);//rougly one rendering frame so this has the chance to render in the browser
await _jsRuntime.InvokeVoidAsync("scrollToSelectedRow", "." + theGridClass);

}
.............. // this function takes a selector that describes the desired grid
// and then finds the first selected row, then scrolls to it
// via standard browser methods - effectively, the grid does not
// interact or implement this. Suitable for regular paging mode only, not for virtual scrolling
function scrollToSelectedRow(gridSelector) {
var gridWrapper=document.querySelector(gridSelector);
if (gridWrapper) {
var selectedRow=gridWrapper.querySelector("tr.k-selected");
if (selectedRow) {
selectedRow.scrollIntoView();
}
}
} SelectedItems_ works fine. The row is selected. But scroll not working Debug javascript and everingthing is found

### Response

**Hristian Stefanov** commented on 24 Feb 2023

Hi Louis, The provided code looks OK. In the attached project (see " sample-ScrollIntoViewSelectedRow.zip "), I have tested the described configuration carefully. As a result, the javascript function seems to work as expected on my machine. It scrolls correctly to the selected row. Please run the attached sample to see if the result you get is the same. Maybe there is something else I'm missing from the actual project that will help me reproduce the problem. If, after comparing both projects, the problem still appears, modify it to show the problem/the full configuration and attach it back. That will allow me to see the behavior firsthand and investigate further. Thank you. I look forward to hearing from you.
