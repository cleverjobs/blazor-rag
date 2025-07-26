# Resize of charts when browser size change

## Question

**Alb** asked on 12 Sep 2019

I have 2 horizontal charts that are set to 100% width, when resizing the browser the charts are not resize to be 100% of the new browser size so they are left out of the window. Is there any way to do this? could you add this feature to your charts so they can autoajust to any resolution when resizing the browser?

## Answer

**Marin Bratanov** answered on 13 Sep 2019

Hi Alberto, You can Follow the progress of such a feature in the following page (I have added your vote already): [https://feedback.telerik.com/blazor/1426274-allow-charts-to-resize-reformat-on-changes-to-browser-zoom-or-resize.](https://feedback.telerik.com/blazor/1426274-allow-charts-to-resize-reformat-on-changes-to-browser-zoom-or-resize.) This is unlikely to be "automatic", however, because there are far too many events/use cases for it to work out of the box. Elements in the layout may resize without the browser resizing, for example, so that cannot be captured by us, or a browser resize may not trigger a new layout size, but we cannot know we must not redraw the charts. Thus, the approach for making charts responsive is for us to expose a method that lets you do that, so you can call it when needed by your business logic. Regards, Marin Bratanov

### Response

**Shawn** answered on 18 Jun 2020

The Grid widget is automatic on resize. Is there something special about the Chart widget that makes it not possible to be automatic?

### Response

**Marin Bratanov** answered on 18 Jun 2020

Hello Shawn, The grid is HTML so it can use responsive design (things like em units, percentage widths, and so on). The charts are not - they would be impossible to style and render correctly if they were, and it would destroy performance. So, the charts are either SVG elements, or a <canvas>, depending on how you choose to render them, which cannot be responsive in the same CSS manner. Hence, the need for an explicit method call that can invoke re-calculations of the size. The following sample project shows one way to do that: [https://github.com/telerik/blazor-ui/tree/master/chart/responsive-chart](https://github.com/telerik/blazor-ui/tree/master/chart/responsive-chart) Regards, Marin Bratanov

### Response

**Ted** commented on 23 May 2024

Why isn't this done out of the box by Telerik Blazor charts? Why do we have to add a bunch of JS interop to get this to work? There should be a simple flag/bool on the TelerikChart that tells it whether or not to resize to match its parent container. ALL other 3rd party Blazor chart work this way. When can you get a fix in for this??

### Response

**Hristian Stefanov** commented on 27 May 2024

Hi Ted, Thank you for sharing your feedback here. Our Charts offer a built-in Refresh method that enables you to adjust the chart size according to your specific requirements. This method can work without the need for JavaScript interop, it depends on the case. JavaScript is necessary to detect browser window resize events. However, it is not always required; for example, when the chart is nested within a component, you can simply call the Refresh method within the parent component's change handler. I can confirm that this is currently the recommended approach for handling such scenarios. Additionally, if you have a specific enhancement idea that would enable the Chart to detect window resizing automatically, I encourage you to share it on our Public Feedback Portal. When submitting the request, please provide detailed insights into how you envision this functionality operating or if you've encountered a similar implementation elsewhere. The feature requests logged in the portal are reviewed and evaluated by the Telerik Blazor team. If their status changes to "Unplanned," they are considered valid, and based on the community's interest, they may be planned for implementation in subsequent releases. Kind Regards, Hristian

### Response

**Ted** commented on 27 May 2024

Thanks, as commented above, I'm not sure why the Charts would work any differently than all the other Telerik Blazor controls work as far as resizing, so the Charts behavior is odd and inconsistent. All other Telerik controls resize automatically with the parent size if 100%-resizing is specified on the element. It's also really annoying for every developer to have to come up with their own solutions for this bug. Further, the solution proposed above does not work if the parent div is resized but the parent window is not resized, so it is not a viable solution at all, except in the simplest of use cases. We ended up using the library below with some custom code to get the chart to redraw on resizing of the parent div. However, it would be really nice if Telerik would fix this bug and implement resizing natively, out-of-the-box. [https://github.com/Author-e/BlazorObservers](https://github.com/Author-e/BlazorObservers)

### Response

**Hristian Stefanov** commented on 30 May 2024

Hi Ted, I confirm that all the other Telerik Blazor components, that automatically adjust themselves, are rendered as HTML. This allows them to use responsive design (things like em units, percentage widths, and so on). However, the Charts are not rendered as HTML because they would be impossible to style and render correctly if they were, and it would destroy performance due to the number of rendered elements needed. Thus, the Charts are either SVG elements or a <canvas>, depending on how you choose to render them, which cannot be responsive in the same CSS manner. Overall, the developers are responsible for choosing at which moment to refresh the Chart using its method rather than this being a bug. Regarding the scenario where the parent div is resized without resizing the parent window, I can confirm that the sample project we are providing serves as a foundational starting point. There are numerous scenarios involving different developers who use multiple containers with numerous chart instances, making it challenging to cover all possibilities in a single example. Generally, it is up to the developer to build upon this foundation and implement custom logic to achieve the desired result. The primary option of the chart is to have the capability to refresh. Kind Regards, Hristian
