# Editor in Div mode not updating when value changed programatically.

## Question

**Mic** asked on 27 Sep 2024

I'm using an editor to capture rich text to add to the database. After I add it, I clear the field out that is bound to the editor but the editor does not update on the page. It still has the previous values. <TelerikEditor @ref="@AnswerEditor" @bind-Value="@FaqToAdd.Answer" Tools="@EditorTools" EditMode="EditorEditMode.Div" Height="auto" DebounceDelay="0" Width="100%"> </TelerikEditor>

### Response

**Hristian Stefanov** commented on 30 Sep 2024

Hi Michael, I have tried to recreate the described problem within this demo: REPL link. As a result, the Editor's value seems to be changing correctly without reverting. Please run and test the REPL sample to see if the result you get is the same. As a next step, modify the above example to reproduce the issue and send back the REPL link to me for further inspection. This will help me continue investigations. I look forward to hearing back from you. Kind Regards, Hristian
