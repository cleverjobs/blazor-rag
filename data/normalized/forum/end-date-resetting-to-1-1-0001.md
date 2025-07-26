# End Date resetting to 1/1/0001

## Question

**Mar** asked on 23 Mar 2021

If you look at the two attached screen shots. The date range picker is initialized with a start and end date. If the start date is changed, the end date is reset to 1/1/0001. I have configured the date range picker as: <TelerikDateRangePicker @bind-StartValue="@NewRecSet.StartDate" @bind-EndValue="@NewRecSet.EndDate" Min="DateTime.Today" /> My expectation is that the end date should not change from what was set as the initial value.

## Answer

**Svetoslav Dimitrov** answered on 26 Mar 2021

Hello Marc, The behavior you are experiencing for the component is expected, let me provide some additional information. If you select a StartDate that is already in the Range (range being 20th Match 2021 to 27th March 2021 ) the end date will remain the same since the Range is not changed, only its start date. When you select a new date (out of the range) the component clears the value for the EndDate too so that your user can select a new one. The reason behind that is because the user might a date which is after the predefined value of the EndDate. Let me know if you have any additional questions or suggestions for improvements. Regards, Svetoslav Dimitrov Progress Telerik
