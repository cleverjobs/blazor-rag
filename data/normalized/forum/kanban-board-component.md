# Kanban Board Component

## Question

**Kel** asked on 18 Apr 2020

Any plans to add a Kanban board component similar to this? [https://www.syncfusion.com/blazor-components/blazor-kanban-board](https://www.syncfusion.com/blazor-components/blazor-kanban-board)

### Response

**Manuel** commented on 26 Oct 2023

Hello Telerik Team, It seems the DnD is now part of Blazor event handling. [https://learn.microsoft.com/en-us/aspnet/core/blazor/components/event-handling?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/event-handling?view=aspnetcore-8.0) Can you please consider adding this component to your library hopefully soon?

### Response

**Svetoslav Dimitrov** commented on 30 Oct 2023

Hello Manuel, We have an open feature request for the Kanban Board. I have added your Vote for it and you can click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov

## Answer

**Marin Bratanov** answered on 19 Apr 2020

Hello Kelly, At the moment, the Blazor framework does not allow drag-and-drop (you can read more about this here ) and once it does we might consider one. The Syncfusion implementation seems to be JS based only (see the attached screenshot) and we're wary of wrappping JS components into Blazor components, we'd rather go native. That said, we haven't had such a request and you can open a new enhancement idea on our portal if you like: [https://feedback.telerik.com/blazor](https://feedback.telerik.com/blazor) Regards, Marin Bratanov

### Response

**Kelly** answered on 19 Apr 2020

Hi Marin, Thanks for the reply. What about this post? Seems to be a start of a Kanban with drag and drop. [https://chrissainty.com/investigating-drag-and-drop-with-blazor/](https://chrissainty.com/investigating-drag-and-drop-with-blazor/)

### Response

**Wayne** answered on 20 Apr 2020

Hi, Have a look at this sample here [https://blazordragdrop.azurewebsites.net/](https://blazordragdrop.azurewebsites.net/) Its built with and Easy-to-use Drag and Drop Library for Blazor at [https://github.com/Postlagerkarte/blazor-dragdrop](https://github.com/Postlagerkarte/blazor-dragdrop) Hope this helps Regards, Wayne

### Response

**Marin Bratanov** answered on 20 Apr 2020

We are aware of several JS based implementations, and the last drag-drop example is perhaps similar to something we might have to implement on our own. It is non-trivial, though, and it will take time to do, which is time in which we won't be doing other high-priority tasks (say, the grid export). At the same time, there is an expectation that the framework will provide some facility, so we would have to rewrite a home-grown implementation once the framework provides something. We'd want to avoid such double work. In summary, at the moment, JS interop and often a service are still required to handle this, and both are, to an extent, problematic (for example, adding a service will either require more complex setup and be viewed as a breaking change, or will cause problems with mocking and testing). Regards, Marin Bratanov
