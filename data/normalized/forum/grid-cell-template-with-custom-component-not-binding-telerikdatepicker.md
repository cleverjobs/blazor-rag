# Grid cell template with custom component not binding TelerikDatePicker

## Question

**Cla** asked on 30 Jan 2025

As you cas see from the sample below, i have a grid with row filter. In the FilterCellTemplate i use a custom component named DateFilterCell. In DateFilterCell i show a TelerikDatePicker. When i run this sample and try to set the datepicker value from the calendar, the value does not bind. What's wrong? Thanks [https://blazorrepl.telerik.com/GfEFHkFA35AZCMp451](https://blazorrepl.telerik.com/GfEFHkFA35AZCMp451)

## Answer

**Tsvetomir** answered on 31 Jan 2025

Hello Claudio, Thank you for the provided runnable example. For such scenarios, to make sure the value of the custom component is properly bound, is required to use one-way binding with its ValueChanged event. <TelerikDatePicker Value="Value" ValueChanged="@((DateTime? newValue)=> (OnValueChangeAsync(newValue)))" />

@code {
[ Parameter ] public DateTime? Value { get; set; }
[ Parameter ] public EventCallback<DateTime?> ValueChanged { get; set; } private async Task OnValueChangeAsync ( DateTime? value ) {
Value=value; if (ValueChanged.HasDelegate)
{ await ValueChanged.InvokeAsync(Value);
}
} } For you convenience, I've modified the provided REPL example and sending it back you to see the result. I hope this serves you well. Regards, Tsvetomir Progress Telerik
