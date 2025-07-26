# Null tooltip after tooltip is opened

## Question

**Osc** asked on 20 Jul 2021

Hello, I'm having a weird behaviour using your Tooltip component. <TelerikTooltip TargetSelector="#clickTarget" ShowOn="@TooltipShowEvent.Click"> <Template> Tooltip content </Template> </TelerikTooltip> <span id="clickTarget"> <strong> Click </strong> me to see the tooltip. </span> <span id="clickTarget"> <strong> Click </strong> me to see the tooltip. </span> Just two spans and a tooltip which is shown when any of these spans is clicked. The weird behaviour is that these spans are showing a "default title tooltip" on hovering, showing null in its content, after I have clicked them to show the telerik tooltip I've defined. They still are showing the telerik tooltip on click, but also a "default title tooltip" on hovering, showing null. Please take a look at the attached gif. As you can see, after, and just after, I have clicked the spans, a new null tooltip is appearing on hover. It is like your component was setting the span title to "null" or something like that. Any way of removing this behaviour? Thanks!

## Answer

**Radko** answered on 20 Jul 2021

Hello Oscar, Thank you for the provided code snippet. Indeed, setting the ShowOn parameter to TooltipShowEvent.Click should prevent the default tooltip from appearing. This is an issue we are aware of as described here: Tooltip Displays on Hover when on Click is Selected. A fix is currently scheduled for our next release in early August. I encourage following the topic to receive future status updates. Please let me know if you need any additional information. Thank you. Regards, Radko Stanev Progress Telerik
