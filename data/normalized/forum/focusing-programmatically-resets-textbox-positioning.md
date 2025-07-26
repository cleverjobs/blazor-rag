# Focusing Programmatically Resets Textbox Positioning

## Question

**JoeJoe** asked on 14 Apr 2025

I have a scenario where I need to shift the position of TelerikTextBox's `k-input-inner` element using the CSS properties`top` and `left`. This works fine until I use FocusAsync() to programmatically focus on the textbox. This causes the textbox to reset its position and disregard the position styling. Please see the REPL link below. To reproduce, click on the "Focus" button and observe how the placeholder shifts. [https://blazorrepl.telerik.com/wTkelobC56YIRoZL13](https://blazorrepl.telerik.com/wTkelobC56YIRoZL13) To note, the desired view is with the input text position shifted from the original position like so: Hitting tab reverts it to the original positioning which is undesirable:

## Answer

**Tsvetomir** answered on 15 Apr 2025

Hello Joe, Thank you for the provided information about your scenario. The encountered behavior seems to be browser-related, due to the different position of the input field, which makes it not fully visible. In short, focusing the input programmatically moves the focus to the input and "scrolls" the browser into the current view. In other words, the browser ensures that the whole input field is fully visible on focus. I hope this sheds some light on the behavior. To achieve the desired outcome requires a different CSS approach that relies on the input padding. To assist you further, I've updated the provided REPL - [https://blazorrepl.telerik.com/czEobTuW38rrAuTB09](https://blazorrepl.telerik.com/czEobTuW38rrAuTB09) I hope this serves you well and helps you to move forward with your project. Regards, Tsvetomir
