# TelerikCalendar header is unexpected transparent

## Question

**Ali** asked on 20 May 2025

I'm using a TelerikCalendar component in a TelerikAnimationContainer and everything works fine, except that the calendar header is transparent and the background text is visible when the calendar pops up. I've tried setting a higher z-index to the calendar, but it doesn't helped. <style>.picker-popup>.k-calendar { border-width: 0;
}.date-time-box-calendar { width: 26vw; height: 30vw; background-color: beige;
} </style> <TelerikAnimationContainer @ref="@calendarContainer" Class="picker-popup k-calander"> <TelerikCalendar class="date-time-box-calendar" Value="@Source" View="CalendarView.Month" Views="2" ValueChanged="@OnDateChangeHandler"> </TelerikCalendar> </TelerikAnimationContainer> @{
async Task OnClickCalendarHanlder()
{
await ToggleCalendar();
}

async Task ToggleCalendar()
{
await calendarContainer.ToggleAsync();
}
} Any idea, how can I get the calendar to most front view? What is my mistake?
