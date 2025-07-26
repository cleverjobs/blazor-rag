# Responsiveness font scaling?

## Question

**Bla** asked on 30 Aug 2021

Hello. I am testing the widgets and I see that these, in general, use non-scalable units. Consequently what I am doing is overwriting the CSS applied to these to get a responsiveness site. This takes quite a bit of time which is why I ask you if there is a relatively simple way to scale the font size of the components based on the viewport size? Regards,

## Answer

**Dimo** answered on 02 Sep 2021

Hello Ludwig, It is possible to switch our components to a scalable font-size with a few selectors. Try the following: body.k-widget, body.k-button, body.k-animation-container { font-size: max ( 1.25vw, 16px );
} I may be missing something, but the above rule should be a good starting point that includes pretty much everything that our components render. If needed, add more classes in the same fashion. The "body" part is used only to increase the CSS specificity. On a side note, you can consider posting a feature request in the Themes feedback portal. In this way, we will be able to measure the community interest and prioritize. Regards, Dimo Progress Telerik

### Response

**Blazorist** answered on 02 Sep 2021

I've made some CSS replacements but not the selector that you mention. I will try it. Thanks Dimo for your answer. Ludwig.
