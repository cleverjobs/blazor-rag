# Left value of inline css is incorrect

## Question

**Flo** asked on 20 Jan 2020

My "page-wrapper" has "left" property set to 60px. DropdownList is adding inline style to list with incorrect "left" value which is causing list to not being allined with input, as you can see in attached image. How dropdown list is calculating this values? Can I override this behaviour? It is worth to mention that normal jquery-kendo Dropdown behaves correctly, so this is a problem strictly with balzor version.

## Answer

**Marin Bratanov** answered on 20 Jan 2020

Hello Tomasz, My best guess is that the TelerikRootComponent in your blazor app is not aligned with the browser viewport, body and app tags: [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#popups-do-not-work](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#popups-do-not-work) If this does not help you solve this, please open a support ticket and send me a simple reproducible where I can observe the problem so I can offer a more concrete answer. Regards, Marin Bratanov

### Response

**Flotman** answered on 20 Jan 2020

I am adding Blazor Components into existing MVC application so TelerikRootComponent is not positioned as in usual File->New->Server Side BlazorApp template form VS. It is located inside this one specific view, so this might be the problem.

### Response

**Marin Bratanov** answered on 20 Jan 2020

Hello Tomasz, That's a likely reason for the problem. In such a scenario the Blazor component hierarchy does not get up to an <app> component level and it is limited to where the component is defined in the rest of the markup. I'm afraid that there is no solution for this in Blazor - there simply is not access to the DOM. Regards, Marin Bratanov
