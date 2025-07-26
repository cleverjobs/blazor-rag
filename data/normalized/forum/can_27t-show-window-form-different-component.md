# Can't show window form different component

## Question

**Rob** asked on 22 Oct 2020

Window-component: <TelerikWindow @bind-Visible="@_visible"> <WindowTitle>Window</WindowTitle> </TelerikWindow> <TelerikButton OnClick="Show">Toggle</TelerikButton> @code { private bool _visible; public void Show() { _visible=!_visible; } } Other component: <WindowComponent @ref="_windowComp"/> <TelerikButton OnClick="()=> _windowComp.Show()">Show</TelerikButton> @code { private WindowComponent _windowComp; } Nothing happens when pressing the "Show"-button, although debugging clearly shows that the Show()-method is executed.

## Answer

**Svetoslav Dimitrov** answered on 23 Oct 2020

Hello Robert, You should call a StateHasChanged() at the end of the show method (like the example I added below). The reason is that Blazor does not know what that method does and if it should render the HTML anew. Code snippet: public void Show ( ) {
_visible=!_visible; StateHasChanged(); } Regards, Svetoslav Dimitrov
