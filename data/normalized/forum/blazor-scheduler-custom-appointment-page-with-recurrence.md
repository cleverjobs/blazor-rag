# Blazor Scheduler Custom Appointment Page with Recurrence

## Question

**Pet** asked on 10 Sep 2024

Hi I have created a custom appointment page, which works fine, but I can't find a simple way to replicate the recurrence functionality of the standard add/edit appointment page. The only information I have been able to find is that I need to completely recreate the functionality, which seems to be a great deal of effort. Have I missed something? Is it possible to expose the recurrence object? TIA

## Answer

**Dimo** answered on 12 Sep 2024

I am copy-pasting my ticket response for community visibility. @Peter please notify us when posting duplicate forum threads and support tickets, otherwise there is a risk for two different members of our team to handle your requests.===We have a feature request to expose the recurrence editor as a standalone component. Until we implement this enhancement, I confirm that manual coding is required. It is possible to use our internal recurrence editor components even now, but we strictly don't endorse or provide technical support for such an approach. I recommend downloading our source code and looking in: Telerik.Blazor/Components/Scheduler/EditForm/ SchedulerEditForm.razor @using System.Text.Json

<Telerik.Blazor.Components.Scheduler.EditForm.RecurrenceEditor.RecurrenceIntervalEditor Rule="@MyRule" /> <Telerik.Blazor.Components.Scheduler.EditForm.RecurrenceEditor.RecurrenceEditor @bind-Rule="@MyRule" Start="@Appt.Start" /> <Telerik.Blazor.Components.Scheduler.EditForm.RecurrenceEditor.RecurrenceEndEditor Rule="@MyRule" Start="@Appt.Start" /> <TelerikButton OnClick="@( ()=> { } )"> Refresh UI </TelerikButton> <h3> <code> MyRule </code> </h3> <pre> @JsonSerializer.Serialize(MyRule, new JsonSerializerOptions() { WriteIndented=true }); </pre> @code {
private Appointment Appt { get; set; }=new () { RecurrenceRule="FREQ=WEEKLY;BYDAY=MO,WE,FR" };

private Telerik.Recurrence.RecurrenceRule? MyRule { get; set; }

protected override void OnInitialized () {
MyRule=Telerik.Recurrence.RecurrenceRule.Parse(Appt.RecurrenceRule);
}

public class Appointment {
public DateTime Start { get; set; }=DateTime.Today;
public string RecurrenceRule { get; set; }=string.Empty;
}
}

### Response

**Peter** commented on 07 Dec 2024

I've tried this but couldn't figure out how to edit just the current occurrence (not the whole series). How can I do this?
