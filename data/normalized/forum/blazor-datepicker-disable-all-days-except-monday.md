# Blazor DatePicker Disable all days except Monday

## Question

**MID** asked on 26 Apr 2022

Hi, I'm coming from a Kendo JQuery background and currently creating an app using Blazor UI. I can see the datepicker can disable a range of dates but I need to configure it to disable all days which are not Mondays. Is this possible?

## Answer

**Hristian Stefanov** answered on 27 Apr 2022

Hello, I'm glad to see you are creating a Blazor app. To disable all dates except Monday, use the DatePicker DisabledDates parameter. Here is an example I prepared for you: <TelerikDatePicker @bind-Value="datePickerValue" Format="dd MMMM yyyy" Min="@Min" Max="@Max" DisabledDates="DisabledDates"> </TelerikDatePicker> @code {
IEnumerable <DateTime> GetDaysBetween(DateTime start, DateTime end)
{
for (DateTime i=start; i <end; i=i.AddDays(1))
{
yield return i;
}
}

protected override async Task OnInitializedAsync()
{
var disabledDates=GetDaysBetween(Min, Max)
.Where(d=> d.DayOfWeek !=DayOfWeek.Monday);

DisabledDates=new List <DateTime> (disabledDates);
}

private List <DateTime> DisabledDates=new List <DateTime> ();

DateTime datePickerValue { get; set; }=new DateTime(2022, 4, 25, 19, 30, 45);
public DateTime Min=new DateTime(1990, 1, 1, 8, 15, 0);
public DateTime Max=new DateTime(2025, 1, 1, 19, 30, 45);
} Please run and test it to see the result. In short, the example loops through all the dates between Min and Max. Then, it gets only the dates that are not Monday. I hope this helps. If there is anything else we can help with, I would be glad. Thank you. Regards, Hristian Stefanov Progress Telerik
