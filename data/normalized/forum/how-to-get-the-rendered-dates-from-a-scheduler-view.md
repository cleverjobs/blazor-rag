# How to get the rendered dates from a scheduler view

## Question

**Joh** asked on 03 May 2024

I need to know how I can get all the rendered dates from the scheduler for the current view? I know that I have the data that I provide to the scheduler, but I am really concerned with recurring events. For a recurring appointment that is provided to the scheduler data, it could render up to six unique events. I am trying to get a list of those event. I tried the OnCellRender event which iterates thru all the days on the scheduler, but there is nothing in the event data to identify if an appointment was rendered on that day or not. I tried the OnItemRender event which iterates thru the appointments on the view, but for the recurring events it always gives the date in the defined appointment not the actual date that it was rendered. For a use case, I want to use a Calendar to show a minified version of active days in a month. Since some of the events are recurring, I cannot just use the appointment data. I would like to give it to the scheduler and let the scheduler tell me what days are rendered as a result of the provided appointments. For this appointment list, I should get the following dates returned: 5/2, 5/9, 5/16, 5/23, 5/30, 6/6, 5/25, 5/26 new SchedulerAppointment
{
Title="Vet visit",
Description="The cat needs vaccinations and her teeth checked.",
Start=new DateTime( 2024, 5, 2, 11, 30, 0 ),
End=new DateTime( 2024, 5, 2, 12, 0, 0 ),
IsAllDay=false,
RecurrenceExceptions=new List<DateTime>(),
RecurrenceId=Guid.NewGuid(),
RecurrenceRule="FREQ=WEEKLY;BYDAY=TH" } new SchedulerAppointment
{
Title="Planning meeting",
Description="Kick off the new project.",
Start=new DateTime( 2024, 5, 25, 9, 30, 0 ),
End=new DateTime( 2024, 5, 25, 12, 45, 0 )
} new SchedulerAppointment
{
Title="Vet visit",
Description="The cat needs vaccinations and her teeth checked.",
Start=new DateTime( 2024, 5, 26, 11, 30, 0 ),
End=new DateTime( 2024, 5, 26, 12, 0, 0 )
}

## Answer

**Dimo** answered on 07 May 2024

Hi Johnathan, To find all occurrences of a recurring appointment in a given period, you need to expand the recurrence programmatically and inspect the Start and End properties of the Occurrence objects in the obtained collection. The following code shows a simple example. The values of RangeStart and RangeEnd will depend on the current Scheduler View and current Scheduler Date. protected override void OnInitialized ( ) {
SchedulerAppointment existingEvent=new SchedulerAppointment
{
Title="Recurring meeting",
Start=new DateTime( 2024, 4, 9, 9, 0, 0 ),
End=new DateTime( 2024, 4, 9, 9, 30, 0 ),
RecurrenceRule="FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" }; var expandOptions=new Telerik.Recurrence.RecurrenceOptions
{
StartDate=existingEvent.Start, RangeStart=DateTime.Now, RangeEnd=DateTime.Now.AddMonths( 1 ), Duration=(TimeSpan)(existingEvent.End - existingEvent.Start)
}; var rule=Telerik.Recurrence.RecurrenceRule.Parse(existingEvent.RecurrenceRule); IEnumerable<Telerik.Recurrence.Occurrence> expandedOccurrences=rule.ExpandRecurrence(expandOptions); base.OnInitialized();
} public class SchedulerAppointment { public string Title { get; set; }=string.Empty; public DateTime Start { get; set; } public DateTime End { get; set; } public string RecurrenceRule { get; set; }=string.Empty; public bool IsAllDay { get; set; }
} Regards, Dimo Progress Telerik
