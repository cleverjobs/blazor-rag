# Scenario where Telerik Tooltip is hidden but default tooltip displays instead

## Question

**Dou** asked on 24 Jun 2021

I have a div which has a couple of buttons contained within it on the lower left corner. I have a TelerikTooltip with the target selector pointed to my div. Most of the time the tooltip works fine but I have found that if I move the mouse onto the div from the lower left corner where the buttons are, the TelerikTooltip shows up correctly while the mouse is over the buttons but when I move the mouse farther into the div and away from the buttons the TelerikTooltip gets hidden and a default tooltip is displayed. It behaves this way whether I use a title on the div or a template on the TelerikTooltip. Any way to keep the TelerikTooltip visible and avoid the default tooltip from being displayed?

### Response

**Marin Bratanov** commented on 26 Jun 2021

Could you add a simple runnable reproducible to your post (you can edit it)? This looks a lot like a layout behavior where the mouseover and mouseout events bubble up and fire on another element than the target of the tooltip so maybe the solution could be to target an element that is higher, so all mouseover events get to it regardless of where the mouse comes in from (whether it is over the buttons or not). At this point I'm only guessing though, only a reliable reproducible would show what's happening.

### Response

**Doug** commented on 28 Jun 2021

Marin, I attached a reproducible. If the mouse enters the red div from the side or the top you see the Telerik tooltip. If you enter from the bottom where the links (buttons) are you'll see the Telerik tooltip when you're over the links but if you move farther up, the Telerik tooltip goes away and the default tooltip is displayed.

## Answer

**Kristian** answered on 01 Jul 2021

Hi Doug, Thank you for the project. I was able to reproduce the problem and I confirm that this is a bug in the Tooltip. It seems that the tooltip thinks that the mouse is not over the target element anymore and that is why the element is hidden and the default tooltip is shown. I logged a bug report and added your vote to it: [https://feedback.telerik.com/blazor/1526222-telerik-tooltip-closes-before-leaving-the-target-element.](https://feedback.telerik.com/blazor/1526222-telerik-tooltip-closes-before-leaving-the-target-element.) You can follow the item so you can get updates when the status has changed. Unfortunately, I'm wasn't able to bypass the problem, so I can't give you a workaround right now. We will try to fix the problem as soon as possible. Regards, Kristian
