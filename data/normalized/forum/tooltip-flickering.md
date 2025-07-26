# Tooltip Flickering

## Question

**SamSam** asked on 14 Aug 2023

I'm using the Blazor Tooltip inside Scheduler ItemTemplates. The content of my Tooltips is defined inside a Template. Intermittently, the tooltip is flickering very fast as the mouse hovers between Scheduler events. I've not observed any patterns to the flickering behavior, as it sometimes ceases entirely. In the past, when using Javascript to render rich content in tooltips, I've added a delay, but that doesn't appear to be an option with this control. Any recommendations or workarounds to address this behavior?

### Response

**Víctor** commented on 14 Aug 2023

Not only in scheduler, but in many places the tooltip flikers...

### Response

**Sam** commented on 14 Aug 2023

You're correct. I just saw it happen with my Tooltip that is tied to a grid command button.

## Answer

**Hristian Stefanov** answered on 15 Aug 2023

Hi all, I'm pasting here the answer I gave in Sam's private ticket so the community can benefit from it.=======It seems that the described flickering behavior appears due to a missing functionality - currently, the tooltip does not remain visible if it shows somewhere where the mouse cursor is. In the meantime, you can use the following CSS to avoid the flickering: <style>.no-flicker { pointer-events: none;
} </style> <TelerikTooltip TargetSelector=".tooltip-target" Class="no-flicker"> </TelerikTooltip> I look forward to hearing whether the above approach works well for you and aligns with your needs.=======Regards, Hristian Stefanov Progress Telerik
