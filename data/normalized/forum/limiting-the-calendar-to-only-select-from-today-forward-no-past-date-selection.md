# Limiting the calendar to only select from today forward (no past-date selection)

## Question

**che** asked on 11 Aug 2021

Is there a way to prevent the user from selecting dates in the past? When the current month is shown, I assume I need to create a List<DateTime> containing all the dates in the current month that are in the past and assign that List to the calendar's DisabledDates. If there is another way, please advise. The other part of this question is: How we prevent the user from even viewing past months? Thanks a lot!

## Answer

**Nadezhda Tacheva** answered on 16 Aug 2021

Hi Francis, While setting the Min value for the Calendar is the easier approach as Matthias proposed, you have indeed found a bug and the scenario is very specific. It appears that if the Min parameter of the Calendar excludes at least one whole month of the current year and you navigate to next year, you cannot navigate back to the current year from the Decade view. You can only navigate to future years. The Today button, however works as expected and clicking it will navigate you to the correct year. With the above being said, I opened a bug report in our public feedback portal that you can find here - If the Min parameter excludes a whole month of the current year and you navigate to next year, you cannot navigate back to the current year from the Decade view. I have added your vote to increase its popularity as we are prioritizing the bug fixes based on the community interest and demand. As I opened the report on your behalf, you are subscribed and will receive email notifications when its status changes. This is the best way to keep in track with the progress of the bug as once we know which release will contain its fix, we will update its status in the feedback portal and you will be notified via email accordingly. In regards to your second concern - preventing the user from even viewing past months - you can use some custom CSS to achieve that. For the disabled dates/months/years we add class called k-state-disabled. You can use that to hide the disabled months in the desired view. You can also use your dev tools to inspect and find the correct selector for the view, so you hide only the disabled elements in the corresponding view. The example below demonstrates how to hide the disabled months in the year view. <style>
.k-calendar-yearview .k-state-disabled{
visibility:hidden;
}
</style> <TelerikCalendar Min="@min" Max="@max" @bind-Date="@theDate">
</TelerikCalendar>

@code { private DateTime min=DateTime.Today; private DateTime max=new DateTime( 2025, 12, 31 ); private DateTime theDate { get; set; }=DateTime.Now;
} I hope you will find the above information useful. if any further questions appear, please let us know. We will be happy to step in and assist. Last but not least, as a small gesture of gratitude for reporting the bug, I have added some Telerik points to your account. Regards, Nadezhda Tacheva Progress Telerik

### Response

**chesk345** commented on 17 Aug 2021

Thank you - I will try your suggestion shortly - I have to focus on another area for the moment.

### Response

**Matthias** answered on 11 Aug 2021

Hi, try this: <TelerikCalendar Date="aDate" OnCellRender="RenderCell"> </TelerikCalendar> code DateTime aDate { get; set; } void RenderCell ( CalendarCellRenderEventArgs args ) { if (args.Date <DateTime.Today)
{
args.Class="not-allowed-cell";
}
} style .not-allowed-cell { pointer-events: none; cursor: not-allowed; background-color: whitesmoke;
} regards Matthias

### Response

**chesk345** commented on 11 Aug 2021

Hi Matthias... This works in the cells of the monthly calendar, but it has the issue with the year selection that I describe under your second answer below. Current Year cannot be returned to:

### Response

**Matthias** answered on 11 Aug 2021

by the way, it is even easier if you specify the minimum. <TelerikCalendar Date="aDate" Min="DateTime.Today"> </TelerikCalendar> Then past months can't be shown via another view either.

### Response

**chesk345** commented on 11 Aug 2021

HI Mattias - This looks like exactly what I need, but I may have found a bug. If I select a future year (say, 2022) and then try to return to the current year (2021) it will not allow the change back to 2021. The issue happens in 2.25.0 and 2.26.0. I will have a look at the longer solution above as a work around...

### Response

**Nadezhda Tacheva** answered on 16 Aug 2021

Hi Matthias, I have added some Telerik points to your account as well for proactively assisting Francis with resolving the case. Thank you for being a valuable member of the Telerik community! Regards, Nadezhda Tacheva Progress Telerik

### Response

**Matthias** commented on 16 Aug 2021

Hi Nadezhda, Thank you very much - I could not really help much. Greetings from Berlin Matthias

### Response

**chesk345** commented on 17 Aug 2021

Thank you both, Nadezhda & Matthias.

### Response

**Nadezhda Tacheva** answered on 17 Aug 2021

Hi Francis, Meanwhile, I was able to further investigate the approach proposed by Matthias for handling the OnCellRender event of the Calendar and adding styles to visually disable the past dates. It appears that in the decade view the not-allowed-cell class is also applied to the cells holding the years that contain dates with this class (in this case including 2021). So, to also cover the other Calendar views you need to specify separate conditions for them in which the not-allowed-cell class will be applied. The CalendarCellRenderEventArgs contain a field for the CalendarView, so you can easily check the current view. I have prepared a sample demonstrating how to achieve the described approach. I added it in an admin edit of the public bug report here. You may use it as a workaround by the time the bug is fixed. Regards, Nadezhda Tacheva
