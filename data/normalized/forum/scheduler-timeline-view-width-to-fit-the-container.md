# Scheduler Timeline View width to fit the container.

## Question

**Her** asked on 17 Jan 2025

Hi , currently working on a dashboard to display some data and need to display the Scheduler timeline view , but the problem is that the timeline width is too wide and you need to scroll to view events in the evening . How to make the timeline view to fit the container? as this is going to be display on a dashboard with no user interface (to scroll ). Using Blazor 9 and latest kendo UI . Thanks

## Answer

**Dimo** answered on 17 Jan 2025

Hello Hernando, Please refer to the available Scheduler TimelineView parameters and: Reduce the slot divisions (currently they are two). Note that this may also reduce the precision of the displayed start / end times. Reduce the column width. Note. that this must be a fixed number and the columns don't resize at runtime. Change the start and end times, if possible. <TelerikScheduler> <SchedulerViews> <SchedulerTimelineView SlotDivisions="1" ColumnWidth="100" StartTime="@(DateTime.Today.AddHours(6))" EndTime="@(DateTime.Today.AddHours(18))" /> </SchedulerViews> </TelerikScheduler> Regards, Dimo Progress Telerik

### Response

**Hernando** commented on 20 Jan 2025

Thanks that's perfect

### Response

**Hernando** commented on 20 Jan 2025

Hi @Dimo another question how to change the height of the slot to add more data . thanks

### Response

**Dimo** commented on 21 Jan 2025

I am afraid that's not supported at this point. You can vote for and follow these feature requests: Scheduler RowHeight Scheduler Appointment Height
