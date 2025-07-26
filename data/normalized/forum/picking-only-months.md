# Picking Only Months

## Question

**Dre** asked on 29 Mar 2021

An app needs to process data for the month - is there a way to use DatePicker and choose only the Month/Year ?? Displaying it is quite easy with Format. Thanks

## Answer

**Marin Bratanov** answered on 30 Mar 2021

Hello Drewanz, You can use the BottomView to limit how far down the user can go to. If they can go down only to the Year view they will effectively select months. You can also set a Format that shows the month and year only too. Here is an example of both: @selectedDate <br /> <TelerikDatePicker @bind-Value="@selectedDate" BottomView="@CalendarView. Year " Format="MMM yy"> </TelerikDatePicker> @code{
DateTime selectedDate { get; set; }=DateTime.Now;
} Regards, Marin Bratanov Progress Telerik

### Response

**Drewanz** answered on 30 Mar 2021

PERFECT ! Many thanks!
