# Dismiss tooltip by clicking on triggering element

## Question

**Edw** asked on 21 Aug 2023

Apologies if duplicate. It seems that when Tooltip's ShowEvent is set to Click, you can click anywhere in the browser window except on the element that triggers the tooltip to open. I think it would be better behavior to have the triggering element toggle the tooltip instead of only opening. Is there perhaps a workwround?

## Answer

**Svetoslav Dimitrov** answered on 24 Aug 2023

Hello Edward, Can you provide a bit more information on the need to close the tooltip upon clicking on the parent container? I am asking because this is the first time anyone requested such feature and I am interested to find out more on the topic. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Edward** answered on 26 Aug 2023

It just seems to make more sense for the triggering element to act as a toggle whereas currently it can only open the tooltip. As an example, we have question mark icons next to elements on the page. Clicking on each opens a tooltip with some help text. We find it counter-intuitive that you have to click somewhere else on the page to close the tooltip, not the question mark icon itself. We would like to find a way for it to work as a toggle.

### Response

**Svetoslav Dimitrov** commented on 30 Aug 2023

Hello Edward, You can achieve the desired behavior by: Setting the ShoOn parameter of the tooltip to TooltipShowEvent.Hover Adding an onclick event for the element that contains the question mark icon Create a small JS function that checks if the Tooltip is rendered in the DOM In the OnClick handler close the tooltip programmatically if was previously rendered in the DOM Here is a code snippet: JavaScript: function isTooltipVisible ( ) { let tooltipElement=document.getElementById( "visible-tooltip" ); return tooltipElement==null? false: true;
} C#: @inject IJSRuntime js

<TelerikTooltip TargetSelector=".tooltip-target" ShowOn="@TooltipShowEvent.Hover" Id="visible-tooltip" @ref="TooltipReference" />

<div style="padding: 5em;">
<span title="I am a Telerik Blazor Tooltip." class="tooltip-target">
<TelerikButton Icon="@FontIcon.QuestionCircle" OnClick="@HideTheTooltip" />
</span>
</div>

@code { private TelerikTooltip TooltipReference { get; set; } bool isVisibleTooltip { get; set; } private async Task HideTheTooltip ( ) {
isVisibleTooltip=await js.InvokeAsync<bool>( "isTooltipVisible" ); if (isVisibleTooltip)
{
TooltipReference.Tooltip_Close();
}
}
} Let me know if this solution works as expected for you.
