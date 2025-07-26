# Next button should go to next enabled step

## Question

**Dea** asked on 30 May 2022

Hi, According to [https://docs.telerik.com/blazor-ui/components/wizard/structure/buttons](https://docs.telerik.com/blazor-ui/components/wizard/structure/buttons) "If the next step is disabled, the ["Next"] button will also appear as disabled." Can I ask why this is? Shouldn't it simply take you to the next enabled step? This is the behaviour I need - is there a workaround? Thanks, Dean

## Answer

**Dimo** answered on 02 Jun 2022

Hi Dean, This behavior was considered during the initial development of the Wizard, but it was ultimately rejected, mainly to be on the safe side in terms of UX/API predictability and simplicity. It is possible to achieve the desired result with custom Wizard buttons. Regards, Dimo
