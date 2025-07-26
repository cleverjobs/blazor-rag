# Custom tools rendered each time new

## Question

**Hol** asked on 11 Jan 2023

Hi, I have a TelerikEditor with additional custom tools: In the razor-file: <TelerikEditor @bind-Value="@myContent" Toosl="@tools">
<EditorCustomTools>
@* Custom tools here *@</EditorCustomTools>
</TelerikEditor> in the code behind file: private List <IEditorTool> tools { get; set; }=new List<IEditorTool>(); protected override Task OnInitializedAsync ( ) {
tools=EditorToolSets.All;
tools.Add( new CustomTool( "MyTools" ); return base.OnInitializedAsync();
} At this point, all works as expected. But when I navigate to another page in my wasm App and then navigate back to the page with the editor, the custom tools is renderd twice. If I navigate away and back to the page once more, the custom tool is now renderd three times. If I do it again: four times the custom tool .... I tried: tools=new(); as first line in OnInitializedAsync, but with the same result. I think it is a rendering problem. I checked tools.Count at the beginning of OnInitializedAsync and it is alway 0. Any suggestions? :-)

## Answer

**Svetoslav Dimitrov** answered on 16 Jan 2023

Hello Holger, My best suggestion would be to add the custom tools with the initialization of the tools collection: public List <IEditorTool> Tools { get; set; }=new List<IEditorTool>()
{ new CustomTool( "ColorTools" ), new CustomTool( "CleanFormattingTool" ), new CustomTool( "InsertVideo" ), new CustomTool( "InsertHtmlTools" )
}; or provide a new collection in the OnInitialized: public List<IEditorTool> ToolCollection { get; set; } protected override void OnInitialized ( ) {
ToolCollection=new List<IEditorTool>()
{ new CustomTool( "ColorTools" ), new CustomTool( "CleanFormattingTool" ), new CustomTool( "InsertVideo" ), new CustomTool( "InsertHtmlTools" )
}; base.OnInitialized();
} By using both approaches everything seems to render as expected. As an attached file you can see a demo WASM application where the second one is implemented. Can you try the application and the approach on your own and get back to me if it works as expected for you too? Regards, Svetoslav Dimitrov
