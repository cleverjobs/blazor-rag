# CheckBox binding not update main component property if inside a Dialog

## Question

**Cla** asked on 12 Sep 2024

I have a bool property binded in two way to a dialog checkbox. if i change the check value, the variabile inside the dialog in binded correctly, but the variable binded in the main component in not updated. Check this sample, if i set the check and close the dialog, the parent compoent variable is not updated. [https://blazorrepl.telerik.com/ceuZbwah44LSdBQu06](https://blazorrepl.telerik.com/ceuZbwah44LSdBQu06) how to solve? Main.Razor @if (IsDialogVisible) { <CheckDialog @bind -CheckValue="CheckValue" OnClose="()=> IsDialogVisible=false" /> } <p> CheckValue is @CheckValue </p> @code { private bool IsDialogVisible {get;set;}=true; private bool CheckValue {get;set;} } CheckDialog.Razor <TelerikDialog @ref="Dialog" Visible="true" ShowCloseButton="false"> <DialogContent> <TelerikCheckBox @bind -Value="CheckValue" OnChange="()=> Dialog.Refresh()" /> Check test </DialogContent> <DialogButtons> <TelerikButton OnClick="()=> OnClose.InvokeAsync()"> Close </TelerikButton> </DialogButtons> </TelerikDialog> @code { private TelerikDialog Dialog {get;set;} [Parameter] public bool CheckValue {get;set;} [Parameter] public EventCallback <bool> CheckValueChanged {get;set;} [Parameter] public EventCallback OnClose {get;set;} }

## Answer

**Dimo** answered on 13 Sep 2024

Hi Claudio, The same problem exists without a Dialog: [https://blazorrepl.telerik.com/coYXlnPS54yt3iyy01](https://blazorrepl.telerik.com/coYXlnPS54yt3iyy01) The problem is that the code in CheckDialog.razor is not invoking the CheckValueChanged EventCallback anywhere, which will update CheckValue in the parent component. This should happen in the ValueChanged handler of the CheckBox. Please consult the Microsoft documentation about parameter binding. Regards, Dimo Progress Telerik
