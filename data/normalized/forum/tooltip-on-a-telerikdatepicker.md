# tooltip on a TelerikDatePicker?

## Question

**Dea** asked on 09 Feb 2023

When I try to add a tooltip on this all I get is a small black bubble icon above the control. <TelerikDatePicker Min="@Min" Max="@Max" @bind-Value="@DTR11_selectedDate" Id="DTR11" DebounceDelay="@DebounceDelay" Title="Check me off to include this in the data!" Class="tooltip-target"> </TelerikDatePicker>

## Answer

**Hristian Stefanov** answered on 14 Feb 2023

Hi Deason, The Title parameter in the DatePicker renders a text in the header of the popup (action sheet). It is applicable only when AdaptiveMode is set to Auto. That makes it different from a standard HTML title attribute. Thus, the easiest way to achieve the desired result is to wrap the DatePicker with a div element and set its class and standard title attributes. I have prepared an example for you: <TelerikTooltip TargetSelector=".tooltip-target" /> <div style="padding: 5em;"> The selected date is: @datePickerValue.ToShortDateString() <br /> <div title="Check me off to include this in the data!" class="tooltip-target"> <TelerikDatePicker @bind-Value="datePickerValue" Format="dd MMMM yyyy" Min="@Min" Max="@Max"> </TelerikDatePicker> </div> </div> @code {
DateTime datePickerValue { get; set; }=DateTime.Now;
public DateTime Min=new DateTime(1990, 1, 1, 8, 15, 0);
public DateTime Max=new DateTime(2025, 1, 1, 19, 30, 45);
} If further assistance is needed, I would be glad. Regards, Hristian Stefanov
