# How to set a default Title

## Question

**Toy** asked on 20 Feb 2025

Is there a way to set a default title when a day is clicked to add new event in the Telerik Scheduler? And to set the IsAllDay to true by default? I only need to do this when calendar is double-clicked to add new event. Thanks, Toya

## Answer

**Hristian Stefanov** answered on 21 Feb 2025

Hi Toya, To set a default title and mark an event as "All Day" when double-clicking on a day in the Telerik Scheduler, you can handle the OnEdit event of the Scheduler: private void EditHandler ( SchedulerEditEventArgs args ) {
SchedulerAppointment item=args.Item as SchedulerAppointment; if (!args.IsNew) // an edit operation, otherwise - an insert operation { //some custom logic } else { item.Title="Test";
item.IsAllDay=true; }
} Regards, Hristian Stefanov Progress Telerik

### Response

**Toya** commented on 21 Feb 2025

I did that and it updates the items after the appointment has been created, the form requires you to enter title. I wasn't able to get that to work so that the popup opens up with title and isallday checked.

### Response

**Hristian Stefanov** commented on 25 Feb 2025

Hi Toya, I have prepared for you a runnable example below that demonstrates a predefined title and isallday checked in the editing popup. Please run and test it to see the result. <TelerikScheduler Data="@Appointments" OnUpdate="@UpdateAppointment" OnCreate="@AddAppointment" OnDelete="@DeleteAppointment" OnEdit="@EditHandler" OnCancel="@CancelHandler" AllowCreate="true" AllowDelete="true" AllowUpdate="true" @bind-Date="@StartDate" Height="600px" @bind-View="@CurrView"> <SchedulerViews> <SchedulerDayView StartTime="@DayStart" /> <SchedulerWeekView StartTime="@DayStart" /> <SchedulerMultiDayView StartTime="@DayStart" NumberOfDays="10" /> </SchedulerViews> </TelerikScheduler> @code {
private SchedulerView CurrView { get; set; }=SchedulerView.Week;
private DateTime StartDate { get; set; }=new DateTime(2019, 12, 2);
private DateTime DayStart { get; set; }=new DateTime(2000, 1, 1, 8, 0, 0); //the time portion is important

private List <SchedulerAppointment> Appointments { get; set; }

private async Task UpdateAppointment(SchedulerUpdateEventArgs args)
{
SchedulerAppointment item=(SchedulerAppointment)args.Item;

await MyService.Update(item);

await GetSchedulerData();
}

private async Task AddAppointment(SchedulerCreateEventArgs args)
{
SchedulerAppointment item=args.Item as SchedulerAppointment;

await MyService.Create(item);

await GetSchedulerData();
}

private async Task DeleteAppointment(SchedulerDeleteEventArgs args)
{
SchedulerAppointment item=(SchedulerAppointment)args.Item;

await MyService.Delete(item);

await GetSchedulerData();
} private void EditHandler(SchedulerEditEventArgs args)
{
SchedulerAppointment item=args.Item as SchedulerAppointment;
if (!args.IsNew) // an edit operation, otherwise - an insert operation
{
//some custom logic
}
else
{
item.Title="Test";
item.IsAllDay=true;
}
} private void CancelHandler(SchedulerCancelEventArgs args)
{
SchedulerAppointment item=args.Item as SchedulerAppointment;
}

public class SchedulerAppointment
{
public Guid Id { get; set; }
public string Title { get; set; }
public string Description { get; set; }
public DateTime Start { get; set; }
public DateTime End { get; set; }
public bool IsAllDay { get; set; }
public string RecurrenceRule { get; set; }
public List <DateTime> RecurrenceExceptions { get; set; }
public Guid? RecurrenceId { get; set; }

public SchedulerAppointment()
{
Id=Guid.NewGuid();
}
}

private async Task GetSchedulerData()
{
Appointments=await MyService.Read();
}

protected override async Task OnInitializedAsync()
{
await GetSchedulerData();
}

public static class MyService
{
private static List <SchedulerAppointment> _data { get; set; }=new List <SchedulerAppointment> ()
{
new SchedulerAppointment
{
Title="Board meeting",
Description="Q4 is coming to a close, review the details.",
Start=new DateTime(2019, 12, 5, 10, 00, 0),
End=new DateTime(2019, 12, 5, 11, 30, 0)
},

new SchedulerAppointment
{
Title="Vet visit",
Description="The cat needs vaccinations and her teeth checked.",
Start=new DateTime(2019, 12, 2, 11, 30, 0),
End=new DateTime(2019, 12, 2, 12, 0, 0)
},

new SchedulerAppointment
{
Title="Planning meeting",
Description="Kick off the new project.",
Start=new DateTime(2019, 12, 6, 9, 30, 0),
End=new DateTime(2019, 12, 6, 12, 45, 0)
},

new SchedulerAppointment
{
Title="Trip to Hawaii",
Description="An unforgettable holiday!",
IsAllDay=true,
Start=new DateTime(2019, 11, 27),
End=new DateTime(2019, 12, 05)
},

new SchedulerAppointment
{
Title="Morning run",
Description="Some time to clear the head and exercise.",
Start=new DateTime(2019, 11, 27, 9, 0, 0),
End=new DateTime(2019, 11, 27, 9, 30, 0),
RecurrenceRule="FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
}
};

public static async Task Create(SchedulerAppointment itemToInsert)
{
itemToInsert.Id=Guid.NewGuid();
_data.Insert(0, itemToInsert);
}

public static async Task<List <SchedulerAppointment>> Read()
{
return await Task.FromResult(_data);
}

public static async Task Update(SchedulerAppointment itemToUpdate)
{
var index=_data.FindIndex(i=> i.Id==itemToUpdate.Id);
if (index !=-1)
{
_data[index]=itemToUpdate;
}
}

public static async Task Delete(SchedulerAppointment itemToDelete)
{
if (itemToDelete.RecurrenceId !=null)
{
// a recurrence exception was deleted, you may want to update
// the rest of the data source - find an item where theItem.Id==itemToDelete.RecurrenceId
// and remove the current exception date from the list of its RecurrenceExceptions
}

if (!string.IsNullOrEmpty(itemToDelete.RecurrenceRule) && itemToDelete.RecurrenceExceptions?.Count> 0)
{
// a recurring appointment was deleted that had exceptions, you may want to
// delete or update any exceptions from the data source - look for
// items where theItem.RecurrenceId==itemToDelete.Id
}

_data.Remove(itemToDelete);
}
}
} Kind Regards, Hristian

### Response

**Toya** commented on 25 Feb 2025

Thank you! Once I saw the example I understood how it worked.
