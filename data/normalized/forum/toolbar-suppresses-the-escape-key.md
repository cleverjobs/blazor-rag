# Toolbar suppresses the Escape key

## Question

**Vit** asked on 06 May 2025

Hello Telerik, In my Blazor Hybrid application, I have a toolbar with a textbox in it; I want to add some hotkeys to it: on pressing Enter, process the textbox value, and in pressing Escape, revert the textbox value to the default. The problem is with the toolbar. I have this piece of code: @code {
private void OnKeyUp(KeyboardEventArgs args)
{
Debug.WriteLine("key up: " + args.Code);
}
} <TelerikToolBar> <ToolBarTemplateItem> <div @onkeyup="OnKeyUp" tabindex="-1"> <TelerikTextBox Value="Some Value" /> </div> </ToolBarTemplateItem> </TelerikToolBar> It works perfectly for any pressed key, including Enter - except the Escape key. When I press Escape, the textbox loses focus, and I don't get the keyboard event. I tried the keydown and keypress events, too. In contrast, when I press Tab, I get the keydown event before the textbox loses focus (but no keyup event). If I place the textbox directly on the page, without the toolbar, the keydown and keyup events work correctly, and I get the events for the Escape key. Apparently, TelerikToolBar is doing... something. Is there a way to: a) make the toolbar less aggressive and let me handle the keydown/keyup events, or b) detect the Escape and Enter keyclicks from the TelerikTextBox component, to avoid the need for handling the javascript events? As a curiosity, when focussed on this text box, try pressing Win and then Escape. It produces this sequence of events: "keydown MetaLeft" -> "focusout" -> "focusin" -> "keyup Escape". Yes, you get the Escape event, and the focus returns to the textbox. Thank you.

## Answer

**Nadezhda Tacheva** answered on 08 May 2025

Hi Vitaly, Indeed, as part of the keyboard navigation implementation of the Toolbar, we are preventing the propagation of the onkeydown event when Esc is pressed. To work this behavior around and detect the Esc press, you can use this approach: [https://blazorrepl.telerik.com/wfYzEClR32bBBWjt07.](https://blazorrepl.telerik.com/wfYzEClR32bBBWjt07.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Vitaly** commented on 08 May 2025

Thank you! I can confirm that this workaround works. I'll just leave it here for future reference: <TelerikToolBar> <ToolBarTemplateItem> <div @onkeyup="OnKeyUp" onkeydown="event.stopPropagation()"> <TelerikTextBox Value="Some Value" /> </div> </ToolBarTemplateItem> </TelerikToolBar> @code {
private void OnKeyUp(KeyboardEventArgs args)
{
Console.WriteLine("TextBox in Toolbar - key up: " + args.Code);
} }

### Response

**Nadezhda Tacheva** commented on 09 May 2025

Thank you for confirming, Vitaly! I am glad I was able to help.
