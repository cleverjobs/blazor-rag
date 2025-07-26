# Textbox Focus

## Question

**Vis** asked on 02 Dec 2021

Hi, I have modal popup and I need to add Textbox Focus in first field in the window on loading. Thanks, Vishnu Vardhanan

## Answer

**Apostolos** answered on 06 Dec 2021

Hello Vishnu, All our input components offer a FocusAsync method that lets you focus them programmatically. To implement the functionality, I'll provide the following step by step guidance: Add a reference to the textbox that you want to focus: <TelerikTextBox @ref="@TextboxRef" /> @code {
TelerikTextBox TextboxRef { get; set; }
} When you set the Window's Visible attribute to true and the popup renders, the Blazor framework will fire the OnAfterRenderAsync event. The OnAfterRenderAsync handler is the place to focus the desired textbox. Note that you will need a small delay ( await Task.Delay(300) ) to wait for the textbox JavaScript instance to initialize. The OnAfterRenderAsync event fires a lot of times during the page life cycle. You will need a boolean flag to detect when to focus the textbox (e.g. FocusFlag ). Set this flag to true when you set the Window Visible attribute to true. The following snippet demonstrates the above instructions. I also created this REPL example that you can use as reference. <TelerikWindow @bind-Visible="@WindowIsVisible" Width="250px"> <WindowTitle> Window Title </WindowTitle> <WindowContent> <label for="name"> Name </label> <br /> <TelerikTextBox @ref="@TextboxRef" Id="name"> </TelerikTextBox> <br /> <label for="email"> Email </label> <br /> <TelerikTextBox InputMode="email" Id="email"> </TelerikTextBox> </WindowContent> </TelerikWindow> <TelerikButton OnClick="@ToggleWindow"> Open Window and Focus TextBox </TelerikButton> @code {

bool FocusFlag { get; set; }=false;
bool WindowIsVisible { get; set; }
TelerikTextBox TextboxRef { get; set; } async Task ToggleWindow()
{
WindowIsVisible=!WindowIsVisible; if (WindowIsVisible)
{ FocusFlag=true; }
}

protected override async Task OnAfterRenderAsync(bool firstRender)
{ if (WindowIsVisible && FocusFlag) {
FocusFlag=false; await Task.Delay( 300 ); await TextboxRef.FocusAsync();
} await base.OnAfterRenderAsync(firstRender);
}
} Regards, Apostolos

### Response

**Vishnu** commented on 23 Dec 2021

Hi Team, Thanks for the update. Above is for the button click event. I need for Page Intialization and I have tried for Page Intialization and it's not working. Could please update on the same.

### Response

**Vishnu** commented on 04 Jan 2022

Could you please update on the same Thanks, Vishnu Vardhanan

### Response

**Karl** commented on 05 Dec 2023

The required 300ms delay seems like an unfortunate workaround. I would love to be able to focus elements without a noticeable pause. While I could likely shorten the delay (100-200ms) ... the best answer would require a solution that doesn't require delaying at all. Is there anything in the backlog tracking why this is necessary?

### Response

**Dimo** commented on 06 Dec 2023

@Karl - The Blazor framework doesn't expose events for components to know when they are actually rendered on the page. So you either need to track the HTML DOM tree in the browser with JavaScript MutationObserver, or use magic numbers for a delay. The second approach is a lot easier to implement, hence we suggest it.
