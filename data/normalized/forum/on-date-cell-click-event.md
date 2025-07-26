# On Date Cell click event

## Question

**Zhi** asked on 20 Jan 2021

Hello, Is there a "On Date Cell click" event? For example, based on this example from ASP.NET AJAX ([https://demos.telerik.com/aspnet-ajax/scheduler/mobile-examples/overview/default.aspx?name=overview),](https://demos.telerik.com/aspnet-ajax/scheduler/mobile-examples/overview/default.aspx?name=overview),) on clicking a particular the Date Cell in month view, it gets highlighted. I would like to do more than modifying the css (e.g. highlighting) on click, and I'm wondering if such a functionality is available. Thanks!

## Answer

**Zhi Yuan** answered on 20 Jan 2021

Apologies for not adding this information in my earlier post: this behavior can be found in Calendar's ValueChanged event.

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hello, Would the following functionality meet your needs: [https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot.](https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot.) At the moment, I imagine it could be through an event like OnSlotRender where you could add a class for appearance, and maybe also a template for the slot where you could add content and also hook your own event handlers to it (which would also allow you to highlight your elements by using CSS classes). Of course, that's just a guess at this point - this slot customization has not been implemented yet so I don't know if it will have all those templates and events, nor how exactly it will come to be. As for the calendar - that's a completely separate component from the scheduler (this thread was opened in the scheduler forums). The Blazor calendar can also respond to date selection through an event: [https://docs.telerik.com/blazor-ui/components/calendar/selection.](https://docs.telerik.com/blazor-ui/components/calendar/selection.) When the following feature is completed, you would also be able to customize its day templates too: [https://feedback.telerik.com/blazor/1446960-add-day-cell-customisation-templates-to-the-calendar](https://feedback.telerik.com/blazor/1446960-add-day-cell-customisation-templates-to-the-calendar) and I see that you have voted for this back in November. Regards, Marin Bratanov

### Response

**Zhi Yuan** answered on 20 Jan 2021

Hi Marin, Thanks for your prompt reply! Apologies for not being clear, what I meant was that the calendar has a ValueChanged event, which triggers when user clicks on a date cell. As such, I'm wondering if Scheduler has a similar event. Also, since you mentioned this issue [https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot,](https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot,) can I know the different between Template & Slot? Thanks again Marin!

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hello Zhi Yuan, The scheduler does not have a similar event and it is likely that templates for the slots will let you achieve that. The Template is a Blazor framework concept where a component lets its parent decide what will be rendered in that component. For example, you component would decide what the scheduler would render in its slots, instead of the scheduler deciding that. Most coponents have various such templates, for example - the scheduler already has two appointment templates that also let you handle single click, double click, contextmenu and other events in them. The Slot is a concept specific to the scheduler component - it is the single unit of time that it renders, you can read more about this in the documentation, for example the Slot section of the DayView article: [https://docs.telerik.com/blazor-ui/components/scheduler/views/day#slots.](https://docs.telerik.com/blazor-ui/components/scheduler/views/day#slots.) Thus, a slot can have a template (just like many other aspects of a component). Regards, Marin Bratanov

### Response

**Zhi Yuan** answered on 20 Jan 2021

Hi Marin, Thanks again for such a comprehensive response! Just another question for clarification: I'm looking for the functionality such that an event is fired when a date cell is selected (i.e. clicked by a mouse / tapped on a mobile device) in the Month view. From what I'm reading, it seems that slots are only relevant for Day & Week views because these views display Time, while the Month view does not display Time. If that's the case, then it would be a separate issue from [https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot,](https://feedback.telerik.com/blazor/1480581-customize-scheduler-slot,) am I right? Thanks Marin!

### Response

**Marin Bratanov** answered on 20 Jan 2021

Hello, The month view also has slots - the concept is the same - each division in the scheduler itself is a slot, and in the case of the Month view the slots are a month each. In that view there are no settings for the slots (there simply aren't any meaningful settings such as length in hours) and that's why there isn't explicit documentation for them. I expect that a slot customization feature will allow you to customize the month slots too. Regards, Marin Bratanov
