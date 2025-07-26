# ToolTip position with width only set

## Question

**Kel** asked on 04 Apr 2020

When I set the ToolTip width only (no height), the position gets jacked up. If I add a height it is fine. I would like to not have to set the height but rather let the height adjust to the content.

## Answer

**Eyup** answered on 06 Apr 2020

Hi Kelly, I tried to reproduce the mentioned scenario but it looks fine on my side: This is the mark-up I am using: <TelerikTooltip TargetSelector="#click-tooltip" ShowOn="@TooltipShowEvent.Click" Width="200px" Position="TooltipPosition.Bottom"> <Template> Test Content <br /> Second line <br /> Third line <br /> <input /> <br /> Last line </Template> </TelerikTooltip> <div class="text-center mt-3"> <span id="click-tooltip" class="k-button k-primary button-wide" title="Shown on click"> Click Me! </span> </div> I've also tested with animation container: Here is the code: <TelerikButton OnClick="@Toggle"> Show/Hide Animation Container </TelerikButton> <br /> <TelerikAnimationContainer @ref="@AnimationContainer" Top="50px" Width="200px" Class="k-popup"> Test Content <br /> Second line <br /> Third line <input /> Last line </TelerikAnimationContainer> But in your specific configuration there might be something which leads to this issue. You can try to explicitly set Height="auto", as demonstrated here: [https://docs.telerik.com/blazor-ui/common-features/dimensions#examples](https://docs.telerik.com/blazor-ui/common-features/dimensions#examples) I hope this will prove helpful. Regards, Eyup

### Response

**Kelly** answered on 06 Apr 2020

If you change Position="TooltipPosition.Bottom" to Position="TooltipPosition.Top", your example will demonstrate the issue. I was able to use your example, and it worked with position Bottom, but not Top.

### Response

**Eyup** answered on 07 Apr 2020

Hello Kelly, In this case you can remove the Width property to resolve the issue. There are 2 correct ways of setting the Dimensions of the Tooltip: 1. Remove both the Height and Width properties so that the component will apply the required boundaries automatically. This is explained in the green Note at the end of this article: [https://docs.telerik.com/blazor-ui/components/tooltip/overview](https://docs.telerik.com/blazor-ui/components/tooltip/overview) 2. Set both the Height and Width properties if you want to apply custom sizing to the component. This is required because the tooltip is able to take its height dynamically only after its content is loaded on the client browser. This causes the height (bottom part) of the tooltip to expand in the Y axis direction (down) automatically to contain all the inner elements. And this works in the default case. However, when the Position is set to be Top, the displaying of the Tooltip happens before the actual resizing/expanding. Since at the moment of showing of the Tooltip, its final height is still unknown, the calculation of the Top position ends up not being correct. To resolve that, you will need to set and return fixed Height if you want to have fixed Width. Regards, Eyup
