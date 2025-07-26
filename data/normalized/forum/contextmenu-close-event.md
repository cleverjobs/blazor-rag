# ContextMenu close event

## Question

**Nik** asked on 09 Jan 2023

Hello, Is there a way to capture when the contextmenu is closed? If user presses one action or just clicks outside the menu. Either a method or an event. Thanks

## Answer

**Dimo** answered on 12 Jan 2023

Hi Nikolas, If the user clicks on a ContextMenu item, the app will know about this in the ContextMenu's OnClick event. On the other hand, currently there is no built-in way to know when the user hits Escape or clicks outside the ContextMenu. There is a public feature request for ContextMenu OnHide event with an example - you will need click and keydown handlers on the documentElement. From these handlers, notify the .NET runtime that the ContextMenu has closed. Regards, Dimo Progress Telerik
