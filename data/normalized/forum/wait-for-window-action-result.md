# Wait for Window action result

## Question

**Iva** asked on 11 Jun 2021

Hello! I am trying to use a Window component as a dialog with awaiting the result of an action. Until the user presses the confirm or cancel button, the calling code must wait for an action. In a Dialog component (not a Window component) this is implemented as: var result=await dialog.Show().Result; My implemetation for Window component (component have two buttons with OnClick="@Submit(true or false)"): bool isVisible, dialogResult;
CancellationTokenSource tokenSource; public async Task<bool> Show ( ) {
isVisible=true; await InvokeAsync(StateHasChanged); return await Task.Run(WaitForResult); } // Waiting for action private async Task<bool> WaitForResult ( ) { tokenSource=new(); while (!tokenSource.Token.IsCancellationRequested) ; isVisible=false; await InvokeAsync(StateHasChanged); return dialogResult; } private async void Submit ( bool result ) {
dialogResult=result;
tokenSource.Cancel(); } This works, but WaitForResult method is overloading processor. PLEASE help me with correct impementation...

## Answer

**Marin Bratanov** answered on 14 Jun 2021

Hi Ivan, The most straightforward idea I can offer is simply using the Confirm Dialog we provide: [https://demos.telerik.com/blazor-ui/dialog/predefined-dialogs.](https://demos.telerik.com/blazor-ui/dialog/predefined-dialogs.) If you want more complex content, click the Vote and Follow buttons here: [https://feedback.telerik.com/blazor/1521466-rendering-html-texts-in-header-and-content-custom-dialog-content-html-components.](https://feedback.telerik.com/blazor/1521466-rendering-html-texts-in-header-and-content-custom-dialog-content-html-components.) In the meantime, the following samples can be an alternative: [https://github.com/telerik/blazor-ui/tree/master/common/confirm-button](https://github.com/telerik/blazor-ui/tree/master/common/confirm-button) and [https://github.com/telerik/blazor-ui/tree/master/common/message-box.](https://github.com/telerik/blazor-ui/tree/master/common/message-box.) Regards, Marin Bratanov Progress Telerik
