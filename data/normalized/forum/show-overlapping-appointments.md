# Show overlapping appointments

## Question

**Kyl** asked on 18 Apr 2025

How much control do we have for displaying overlapping appointments? Right now, they show side-by-side which makes them hard to read: Is it possible to lay them out differently so they overlap, giving more space to read the contents. Similar to how Google Calendar does it.

## Answer

**Anislav** answered on 22 Apr 2025

There’s no built-in support for changing how overlapping appointments are rendered. One possible workaround is to simplify the information shown in the appointment title and display more details in a custom tooltip. Here's an example: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/scheduler-custom-appointment-tooltips](https://www.telerik.com/blazor-ui/documentation/knowledge-base/scheduler-custom-appointment-tooltips) Regards, Anislav Atanasov

### Response

**Dimo** answered on 22 Apr 2025

Hi Kyle, Google Calendar's approach seems to rely on a fixed font size and text height, which we don't have the luxury to assume lightly. And even their overlapping approach doesn't work well if the appointment titles become longer or there is not enough horizontal space: While the described feature is surely possible to implement (even with a random font size), I personally doubt about its cost-benefit ratio and business value. Nevertheless, I will discuss this with the team on our weekly feature request review. In the meantime, if your scenario involves a lot or appointments at the same time, then I recommend the Day and Agenda views, which provide more real estate and better readability. Or, you can consider a Tooltip integration with a Scheduler item template. (The Scheduler Appointment Tooltips KB uses a separate tooltip instance for each appointment, which is not efficient. An update is already awaiting a review.) <TelerikScheduler Data="@SchedulerData" @bind- Date="@SelectedDate" Height="60vh"> <SchedulerViews> <SchedulerWeekView StartTime="@StartTime" /> <SchedulerMonthView /> </SchedulerViews> <ItemTemplate> @{ var dataItem=(Appointment)context; } <div class="k-event-template scheduler-tooltip-target" data-id="guid-@dataItem.Id" style="height:100%"> @dataItem.Title </div> </ItemTemplate> </TelerikScheduler> <TelerikTooltip TargetSelector=".scheduler-tooltip-target"> <Template> @{ var appointment=GetAppointmentById(context.DataAttributes["id"]); } <div> @appointment.Title </div> <div> @appointment.Start.ToString("g") - @appointment.End.ToString("g") </div> </Template> </TelerikTooltip> @code {
private SchedulerDataService AppointmentService=new ();

private DateTime SelectedDate { get; set; }=DateTime.Today;
private DateTime StartTime { get; set; }=DateTime.Today.AddHours( 7 );

private List<Appointment> SchedulerData { get; set; }=new ();

private Appointment GetAppointmentById ( string id ) { return SchedulerData.First( x=> string.Concat( "guid-", x.Id)==id);
}

protected override async Task OnInitializedAsync ( ) {
SchedulerData=await AppointmentService.GetAppointmentsAsync();
}

public class SchedulerDataService {
public async Task<List<Appointment>> GetAppointmentsAsync ( ) { await Task.Delay( 1 ); return GetAppointments();
}

public List<Appointment> GetAppointments ( ) {
List<Appointment> data=new List<Appointment>();
DateTime baselineTime=GetStartTime();

data.Add( new Appointment
{
Title="Vet visit",
Description="The cat needs vaccinations and her teeth checked.",
Start=baselineTime.AddHours( 3 ),
End=baselineTime.AddHours( 3 ).AddMinutes( 30 )
});
data.Add( new Appointment
{
Title="Trip to Hawaii",
Description="An unforgettable holiday!",
IsAllDay=true,
Start=baselineTime.AddDays(- 10 ),
End=baselineTime.AddDays(- 2 )
});
data.Add( new Appointment
{
Title="Jane's birthday party",
Description="Make sure to get her fresh flowers in addition to the gift.",
Start=baselineTime.AddDays( 5 ).AddHours( 10 ),
End=baselineTime.AddDays( 5 ).AddHours( 18 ),
});
data.Add( new Appointment
{
Title="One-on-one with the manager",
Start=baselineTime.AddDays( 2 ).AddHours( 3 ).AddMinutes( 30 ),
End=baselineTime.AddDays( 2 ).AddHours( 3 ).AddMinutes( 45 ),
});
data.Add( new Appointment
{
Title="Brunch with HR",
Description="Performance evaluation of the new recruit.",
Start=baselineTime.AddDays( 3 ).AddHours( 3 ),
End=baselineTime.AddDays( 3 ).AddHours( 3 ).AddMinutes( 45 )
});
data.Add( new Appointment
{
Title="Interview with new recruit",
Description="See if John will be a suitable match for our team.",
Start=baselineTime.AddDays( 3 ).AddHours( 1 ).AddMinutes( 30 ),
End=baselineTime.AddDays( 3 ).AddHours( 2 ).AddMinutes( 30 )
});
data.Add( new Appointment
{
Title="Conference",
Description="The big important work conference. Don't forget to practice your presentation.",
Start=baselineTime.AddDays( 6 ),
End=baselineTime.AddDays( 11 ),
IsAllDay=true });
data.Add( new Appointment
{
Title="New Project Kickoff",
Description="Everyone assemble! We will also have clients on the call from a later time zone.",
Start=baselineTime.AddDays( 3 ).AddHours( 8 ).AddMinutes( 30 ),
End=baselineTime.AddDays( 3 ).AddHours( 11 ).AddMinutes( 30 )
});
data.Add( new Appointment
{
Title="Get photos",
Description="Get the printed photos from last week's holiday. It's on the way from the vet to work.",
Start=baselineTime.AddHours( 2 ).AddMinutes( 15 ),
End=baselineTime.AddHours( 2 ).AddMinutes( 30 )
}); return data;
}

public DateTime GetStartTime ( ) {
DateTime dt=DateTime.Now;
int daysSinceMonday=dt.DayOfWeek - DayOfWeek.Monday; return new DateTime(dt.Year, dt.Month, dt.Day - daysSinceMonday, 8, 0, 0 );
}
}

public class Appointment {
public Guid Id { get; set; }
public string Title { get; set; }=string.Empty;
public DateTime Start { get; set; }
public DateTime End { get; set; }
public bool IsAllDay { get; set; }
public string Description { get; set; }=string.Empty;

public Appointment ( ) { var rand=new Random();
Id=Guid.NewGuid();
}
}
} Regards, Dimo Progress Telerik

### Response

**Kyle** commented on 22 Apr 2025

Thank you for bringing it up with the team. I understand there are likely challenges but I wouldn't say there's no business value. We're looking at workarounds now because of this. The use case is we want customers to choose from a list of available slots to schedule. The slots are four hours long. Here's how it's rendered: This isn't super useful as it stands so we'll investigate the tooltip idea and will likely have to enable a day view which we were hoping to avoid as users will have to click back and forth to different days. We'll also likely need to play with the CSS to make the borders a little more obvious. I appreciate the code snippets.

### Response

**Dimo** commented on 23 Apr 2025

It seems to me that the app is using "empty" appointments to simulate predefined slots for the users to choose from? As a result, the Scheduler renders the maximum possible number of appointments by default. Do I understand correctly? If yes, then I am afraid the discussed request for appointment overlapping becomes less compelling, because the component usage deviates from the core idea and I can't remember seeing something like this before. Have you researched or considered different UI to facilitate slot selection? In terms of built-in features, perhaps we should think of ways to enhance the slots UI or the creation of new appointments, rather than the existing "appointments". This will make the component less cluttered in scenarios like yours. If not, then please elaborate what does the screenshot represent.

### Response

**Kyle** commented on 30 Apr 2025

Hi Dimo, Your understanding is correct. It's to select from a list of pre-defined empty slots. We decided on the scheduler because it's similar to how we present the information in other parts of the platform but that's a good suggestion. It could be worth examining other ways of presenting the information. The rules are fairly complicated and vary between clients so I don't want to turn this into an unpaid consulting session. We'll take a closer look at the requirements and see if we can come up with some alternatives. I appreciate the suggestion and the offer to brainstorm. -- Kyle
