# Display the prompt and output for the AIPrompt as one view

## Question

**Ste** asked on 11 Feb 2024

I am wondering if it is possible to change the AIPrompt to be a bit more like a chat then a separate request/prompt, and then having it as it currently operates as separate window/tab displaying the prompt and user response and the second tab having the output to the prompt. It would seem to me that it is smoother to have it all in one, rather than separate. Is there any solution? Steve

## Answer

**Dimo** answered on 14 Feb 2024

Hello Steve, Yes, you can use AIPrompt templates to merge all the UI in one view: <TelerikAIPrompt @ref="@AIPromptRef" @bind-Prompt="@Prompt"> <AIPromptViews> <AIPromptPromptView ButtonIcon="@SvgIcon.TellAFriend"> <ViewTemplate> <div style="height:300px;overflow:auto;"> @foreach (var item in Outputs)
{ <div @key="@item"> <h5> @item.Title </h5> <p> @item.Text </p> </div> } </div> </ViewTemplate> <FooterTemplate> <TelerikTextArea @bind-Value="@Prompt" Rows="3" /> <TelerikButton OnClick="@HandlePromptRequest"> Send </TelerikButton> </FooterTemplate> </AIPromptPromptView> </AIPromptViews> </TelerikAIPrompt>

@code {
private TelerikAIPrompt? AIPromptRef { get; set; }

private string Prompt { get; set; }=string.Empty;

private List<AIOutput> Outputs { get; set; }=new ();

private void HandlePromptRequest ( ) {
Outputs.Add( new AIOutput($ "New Title {DateTime.Now.Millisecond}", $ "Response at {DateTime.Now.ToLongTimeString()} for {Prompt}" ));

Prompt=string.Empty;
}

public class AIOutput {
public string Text { get; set; }

public string Title { get; set; }

public AIOutput ( string title, string text ) {
Title=title;
Text=text;
}
}
} Regards, Dimo Progress Telerik

### Response

**Steven** commented on 14 Feb 2024

That worked very well, thank you for the quick response to this problem. Steve
