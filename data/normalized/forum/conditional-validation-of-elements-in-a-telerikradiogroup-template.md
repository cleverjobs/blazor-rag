# Conditional validation of elements in a TelerikRadioGroup template?

## Question

**Joh** asked on 18 Jul 2024

I have a RadioGroup that I am using a TemplateItem to display three radio buttons. When any of the radio buttons are selected another small set of form fields are enabled and if the radio button is deselected the same form fields are disabled. This works well but I would like to add field validation to the mix by enabling field validation for the form fields when they are active and removing the validation when they are not active. I've tried creating some custom attribute validators but am not sure how to pick up the action of selecting a radio button. Any ideas on how to best accomplish this task? i.e. In the picture below, I only wish to validate the Month/Date/Year if the "End by" radio is selected & only validate the numeric field if the "End after" radio is selected. <ItemTemplate Context="context2"> @{
var item=(ScheduleEndModel)context2;
if (item.Id==1)
{
AppState.Schedule.IsEndNever=false; <strong> End by: </strong> <TelerikDatePicker @bind-Value="@AppState.Schedule.EndDate" OnChange="@StateChangeTrigger" Min="@DateTime.Today" Max="@DateTime.MaxValue" Format="MM/dd/yyyy" DebounceDelay="@DebounceDelay" ShowWeekNumbers="true" Width="10vw" Enabled="@EnableOnDate"> <DatePickerFormatPlaceholder Day="Day" Month="Month" Year="Year" /> </TelerikDatePicker> }else
if (item.Id==2)
{
AppState.Schedule.IsEndNever=false; <strong id="endtype1"> End after: </strong> <TelerikNumericTextBox @bind-Value="@AppState.Schedule.EndAfterOccurrenceCount" OnChange="@StateChangeTrigger" Width="7vw" Enabled=@EnableAfterCount> </TelerikNumericTextBox> <strong> occurrence(s) </strong> }
else if (item.Id==3)
{
AppState.Schedule.IsEndNever=true; <strong> No end </strong> }
} </ItemTemplate> </TelerikRadioGroup>

## Answer

**Nadezhda Tacheva** answered on 23 Jul 2024

Hi John, Achieving conditional validation is possible but it is a matter of custom implementation. You have different options to go for, you may find some useful resources here: Conditional Form Validation. Regards, Nadezhda Tacheva
