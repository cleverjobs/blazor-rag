# Replacing bootstarp with kendo css classes

## Question

**Mar** asked on 08 Nov 2021

I am trying to get rid of bootstrap and looking in the telerik sass source for inspiration. Would like to know How to layout forms using the form css classes. Don't like the auto layout. TabStrip can I use it to build a tabstrip without content like bootstrap "nav nav-tabs" In general where can I find information for all the kendo classes?

## Answer

**Marin Bratanov** answered on 08 Nov 2021

Hello Martin, We are not aiming at making a bootstrap alternative or a clone, and so for layouts I can still suggest you use a tool that targets that task. You may find useful this section of the documentation regarding Bootstrap: [https://docs.telerik.com/blazor-ui/styling-and-themes/overview#bootstrap-notes](https://docs.telerik.com/blazor-ui/styling-and-themes/overview#bootstrap-notes) Our themes and components aim at styling themselves and we do not supply public documentation about our classes. Their usage may vary and change, and it is not something that we consider public API. To answer your concrete questions: making form layouts - any tool that can do this should be usable with our components. What you can do with regular <input> elements, you should be able to do with our input components instead. If the tool you use adds global styles (say, things like input { padding: 1em; } or some other similar rule - that might affect our components negatively, but there isn't much we can do to defend against such rules - we can't add resets for every possible rule for every possible element, that would bloat our styles many times. tab strip - we have a tabstrip component for that and it does not require bootstrap. If there is no selected tab, there will be no content rendered - we render content only for the active tab, and that can be a blazor component whos rendering you determine. Regards, Marin Bratanov Progress Telerik

### Response

**Martin Herløv** commented on 08 Nov 2021

Hi good to know the corract usages of the kendo classes. Sometimes it just hard to find the right "glue" to pice it all together, always sitting with a nagging feeling of reinventing the wheel. About the tab. I know you have a tab and I am already using it. I would like a tab strip that has no content. So it's more like buttons.

### Response

**Marin Bratanov** commented on 08 Nov 2021

Perhaps a menu (even has built-in navigation) or a ButtonGroup?
