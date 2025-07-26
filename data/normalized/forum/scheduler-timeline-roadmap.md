# Scheduler Timeline Roadmap

## Question

**Alb** asked on 31 Jul 2019

Hi, Is there an estimation to have Scheduler for Blazor? I need to do a timeline view of activity per user where you have a bar with different colours to represent different status during that time. Would that be possible to do with the scheduler timeline view? I have attached a screenshot of something similar to what i want to do. Could you advise if this will be available for scheduler for blazor and when? Thanks!

## Answer

**Marin Bratanov** answered on 01 Aug 2019

Hi Alberto, At the moment, a full featured grid is our top priority. This includes child components it needs like a menu, various date/time pickers and the like. After that, we will immediately start working on a scheduler component. You can Follow its status in the following page (I already added your vote): [https://feedback.telerik.com/blazor/1408056-scheduler-component.](https://feedback.telerik.com/blazor/1408056-scheduler-component.) Hopefully, we could start working on that in late September, and maybe release its first iteration in in early 2020, or even before the end of the year. On the feasibility of such a view - a timeline view where you have appointments that strictly match the times should let you have a similar appearance. The "Time Worked" column, though, is not something I expect the scheduler will have, as it is quite a specific thing. What I can suggest you consider (at least for the time being) is to use a grid for this - the time slots seem to be a limited number and you could use columns for that. A column template or a row template in the grid can let you color the corresponding cells as desired (although partial coloring will be a bit more difficult, you could achieve it with two div elements that have different colors and appropriate percentage widths). The color fill is actually a great candidate for its own component that renders the needed amount of elements with their widths and colors inside the cells. I did something similar for rendering labels in the grid on the Issues page in this sample app. Regards, Marin Bratanov

### Response

**blake** answered on 01 Aug 2019

its interesting

### Response

**Alberto** answered on 04 Sep 2019

I was not able to build custom solution for this, so i am using google timeline js chart for this, but if you could include a similar timeline component for blazor or adapt the scheduler to support a similar timeline view to the google one would be great!

### Response

**Alberto** answered on 04 Sep 2019

I think such component is quite useful in many scenarios like project managment, gantt charts, time schedules, etc

### Response

**Marin Bratanov** answered on 05 Sep 2019

Hi Alberto, I feel like the closest component we tend to have in our suites is a gantt, similar to this: [https://demos.telerik.com/kendo-ui/gantt/index.](https://demos.telerik.com/kendo-ui/gantt/index.) If that would suit your needs, I'd encourage you to Vote and Follow this feature: [https://feedback.telerik.com/blazor/1419052-gantt-chart.](https://feedback.telerik.com/blazor/1419052-gantt-chart.) The timeline view in a scheduler would probably look like this and would not be exactly what you seem to need: [https://demos.telerik.com/kendo-ui/scheduler/timeline.](https://demos.telerik.com/kendo-ui/scheduler/timeline.) If you would like to see a clone of the Google TimeLine chart, I would encourage you to post a feature request for such a feature in the

### Response

**Alberto** answered on 09 Sep 2019

I think your schedule timeline may work as long as you allow to add events with differents colours for same user. Because now for one user all the events are same colour for a user.

### Response

**Marin Bratanov** answered on 09 Sep 2019

Hello Alberto, It is likely that the events will get a template (even it not for v1 of the scheduler) so you should be able to colorize them as you require through your own code. Regards, Marin Bratanov

### Response

**Peter** answered on 09 Dec 2020

Hi! Is any news about blazor timeline?

### Response

**Marin Bratanov** answered on 10 Dec 2020

Hello Peter, The best way to get news is to click the Follow button on its Feedback Portal page: [https://feedback.telerik.com/blazor/1446466-timeline-view.](https://feedback.telerik.com/blazor/1446466-timeline-view.) This will send you email status updates. Regards, Marin Bratanov
