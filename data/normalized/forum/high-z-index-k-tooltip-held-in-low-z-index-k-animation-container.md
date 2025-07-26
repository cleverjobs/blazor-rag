# High z-index k-tooltip held in low z-index k-animation-container

## Question

**Nat** asked on 05 Sep 2024

In Telerik themes, we see this z-index on .k-tooltip. This would put it comfortably above some other high z-index values we had to use. .k-tooltip { z-index: 12000; } However, it's held within a div class="k-animation-container telerik-blazor" which has low z-index such as 3 or 11. This puts it below our z-index, which might be in the 900s. Was there a reason this k-animation-container z-index was so low?

## Answer

**Dimo** answered on 10 Sep 2024

Hello Nathan, The expected z-index style of <div class="k-animation-container"> should start from 10,002. with one exception. If the tooltip target has a z-index of A, the animation container element will have A + 1. So, either remove the tooltip target's z-index style, or increase it. Update 1: On second thought, I think the idea of our algorithm should be to increase the default z-index, not decrease it. I started a discussion about this in the team. Update 2: The issue is now fixed and the changes will take effect in our next release. Regards, Dimo Progress Telerik
