# Window Event VisibleChanged not firing

## Question

**Hen** asked on 12 Jan 2024

I want to use the VisibleChanged-Event but it is only firing, if the User closes the Window through "CloseOnOverlayClick" A click on an Action-Button or setting the isVisible-Property to false does not work. Here is my Code: <TelerikWindow Class="window-dialog" Centered="true" Visible="@isVisible" VisibleChanged="@VisibleChangedHandler" Modal="true" CloseOnOverlayClick="true"> <WindowTitle> <strong> Log-In </strong> </WindowTitle> <WindowActions> <WindowAction Name="Close" OnClick="@(()=>isVisible=false)" /> </WindowActions>...

### Response

**Dimo** commented on 12 Jan 2024

@Hendrik - I don't observe such а behavior: [https://blazorrepl.telerik.com/meEPPGbb36wgTebg36](https://blazorrepl.telerik.com/meEPPGbb36wgTebg36) Please send a similar runnable test page for inspection.

### Response

**Hendrik** commented on 13 Jan 2024

Here is a sample project. I saw that the sample is running on your webside but it does not work in a real project. The project is based on the newest Web-App-Template (.NET 8) and everything is made by the book refering to your documentation.

### Response

**Dimo** commented on 15 Jan 2024

@Hendrik - sorry about the misunderstanding. I understood the opposite from what you said. VisibleChanged does not fire when clicking on the Close WindowAction, because it has an OnClick handler, which replaces the built-in behavior with custom logic. If you want the VisibleChanged event to fire for the action button, then remove the OnClick handler, which does not seem to be necessary anyway. Other than that, the provided project works as expected: VisibleChanged fires when clicking on the modal overlay. VisibleChanged does not fire when clicking on the button inside the Window content, because the button closes the Window programmatically. Our components fire events that result from user behavior, and not from programmatic algorithms.

### Response

**Hendrik** commented on 15 Jan 2024

Thank you. That was helpful.
