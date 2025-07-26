# Is there a way to access the date of a recurring appointment on clicking in Blazor scheduler?

## Question

**Mar** asked on 24 Jul 2024

Hi, I've been following this example regarding opening a context menu when right clicking an appointment [https://github.com/telerik/blazor-ui/blob/master/scheduler/appointment-context-menu/](https://github.com/telerik/blazor-ui/blob/master/scheduler/appointment-context-menu/) and I'm wondering if it's possible to access the Date of the specific occurrence that was clicked when using recurring appointments. For example being able to access Mon, 7/22 when right clicking on it to then assigning it to a private variable on the page and such? Best Regards, Marzuk

## Answer

**Dimo** answered on 29 Jul 2024

Hello Marzuk, Currently the Scheduler ItemTemplate context exposes the data item with the recurrence rule, but not occurrence information. We have a feature request to enhance the template and provide the specific occurrence. I voted on your behalf. You can also review the provided workaround - extract the occurrence DateTime from the rendered HTML with JavaScript. Regards, Dimo

### Response

**Marzuk** commented on 29 Jul 2024

Good morning, Awesome, good to know. Yeah I created a similar workaround using Javascript. Best Regards, Marzúk Ingi
