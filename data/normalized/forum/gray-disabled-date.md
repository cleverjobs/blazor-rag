# Gray disabled date

## Question

**Gia** asked on 29 Apr 2020

Hi Is it possible gray out disabled date on Calendar control ?? Tnx

## Answer

**Svetoslav Dimitrov** answered on 30 Apr 2020

Hello Giampaolo, Thank you for participating in our Blazor community! By default the color of the disabled dates (the font color) is gray as you can see in the Calendar Disabled Dates demo on this link: [https://demos.telerik.com/blazor-ui/calendar/disabled-dates.](https://demos.telerik.com/blazor-ui/calendar/disabled-dates.) What we do when there are disabled dates is to add a CSS class - k-state-disabled, to the specific <td> that contains the date. Should you require any additional customization you can apply CSS styles by targeting the k-state-disabled class. Below you can see a quick example of that. When you run the code snippet you will see that the background color of the disabled dates cells will be gray and their font color - blue. <style>.k-state-disabled { background-color:gray; color:blue;
} </style> <div class="alert alert-info"> You will not be able to book an event hall for the dates between April 10th 2020 and April 12th 2020 (Easter Day).
You can select multiple dates. </div> @{
if (SelectedDatesList.Any())
{
DateTime firstSelectedDate=SelectedDatesList.FirstOrDefault();
DateTime lastSelectedDate=SelectedDatesList.LastOrDefault(); <div class="alert alert-success"> The event hall will be booked between <strong> @FormatDate(firstSelectedDate) and @FormatDate(lastSelectedDate) </strong> </div> if (firstSelectedDate <EasterDate && lastSelectedDate> EasterDate)
{
string firstDisabledDate=FormatDate(DisabledDatesList.FirstOrDefault());
string lastDisabledDate=FormatDate(DisabledDatesList.LastOrDefault()); <div class="alert alert-danger"> In the selected time period you will not be able to use the hall between <strong> @firstDisabledDate and @lastDisabledDate </strong> </div> }
}
} <TelerikCalendar Min="@MinDate" Max="@MaxDate" @bind-Date="@DateToNavigate" DisabledDates="@DisabledDatesList" SelectionMode="CalendarSelectionMode.Multiple" @ref="CalendarReference" ValueChanged="@SelectionHandler"> </TelerikCalendar> @code {
DateTime EasterDate { get; set; }
DateTime MinDate { get; set; }
DateTime MaxDate { get; set; }
DateTime DateToNavigate { get; set; }
List <DateTime> DisabledDatesList { get; set; }=new List <DateTime> ();
List <DateTime> SelectedDatesList { get; set; }=new List <DateTime> ();

TelerikCalendar CalendarReference;

protected override void OnInitialized()
{
EasterDate=GetEasterDate();
MinDate=EasterDate.AddMonths(-3);
MaxDate=EasterDate.AddMonths(3);
DateToNavigate=EasterDate;

DisabledDatesList=new List <DateTime> ()
{
EasterDate.AddDays(-2),
EasterDate.AddDays(-1),
EasterDate
};
}

DateTime GetEasterDate()
{
return new DateTime(2020, 4, 12);
}

void SelectionHandler()
{
SelectedDatesList=CalendarReference.SelectedDates;
SelectedDatesList.Sort();
}

string FormatDate(DateTime dateToFormat)
{
return dateToFormat.ToString("dd MMM yyyy");
}
} Regards, Svetoslav Dimitrov

### Response

**Giampaolo** answered on 30 Apr 2020

Really tnx And is it possibile set some dates with different backgruond color, without disabled it ?? tnx

### Response

**Svetoslav Dimitrov** answered on 04 May 2020

Hello Giampaolo, There is an open Feature Request on our Feedback Portal for customization template for the day cell in the Calendar. You can see it from here: [https://feedback.telerik.com/blazor/1446960-add-day-cell-customisation-templates-to-the-calendar.](https://feedback.telerik.com/blazor/1446960-add-day-cell-customisation-templates-to-the-calendar.) I have given a Vote on your behalf to raise it's popularity. You can Follow it for email notifications. Regards, Svetoslav Dimitrov
