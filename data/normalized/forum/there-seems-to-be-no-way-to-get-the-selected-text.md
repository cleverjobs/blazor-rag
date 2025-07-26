# There seems to be no way to get the selected text

## Question

**Bla** asked on 09 Nov 2020

I am attempting to create a custom tool to add code formatting to selected text. The format command does not work with anything outside the predefined list of drop down options. If I were able to get the selected text I could simply modify that with the wrapping, but it seems there is no way to do that in the Blazor version, unless I am missing something? Any help would be greatly appreciated.

## Answer

**Svetoslav Dimitrov** answered on 12 Nov 2020

Hello Blane, You could get the selected text using some JavaScript methods. Below I have made 2 examples, which are based on the Edit mode of the Editor: Div Edit mode: C#: @using Telerik.Blazor.Components.Editor

@inject IJSRuntime js <TelerikEditor Tools="@Tools" @bind-Value="@TheEditorContent" EditMode="@EditorEditMode.Iframe"> <EditorCustomTools> <EditorCustomTool Name="GetSelectedText"> <TelerikButton OnClick="@GetSelectedText"> Get selected text </TelerikButton> </EditorCustomTool> </EditorCustomTools> </TelerikEditor> Selected text: @SelectedText

@code {
string TheEditorContent { get; set; }=" <h1> Lorem ipsum </h1> <p> Dolor sit amet. </p> ";
List <IEditorTool> Tools { get; set; }
public string SelectedText { get; set; }

protected override Task OnInitializedAsync()
{
Tools=new List <IEditorTool> (EditorToolSets.Default);

// register the custom tool for the toolbar - it uses the Name parameter from the markup
Tools.Add(new CustomTool("GetSelectedText"));

return base.OnInitializedAsync();
} async Task GetSelectedText()
{
SelectedText=await js.InvokeAsync <string> ("getSelectedText");
} } JS: function getSelectedText ( ) { return window.getSelection().toString();
} IFrame Edit mode: C#: @using Telerik.Blazor.Components.Editor

@inject IJSRuntime js

<TelerikEditor Tools="@Tools" @bind-Value="@TheEditorContent" EditMode="@EditorEditMode.Iframe">
<EditorCustomTools> <EditorCustomTool Name="GetSelectedText">
<TelerikButton OnClick="@GetSelectedText">Get selected text</TelerikButton>
</EditorCustomTool> </EditorCustomTools>
</TelerikEditor>

Selected text: @SelectedText

@code { string TheEditorContent { get; set; }="<h1>Lorem ipsum</h1><p>Dolor sit amet.</p>";
List<IEditorTool> Tools { get; set; } public string SelectedText { get; set; } protected override Task OnInitializedAsync ( ) {
Tools=new List<IEditorTool>(EditorToolSets.Default); // register the custom tool for the toolbar - it uses the Name parameter from the markup Tools.Add( new CustomTool( "GetSelectedText" )); return base.OnInitializedAsync();
} async Task GetSelectedText ( ) {
SelectedText=await js.InvokeAsync<string>( "getSelectedText" );
} } JS: function getSelectedText ( ) { var editorIframe=document.querySelector( ".k-editor iframe" ); return editorIframe.contentDocument.getSelection().toString();
} I hope this helps you move forward with your application. If I can be of any further assistance do not hesitate to follow up on this thread. Regards, Svetoslav Dimitrov

### Response

**Blane Bunderson** answered on 16 Nov 2020

Svetoslav, Thank you, this solution has gotten me pretty much there. The only issue I am having is with edge cases such as single letter selection. Is there a way to get the index or cursor position of the selection as well or is this limited to text matching to find where the selection is in the document string itself? Thanks

### Response

**Svetoslav Dimitrov** answered on 18 Nov 2020

Hello Blane, Selecting a single letter seems to work for me as expected when using the code snippet (for the Iframe edit mode) below. As an attached file I have sent a screen recording so that we are on the same page and I see if I am missing something. Regards, Svetoslav Dimitrov

### Response

**Blane Bunderson** answered on 18 Nov 2020

Svetoslav, That zip file does not work for me. Windows says it is invalid when attempting to open and that its empty when attempting to extract. Not sure what the issue is. Anyhow, I think I did not describe the issue clearly enough. Yes I am able to get the selected text when the selection is one letter, however the issue is matching that selection to the bound data in the editor in order to make changes to it. For instance, let's say the following is the bound text: "Lorem ipsum dolor." If my selection was the last letter of the second word, I would get "m" as the result. I want to make the selections font red. If I try to find the selection in the document without knowing the actual index, it will return the last letter of the first word because it is the first instance of the selection (assuming the use of FirstOrDefault). Therefore, the wrong text will have the action done upon it. What I am asking is if there is a way to get the index so that I don't have to rely only on string matching and hoping that there is only one instance of the selection in the text. Thank you for the assistance.

### Response

**Svetoslav Dimitrov** answered on 23 Nov 2020

Hello Blane, As an attached file, you could see a demo project modified so that It uses a custom tool to make the color of the text red. When I select a text (or a single character) it seems to work for me as expected and make the font-color red. Could you run it locally and see if this works as expected for you? If it does you could compare it against your own code and see if any difference causes the issue. If it does not, could you modify the application so that I could reproduce the issue and investigate it? If I missed something or I misunderstood the question, let me know. Regards, Svetoslav Dimitrov

### Response

**Blane Bunderson** answered on 23 Nov 2020

Svetoslav, Just for your information, your zips are unable to be opened with standard windows extraction methods. We had to use 3rd party software to open these zips, unlike the zips in all other forum posts. Not sure why that is, but just wanted to let you know. As mentioned above in the original post, my goal is not to make the text red. I am not using the Formatting commands as you used. This was just an example to help you understand the flow of the issue that occurs with the single character selection and text matching. In the original post I made clear that I was performing formatting outside of the available format commands available by default. I will try to make the issue clear all in one post now: My goal here (as mentioned in the original post) is to add code-style formatting to a text selection. To make this clear, an example of this would be to take the given text you provided in the sample, "<h1>Lorem ipsum</h1><p>Dolor sit amet.</p>", and select a part of the text and wrap it in code tags. If my selection was "ipsum", this would result with "<h1>Lorem <code>ipsum</code></h1><p>Dolor sit amet.</p>". This works well with the sample code you provided directly after my original post when the selection is unique within the TheEditorContent string property bound as the content to the editor. In the case of a unique selection, string matching works fine and I can find the selection in the data and do a string.Replace() to add the wrapping. My issue is this, when the selection is not unique, string matching is not enough to find the selected text in the string property bound as content to the editor. If for example I selected, as mentioned in my last reply, the last letter of the second word, the 'm' in "ipsum", and tried to find the selection in the content property, my string matching would return the last letter of the first word, the 'm' in "Lorem". The result I would have expected would be "<h1>Lorem ipsu<code>m</code></h1><p>Dolor sit amet.</p>", however the result I end up with instead would be "<h1>Lore<code>m</code> ipsum</h1><p>Dolor sit amet.</p>". Possibly it is the single character that is causing confusion. Here is an example with whole words. If the bound content was "<h1>Lorem ipsum</h1><p>Lorem ipsum.</p>" and I selected the second occurence of "ipsum", my string matching would return the first occurence of "ipsum" instead which would cause the wrong selection to be wrapped in code tags and thus formatting to be applied to the wrong text. My expected result would be "<h1>Lorem ipsum</h1><p>Lorem <code>ipsum</code>.</p>", but the result would actually be "<h1>Lorem <code>ipsum</code></h1><p>Lorem ipsum.</p>". Unfortunately, the only allowed file types for attaching are .jpg, .jpeg, gif, and .png, so I cannot modify and send back the sample, but I will attach a screenshot of the adjusted index page. I hope I have made this clear. The bottom line is that I would like to know if there is a way to get the actual index of the selected text. Thanks, Blane

### Response

**Blane Bunderson** answered on 23 Nov 2020

Apologies, I see now where the confusion with the red text in my last post came from as I did not resolve that line of thought.

### Response

**Svetoslav Dimitrov** answered on 25 Nov 2020

Hello Blane, Thank you for the additional explanation you have provided and sorry it took me as long to understand it. Getting the index of the character would require a slight update to the JavaScript function. The anchorOffset would return the index of the character and it is 0 based, whereas the focusOffset would return the end index. Below, you can see a revised example: C#: @using Telerik.Blazor.Components.Editor

@inject IJSRuntime js

<TelerikEditor Tools="@Tools" @bind-Value="@TheEditorContent" EditMode="@EditorEditMode.Iframe" @ref="EditorRef">
<EditorCustomTools>
<EditorCustomTool Name="GetSelectedText">
<TelerikButton OnClick="@GetSelectedText">Get selected text</TelerikButton>
</EditorCustomTool>

<EditorCustomTool Name="ImportantFragment">
<TelerikButton OnClick="@MarkImportant" Icon="@IconName.Star"></TelerikButton>
</EditorCustomTool>
</EditorCustomTools>
</TelerikEditor> Selected text starting index: @startCharIndex
<br />
End index: @endCharIndex @code { string TheEditorContent { get; set; }="<h1>Lorem ipsum</h1><p>Dolor sit amet.</p>";
List<IEditorTool> Tools { get; set; }
TelerikEditor EditorRef { get; set; } public int startCharIndex { get; set; } public int endCharIndex { get; set; } protected override Task OnInitializedAsync ( ) {
Tools=new List<IEditorTool>(EditorToolSets.Default); // register the custom tool for the toolbar - it uses the Name parameter from the markup Tools.Add( new CustomTool( "GetSelectedText" ));
Tools.Add( new CustomTool( "ImportantFragment" )); return base.OnInitializedAsync();
} async Task MarkImportant ( ) { await EditorRef.ExecuteAsync( new FormatCommandArgs( "foreColor", "red" ));
} async Task GetSelectedText ( ) { startCharIndex=await js.InvokeAsync<int>( "getSelectedTextStartIndex" );
endCharIndex=await js.InvokeAsync<int>( "getSelectedTextEndIndex" ); }
} JS: function getSelectedTextStartIndex ( ) { var editorIframe=document.querySelector( ".k-editor iframe" ); var charIndex=editorIframe.contentDocument.getSelection().anchorOffset; return charIndex;
} function getSelectedTextEndIndex ( ) { var editorIframe=document.querySelector( ".k-editor iframe" ); var charIndex=editorIframe.contentDocument.getSelection().focusOffset; return charIndex;
} I hope this would help you move forward with your application. Regards, Svetoslav Dimitrov

### Response

**Blane Bunderson** answered on 25 Nov 2020

Svetoslav, Thank you for the additional help. Unfortunately, these functions only return the indices of the character within the line. It does not help to find the index of the selection within the document. What I am looking for is a way to find the precise user selection in the overall document, not the line, when there are duplicates of the selection present. Thanks, Blane

### Response

**Svetoslav Dimitrov** answered on 27 Nov 2020

Hello Blane, I believe we completely understood the end result you are looking for. In order to achieve it, I would suggest you use the insertHtml command for the Editor and get that plain selection from the browser. Below, you can see a modified version of the example from my previous posts: C#: @using Telerik.Blazor.Components.Editor

@inject IJSRuntime js

<TelerikEditor Tools="@Tools" @bind-Value="@TheEditorContent" EditMode="@EditorEditMode.Iframe" @ref="EditorRef">
<EditorCustomTools> <EditorCustomTool Name="InsertCode">
<TelerikButton OnClick="@InsertCode" Icon="@IconName.CodeSnippet">Insert Code From Plain Selection</TelerikButton>
</EditorCustomTool> </EditorCustomTools>
</TelerikEditor>

Selected text: @SelectedText

@code { string TheEditorContent { get; set; }="<h1>Lorem ipsum</h1><p>Dolor sit amet.</p><div style='color: red'>Dolor sit amet.</div><p>Dolor sit amet.</p>";
List<IEditorTool> Tools { get; set; }
TelerikEditor EditorRef { get; set; } public string SelectedText { get; set; } protected override Task OnInitializedAsync ( ) {
Tools=new List<IEditorTool>()
{ new Bold(), new ViewHtml(), new CustomTool( "InsertCode" ),
}; return base.OnInitializedAsync();
} async Task InsertCode ( ) {
SelectedText=await js.InvokeAsync<string>( "getSelectedText" ); await EditorRef.ExecuteAsync( new HtmlCommandArgs( "insertHtml", $"<code> {SelectedText} </code>", true ));
} } JavaScript: function getSelectedText ( ) { var editorIframe=document.querySelector( ".k-editor iframe" ); return editorIframe.contentDocument.getSelection().toString();
} I hope this would help you move forward with your application. Regards, Svetoslav Dimitrov

### Response

**Blane Bunderson** answered on 27 Nov 2020

Svetoslav, Unfortunately, I have other logic I must apply to the selection, finding the beginning and end of the paragraph to automatically extend the selection for example, and I also need to add tags other than just "<code>". The one and only roadblock I have in completing this is discerning between two items when the selection is not unique. I really just need to be able to find the index of the selection in the overall document. Is it safe to assume that there is currently no way of doing this? Blane

### Response

**Svetoslav Dimitrov** answered on 01 Dec 2020

Hello Blane, I believe I understood the desired behavior, you would like to implement a Word-like behavior. Such a solution is a custom one and the Editor does not provide a built-in way to achieve it. The selection exists only in the browser (the selection object) and should be altered with JavaScript. You could see the notes from this Knowledge-Based article. At this time, I could not offer a different solution which the Editor can perform as a built-in one. Regards, Svetoslav Dimitrov
