# How to use custom Dialog to replace pre-defined Dialog functions

## Question

**Bry** asked on 28 Apr 2023

I am interested in replacing the predefined dialog function (Alert, Confirm, Prompt) with custom dialogs. I have the Alert working, but not sure how to setup a custom version of ConfirmAsync. I know I need to do an await in my custom routine, but how do I setup the async logic flow? Is an async version of the VisibleChanges event required? Is there are example you can point me to? Thanks, Bryan

### Response

**Dimo** commented on 03 May 2023

Bryan - if I understand correctly, you are seeking advice on the implementation of your own component. In this case, my advice is to download our source code and see how we have implemented Services/DialogFactory.cs and Components/Dialog/DialogBuilder.razor.cs

### Response

**Bryan** commented on 03 May 2023

Fantastic, thanks Bryan

### Response

**Sheraz** commented on 13 Mar 2024

Hi Bryan, I am in a similar kind of situation and would like to extend the DialogBuilder with in my application. Please can you tell me whether you were able to achieve what you were looking to do or not?

### Response

**Bryan** commented on 14 Mar 2024

/// <summary> /// Displays a modal message box /// </summary> /// <param name="message"></param> /// <param name="title"></param> /// <param name="buttons"></param> /// <param name="icon"></param> /// <param name="defaultButton"></param> /// <param name="titleIcon"></param> /// <param name="helpUrl"></param> /// <param name="moreContent"></param> /// <returns>Result of user action</returns> public async Task<DialogResult> MessageBox(string message, string title, MessageBoxButtons buttons, MessageBoxIcon icon, DefaultButton defaultButton, DialogTitleIcon titleIcon=DialogTitleIcon.Default, string helpUrl=null, RenderFragment moreContent=null) { _shouldRender=false; //small optimization, redraw when everything is set _message=message; _title=title; _extraContent=moreContent; _helpUrl=helpUrl; _dialogButtons=buttons; SetIcon(icon); SetButtons(_dialogButtons, _helpUrl); SetTitleIcon(titleIcon); Open(); await Task.Delay(500); if (defaultButton !=DefaultButton.Button1) //First button will automatically get focus { await JsRuntime.InvokeVoidAsync("SetControlFocus", GetButtonSelector(defaultButton)); } await AwaitAction(); Close(); return _result; } private void Open() { _shouldRender=true; _visible=true; StateHasChanged(); } private void Close() { _visible=false; StateHasChanged(); } private protected virtual async Task AwaitAction() { while (!_actionTaken) { await Task.Delay(DefaultActionTakenWaitDelay); } _actionTaken=false; } Relevant, but incomplete code posted here, basically, make your own dialog visible, and add AwaitAction which just loops around waiting for the user to click a button, hide it when they do, nothing fancy. DefaultActionTakenWaitDelay is just a constant I set to 20. Bryan
