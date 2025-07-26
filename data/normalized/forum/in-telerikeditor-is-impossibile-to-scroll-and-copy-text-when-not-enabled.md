# In TelerikEditor is impossibile to scroll and copy text when not enabled

## Question

**Mar** asked on 22 Dec 2022

Is that behaviour by design?

## Answer

**Tsvetomir** answered on 27 Dec 2022

Hello Marco, For the time being - yes. The read-only state disables all of the pointer events, therefore, click and selection are ignored. If users need access to read-only content, you can render the Editor Value in a scrollable <div> and toggle it with the Editor component when users should edit: <p> <label> <TelerikCheckBox @bind-Value="@EditorEnabled" /> Enable Editor </label> </p> @if (EditorEnabled)
{ <TelerikEditor Height="160px" @bind-Value="@Value" EditMode="@EditorEditMode.Div" /> } else { <div class="k-panel" style="height:160px;overflow:auto;"> @( new MarkupString(Value) ) </div> } @code { string Value { get; set; }=@"<p>foo</p><p><strong>bar strong</strong></p><p>baz</p>
<p>foo</p><p><strong>bar strong</strong></p><p>baz</p>";

bool EditorEnabled { get; set; }=true;
} Regards, Tsvetomir Progress Telerik
