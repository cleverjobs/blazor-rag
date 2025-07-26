# Blazor AnimationContainer relative placement

## Question

**Bar** asked on 30 Jan 2025

Our designer has discovered the Telerik for Blazor AnimationContainer and is excited to use it, including in areas of our site that collapse and expand. This makes the absolute placement a bit of a problem. Is there an official workaround to this limitation? A good way to simulate relative placement of the AnimationContainer?

## Answer

**Dimo** answered on 31 Jan 2025

Hi Barron, Is this what you are trying to achieve? [https://blazorrepl.telerik.com/czkFRbbq429N5fo055](https://blazorrepl.telerik.com/czkFRbbq429N5fo055) It's worth noting that the AnimationContainer is not designed for this specific scenario. You can also review this article in case there is some other more suitable component: Telerik Blazor Popup Components Regards, Dimo Progress Telerik

### Response

**Barron** commented on 31 Jan 2025

Thank you, this does exactly what I am looking for. Essentially, for this particular scenario, we are looking for an image that can be shown or hidden on demand, but that includes a nice animation. We may include more complex contents in the future, but the container must exist within the layout of the page, and not sit on top of it like a popup. Out of curiosity, why is relative positioning not officially supported? Are there known scenarios where it breaks?

### Response

**Dimo** commented on 03 Feb 2025

Hi Barron, Relative containers participate in the so called "normal flow" of the page. In simple terms, this means that these containers take up real estate and push other content around. Usually, this is a rare requirement and it's mostly feasible for smaller elements. When it comes to larger animated or expandable content, we have other components that can be considered: PanelBar Splitter Expansion Panel (similar to the PanelBar, still a feature request) You can also take at look at: Layout components in Telerik UI for Blazor Popup components in Telerik UI for Blazor
