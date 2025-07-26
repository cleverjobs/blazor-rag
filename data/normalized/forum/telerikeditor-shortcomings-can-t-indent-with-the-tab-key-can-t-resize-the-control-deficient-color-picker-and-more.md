# TelerikEditor shortcomings: can't indent with the Tab key, can't resize the control, deficient color picker, and more

## Question

**Cha** asked on 25 Oct 2024

Hi, due to SyncFusion changing their licensing for small organizations, I'm converting our app from SyncFusion to Telerik. In most cases, Telerik controls are equivalent or superior. Not so with the Editor control. :( Users expect editors to be Microsoft Word like, within reason, and the Editor control is seriously lacking. 1 - Users have to be able to indent with the Tab key. Please provide an option for Tab to indent and not jump out of the control. 2 - Can't resize the control, like we can here in this forum field? It's basic functionality. Auto sizing up to a max would be helpful. I found the feature request showing how to set a min-height and max-height. What it doesn't say is the Div mode has a height somewhere in the framework of 250 (and an incomplete width?), so you have set the height in the control, even if it's blank. 3 - Viewing html source of the editor pops up a small window that you can only resize vertically, but not horizontally?!? It's basically unusable, unless you want to copy the content out and edit it somewhere else. 4 - The color picker is basically unusable. It should be two controls, like any other respectable editor: the first applies the currently selected color (which the control remembers and visually shows), and the second is a drop down that allows you to select the color (which it remembers), it applies that color, and then the palette closes. The existing picker does none of this. :( And Red is missing from the palette?? 5 - The documentation for most controls has a section "appearance". This one doesn't? The info on controlling the height and width should be in this missing section, including how-to for Div vs iFrame. 6 - More documentation on the existing toolbars would be helpful for customization. I shouldn't have to step through the code and analyze what's in "new List<IEditorTool>(Telerik.Blazor.Components.Editor.EditorToolSets.All)" to figure out how to remove unwanted tools? 7 - EditorPasteSettings seems to be broken. I can copy from Word, paste into the control, look at the source in the tiny window, and right at the top is a class="MsoNormal". The documentation indicates this is on by default, but it doesn't matter whether I omit that parameter, or explicitly set it to true, Mso classes still come in. I didn't test if the other default paste cleanup functionality is working or not. 8 - My users require the "Insert Symbol" tool on the toolbar. SyncFusion provided me custom code to add this to their control with a dialog. Can Telerik do the same? All of this functionality exists in the state of the art SyncFusion editor. Sadly I'm going to have to continue to use the SfRichTextEditor control and minimal SyncFusion content until the TelerikEditor control is updated. If I were Telerik, I would be embarrassed by this control. :( I'm using .NET 8 with the current Telerik UI, which is 6.2.0. Thanks for your time. Regards, Charles P.S. On a side note, your document conversion code is fantastic. I can import a Word doc with your
DocxFormatProvider and convert it to html with your HtmlFormatProvider
and the content is almost perfect, if not perfect.

## Answer

**Dimo** answered on 30 Oct 2024

Hi Charles, Thanks for sharing detailed feedback. Here are some comments and tips on your list: 1. Indent with Tab This is an existing feature request: Indent Editor content with Tab and prevent tabbing out 2. Editor Resizing This is also an existing feature request: Resize Editor 3. HTML Viewer Resizing This is supported and works on my side: Editor Tools demo A possible downside is that you need to resize the popup window and the textarea element separately. I will check if we can make this a single user action. 4. Color Tool UX The current mechanism and logic is that the ColorPickers show the current color when the caret is at a specific location in the Editor content. You are asking about a somewhat opposite logic - show the last used color and set it with a single click. I agree this makes sense and I will discuss this with the UX team. Closing the dropdown automatically makes complete sense. I will check why the behavior is as is, and will probably log a public item for tracking. 5. Appearance Documentation When we have a dedicated "Appearance" documentation, we usually mean a few specific properties, which the Editor doesn't have. This can change in the future. 6. Toolbar and Tools Documentation All built-in tools are listed in the Built-in Editor Tools article and demonstrated in the Editor Tools online demo. I agree that it makes sense to list the default tools explicitly here and we will do it. 7. Editor Paste Settings I made some test and it turned out that RemoveMsClasses="true" is indeed true by default, but it depends on RemoveAttributes being set to anything. I will investigate further if there is a need to log a bug or fix the documentation. This is the easiest workaround: <TelerikEditor> <EditorSettings> <EditorPasteSettings RemoveAttributes="@( new List<string>() )"> </EditorPasteSettings> </EditorSettings> </TelerikEditor> 8. Insert Symbol This should be achievable with a custom Editor tool that uses the insertHtml command. Regards, Dimo Progress Telerik

### Response

**Charles** commented on 30 Oct 2024

Hi, thanks for the detailed response. I realize a lot of this I can probably manage with some heavy customization. I'd rather not go there, as I was hoping the Telerik controls are "drop in". But the more I use Telerik controls, the more I come to the conclusion that they are somewhat "generic", for lack of better of word, and customization is required. I already have custom controls built around many of them, and I guess I'll have to do the same here if I want to completely retire SyncFusion from this application.

### Response

**Charles** commented on 31 Oct 2024

For comparison, the Grid control is perfect, exactly as it is. It's well refined, thought out, and "drop in", ready to use. The Editor control is the polar opposite. :(

### Response

**Dimo** commented on 01 Nov 2024

Charles, just FYI, this thread resulted in the following improvements so far: (point 3) The textarea in the View HTML dialog will resize together with the popup. (point 4) I sent an inquiry about the Color Tool UX. (point 6) The built-in Editor toolsets are now documented. (point 7) RemoveMsClasses will no longer require RemoveAttributes to be set explicitly. The documentation clarifies that paste cleanup is not enabled by default. The two bug fixes will be released in about two weeks. I am awarding you some Telerik points for your contribution.

### Response

**Charles** commented on 01 Nov 2024

Thank you. This is helpful.
