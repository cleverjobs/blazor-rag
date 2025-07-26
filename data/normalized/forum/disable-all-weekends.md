# Disable all weekends

## Question

**And** asked on 04 Jul 2020

Hi, Is there any way to disable all weekends on Calendar control? Yes, I could create a list of disable dates but it will be a huge list. I just curious if there is some setting to do that. Thanks.

## Answer

**Svetoslav Dimitrov** answered on 06 Jul 2020

Hello Andrey, You could use a method to generate all the weekend dates and add them to the disabled dates collection. You could iterate from a start date and end date and check if the day of week is Sunday or Saturday, if so add it to the collection. Below you can see a quick sample (you can edit it to, for example, loop between your min and max dates): <TelerikCalendar SelectionMode="@CalendarSelectionMode.Single" ValueChanged="@( (DateTime d)=> OnBeginDateChangeHandlerAsync(d) )" Value="@begindate" @bind-Date="@begindate" DisabledDates="@DisabledDates">
</TelerikCalendar>

@code { protected DateTime begindate { get; set; }=DateTime.Now.AddDays( -8 ).Date;

List<DateTime> DisabledDates { get; set; }=new List<DateTime>(); private void GetWeekends ( ) { for (DateTime date=DateTime.Today; date <=DateTime.Today.AddDays( 365 ); date=date.AddDays( 1 ))
{ if (date.DayOfWeek==DayOfWeek.Sunday || date.DayOfWeek==DayOfWeek.Saturday)
DisabledDates.Add(date);
}
} protected override async Task OnInitializedAsync ( ) {
GetWeekends(); await base.OnInitializedAsync();
} async Task OnBeginDateChangeHandlerAsync ( DateTime date ) { await Task.Delay( 20 );

begindate=date;
}
} You may also find interesting this feature request for an event that would let you generate this list on demand for the current month only: [https://feedback.telerik.com/blazor/1456008-event-for-when-the-month-has-been-changed-datechanged.](https://feedback.telerik.com/blazor/1456008-event-for-when-the-month-has-been-changed-datechanged.) If that would suit your needs, Vote for it and Follow it for email status updates. Regards, Svetoslav Dimitrov
