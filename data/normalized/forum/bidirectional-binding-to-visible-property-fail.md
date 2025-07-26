# bidirectional binding to Visible property fail

## Question

**Jua** asked on 09 Nov 2020

With this code <TelerikLoader @bind-Visible="isLoading" /> return this error: Object of type 'Telerik.Blazor.Components.TelerikLoader' does not have a property matching the name 'VisibleChanged'. I only wan't show the loader when isLoading it's true.

## Answer

**Svetoslav Dimitrov** answered on 11 Nov 2020

Hello Juan, You could show the Loader by changing the value of the property bound to it. Below, I have made a couple of examples. More information on the Loader can be found in our documentation. Example: Show the Loader on button click. <TelerikButton OnClick="@(_=> showLoader=true)">Show Loader</TelerikButton>

<TelerikLoader Visible="@showLoader"></TelerikLoader>

@code { public bool showLoader { get; set; }
} Example 2: Show loader while fetching data from a database This example would use Task.Delay simulating the usage of a database. @if (!MyData.Any())
{ <TelerikLoader Visible="true"> </TelerikLoader> }
else
{
@MyData.FirstOrDefault()
}

@code {
public List <string> MyData { get; set; }=new List <string> ();

public async Task LoadData()
{
MyData.Add("Some Data");
}

public bool showLoader { get; set; }

protected override async Task OnInitializedAsync()
{
await Task.Delay(2000);
await LoadData();
}
} Example 3: Loading Panel A sample implementation of a loading panel can be found in our documentation. If I could further assist you in any way do not hesitate to open a support ticket or follow up on this conversation. Regards, Svetoslav Dimitrov

### Response

**Rafael** commented on 13 Nov 2022

This does not seem to work for me. I have a modal component where I wanted the parent component to signal the ModalDialog that it wants to show the TelerikLoader via two way binding, but it seems like the binding doesn't have any effect. Any ideas? <TelerikDialog @bind-Visible="@ShowModal" ShowCloseButton="false" ButtonsLayout="DialogButtonsLayout.End"> <DialogTitle> <TelerikIcon IconClass="k-icon k-i-exclamation-circle"></TelerikIcon> <strong>@Title</strong> </DialogTitle> <DialogContent> <strong>@Text</strong> </DialogContent> <DialogButtons> @switch (DialogType) { case ModalDialogType.OkCancel: <TelerikButton ThemeColor="@(ThemeConstants.Button.ThemeColor.Primary)" OnClick="@ModalOk"> Ok <TelerikLoader ThemeColor="light" Visible="@_showLoader "/> </TelerikButton> <TelerikButton OnClick="@ModalCancel">Cancel</TelerikButton> break; case ModalDialogType.YesNo: <TelerikButton ThemeColor="@(ThemeConstants.Button.ThemeColor.Primary)" OnClick="@ModalOk"> Yes <TelerikLoader ThemeColor="light" Visible="@_showLoader "/> </TelerikButton> <TelerikButton OnClick="@ModalCancel">No</TelerikButton> break; default: <TelerikButton ThemeColor="@(ThemeConstants.Button.ThemeColor.Primary)" OnClick="@ModalOk"> @ConfirmText <TelerikLoader ThemeColor="light" Visible="@_showLoader "/> </TelerikButton> <TelerikButton OnClick="@ModalCancel">@CancelText</TelerikButton> break; } </DialogButtons> </TelerikDialog> public partial class ModalDialog: ComponentBase { [Parameter] public bool ShowModal { get; set; } [Parameter] public bool ShowLoader { get=> _showLoader; set { if (_showLoader==value) return; _showLoader=value; InvokeAsync(StateHasChanged); ShowLoaderChanged.InvokeAsync(value); } } [Parameter] public string Title { get; set; }=""; [Parameter] public string Text { get; set; }=""; [Parameter] public string ConfirmText { get; set; }="Confirm"; [Parameter] public string CancelText { get; set; }="Cancel"; [Parameter] public ModalDialogType DialogType { get; set; } [Parameter] public EventCallback OnClose { get; set; } [Parameter] public EventCallback OnConfirm { get; set; } [Parameter] public EventCallback<bool> ShowLoaderChanged { get; set; } private bool _showLoader; private Task ModalOk()=> OnConfirm.InvokeAsync(); private Task ModalCancel()=> OnClose.InvokeAsync(); } ****From the Parent**** <ModalDialog ShowModal="@_showModal" Text="@_modalText" @bind-ShowLoader="@_showLoader" Title="@_modalTitle" DialogType="ModalDialogType.YesNo" OnClose="@OnCancel" OnConfirm="@OnConfirm"/>

### Response

**Svetoslav Dimitrov** commented on 16 Nov 2022

Hello Rafael, The Loader component exposes just a parameter that controls the visibility - Visible. The VisibleChanged event is not implemented, thus two-way value binding is not exposed. I have prepared a basic sample with a Telerik Dialog that has a Loader in its content and it seems to work for me as expected: Modal Dialog: <TelerikDialog Visible="@DialogVisible" VisibleChanged="@(async (bool v)=> await InvokeDialogVisibleChanged(v) )" Title="@Title">
<DialogContent>
A new version of <strong>Telerik UI for Blazor</strong> is available. Would you like to download and install it now?
</DialogContent>
<DialogButtons>
<TelerikLoader Visible="@LoaderVisible"></TelerikLoader>
<TelerikButton OnClick="@(()=> { DialogVisible=false; })">Skip this version</TelerikButton>
<TelerikButton OnClick="@(()=> { DialogVisible=false; })">Remind me later</TelerikButton>
<TelerikButton OnClick="@(()=> { DialogVisible=false; })" ThemeColor="primary">Install update</TelerikButton>
</DialogButtons>
</TelerikDialog>

@code {
[ Parameter ] public bool DialogVisible { get; set; }
[ Parameter ] public bool LoaderVisible { get; set; }

[ Parameter ] public EventCallback<bool> DialogVisibleChanged { get; set; } private async Task InvokeDialogVisibleChanged ( bool value ) {
DialogVisible=value; if (DialogVisibleChanged.HasDelegate)
{ await DialogVisibleChanged.InvokeAsync(DialogVisible);
}
} private string Title { get; set; }="Software Update";
} Usage: <ModalDialog @bind-DialogVisible="@isDialogVisible" LoaderVisible="@isLoaderVisible"> </ModalDialog> @code {
private bool isDialogVisible {get;set;}=true;
private bool isLoaderVisible {get;set;}=true;
} Can you try the same approach and get back to me if it works as expected?

### Response

**Jose Antonio** commented on 18 Jan 2023

Hi Svetoslav Dimitrov, this code works for me ... thanks!!!
