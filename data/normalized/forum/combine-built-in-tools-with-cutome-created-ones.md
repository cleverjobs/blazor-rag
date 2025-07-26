# Combine built in tools with cutome created ones

## Question

**Oma** asked on 31 Jan 2024

Hi, Using the editor, is it possible to combine the built-in tools and the custom ones? I would like to use the Tools="EditorToolSets.All" as well as the @ToolCollection that I created at the same time. Regards, Omar

## Answer

**Omar** answered on 01 Feb 2024

Hello Dimo, I struggled to locate instructions on incorporating a custom tool button onto the default toolbar. It's possible that I overlooked something in the documentation. My objective is to include a custom button on the "EditorToolSets.All" toolbar, allowing users to easily insert a video link. Fortunately, I've now managed to resolve this issue: <TelerikEditor @ref="Editor" Tools="@ToolCollection" Height="300px" @bind-Value="@Description"> </TelerikEditor> protected override async void OnInitialized () {
ToolCollection=new List<IEditorTool>(EditorToolSets.All); // create a tool group var UndoRedoGroup=new EditorButtonGroup( new EditorNS.Undo(), // add individual tools to the group new EditorNS.Redo()
);
ToolCollection.Add(UndoRedoGroup);
EditorButtonGroup Video=new EditorButtonGroup();
ButtonTool bt=new ButtonTool();
bt.Title="Insert video";
bt.OnClick=EventCallback.Factory.Create<MouseEventArgs>( this, ExecuteInsertVideo);
bt.Icon=SvgIcon.VideoExternal;
Video.Tools.Add(bt);
ToolCollection.Add(Video);
} Could you guide me to the section in the documentation that explains how to add a custom button to the predefined editor toolbar? Regards, Omar

### Response

**Dimo** commented on 02 Feb 2024

See Telerik Blazor Editor Custom Tools. You need the CustomTool("tool-name") constructor. ButtonTool is a base class that is not meant to be used directly for custom tools.

### Response

**Omar** commented on 02 Feb 2024

The above code that I wrote worked very well.

### Response

**Dimo** answered on 31 Jan 2024

Hi Omar, Yes, it is possible to add Editor tools to a predefined collection, or also reoder tools in a predefined collection. Is our documentation hard to navigate or to find the required information? Let me know if you find any difficulties while using it. Regards, Dimo Progress Telerik
