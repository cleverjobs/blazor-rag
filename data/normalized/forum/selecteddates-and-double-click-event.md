# SelectedDates and Double-click event

## Question

**Dav** asked on 14 Oct 2019

Hi, We use the Kendo Calendar for a page on an internal site that i'm trying to update with Blazor. The Kendo Calendar highlights multiple date that someone has booked, they can double-click to add/remove dates. I don't seem to be able to accomplish this with the Blazor Calendar, I can pre-load existing dates fine, but if I select a new date the pre-loaded dates vanish. Do I need to reload dates on each click? Also, will we get a double-click handler in the future? <TelerikCalendar Date="@startDate" Min="@min" View="CalendarView.Month" SelectionMode="@CalendarSelectionMode.Multiple" SelectedDates="@selectedDates" ValueChanged="@CalendarChangeHandler" @ref="calendar"> </TelerikCalendar> @code { DateTime startDate=DateTime.Today; DateTime min=DateTime.Today.AddDays(1); private List<DateTime> selectedDates { get; set; } private Telerik.Blazor.Components.TelerikCalendar calendar; protected override async Task OnInitializedAsync() { selectedDates=_timeOffFactory.GetDates(); } private void CalendarChangeHandler(DateTime newDate) { selectedDates.Add(newDate); } }

## Answer

**Marin Bratanov** answered on 14 Oct 2019

Hi David, Are you highlighting the dates in the Kendo calendar through templates like this: [https://demos.telerik.com/kendo-ui/calendar/template?](https://demos.telerik.com/kendo-ui/calendar/template?) I am asking because the Blazor Calendar does not have that feature yet (which would, by the way, allow you to hook the desired events easily in the template markup). To answer all the questions explicitly as well: At the moment, this is the expected behavior, single clicks perform selection and this is the only similar feature available right now. Highlighting is not available. We are working on a Scheduler component, though, and it will let you add events. Will there be a double click event - I am not sure there will be an out-of-the-box one. This generally a very tough decision for all components because templates in Blazor are super powerful and can be used to hook such events. At this point we don't know if we will start exposing events outside of templates, because then using the templates is likely to break the built-in events by overriding the rendering they attach to. To keep the current dates selection, the user must hold the Ctrl key while clicking on a day. This is how multiple selection is implemented, this works in the same fashion file selection in places like Windows Explorer works. For the time being I can suggest you keep a list of the items you want to denote as always selected, and ensure that they are always present in the selection, so the user effectively cannot deselect them: <TelerikCalendar SelectionMode="@CalendarSelectionMode.Multiple" ValueChanged="@MultipleSelectionChangeHandler" DisabledDates="@DisabledDates" SelectedDates="@chosenDates" @bind-Date="@startDate" @ref="multipleSelCalendar">
</TelerikCalendar>
<br />
@if (chosenDates !=null && chosenDates.Count> 0 )
{
<ul>
@foreach (DateTime date in chosenDates)
{
<li>@date.ToString( "dd MMM yyyy" )</li>
}
</ul>
}

@code { private DateTime startDate=new DateTime( 2019, 4, 1 ); private List<DateTime> DisabledDates=new List<DateTime>() { new DateTime( 2019, 4, 1 ), new DateTime( 2019, 4, 2 ) }; private List<DateTime> chosenDates { get; set; } private List<DateTime> origSelection { get; set; } private Telerik.Blazor.Components.TelerikCalendar multipleSelCalendar; private void MultipleSelectionChangeHandler ( ) {
chosenDates=multipleSelCalendar.SelectedDates; //ensure that, after user selection, the static ones you want are still selected foreach (DateTime origItem in origSelection)
{ if (!chosenDates.Contains(origItem))
{
chosenDates.Add(origItem);
}
}
} protected override async Task OnInitializedAsync ( ) {
origSelection=new List<DateTime>()
{ new DateTime( 2019, 4, 3 ), new DateTime( 2019, 4, 5 )
}; if (chosenDates==null )
{
chosenDates=new List<DateTime>();
} // populate the desired initial selection in the actual selection foreach (DateTime item in origSelection)
{
chosenDates.Add(item);
}
}
} Perhaps if templates get implemented you will be able to denote the special days from model values. At this point I cannot say how/if this would get implemented. I would encourage you to post a feature request for such a feature in the

### Response

**Marin Bratanov** answered on 15 Oct 2019

Hi all, I put this up in the Knowledge Base for the time being, because I can't guarantee when a better solution will be available: [https://docs.telerik.com/blazor-ui/knowledge-base/calendar-always-selected-dates.](https://docs.telerik.com/blazor-ui/knowledge-base/calendar-always-selected-dates.) Regards, Marin Bratanov

### Response

**David Rhodes** answered on 15 Oct 2019

Thanks for the update The downside here is that I would need to call the database on every interaction with the calendar to get the list of dates, your example uses a static list. In our MVC/Kendo version I have an array on the client which I can add to easily, so I only call the db once on first load. Maybe it's me not understanding Blazor fully yet!

### Response

**Marin Bratanov** answered on 15 Oct 2019

Hi David, The "origSelection" is the list that should come from the database and is local for the component, much like a local array in an MVC view would be used on the client in jQuery. In my example, I hardcode a few items in the OnInitialized event, you should instead call the appropriate service to fetch that same data. Where it comes from is not really relevant for this case, that is up to the blazor app itself. Thus, you need to call the database only when the component initializes (you can further even implement state in the app so that when it gets initialized subsequently, it can use cached values from the app instead of going to the database). Regards, Marin Bratanov

### Response

**David Rhodes** answered on 16 Oct 2019

Thanks, got it now! Do you know how I can maintain the calendar month view when selecting? eg at the moment when I select a date in November, it changes the display back to October.

### Response

**Marin Bratanov** answered on 16 Oct 2019

Hi David, This can happen if you don't use two-way binding for the variable that controls the view or the date. Regards, Marin Bratanov

### Response

**David Rhodes** answered on 16 Oct 2019

I use <TelerikCalendar Date="@startDate" ValueChanged="@CalendarChangeHandler"...> private DateTime min=DateTime.Today.AddDays(1); I don't see the same behaviour in your demo though, that seems to work fine [https://demos.telerik.com/blazor-ui/calendar/overview](https://demos.telerik.com/blazor-ui/calendar/overview)

### Response

**David Rhodes** answered on 16 Oct 2019

Fixed it, not sure why I was binding startdate, wasn't needed
