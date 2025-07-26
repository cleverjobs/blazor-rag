# trigger tab key when enter key is pressed

## Question

**Ric** asked on 26 Jan 2021

As the title states, when a user presses enter in a textbox, how could I trigger the key down event for tab? Will this be a jsinvoke?

## Answer

**Marin Bratanov** answered on 27 Jan 2021

Hello Rick, The tricky part is that even if you create and dispatch a keypress event from code, the browser won't execute the action - that's a security feature. Imagine if the application could trigger key sequences that the browser acts on - causing Alt+F4 will close the browser and make the user lose their work. So, you can capture the enter event and then write some code to execute the desired action yourself. I made an example here for you that shows how you can focus the next input: @inject IJSRuntime _js

@* Move this script to a proper location, this hack here
lets it stay in the Blazor component to make the snippet easy to copy *@<script suppress-error="BL9992"> function invokeTabKey ( ) { // get the active element when Enter was pressed and // if it is an input, focus the next input // NOTE: You cannot really trigger the browser event - // even if you do, the browser won't execute the action // (such as focusing the next input) so you have to define the action var currInput=document.activeElement; if (currInput.tagName.toLowerCase()=="input" ) { var inputs=document.getElementsByTagName( "input" ); var currInput=document.activeElement; for ( var i=0; i <inputs.length; i++) { if (inputs[i]==currInput) { var next=inputs[i + 1 ]; if (next && next.focus) {
next.focus();
} break;
}
}
}
} </script> <div @onkeypress="@KeyPressHandler"> <TelerikTextBox> </TelerikTextBox> <br /> <br /> <TelerikTextBox> </TelerikTextBox> <br /> <br /> <TelerikTextBox> </TelerikTextBox> </div> @code{
async Task KeyPressHandler(KeyboardEventArgs e)
{
if(e.Key.ToLowerInvariant()=="enter")
{
await _js.InvokeVoidAsync("invokeTabKey");
}
}
} Regards, Marin Bratanov

### Response

**Rick** answered on 27 Jan 2021

Thanks Marin, this looks like it will be workable. I will give this a shot later today, I suspect it will do exactly what I need.
