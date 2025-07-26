# TelerikEditor iFrame is not update upon value update

## Question

**Ric** asked on 20 Feb 2024

I'm using the TelerikEditor component: <TelerikEditor @ref="@SummaryEditor" Class="rich-editor" EditMode="@EditorEditMode.Iframe" Value="@TextDisplayModel.Text" ValueChanged="@RichEditorValueChanges" ValueExpression="@((()=> TextDisplayModel.Text))"> </TelerikEditor> And upon updating the variable TextDisplayModel.Text with a new value, the displayed text is not updated. I confirmed with DevTools that despite the textarea associated with the TelerikEditor component being updated, the iframe content does not update, as you can see on the following screenshot. Has anyone encountered this problem?

### Response

**René** commented on 09 Sep 2024

I have the same problem. With the following code, after calling SetText (by clicking on a button) the string is processed and saved to the variable but then it is not displayed in the editor. I could not reproduce this in blazorrepl though but on our live server it happens very often. I found a workaround which seems to work. I had to add the ExecuteAsync line you can see below in my code. <TelerikEditor @ref="My Editor " @bind-Value="TextVariable " Width="100%" Height="calc(100vh - 310px)" Class="bewa-editor-without-toolbar" ReadOnly="true" /> private async Task SetText () { ShowLoader=true; await InvokeAsync ( StateHasChanged ); TextVariable=await GetText(); ShowLoader=false; await InvokeAsync ( StateHasChanged ); // Workaround, to refresh the Editor await My Editor. ExecuteAsync ( new HtmlCommandArgs ( "insertHtml", string. Empty, true )); }

## Answer

**Hristian Stefanov** answered on 23 Feb 2024

Hi Ricardo, I have prepared an example of a working configuration that correctly updates the Editor's value in Iframe edit mode. Please use it as a reference. Update Editor's value: <TelerikTextArea @bind-Value="@TextDisplayModel.Text" /> <TelerikEditor @ref="@SummaryEditor" Class="rich-editor" EditMode="@EditorEditMode.Iframe" Value="@TextDisplayModel.Text" ValueChanged="@RichEditorValueChanges" ValueExpression="@((()=> TextDisplayModel.Text))"> </TelerikEditor> @code {
private TelerikEditor SummaryEditor { get; set; }
private DisplayModel TextDisplayModel=new DisplayModel() { Text="test" };

private void RichEditorValueChanges(string value)
{
// update the view-model
TextDisplayModel.Text=value;
}

public class DisplayModel
{
public string Text { get; set; }
}
} Let me know if you are still facing difficulties. Regards, Hristian Stefanov Progress Telerik

### Response

**Ricardo** commented on 12 Mar 2024

Hi Hristian! I'm terribly sorry for taking so long to comment back! I should have added that the TelerikTextArea element I mentioned is a child of the TelerikEditor component, it comes with it but is not visible. Sometimes, when I render my page, I cannot see the text on my TelerikEditor, but I can confirm via the DevTools window that the hidden TextArea was updated. Also, I update the view-model exactly has you suggested.

### Response

**Hristian Stefanov** commented on 13 Mar 2024

Hi Ricardo, I'm still not completely sure what your configuration looks like, except for the Editor. Could you clarify a bit more the issue here and provide a runnable reproduction so I can investigate further? Kind Regards, Hristian
