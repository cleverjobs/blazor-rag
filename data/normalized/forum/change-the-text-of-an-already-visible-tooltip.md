# Change the text of an already visible tooltip.

## Question

**Dav** asked on 13 Sep 2023

I am trying to create something I've seen a lot on other websites. I want to create a tooltip that shows "Copy to clipboard" when I hover over a <span> element, but when I click on the <span> I want the text to change to "Copied!" This is what I am doing now <TelerikTooltip TargetSelector="#propvalue>span[title]" Position="@TooltipPosition.Top" ShowOn="@TooltipShowEvent.Hover" @ref="@tooltipHover"> <Template> @{ <div> @copyToolTip </div> } </Template> </TelerikTooltip> <span id="myCoolSpan" style="cursor:pointer;" onclick="@(()=>_copyButtonHandler(value as string))" title="this is the title"> Text of my span </span> private async Task _copyButtonHandler( string value )
{
copyToolTip="Copied!"; await _clipboardService.WriteTextAsync( value );
}

### Response

**Hristian Stefanov** commented on 14 Sep 2023

Hi David, We have a knowledge base article that demonstrates how to dynamically update the content of a Tooltip without the need to close it: Tooltip Does Not Update Content with the View-Model fields and events. As a next step, apply the recommended approach from there, and let me know whether it works well for you. Kind Regards, Hristian
