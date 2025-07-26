# Icon on Right of Text

## Question

**BobBob** asked on 09 Apr 2021

Is there any way to make the icon appear to right of the text instead of the left? I have tried messing with css to get this work, but as of now, have not had much luck. Would be nice if there was an IconPosition Setting on the button.

## Answer

**Bob** answered on 09 Apr 2021

Never mind I figured it out with the css, but a setting would still be nice. For those interested, I added a class to the button called iconRight and then added the following scss: button.iconRight { flex-direction: row-reverse; span.k-icon { margin: 0 -8px 0 8px; } }

### Response

**Hristian Stefanov** answered on 14 Apr 2021

Hi Bob, The easiest way to do that is by adding the TelerikIcon nested in the TelerikButton content. This way you can change the position of the icon however you want. The example snippet below demonstrates how to achieve that. It showcases two icons added on both sides of the text in the button. <TelerikButton>
<TelerikIcon Icon="check-outline" />
Check it
<TelerikIcon Icon="check-outline" />
</TelerikButton> Also, after your question, I have created this knowledge base article for changing icons position in a button and adding more than one icon inside, where anyone interested can see more details related to this case. Regards, Hristian Stefanov Progress Telerik
