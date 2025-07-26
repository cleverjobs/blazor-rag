# Select all the content of DatePicker on click

## Question

**nee** asked on 29 Feb 2024

When user click on the input field of DatePicker, it either select date, or month, or year, but we want to select whole date input field like it highlights/selects whole content on Tab key. Tried with the following code but still no luck. <span @onfocusin="@FocusHandler"> <TelerikDatePicker @bind-Value="@SelectedDate" Min="@Min" Max="@Max" Format="MM/dd/yyyy" DebounceDelay="@DebounceDelay" ShowWeekNumbers="true" @ref="@DateRef"> <DatePickerFormatPlaceholder Day="day" Month="month" Year="year" /> </TelerikDatePicker> </span> @code {
private DateTime? SelectedDate { get; set; }
private DateTime Max=new DateTime(2050, 12, 31);
private DateTime Min=new DateTime(1950, 1, 1);
private int DebounceDelay { get; set; }=200;
private TelerikDatePicker<DateTime?> DateRef { get; set; }
private async Task FocusHandler()
{
await DateRef.FocusAsync();
}
} It gets selected on buttonclick though (code snippet below where it selects all content on button click) - <TelerikButton OnClick="@FocusHandler"> Focus Date </TelerikButton> <TelerikDatePicker @bind-Value="@SelectedDate" Min="@Min" Max="@Max" Format="MM/dd/yyyy" DebounceDelay="@DebounceDelay" ShowWeekNumbers="true" @ref="@DateRef"> <DatePickerFormatPlaceholder Day="day" Month="month" Year="year" /> </TelerikDatePicker> @code {
private DateTime? SelectedDate { get; set; }
private DateTime Max=new DateTime(2050, 12, 31);
private DateTime Min=new DateTime(1950, 1, 1);
private int DebounceDelay { get; set; }=200;
private TelerikDatePicker<DateTime?> DateRef { get; set; }
private async Task FocusHandler()
{
await DateRef.FocusAsync();
}
} Any help would be appreciated! TIA. -Neelima

### Response

**Brad** commented on 18 Jun 2024

Hristian, I reviewed the May(Q2) release and I do not see the documentation on how to implement this feature on the TelerikDatePicker control. Please advise. Thanks

### Response

**Hristian Stefanov** commented on 20 Jun 2024

Hi Brad, I confirm that the built-in "select all content" functionality is currently implemented only for the TelerikNumericTextBox component. Allow me to provide more context on the decision behind this. The current approach used for the NumericTextBox is not applicable to the DatePicker because the DatePicker's input is segmented. The primary scenario where such functionality might be needed is when deleting the entire date. However, this need is already addressed by the ShowClearButton parameter that toggles a Clear button, which allows users to delete the entire date with a single click. For keyboard users, holding Shift while pressing Delete achieves the same result. Since the Clear button simplifies the process of deleting the entire date, the need for a "select all content" feature in the DatePicker has been reduced. However, if you require the "select all content" functionality for purposes other than deleting the date, please provide more details so we can reconsider adding this feature to the DatePicker. I eagerly anticipate hearing back from you. Kind Regards, Hristian

## Answer

**Hristian Stefanov** answered on 29 Feb 2024

Hi Neelima, A feature request for the desired functionality to highlight the entire content in the date input has already been submitted on our public feedback portal: Always highlight / select all content of the input on focus. This enhancement is already scheduled for around May (Q2 this year). You can subscribe to the public item to receive email notifications for further status updates. Regards, Hristian Stefanov Progress Telerik
