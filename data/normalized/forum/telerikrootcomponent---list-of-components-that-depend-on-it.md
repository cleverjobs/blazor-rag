# TelerikRootComponent - List of Components that depend on it?

## Question

**Sco** asked on 08 Dec 2023

Is there a list somewhere of the Telerik Blazor Components that depend or need the TelerikRootComponent... because a lot of them work without it... the TelerikButton for example can work without it... a definitive list would be nice, thanks in advance!

## Answer

**Dimo** answered on 08 Dec 2023

Hi Scott, All components that use any kind of popup require TelerikRootComponent. All Selects and DateTime pickers Window, Dialog, Tooltip Notification Menu, ContextMenu Buttons with dropdowns (SplitButton, DropDownButton) All components that use any of the above internally. For example, the Grid can use DateTime pickers for filtering or editing. Regards, Dimo Progress Telerik
