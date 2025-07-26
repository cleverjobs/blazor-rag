# Blazor Error: Format Specifier

## Question

**RayRay** asked on 18 May 2022

I am trying to use the Telerik.Blazor.Components.TelerikNumericTextBox. Upon opening the form in question, I receive the following in the output window: [2022-05-18T14:08:20.156Z] Error: System.AggregateException: One or more errors occurred. (Format specifier was invalid.) ---> System.FormatException: Format specifier was invalid. at System.Number.NumberToString(ValueStringBuilder& sb, NumberBuffer& number, Char format, Int32 nMaxDigits, NumberFormatInfo info) at System.Number.FormatDecimal(Decimal value, ReadOnlySpan`1 format, NumberFormatInfo info) at System.Decimal.ToString(String format, IFormatProvider provider) at Telerik.Blazor.Common.Parsers.TelerikGenericDecimal`1.Format(T value, String format) at Telerik.Blazor.Components.TelerikNumericTextBox`1.get_FormattedValue() at Telerik.Blazor.Components.TelerikNumericTextBox`1.get_Text() at Telerik.Blazor.Components.TelerikNumericTextBox`1.GetNumericTextBoxOptions() at Telerik.Blazor.Components.TelerikNumericTextBox`1.OnAfterRenderAsync(Boolean firstRender) The razor markup for the control is: <TelerikNumericTextBox Width=@ControlWidth.ToString() @bind-Value="@NumericValue" Decimals="2" Format="D" Id=@FieldProperties.Field_Name OnChange="@TextOnChangeHandler" /> Right now the control is bound to a Decimal Property (public decimal NumericValue) and the initial value is hardcoded to 1200.26M Any assistance would be appreciated.

## Answer

**Ray** answered on 18 May 2022

Nevermind - I was using an format for a decimal value. Changing it to Format="F" fixed the issue.
