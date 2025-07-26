# Preselect "today" on initialization

## Question

**And** asked on 04 Jul 2020

Hi, I have a calendar control with initial date. It could be "Today" or any other date. The Calendar works fine but the initial date is not visually selected. If I click on any date it's get selected and displayed in "red" but I need it selected initially without user intervention. <TelerikCalendar SelectionMode="@CalendarSelectionMode.Single" ValueChanged="@( (DateTime d)=> OnBeginDateChangeHandlerAsync(d) )" Min="@beginmin" Max="@beginmax" @bind-Date="@begindate"> </TelerikCalendar> @code { protected DateTime begindate { get; set; }=DateTime.Now.AddDays(-8).Date; } Thanks.

## Answer

**Svetoslav Dimitrov** answered on 06 Jul 2020

Hello Andrey, You can preselect the desired date by setting the Value field of the Calendar. You can read more information on our documentation and you can see a sample code snippet on how to do that below: <TelerikCalendar SelectionMode="@CalendarSelectionMode.Single" ValueChanged="@( (DateTime d)=> OnBeginDateChangeHandlerAsync(d) )" Value="@begindate" @bind-Date="@begindate"> </TelerikCalendar> @code {
protected DateTime begindate { get; set; }=DateTime.Now.AddDays(-8).Date;

async Task OnBeginDateChangeHandlerAsync(DateTime date)
{
await Task.Delay(20);

begindate=date;
}
} Regards, Svetoslav Dimitrov

### Response

**Andrey** answered on 06 Jul 2020

Hi Svetoslav, My bad! I expected that the @bind-Date="@begindate" will do the work. Thanks!
