# TelerikWindow - Possible to move location of action buttons?

## Question

**Ryn** asked on 09 Jan 2024

I have seen the example of using a custom CSS style to modify the appearance of the TelerikWindow action buttons (border / background / color). Is it possible to change the location of the action buttons to be at the bottom of the window (preferably just the buttons, and not the whole title bar)?

## Answer

**Rynhardt** answered on 10 Jan 2024

I've got it to work for a fixed size TelerikWindow - e.g.: <TelerikWindow Size="@ThemeConstants.Window.Size.Large" , by declaring and using the following CSS style (making sure to set the background-color to match the one used by '.k-window-titlebar'): .my-title-button.k-window-titlebar button { position: relative!important; top: 100px!important; left: 12px!important; background-color: #7f959f!important;
} But if the window size is not fixed / is dynamic, is there a way to get it to work then?

### Response

**Dimo** answered on 11 Jan 2024

@Rynhardt - the overall approach is a bit hackish. Why do you need to move the Window actions? Instead, you can consider custom commands that work with the Window parameters and API instead (example below). If you prefer the current approach, then use bottom instead of top and absolute instead of relative. <TelerikButton OnClick="@( ()=> WVisible=!WVisible )">Toggle Window</TelerikButton> <TelerikWindow @bind-Visible="@WVisible" State="@WState"> <WindowTitle> Window </WindowTitle> <WindowContent> Content <br /> Content <br /> Content <br /> Content <br /> Content <br /> Content <br /> Content <br /> Content <br /> <TelerikButton OnClick="@OnMaxButtonClick"> Maximize </TelerikButton> <TelerikButton OnClick="@OnRestoreButtonClick"> Restore </TelerikButton> <TelerikButton OnClick="@OnClоseButtonClick"> Close </TelerikButton> </WindowContent> </TelerikWindow> @code {
bool WVisible { get; set; }

WindowState WState { get; set; }

private void OnMaxButtonClick ( ) {
WState=WindowState.Maximized;
}

private void OnRestoreButtonClick ( ) {
WState=WindowState.Default;
}

private void OnClо seButtonClick ( ) {
WVisible=false;
}
}
