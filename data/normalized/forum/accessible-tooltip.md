# Accessible tooltip?

## Question

**Jas** asked on 12 Jan 2021

Is there a way to make the tooltip accessible? It seems only activated by hover or click. It would be enough I think if I could hit enter to activate and deactivate.

## Answer

**Marin Bratanov** answered on 12 Jan 2021

Hi Jason, The Tooltip component has an Id parameter that you can use in the aria-described-by attribute of its target(s) to help screen readers. It is up to the screen reader to detect the change in the DOM and read it out. Using the click event should be sufficient for them to detect an action. <TelerikTooltip TargetSelector="p a[title]" Id="aaaaaaaaaaaaaaa"> </TelerikTooltip> <p> <a aria-describedby="aaaaaaaaaaaaaaa" title="what is 'lorem ipsum'?" href="[https://lipsum.com/">](https://lipsum.com/">) lorem </a> ipsum dolor <a aria-describedby="aaaaaaaaaaaaaaa" title="is this a real word?" href="[https://en.wikipedia.org/wiki/SIT">](https://en.wikipedia.org/wiki/SIT">) sit </a> amet. </p> You can Follow the implementation of a method to show the tooltip here: [https://feedback.telerik.com/blazor/1494644-show-tooltip-programatically](https://feedback.telerik.com/blazor/1494644-show-tooltip-programatically) and for a way to hide it here: [https://feedback.telerik.com/blazor/1476364-close-tooltip-via-method.](https://feedback.telerik.com/blazor/1476364-close-tooltip-via-method.) I've also made this page for you to Follow the addition of WAI-ARIA attributes such as role, aria-live, aria-hidden: [https://feedback.telerik.com/blazor/1501914-tooltip-is-missing-wai-aria-attributes.](https://feedback.telerik.com/blazor/1501914-tooltip-is-missing-wai-aria-attributes.) Regards, Marin Bratanov
