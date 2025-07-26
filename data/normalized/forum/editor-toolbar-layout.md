# Editor toolbar layout

## Question

**Ant** asked on 29 May 2024

I have added 3 Custom buttons to my toolbar in the editor. I would like to use Spacer similar to ToolbarSpacer and would like the clear and save comment buttons to be right justified. How would I do that or if I can't, can it be added?

### Response

**Anthony** commented on 03 Jun 2024

Thanks Hristian! I was able to get it working with: .custom-button-align .k-toolbar-item:nth-child(4){
margin-left: auto;
} You led me in the right direction 😀

## Answer

**Hristian Stefanov** answered on 31 May 2024

Hi Anthony, If you add the built-in tools manually, a ToolbarSpacer does not seem necessary, as you can easily adjust the buttons positioning via some CSS. Here is an example of how to position the three custom buttons on the right using the "margin-left" style: @using Telerik.Blazor.Components.Editor
@using EditorNS=Telerik.Blazor.Components.Editor; <style>.k-toolbar-item:first -of-type { margin-left: auto;
} </style> <TelerikEditor Tools="@Tools" @bind-Value="@TheEditorContent"> <EditorCustomTools> <EditorCustomTool Name="AddFile"> <TelerikButton OnClick="@AddFile" Icon="@SvgIcon.FileAdd" /> </EditorCustomTool> <EditorCustomTool Name="Clear"> <TelerikButton OnClick="@Clear"> Clear </TelerikButton> </EditorCustomTool> <EditorCustomTool Name="Save"> <TelerikButton OnClick="@SaveComment"> Save Comment </TelerikButton> </EditorCustomTool> </EditorCustomTools> </TelerikEditor> @code {
private string TheEditorContent { get; set; }=" <h1> Lorem ipsum </h1> <p> Dolor sit amet. </p> ";
private List <IEditorTool> Tools { get; set; }

protected override Task OnInitializedAsync()
{
Tools=new List <IEditorTool> ();
Tools.Add(new EditorNS.Bold());
Tools.Add(new EditorNS.Italic());
Tools.Add(new EditorNS.Underline());

// register the custom tool for the toolbar - it uses the Name parameter from the markup
Tools.Add(new CustomTool("AddFile"));
Tools.Add(new CustomTool("Clear"));
Tools.Add(new CustomTool("Save"));

return base.OnInitializedAsync();
}

private async Task AddFile()
{
// call the necessary logic here, such as adding a file
}

private async Task Clear()
{
// call the necessary logic here, such as clearing the content
}

private async Task SaveComment()
{
// call the necessary logic here, such as saving the content
}
} Please run and test it to see the result. Let me know if this is what you are looking for. Regards, Hristian Stefanov Progress Telerik
