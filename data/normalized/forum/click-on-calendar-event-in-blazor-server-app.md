# Click on Calendar event in Blazor Server app

## Question

**And** asked on 28 Jun 2020

Hello, I need to update some greed each time a user clicks on calendar. Now we have two events in calendar. The OnChange event fires on date input focus loses, so it not helps me. The ValueChanged works fine but if I type date manually then I lose date input focus on grid update and cannot finish typing. Like, I try to change 6/1/2020 to 6/11/2020. It works if I fast enough but I would prefer to disable the date input field and have the calendar available only. Is it possible to do? Another event OnClick on calendar would help but looks like it is not exist. Thanks.

## Answer

**Marin Bratanov** answered on 28 Jun 2020

Hi Andrey, If redrawing the page causes the date input to lose focus, then the redrawing causes the issue - either there is code that steals the focus, or too much is redrawn, and that's something that the app needs to fix. That said, if you only need a calendar, you can use a standalone calendar component: [https://demos.telerik.com/blazor-ui/calendar/selection.](https://demos.telerik.com/blazor-ui/calendar/selection.) Depending on how you want to select dates, there are suitable events for you to handle to receive the user choice. You can read more in the documentation [https://docs.telerik.com/blazor-ui/components/calendar/selection](https://docs.telerik.com/blazor-ui/components/calendar/selection) When the user clicks on a date, they select it, so with single selection that fires the ValueChanged event. With Multiple selection it also changes the selected range, but it has a different meaning in range selection. That difference in behavior does not exist in a date picker, so it exposes OnChange and ValueChanged only, and you can choose which event to use depending on when you want it to fire. ValueChanged is more immediate but it is a two-way data binding event, and with all such events, it might be better suited to synchronous logic for the view model, while OnChange is better suited to async operations. Regards, Marin Bratanov
