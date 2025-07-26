# Set/limit the number of pages shown in the paging control?

## Question

**Mar** asked on 10 Dec 2019

Is there a way to set/limit the number of pages that show in the paging control? It looks like this is calculated by the grid using the number of items per page (configurable) and how many items in the grid.

## Answer

**Marin Bratanov** answered on 10 Dec 2019

Hello Mark, The grid pager generates the list based on the total count of items in the data source given to the grid and it needs to be managed like that so the correct pager is generated. If it were exposed for configuration, that would allow invalid configurations. Could you provide some more details on what you want to achieve so I can offer a better answer? Is it, by chance, a responsive layout for mobile devices: [https://feedback.telerik.com/blazor/1442883-responsive-layout-for-the-pager?](https://feedback.telerik.com/blazor/1442883-responsive-layout-for-the-pager?) Regards, Marin Bratanov

### Response

**Mark** answered on 10 Dec 2019

Yes, that is the exact issue I'm having. I am testing on an iphone layout using chrome debugger and the last part of the grid's paging footer is being cut off. I placed a vote for the issue. Thanks for quick response. Mark

### Response

**Nick** answered on 11 Dec 2019

Sorry Marin, I've posted a very similar question, I only just spotted Mark's post. Feel free to combine the two. I think my issues are much the same: Incorrect default behaviour on mobile browsers. I'd like a way to decide how many, or at least the maximum "page number buttons" displayed, including an option to not display them at all and just have the first/last, next/previous page arrows.

### Response

**Nick** answered on 11 Dec 2019

Ignore me - I'm going mad - I see I've posted this before and it's been raised as an issue!
