# Adaptive pager not working correctly with a sidebar layout

## Question

**Mik** asked on 14 Apr 2023

When I have a page with a fixed width sidebar, and the pager is in the content area of the page, the adaptive rendering of the pager does not work correctly. I would expect that as the screen size gets smaller, that the pager will start to drop off the page info and the page size dropdown. However, it doesn't do this, and it creates a horizontal scrollbar across the page. Here is a repl illustrating the issue: [https://blazorrepl.telerik.com/wxOIPSvd41wFZsZO20](https://blazorrepl.telerik.com/wxOIPSvd41wFZsZO20) In my troubleshooting, it looks like the adaptive code to drop off the page info and page size is done somewhere in javascript, and I can't find what logic is being used to set a display: none Style on those items. What can be done to get this functionality to work when there is a sidebar layout?

### Response

**Nadezhda Tacheva** commented on 19 Apr 2023

Hi Mike, Thank you for sharing a runnable sample demonstrating the behavior you are experiencing! We will look further into the configuration and perform additional tests to determine the root cause. I will get back to you with more details as soon as possible. Thank you for your patience in the interim as well!

### Response

**Nadezhda Tacheva** commented on 20 Apr 2023

Hi Mike, Thank you once again for your patience! After revising the example in detail, it looks like the behavior you are experiencing is related to the configuration itself rather than the Pager. Based on the current setup, the page-wrapper element has width: 100%. In addition to that, the sidebar element has a fixed min-width: 250px. This effectively makes the total width of the content more than 100% and thus the page-wrapper which contains the Pager overflows the screen. To handle the scenario, I recommend calculating the page-wrapper width taking into consideration the width of the sidebar. Here is the modified sample: [https://blazorrepl.telerik.com/mREIvDFx29Se29Ke01.](https://blazorrepl.telerik.com/mREIvDFx29Se29Ke01.) I hope this will help you move forward with your application. Please let us know if any other questions appear.
