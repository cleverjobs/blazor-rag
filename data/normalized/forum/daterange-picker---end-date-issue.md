# DateRange Picker - End date issue

## Question

**Ila** asked on 01 Sep 2022

Why this happening after selecting the start date?

## Answer

**Tsvetomir** answered on 06 Sep 2022

Hi, Ilan, When the Telerik Blazor DateRangePicker is used and a new date is attempted to be selected, the End date will be set to the default value of the DateTime data type that is 1st of January 0001 (0001/01/01, or any other format used by the specific culture of the application). Based on the provided information, I suspect that the Start and End dates for the component are non-nullable DateTime properties, is that correct? If so, you can make them nullable so that when a selection is initiated, a mask (YYYY/MM/DD) is shown instead of the default date. public DateTime? StartValue { get; set; } public DateTime? EndValue { get; set; } This behavior can be observed in our DateRangePicker Overview demo. Let me know if additional clarification is needed. Kind regards, Tsvetomir
