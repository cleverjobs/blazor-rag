# Weeknumbers in DatePicker

## Question

**Mau** asked on 30 Jun 2020

Is it possible to show the weeknumbers in a DatePicker? We work most of the time with weeknumbers instead of a date so people know they have to select e.g. the monday of week 27 instead of 29-06-2020 Thanks, Maurice

## Answer

**Svetoslav Dimitrov** answered on 30 Jun 2020

Hello Maurice, I have opened a Feature Request on our Feedback Portal regarding adding a week number column in the DatePicker, like this example, you can see it here. I have given a Vote on your behalf and you can Follow it for email notifications. To get the week of the year you could use either the ValueChanged or OnChange events for the DatePicker and pass that DateTime object to a custom method that returns the week number. I have created a code sample, below, where I use the OnChange event for the DatePicker and display the week. @using System.Globalization; <TelerikDatePicker @bind-Value="datePickerValue" OnChange="@MyChangeHandler" /> <br> <div> The selected date @datePickerValue.ToShortDateString() is in @weekOfYear week of the year. </div> @code {
DateTime datePickerValue { get; set; }=DateTime.Now;

int weekOfYear { get; set; }

void MyChangeHandler(object input)
{
DateTime userInput=(DateTime)input;
weekOfYear=GetWeekOfYear(userInput);
}

int GetWeekOfYear(DateTime date)
{
CultureInfo culture=new CultureInfo("en-US");
Calendar cal=culture.Calendar;

CalendarWeekRule weekRule=culture.DateTimeFormat.CalendarWeekRule;
DayOfWeek firstDayOfWeek=culture.DateTimeFormat.FirstDayOfWeek;

return cal.GetWeekOfYear(date, weekRule, firstDayOfWeek);
}
} Regards, Svetoslav Dimitrov
