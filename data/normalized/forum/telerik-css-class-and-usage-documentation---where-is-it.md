# Telerik CSS class and usage documentation - Where is it?

## Question

**TimTim** asked on 13 Oct 2023

Hi - can someone please point me towards definitive documentation for all the Telerik CSS classes and how they work with the Telerik UI for Blazor components - and for other html elements too? I don't mean documentation on how to install/configure the actual styles/style sheets - I mean documentation on the actual css classes themselves. (I'm using the default theme - but it would be good to have CSS docs for the other themes too.) For example, I see examples that use classes like "k-d-flex-col k-align-items-center k-justify-content-evenly" ... I can guess what they do from the context, but it would be nice to see some nicely organized documentation on these and other "k-..." classes and how to use them. Thanks, Tim.

## Answer

**Mark** answered on 17 Oct 2023

It is not really the documentation for your use-case but this design system documentation does provide some useful hints: Progress Design System (telerik.com)

### Response

**Dimo** answered on 13 Oct 2023

Hello Tim, I assume that you need this information in order to customize the appearance of our components. We have: Documentation about theme overrides and implementing custom CSS code. Documentation about WAI-ARIA-related elements and classes. It's split per component, for example this is the WAI-ARIA article for the Grid. Using the DOM inspector instead of documentation is the best option when working with front-end tasks and custom CSS. We don't have explicit documentation about all our CSS classes, because it doesn't make much sense. Here is why: If we list all k-classes and describe them, this will still not provide information about: The exact usage and CSS specificity of each rule. How to override a specific style. There are multiple ways to implement a CSS override, depending on your preferences and exact scenario. If we list all k-classes together with code snippets, this means to copy-paste the whole CSS theme in the documentation, together with a description what each CSS rule does. The size of this documentation will be massive and the initiative itself will be an overkill. There are over 10,000 CSS rules in each of our themes and all this will require maintenance too. Even if we add comments in the theme itself (instead of documentation), the DOM inspector won't show them. The documentation will still not answer questions about overrides or troubleshooting. For example, how will it help if a third-party CSS rule in the app breaks our own styles? Or if an app uses an outdated theme and the components look broken? So, the documentation will still have to be used together with the DOM inspector. The value of this documentation will be almost zero to people who are comfortable with using the DOM inspector. On the other hand, the value will be rather questionable for all others. In both cases, we will have to come up with some ingenious way to structure all this content on multiple pages and make it searchable, because some CSS classes are relevant to multiple components. Overall, the cost-benefit ratio doesn't justify the effort. I am a former front-end developer and I believe that it's a lot more effective and faster to use the DOM inspector, compared to theme or CSS class documentation. Regards, Dimo Progress Telerik

### Response

**Mark** commented on 17 Oct 2023

The DOM inspector is good for some elements. How do you view the styles for elements such as dropouts, maybe TelerikMenu, which only appears on hover, but DOM inspector force state does not have the expected behaviour?

### Response

**Dimo** commented on 17 Oct 2023

The third bullet in the Tools section in the linked page from our documentation answers this question.

### Response

**Mark** commented on 17 Oct 2023

Your 'effective and faster' point begins to suffer when we must dance around breaking on attribute changes and with JavaScript.
