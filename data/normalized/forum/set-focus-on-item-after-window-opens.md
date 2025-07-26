# Set focus on item after window opens

## Question

**BobBob** asked on 24 Sep 2020

I am trying to set focus on a TelerikTextBox when a window is opened, but it would appear the call to js is being made before the window actually opens so the element is null. Is there anyway to wait until the window is actually open and then call js to set focus on the textbox? private async Task NewTicketClick() { newTicket=new NewTicketViewModel { CreatedBy=userId, Owner=userId }; showNewTicketWindow=true; await jSRuntime.InvokeVoidAsync("focusInputFromBlazor", new[] { ".defaultFocus" }); }

## Answer

**Marin Bratanov** answered on 25 Sep 2020

Hi Bob, If you have worked with other JS front-end before, you might have used a setTimeout(someFunction, 0) workaround to let some rendering happen before your function is executed. In Blazor, there are similar needs to wait for something to render before you can actually interact with its DOM - and focus requires JS interop, there is no "native" way to do it. So, you need to wait for the new markup to render (be that a window or something else) and a simple await Task.Delay(30) usually does the trick. Below is a small example that showcases this, and you may want to review (and it it is to your liking, Vote for and Follow) this request. @inject IJSRuntime jSRuntime

<TelerikButton OnClick="@ShowWnd">Show Window</TelerikButton>

<TelerikWindow @bind-Visible="@wndVisible" Modal="true">
<WindowTitle>The dialog</WindowTitle>
<WindowContent>
<TelerikTextBox Class="defaultFocus"></TelerikTextBox>
</WindowContent>
</TelerikWindow>

@code{ bool wndVisible { get; set; } async Task ShowWnd ( ) {
wndVisible=true; await Task.Delay( 30 ); await jSRuntime.InvokeVoidAsync( "focusInputFromBlazor", new [] { ".defaultFocus" });
}
} Regards, Marin Bratanov

### Response

**Bob** answered on 25 Sep 2020

That worked and I am no longer getting a javascript error, however the textbox is not focusing. Even if I go into dev tools after the page has rendered and try to do .focus() on the text box it doesn't take focus. Is there something I have to do special to set focus on a Telerik Textbox?

### Response

**Marin Bratanov** answered on 25 Sep 2020

Hi Bob, There is nothing special for the TelerikTextbox, and the idea I can offer right now is to increase the timeout, try 50 or 100 milliseconds. If that does not help, I suggest you open a support ticket and send me a modified version of my snippet (please keep it runnable) that demonstrates the problem so I can have a look and avoid guessing. Regards, Marin Bratanov
