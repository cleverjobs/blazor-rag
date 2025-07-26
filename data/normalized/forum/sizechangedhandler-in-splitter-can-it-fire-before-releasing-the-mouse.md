# SizeChangedHandler In Splitter, can it fire before releasing the mouse?

## Question

**Pet** asked on 06 Oct 2023

In my current development project, which is based on Blazor, I extensively use the splitter in conjunction with BlazorSize to manage overflow and reconstruct the scrollbar. While this setup works effectively, the user experience is not optimal. This is because the scrollbar, computed by BlazorSize, only appears after the mouse button is released. I considered utilizing the SizeChanged event to address this issue, but it too is triggered only after the mouse button is released. Is there a way to configure the Splitter to trigger these events during the dragging motion, rather than waiting until the mouse button is released?

## Answer

**Dimo** answered on 10 Oct 2023

Hi Peter, Mouse events are very inefficient in Blazor and it's not recommended to fire them too often. That's why we follow best practices and I am afraid it's not possible to configure when our events fire. Regards, Dimo Progress Telerik

### Response

**Peter** commented on 10 Oct 2023

This is what I had already read. I was hoping that there might be a JavaScript hack that could be applied. But at least it's now clear that the customer simply has to live with it. :-) However, it would be exciting to extend the splitter so that it behaves similarly to BlazorSize, meaning that you can specify a time interval in which a reaction is triggered. That might be an idea for an extension of your implementation. Thanks for the response. Peter
