# How to update text field when drop down changes

## Question

**TimTim** asked on 08 Dec 2022

I have a page with several TelerikDropDownList controls with Yes and No options, and an associated text field for notes underneath each one. If the user selects the Yes option, I want to remove any notes in the associated text field. Is this possible? I know about ValueChanged, but only the value is passed to the function. Within the ValueChanged I can't figure out how to get a reference to the TelerikDropDownList that initiated the event and its associated text field. Thanks

## Answer

**Marin Bratanov** answered on 08 Dec 2022

Hello Tim, In Blazor, you change the data in the view-model, not through the component reference. So, an event of the dropdown (ValueChanged or OnChange) lets you capture the user action, and then you simply have to alter the value of the field the text input is bound to. Regards, Marin Bratanov Progress Telerik

### Response

**Tim** commented on 09 Dec 2022

That makes sense. Thank you.
