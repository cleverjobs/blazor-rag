# Line Spacing in Editor

## Question

**Mat** asked on 28 Apr 2022

I am not having any luck tracking down a line spacing option in Editor. For example, bullets are spread too far apart.

## Answer

**Dimo** answered on 03 May 2022

Hello Matt, The list items show with some empty space in-between, because the Editor's ProseMirror engine always inserts a <p> tag inside every <li> tag. I agree that this should not be necessary, but this is how the engine handles block containers. It is possible to hack the engine, but this will break other features. So my suggestions are: Remove the <p> tags via string manipulation of the submitted Editor value. Remove the empty space inside the Editor itself via CSS: If you are using the Div EditMode, add the CSS to the web page normally. If you are using the Iframe EditMode, inject the CSS to the Editor's iframe. Here is an example that shows both options. @inject IJSRuntime js <p> Div mode - the styling of the Editor content depends on the web page </p> <TelerikEditor @bind-Value="@EditorValue" EditMode="@EditorEditMode.Div" Class="no-list-space" /> <style>.no-list-space li> p { margin: 0;
} </style> <p> Iframe mode - the styling of the Editor content depends on the separate web document </p> <TelerikEditor @bind-Value="@EditorValue" EditMode="@EditorEditMode.Iframe" Class="@EditorClass" /> <!-- The suppress-error attribute allows script tags inside Razor components. --> <!-- Move this script to a proper place in production environment. --> <script suppress-error="BL9992"> // function injectEditorStyles ( editorClass, editorStyles ) { var doc=document.querySelector( "." +editorClass + " .k-iframe" ).contentWindow.document; var head=doc.querySelector( "head" ); var style=doc.createElement( "style" );
style.type="text/css"; var css=editorStyles;
style.appendChild(doc.createTextNode(css));
head.appendChild(style);
} // </script> <p> <TelerikButton OnClick="@RemovePTags"> Get Editor Value Without P Tags </TelerikButton> </p> <TelerikTextArea @bind-Value="@EditorValueNoP" /> @code {
string EditorValue { get; set; }=" <ul> <li> <p> foo </p> </li> <li> <p> bar </p> </li> </ul> ";
string EditorStyles { get; set; }="li> p { margin: 0; }";
string EditorClass { get; set; }="no-list-space";

string EditorValueNoP { get; set; }

void RemovePTags()
{
EditorValueNoP=EditorValue.Replace(" <li> <p> ", " <li> ").Replace(" </p> </li> ", " </li> ");
}

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
await js.InvokeVoidAsync("injectEditorStyles", EditorClass, EditorStyles);
}

await base.OnAfterRenderAsync(firstRender);
}
} On a side note, Shift+Enter renders a <br /> tag in the Editor, that is why there is no new bullet. This is expected. Regards, Dimo Progress Telerik

### Response

**Matt** commented on 03 May 2022

Thanks Dimo, I figured there was a way to make it happen, just not exposed. I'll see what I can do to make it work. FYI, the Shift+Enter was mostly an example for my users, but good to confirm.
