# How do you know the current date when opening an instance of a recurring appointment?

## Question

**Rol** asked on 30 Jan 2022

I use a custom dialog to edit the appointment. The appoinment.Start date and the OnEdit(SchedulerEditEventArgs) always show the start of the series, not the date of the instance I opened.

## Answer

**Roland** answered on 06 Feb 2022

I know what the problem is. I don't want to use the Telerik "Do you want to edit the series or the instance?" dialog, so I move that offscreen and click it away in code. I always click on the second button "Edit the series". Now the OnEdit handler is called with only the series data, not the instance data. But when I click on the first button "Edit the instance" OnEdit is called with both series and instance data. Problem solved.

### Response

**Svetoslav Dimitrov** answered on 02 Feb 2022

Hello Roland, You can get the start date and end day of the specific occurrence by using the args.Start and args.End fields. Below, I have added an example to showcase that. <TelerikScheduler Data="@Appointments" OnUpdate="@UpdateAppointment" OnCreate="@AddAppointment" OnDelete="@DeleteAppointment" OnEdit="@EditHandler" OnCancel="@CancelHandler" AllowCreate="true" AllowDelete="true" AllowUpdate="true" @bind-Date="@StartDate" Height="600px" @bind-View="@CurrView">
<SchedulerViews>
<SchedulerDayView StartTime="@DayStart" />
<SchedulerWeekView StartTime="@DayStart" />
<SchedulerMultiDayView StartTime="@DayStart" NumberOfDays="10" />
</SchedulerViews>
</TelerikScheduler>

@code { // sample data and scheduler settings public SchedulerView CurrView { get; set; }=SchedulerView.Week; public DateTime StartDate { get; set; }=new DateTime( 2019, 12, 2 ); public DateTime DayStart { get; set; }=new DateTime( 2000, 1, 1, 8, 0, 0 ); //the time portion is important List<SchedulerAppointment> Appointments { get; set; } async Task UpdateAppointment ( SchedulerUpdateEventArgs args ) {
SchedulerAppointment item=(SchedulerAppointment)args.Item; // perform actual data source operations here through your service await MyService.Update(item); // update the local view-model data with the service data await GetSchedulerData();
} async Task AddAppointment ( SchedulerCreateEventArgs args ) {
SchedulerAppointment item=args.Item as SchedulerAppointment; // perform actual data source operations here through your service await MyService.Create(item); // update the local view-model data with the service data await GetSchedulerData();
} async Task DeleteAppointment ( SchedulerDeleteEventArgs args ) {
SchedulerAppointment item=(SchedulerAppointment)args.Item; // perform actual data source operations here through your service await MyService.Delete(item); // update the local view-model data with the service data await GetSchedulerData(); // see the comments in the service mimic method below. } //Handlers for application logic flexibility void EditHandler ( SchedulerEditEventArgs args ) { DateTime currentOccuranceStartDate=args.Start;
DateTime currentOccuranceEndDate=args.End; SchedulerAppointment item=args.Item as SchedulerAppointment; if (!args.IsNew) // an edit operation, otherwise - an insert operation { // you can prevent opening an item for editing based on a condition if (item.Title.Contains( "vet", StringComparison.InvariantCultureIgnoreCase))
{
args.IsCancelled=true;
}
} else { // new appointment DateTime SlotStart=args.Start; // the start of the slot the user clicked DateTime SlotEnd=args.End; // the start of the slot the user clicked bool InsertInAllDay=args.IsAllDay; // whether the user started insertion in the All Day row }
} void CancelHandler ( SchedulerCancelEventArgs args ) { // you can know when a user wanted to modify an appointment but decided not to // the model you get contains the new data from the edit form so you can see what they did SchedulerAppointment item=args.Item as SchedulerAppointment;
} public class SchedulerAppointment { public Guid Id { get; set; } public string Title { get; set; } public string Description { get; set; } public DateTime Start { get; set; } public DateTime End { get; set; } public bool IsAllDay { get; set; } public string RecurrenceRule { get; set; } public List<DateTime> RecurrenceExceptions { get; set; } public Guid? RecurrenceId { get; set; } public SchedulerAppointment ( ) {
Id=Guid.NewGuid();
}
} async Task GetSchedulerData ( ) {
Appointments=await MyService.Read();
} protected override async Task OnInitializedAsync ( ) { await GetSchedulerData();
} // the following static class mimics an actual data service that handles the actual data source // replace it with your actual service through the DI, this only mimics how the API can look like and works for this standalone page public static class MyService { private static List <SchedulerAppointment> _data { get; set; }=new List<SchedulerAppointment>()
{ new SchedulerAppointment
{
Title="Board meeting",
Description="Q4 is coming to a close, review the details.",
Start=new DateTime( 2019, 12, 5, 10, 00, 0 ),
End=new DateTime( 2019, 12, 5, 11, 30, 0 )
}, new SchedulerAppointment
{
Title="Vet visit",
Description="The cat needs vaccinations and her teeth checked.",
Start=new DateTime( 2019, 12, 2, 11, 30, 0 ),
End=new DateTime( 2019, 12, 2, 12, 0, 0 )
}, new SchedulerAppointment
{
Title="Planning meeting",
Description="Kick off the new project.",
Start=new DateTime( 2019, 12, 6, 9, 30, 0 ),
End=new DateTime( 2019, 12, 6, 12, 45, 0 )
}, new SchedulerAppointment
{
Title="Trip to Hawaii",
Description="An unforgettable holiday!",
IsAllDay=true,
Start=new DateTime( 2019, 11, 27 ),
End=new DateTime( 2019, 12, 05 )
}, new SchedulerAppointment
{
Title="Morning run",
Description="Some time to clear the head and exercise.",
Start=new DateTime( 2019, 11, 27, 9, 0, 0 ),
End=new DateTime( 2019, 11, 27, 9, 30, 0 ),
RecurrenceRule="FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" }
}; public static async Task Create ( SchedulerAppointment itemToInsert ) {
itemToInsert.Id=Guid.NewGuid();
_data.Insert( 0, itemToInsert);
} public static async Task<List<SchedulerAppointment>> Read()
{ return await Task.FromResult(_data);
} public static async Task Update ( SchedulerAppointment itemToUpdate ) { var index=_data.FindIndex(i=> i.Id==itemToUpdate.Id); if (index !=-1 )
{
_data[index]=itemToUpdate;
}
} public static async Task Delete ( SchedulerAppointment itemToDelete ) { if (itemToDelete.RecurrenceId !=null )
{ // a recurrence exception was deleted, you may want to update // the rest of the data source - find an item where theItem.Id==itemToDelete.RecurrenceId // and remove the current exception date from the list of its RecurrenceExceptions } if (! string.IsNullOrEmpty(itemToDelete.RecurrenceRule) && itemToDelete.RecurrenceExceptions?.Count> 0 )
{ // a recurring appointment was deleted that had exceptions, you may want to // delete or update any exceptions from the data source - look for // items where theItem.RecurrenceId==itemToDelete.Id }

_data.Remove(itemToDelete);
}
}
} Regards, Svetoslav Dimitrov

### Response

**Roland** answered on 02 Feb 2022

I have seen the documentation, but like I said " OnEdit(SchedulerEditEventArgs) always show the start of the series ", see the attached image. The series start in januari, I open an instance in februari, and SchedulerEditEventArgs shows the series start date, not the occurrence start date.

### Response

**Svetoslav Dimitrov** commented on 04 Feb 2022

Hello Roland, Could you provide us with a sample runnable application where we can run and debug the described behavior? This would greatly help us in determining the problematic behavior and provide a solution.
