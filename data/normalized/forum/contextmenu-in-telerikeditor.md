# ContextMenu in TelerikEditor?

## Question

**Nat** asked on 27 Feb 2023

Is it possible to use a ContextMenu inside a TelerikEditor? We're attempting to allow users to insert pre-selected phrases with a right-click menu.

### Response

**Aaron** commented on 27 Feb 2023

Is it possible to leverage the use of a custom ContextMenu within the Editor component when using Blazor UI? Do you have any examples of how to implement this as you do in several of your other products?

## Answer

**Yanislav** answered on 02 Mar 2023

Hello, I will share the possible approach Aaron and I discussed here, to make it available to the community, in case anyone has the same question in the future. To open a ContextMenu when the user clicks inside the content of the Editor, you have to: 1. Set a custom class to the Editor and pass it to the Selector configuration of the ContextMenu. <TelerikContextMenu Selector=".context-menu-target"...
<TelerikEditor @ref="@EditorRef" Class="context-menu-target" 2. Set the EditMode of the Editor to 'Div'. EditMode="EditorEditMode.Div" Otherwise, the Editor content will be rendered inside an Iframe and the ContextMenu will not open. Here is a REPL example that demonstrates the approach. Regards, Yanislav
