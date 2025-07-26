# Change Dialog button text

## Question

**Hel** asked on 18 Oct 2021

Can I change the dialog box 'OK' and 'Cancel' button text to 'Yes' and 'No'

## Answer

**Dimo** answered on 20 Oct 2021

Hello, Currently, it is possible to change the Dialog OK and Cancel button text with localization. On the other hand, we plan to introduce a more flexible Dialog component, which will feature fully customizable rich content. Then you will be able to change the button text more easily. The preliminary timeframe is early 2022. Regards, Dimo Progress Telerik

### Response

**HelpDesk** commented on 27 Oct 2021

Thanks Dimo, Looking forward to this new dialog component. Cheers, Gerald

### Response

**Gerard** commented on 10 Feb 2023

This is the current (decompiled) API for your Confirm dialog component: // // Summary: // Opens a confirm dialog. // // Parameters: // text: // The text of the dialog. // // title: // The title of the dialog. // // Returns: // Whether the use confirms or not. public Task<bool> ConfirmAsync(string text, string title) { return _dialogBuilder?.Confirm(text, title); } internal Task<bool> ConfirmAsync(string text, string title, string okButtonText, string cancelButtonText) { return _dialogBuilder?.Confirm(text, title, okButtonText, cancelButtonText); } Why do I need to create a custom prompt component when all you need to do is to make the ConfirmAsync(string text, string title, string okButtonText, string cancelButtonText) method public?

### Response

**Dimo** commented on 13 Feb 2023

@Gerard - The original idea of the predefined Dialogs was to resemble the default browser dialogs. This translated to simple API and a small number of customization options. At the same time, we recognize the need to customize the Dialog buttons' text and here is the public item that you can track. We will do some 2023 planning in the following weeks and the item status may change.
