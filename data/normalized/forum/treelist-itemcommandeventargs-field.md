# TreeList ItemCommandEventArgs.Field

## Question

**Cip** asked on 11 May 2021

Hi everybody, I'm using the InCell EditMode for a TreeList. In my TreeList are present some columns where I don't want to permit the user to edit the value, so from start I'm using the OnEditEventHandler which has as arguments the ItemCommandEventArgs setting the IsCancelled property to true. But If I want to filter out the column on which I want to allow the user to edit the value using the Field property it says that the Field Property is depricated. So is there another way to solve this issue? Thank you.

## Answer

**Marin Bratanov** answered on 11 May 2021

Hi, You can use the EditorTemplate and show an editor or not, or replace it with text or some other logic based on your business logic. Make sure to also review the notes about incell editing (namely about the editor template but also the other sections on how it is supposed to work) You may also want to Follow this page for a potential change in this behavior. Regards, Marin Bratanov

### Response

**Ciprian Daniel** commented on 11 May 2021

If I use the editor template and inside it I add a TelerikNumericTextBox I can't write a number with more then one digits as the dom is regenerated and the focus is put back on the input selecting the number I have entered before. Is there a way to stop the propagation or how can I fix this issue?

### Response

**Marin Bratanov** commented on 11 May 2021

Perhaps you are hitting this bug: [https://feedback.telerik.com/blazor/1485087-teleriktreelist-editortemplate-with-textbox-loses-focus-on-keystroke-in-insert-mode.](https://feedback.telerik.com/blazor/1485087-teleriktreelist-editortemplate-with-textbox-loses-focus-on-keystroke-in-insert-mode.)

### Response

**Ciprian Daniel** commented on 11 May 2021

Yes, something like that. I don't understand why is that happening as I didn't clicked anywhere else so the input should not lose the focus as long as I'm typing something into it.

### Response

**Ciprian Daniel** commented on 12 May 2021

If I use the editor template on every keystroke the treelist is regenerated which is why the focus is lost. If I'm not using the editor template then I can write the values I want. The treelist is regenerated only onblur, but in this case I can't filter out the cells that I don't want to be editable. Maybe there is somtehing I'm not getting right.

### Response

**Marin Bratanov** commented on 12 May 2021

This is a bug whose progress you can Follow in the link above.
