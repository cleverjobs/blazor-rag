# Display TelerikTooltip without Hover or Click

## Question

**RobRob** asked on 26 May 2022

Hi, I would like to use a TelerikTooltip as validation message container, so that the user can click to close the tooltip after reading the message. Can the TelerikTooltip be made to display immediately and then respond to clicks as normal afterwards?

## Answer

**Rob** answered on 30 May 2022

I figured it out and managed to trigger the tooltip to pop-up using JSInterop call at the approprate time in my C# code. function trigger(elementId, delay){ window.setTimeout( function ( ) { document.getElementById(elementId).click();
}, delay) } It's not elegant but it works for now.

### Response

**Dimo** commented on 31 May 2022

Hi Rob, we have programmatic ToolTip display in our pipeline.
