# Need help returning selected values from multiselect.

## Question

**Dav** asked on 04 Jun 2021

I have a mutliselect contained with in a window control which is then hosted on the parent page as a component. The window control also contains a button to click once you select from the multi select which in it's onclick code performs a call back to the mainpage like this: OnSelectedItems.InvokeAsync(selectedItems); At this point the selected items are in the variable. But the parent page does not seem to receive them. I am sending the component code as well as how it's referenced in the parent page. I have tried everything. This is the parent page razor code: EditForm Model="@ps" OnValidSubmit="FilteredSearchAsync"> <button type="submit">Search</button> <label id="lbldodId"> DoD Id: <InputText id="DodIdSearch" @bind-Value="ps.DodId" /> <img src="/Images/icon-magnifying-glass.jpg" @onclick="showPopup" alt="" style="width:25px;height:25px;" /> </label> <SearchFilterPopupComponent IsVisible="@showFilterPopup" InputData="@dodIdList" selectedItems="@selectedDodIds" OnSelectedItems="@UpdateThisComponent"></SearchFilterPopupComponent> <label id="lblFirstName"> First Name: <InputText id="FirstNameSearch" @bind-Value="ps.FirstName" /> </label> <label id="lblLastName"> Last Name: <InputText id="LastNameSearch" @bind-Value="ps.LastName" /> </label> <button @onclick="ClearSearch">Clear</button> </EditForm> protected void UpdateThisComponent() { if (selectedDodIds.Count> 0) // at this point the count is zero { showFilterPopup=false; ps.DodId=selectedDodIds[0]; //just grabbing the first one for now StateHasChanged(); } } This is my component code: <TelerikWindow @bind-Visible="@IsVisible"> <WindowTitle> <strong>The Title</strong> </WindowTitle> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> <WindowContent> <TelerikMultiSelect Data="@InputData" @bind-Value="@selectedItems" Placeholder="Enter Dod ID or click to see all." Width="350px" ClearButton="true" AutoClose="false"> </TelerikMultiSelect> <TelerikButton OnClick="@ItemsSelected">Select</TelerikButton> </WindowContent> </TelerikWindow> public partial class SearchFilterPopupComponent { [Parameter] public List<string> InputData { get; set; } [Parameter] public EventCallback<List<string>> OnSelectedItems { get; set; } [Parameter] public EventCallback<bool> OnVisibleChanged { get; set; } [Parameter] public bool IsVisible { get; set; } [Parameter] public List<string> selectedItems { get; set; } protected void OpenWin() { IsVisible=true; } protected void CloseWin() { IsVisible=false; OnVisibleChanged.InvokeAsync(IsVisible); } protected void ItemsSelected() { IsVisible=false; OnSelectedItems.InvokeAsync(selectedItems); //AT this point all the items selected are in this variable. } } }

## Answer

**Hristian Stefanov** answered on 09 Jun 2021

Hi David, It seems that the problem comes from the way the collection is being received. To fix this problem, receive the collection as an argument in the UpdateThisComponent method. The code block below showcases the method from your example with the changes highlighted. protected void UpdateThisComponent( List <string> selectedDodIds )
{
if (selectedDodIds.Count> 0) // at this point the count is zero
{
showFilterPopup=false;
ps.DodId=selectedDodIds[0]; //just grabbing the first one for now

StateHasChanged();
}
} I hope this helps. If I'm missing something from the scenario or you have any other questions, please let me know. Thank you. Regards, Hristian Stefanov
