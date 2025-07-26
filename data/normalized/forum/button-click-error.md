# Button click error

## Question

**IonIon** asked on 21 Jul 2021

Hi, I updated Telerik Blazor to version 2.25.0 The js file is served from _content folder <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script> When I click any button from application I get the error telerik-blazor.js:49 Uncaught TypeError: Cannot read property 'getAttribute' of undefined
at e.value (telerik-blazor.js:49)
at e.i.close (telerik-blazor.js:49)
at HTMLDocument.i.onMouseDown (telerik-blazor.js:49) I had no problems with the old version (2.24.0) Any idea? Thanks, Ion

## Answer

**Marin Bratanov** answered on 21 Jul 2021

Hi, See this article to troubleshoot similar upgrade problems: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) If this does not help, open a support ticket and send us a runnable sample project so we can investigate. Regards, Marin Bratanov Progress Telerik

### Response

**Alexandru** answered on 22 Jul 2021

After some research, I found the issue: I have a TelerikTooltip available at top-level in application which caused the error :) Not sure why, I commented for the moment and the error has gone. <TelerikTooltip TargetSelector="#cor_info>i[title]" Position="@TooltipPosition.Top" ShowOn="@TooltipShowEvent.Hover"> </TelerikTooltip> Thanks, Ion

### Response

**Marin Bratanov** commented on 22 Jul 2021

Probably because of this issue [https://feedback.telerik.com/blazor/1520299-tooltip-with-no-targetselector-throws-a-javascript-error](https://feedback.telerik.com/blazor/1520299-tooltip-with-no-targetselector-throws-a-javascript-error)
