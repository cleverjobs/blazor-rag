# Hide/Show toolbar in editor

## Question

**Hol** asked on 12 Jan 2023

Hello, I want to provide two modes for editing with the editor. One full-featured editor with all tools (EditorToolSets.All) and one mode with none or only custom tools and I want to switch between the modes. So I tried somethink likse this: private List <IEditorTool> tools { get; set; }=new List<IEditorTool>(); protected override Task OnInitializedAsync ( ) {
tools=EditorToolSets.All;
tools.Add( new CustomTool( "MyTool" );
} private void SwitchModel ( MyMode mode ) { if (mode==MyMode.Full)
{
tools=EditorToolSets.All;
} if (mode==MyMode.None)
{
tools=Clear;
}
} If I switch from MyMode.Full to MyMode.None, all tools disappers. But if I switched back, nothing happens. How can I get the tools back? :-)

## Answer

**Svetoslav Dimitrov** answered on 17 Jan 2023

Hello Holger, We have prepared a demo code snippet where you can see a sample implementation of the behavior you are after, refer to this REPL link. Can you test it and get back to us if it works as expected for you? Regards, Svetoslav Dimitrov

### Response

**Holger** commented on 24 Jan 2023

Ahh.. two Editors :-) I tried it with one. But your solution with two editors worked for me as well. Thanks
