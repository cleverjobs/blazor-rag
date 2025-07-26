# OnCancel does not fire when escaping out of Inline Editing

## Question

**Rol** asked on 01 Aug 2020

A grid with Navigable=true allows me to start editing a newly added record right away, no Command Buttons needed, just some fiddling with grid State stop editing by pressing Escape However, when using Escape no event is fired. Which is fine when I am editing an existing record, because any modifications are just discarded. But when the user is escaping out of a newly added row, I want to dispose of that row and underlying item immediately. Without an event to detect the cancel I don't now how to do that. Any suggestions?

## Answer

**Marin Bratanov** answered on 04 Aug 2020

Hello Roland, I made this public page where you can Follow the status of this issue, and it also contains a concept of a workaround you can try: [https://feedback.telerik.com/blazor/1479052-oncancel-does-not-fire-when-escaping-out-of-inline-editing.](https://feedback.telerik.com/blazor/1479052-oncancel-does-not-fire-when-escaping-out-of-inline-editing.) Regards, Marin Bratanov
