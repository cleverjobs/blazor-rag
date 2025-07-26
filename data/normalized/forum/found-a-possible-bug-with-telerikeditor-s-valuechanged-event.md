# Found a possible bug with TelerikEditor's ValueChanged event

## Question

**Ric** asked on 23 Mar 2025

Hi, I would like to confirm whether the following behavior is a known issue with the TelerikEditor component. Specifically, I am referring to its ValueChange event as documented on Blazor Editor Events - Telerik UI for Blazor. Please, use the following code example instead: @* Provide an initial value and update the view-model through the ValueChanged event *@<TelerikEditor Value="@TheEditorContent" ValueChanged="@ValueChangedHandler">
</TelerikEditor>

@TheEditorContent

@code { string TheEditorContent { get; set; }=@"<div>
<p>Paragraph 1</p>
<p>Paragraph 2</p>
<p>Paragraph 3</p>
<p />
<p />
<p>Paragraph 4</p>
</div>"; void ValueChangedHandler ( string value ) { // update the view-model //TheEditorContent=value; Console.WriteLine( "ValueChanged fired" );
}
} In this example, TheEditorContent string as been assigned a verbatim literal string containing CRLF formatting. The view-model update was commented out. Compile and, hopefully, you'll confirm as I did that if you click or try to type on the editor, the console will infinitely loop over the ValueChangeHandler and print "ValueChanged fired" indefinitely. Furthermore, if you actually update the view-model, although the loop doesn't occur anymore, the ValueChanged event is fired upon cliking once on the editor. I assume that upon update, the editor changes the formatting of the input in such a way that this "bug" is not longer triggered on further clicks. Why does that happen and how can one fix it? PS: I noticed this behaviour on my own project, where I wanted to save the original checksum of the text and compare it with successive new checksums as I edited the text in order to check for text differences. Anyway, due to this problem I have a different checksum as soon as I click the editor, thus triggering other logic of mine warning the user that it needs to save his/her changes (although there aren't any).

## Answer

**Anislav** answered on 24 Mar 2025

I was able to reproduce the issue you described, but I found that the root cause is not the CRLF symbols. Instead, the issue occurs due to empty paragraph tags. I was able to reproduce the behavior using the following simplified example: string TheEditorContent { get; set; }="<br/>"; You can test this behavior using the following link: [https://blazorrepl.telerik.com/QpudQeOD2699JlbT39](https://blazorrepl.telerik.com/QpudQeOD2699JlbT39) I'm not entirely sure whether this is a bug. The TelerikEditor component is built on the ProseMirror engine, a toolkit for creating rich-text editors. This engine modifies the input content to ensure proper formatting and appearance within the editor. It seems that when the engine initializes with an empty or self-closing tag, such as <p /> or <br/>, it applies formatting and then triggers an event to update the Blazor component's value. However, since the TheEditorContent=value line is commented out, the Blazor component's value remains unchanged. As a result, the unformatted initial value is passed back to the underlying engine, causing an infinite loop. Regards, Anislav Atanasov

### Response

**Ricardo** commented on 25 Mar 2025

Thank you so much for pointing out the actual cause of the issue! I'll proccess my HTML and replace the self-closing tags with their open and close tags, correspondingly. Although I understand the reasoning behind your last paragraph, I cannot shake off the feeling that any infinite loop triggered at production level should be considered a bug or at least have documentation available describing this behaviour (if there is any, I apologize in advance).

### Response

**Nadezhda Tacheva** commented on 26 Mar 2025

Hi Ricardo and Anislav, @Anislav, thank you for stepping in and sharing your observations on the current behavior! @Ricardo, while I agree that firing ValueChanged in an infinite loop is not a good behavior, not updating the Editor value may deliver an odd UX. When the user types, it will look like a change is made which will flicker and disappear right after that. Detecting a change in the content for comparison with the old content is one thing but discarding that change by not updating the view-model is a different thing. Can you please provide more details on why you do not update the Editor value in the UI?

### Response

**Ricardo** commented on 27 Mar 2025

Hello Nadezhda! Thank you for answering! The decision to not update the Editor's value was meant solely to simplify the shown example. While assigning the new value to EditorContent does prevent the infinite loop, the underlying issue persists in a different form: even when the value is updated correctly, the ValueChanged event is still triggered upon the first click on the editor. This poses a bit of a challenge towards using checksums for content comparison. I store the original checksum upon rendering the editor, but due to those self-closing tags, when I click the first time on the component, the event is triggered and the HTML is fixed accordingly, but the checksum value is now different, even if the user didn't edit anything.

### Response

**Nadezhda Tacheva** commented on 31 Mar 2025

Hi Ricardo, Thank you for getting back to me with more details! If I properly understand the actual problem that you are hitting is that the ValueChanged fires on the first click in the Editor while the value is not actually changed. Based on my testing, this happens only when the value contains a self-closing tag and on the first click in the Editor. Consecutive clicks in the Editor do not cause ValueChanged to fire. I consider this as an issue, too, as you cannot properly detect the content change. I opened the following item on your behalf: If the value contains a self-closing tag, ValueChanged is fired upon first click in the Editor I also added your vote there to increase its popularity and as a creator, you are subscribed to get status updates.

### Response

**Ricardo** commented on 31 Mar 2025

Hello again Nadezhda, Exactly, the issue is as you described! Thank you so much for reporting the bug for me!
