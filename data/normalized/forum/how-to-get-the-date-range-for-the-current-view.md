# How to get the date range for the current view?

## Question

**Mik** asked on 12 Feb 2025

How can I get the start and end dates that are displayed in the current view? I understand that there is a date changed event, but that doesn't give me the entire date range of what is currently being displayed. I'd like to use that date range to then re-query the database and only pull back the events for that specific range. I currently can't find a way to get that information.

## Answer

**Hristian Stefanov** answered on 17 Feb 2025

Hi Mike, To determine the start and end dates for the current view in the Telerik UI for Blazor Scheduler, you can bind the Date and View parameters to variables. This approach allows you to calculate the date range based on the current view settings. Here's how you can achieve this: Bind the Date and View Parameters: Bind the Date and View parameters of the Scheduler to variables in your component. This helps you identify the current view and the date it is centered on. <TelerikScheduler @bind-Date="SchedulerDate" @bind-View="SchedulerView"> <!-- Your scheduler configuration --> </TelerikScheduler> @code {
private DateTime SchedulerDate { get; set; }=DateTime.Today;
private SchedulerView SchedulerView { get; set; }=SchedulerView.Week;
} Calculate the Start and End Dates: Use the bound SchedulerDate and SchedulerView to calculate the start and end dates for the current view. For instance, if the view is set to a week, calculate the start date by finding the previous Monday and the end date by finding the next Sunday. Re-query the Database: With the calculated start and end dates, you can query your database for events within that range, ensuring you only retrieve the relevant events. Regards, Hristian Stefanov Progress Telerik
