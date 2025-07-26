# Fake recurrence using real events from DB

## Question

**Kyl** asked on 05 Aug 2024

Hi all, I am trying to find a way that I can display events using the Scheduler Blazor component that do not use the recurrence rule, but instead display a list of "real" events returned from the DB that are linked via a parent/child relationship. foreach (var event in events) { event.RecurrenceRule=null; var firstOccurence=new Job
{
Id=new Guid();
Start=new DateTime( event.Start.Value.Ticks).AddDays( 1 ),
End=new DateTime( event.End.Value.Ticks).AddDays( 1 ),
}; var secondOccurence=new Event
{
Id=new Guid();
Start=new DateTime( event.Start.Value.Ticks).AddDays( 2 ),
End=new DateTime( event.End.Value.Ticks).AddDays( 2 ),
};
recurrenceEvents.Add(firstOccurence);
recurrenceEvents.Add(secondOccurence);
}

events.AddRange(recurrenceEvents); The rationale for doing this is to mitigate against issues we have had with long running events and exceeding the Recurrence Exception max length. Doing this currently will not display these events are recurring events, meaning that we lose the functionality of the "Edit Occurrence" or "Edit Series" buttons, and lose the UI element of the recurrence icons in the scheduler. Is there a way of spoofing recurrence for events in the scheduler?

## Answer

**Nansi** answered on 08 Aug 2024

Hi Kyle, Could you please provide more details about the issues you encountered? What do you mean by exceeding the Recurrence Exception max length? In general, the appointment model needs to have a recurrence rule property, so the Scheduler expands one recurring appointment and renders the necessary number of appointments in the UI. If you create many individual appointments and you want them to function like a single built-in recurring appointment, you will have to manually implement all the built-in features of the recurring appointment. Regards, Nansi
