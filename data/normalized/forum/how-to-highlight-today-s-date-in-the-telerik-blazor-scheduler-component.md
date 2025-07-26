# How to highlight today's date in the Telerik Blazor scheduler component?

## Question

**sud** asked on 12 Oct 2022

I developed the Telerik Blazor Scheduler component. Like this: I want to highlight the current date like the team's calendar. Like this: This is a coding part: <TelerikScheduler Data="@Appointments" Date="@StartDate" OnItemClick="@OnItemClick" @bind-View="@CurrView" DateChanged="@DateChangedHandler" Height="480px"> <SchedulerResources> <SchedulerResource Field="ManagerName" Data="@Managers" /> </SchedulerResources> <SchedulerViews> <SchedulerWeekView StartTime="@DayStart" EndTime="@DayEnd" SlotDuration="30" SlotDivisions="5"/> </SchedulerViews> </TelerikScheduler> It can be done or not? Please help me

## Answer

**Svetoslav Dimitrov** answered on 16 Oct 2022

Hello Sudath, We have an open feature request for the OnCellRender event that is scheduled to be released with our upcoming 3.7.0 release, due on the 9th of November. This event will allow you to apply a specific background color based on application logic. Regards, Svetoslav Dimitrov Progress Telerik
