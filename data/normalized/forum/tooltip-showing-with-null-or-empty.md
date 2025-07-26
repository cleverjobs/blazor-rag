# Tooltip showing with null or empty

## Question

**Emm** asked on 28 May 2024

Hi we have been trying to utilise the TelerikTooltip dynamically for a number of different reasons across various controls and buttons. We notice part of the tooltip icon will still display if the controls tooltip property is either null or empty (see the code snippit from the REPL below. Is there an existing way with the TelerikTooltip (without too much hacking) that it will NOT show the tooltip if the target title is null or empty or whitespace? With this snippit you may also notice an issue with trying to use dynamic tooltips in that the tooltip on the button does not update when pressed. Similar to the question found here: [https://feedback.telerik.com/blazor/1460642-the-tooltip-should-be-able-to-re-evaluate-targets-tooltip-not-working-for-elements-not-present-at-first-rendering](https://feedback.telerik.com/blazor/1460642-the-tooltip-should-be-able-to-re-evaluate-targets-tooltip-not-working-for-elements-not-present-at-first-rendering) @if (RepaintTooltipFlag)
{
<TelerikTooltip TargetSelector=".tooltip-target">
</TelerikTooltip>
}
<TelerikButton class="tooltip-target" title="@buttonTooltip" OnClick="@AddMoreContent">show more content</TelerikButton>
@code{ string buttonTooltip { get; set;}=""; bool AllContentVisible { get; set; } //part of workaround bool RepaintTooltipFlag { get; set; }=true; async Task AddMoreContent () {
AllContentVisible=true;
buttonTooltip="More Content Tip"; //workaround RepaintTooltipFlag=false; await Task.Delay( 30 );
RepaintTooltipFlag=true;
}
}

## Answer

**Tsvetomir** answered on 31 May 2024

Hello Emmett, Thank you for the provided code snippet. To not show the tooltip when the target title is null, empty, or whitespace can be achieved by dynamically changing the target's class within the AddMoreContent() method. Thus, the tooltip won't show because it will target a non-existing class. The drawback here is that the new tooltip won't be shown explicitly after clicking the button, but you need to move the cursor away and re-enter. I'm sending you a REPL example that shows the behavior of this approach. On the topic of dynamically updating the Tooltip content, I can confirm that the linked item from our feedback portal is targeting different functionality of the Tooltip. An alternative approach to loading data dynamically is by loading the Tooltip content on demand by using a standalone component in the Tooltip Template. I'm sharing a runnable REPL example to see the result firsthand. If the above approaches don't suit your requirements, please provide me with more information about the use case of changing Tooltip content dynamically. As a side note, if the Tooltip current functionality doesn't meet your expectations, I can recommend you use the Popover component. It gives more variety of built-in functionality that might be more suitable for your scenario. I hope you find the provided information helpful. I eagerly anticipate hearing your feedback. Regards, Tsvetomir Progress Telerik

### Response

**Emmett** commented on 03 Jun 2024

Hi Tsvetomir, Thank you for the detailed response and the few different options to try. The first example as you say isnt ideal as it requires the cursor to navigate away. As our use of this is targeting an "Undo" button not only will the tooltip need to display an initial hover but will need to change on each press, so the need to navigate away isnt acceptable. Changing the tooltips class would then need to follow the same workaround as in the linked suggestion where by the class is changed, redrawn, and then changed back again. An undesirable workaround for something with functional bindings would be better suited. Your component approach for a dynamic tooltip would solve that problem and it is close to what we came up with as a work around, but its just that, a work around for something a functional binding would solve. The popover component would be suitable for a more basic razor component however it isnt a perfect answer and would require a lot more boiler plate controlling its visibility and binding. And with our TelerikTooltip defined at a high level in our page (to avoid having to define it numerous times on the child components) it would require us to pass around callbacks to trigger the visibility and content. So the Tooltip content component solves the dynamic issue. The other two suggestions help to workaround not showing an empty tooltip but all just get around not having a functional binding for the tooltip value and a parameter to not show anything if there is no value to display. It's not a deal breaker but not perfect functionality. Thank you for your help, we can force it to suit our requirements. Regards Emmett

### Response

**Tsvetomir** answered on 05 Jun 2024

Hello Emmett, Thank you for coming back with such detailed feedback about the suggested approaches. I regret to see that the Tooltip does not fully meet your requirements. We are constantly trying to improve our components and will keep in mind the provided feedback about the functionality of the Tooltip. Your cooperation is highly valued. Regards, Tsvetomir Progress Telerik
