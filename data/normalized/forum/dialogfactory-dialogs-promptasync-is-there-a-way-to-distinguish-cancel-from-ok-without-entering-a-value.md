# DialogFactory.Dialogs.PromptAsync is there a way to distinguish cancel from ok without entering a value?

## Question

**Rob** asked on 09 Jun 2022

The DialogFactory.Dialogs methods are really convenient but the prompt is missing some functionality: - how can u distinguish pressing Cancel from pressing Ok without entering a value (both return null) - there should be a way to make it mandatory (solves the above) - what about setting a default value? or am I missing something?

## Answer

**Timothy J** answered on 09 Jun 2022

>> - how can u distinguish pressing Cancel from pressing Ok without entering a value (both return null) <<Do you mean ConfirmAsync? I believe it is just a boolean. True=Ok, False=Cancel (or close) if (!(await Dialogs.ConfirmAsync(s.ToString(), "Delete?"))) return;

### Response

**Robert** commented on 10 Jun 2022

No I mean this one: Task<string> PromptAsync(string text, string title)

### Response

**Timothy J** answered on 10 Jun 2022

Ok.>> - how can u distinguish pressing Cancel from pressing Ok without entering a value (both return null) <<I think if you need to know the differences between the nulls you're going to have to move away from the predefined dialogs and use the custom buttons: Blazor Dialog Action Buttons | Telerik UI for Blazor
