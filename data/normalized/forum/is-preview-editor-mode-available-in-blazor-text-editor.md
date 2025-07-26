# Is Preview Editor Mode available in Blazor Text Editor

## Question

**Far** asked on 29 Jul 2022

We are trying to port a Web Forms project to Blazor and we have TelerikRadEditor (for ASP.NET) in one of our pages. The TelerikRadEditor offered three Editor Modes (Design, HTML and Preview). However in the Blazor TelerikEditor we were unable to find anything about the Preview mode. Can someone confirm whether there is a Preview mode in Blazor TelerikEditor? If yes, then how to enable it/add it.

## Answer

**Dimo** answered on 01 Aug 2022

Hello Farjad, There is an existing feature request about a Preview tool. You can vote and follow it to receive status updates. In the meantime, it is easy to implement such behavior with a custom Editor tool: @using Telerik.Blazor.Components.Editor

<TelerikEditor @bind -Value="@EditorValue" Tools="@EditorTools"> <EditorCustomTools> <EditorCustomTool Name="Preview"> <TelerikButton Icon="search" Title="Preview" OnClick="@ShowPreview"> </TelerikButton> </EditorCustomTool> </EditorCustomTools> </TelerikEditor> <TelerikWindow @bind-Visible="@WindowVisible" Modal="true" Width="70vw" Height="70vh"> <WindowTitle> Editor Value Preview </WindowTitle> <WindowActions> <WindowAction Name="Close" /> </WindowActions> <WindowContent> @( new MarkupString(EditorValue) ) </WindowContent> </TelerikWindow> @code { private string EditorValue { get; set; }=@"<p>Foo <strong>Bar</strong> Baz</p>"; private bool WindowVisible { get; set; } private List<IEditorTool> EditorTools { get; set; }=new List<IEditorTool>() { new Bold(), new Italic(), new Underline(), new CustomTool( "Preview" )
}; private void ShowPreview ( ) {
WindowVisible=true;
}
} Regards, Dimo
