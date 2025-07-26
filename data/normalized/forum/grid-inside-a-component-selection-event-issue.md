# Grid inside a component, selection event issue

## Question

**Mar** asked on 14 Feb 2021

Hi there, I would put a grid inside a component and fire a component's EventCallback when a row of the grid is selected, however seems that there is an issue when you try to call an EventCallback (async) from the grid onselecteditemchanged event (sync) as noted here: [https://docs.telerik.com/blazor-ui/components/grid/selection/single](https://docs.telerik.com/blazor-ui/components/grid/selection/single) "// note: an async operation here can break the selection and may not even render its results in the view// for async operations, use the OnRowClick event" How could I achieve that?

## Answer

**Marin Bratanov** answered on 16 Feb 2021

Hello Marco, At the moment, the closest option I can offer is using the RowClick event. We also have this feature request open for an event that will allow async operations that also render from the selection change: [https://feedback.telerik.com/blazor/1505907-add-an-event-that-fires-after-the-selecteditemschanged-and-can-perform-async-operations.](https://feedback.telerik.com/blazor/1505907-add-an-event-that-fires-after-the-selecteditemschanged-and-can-perform-async-operations.) Hopefully, this will not actually require a new event, but that's how this request came in and at this point we don't yet know what will be possible, so we're keeping it. I've added your Vote to it and you can click the Follow button to get email notifications for upates. Regards, Marin Bratanov
