# NumericTextbox: Show "Blank" instead of "0" but fixed decimals if > "0"

## Question

**Hen** asked on 21 Dec 2022

If a value is "0" then I want to display an empty field. But if a value is greater that "0" I want to format it with 2 decimals. I can not figure an easy way how. Actually I have the choice between "#,###.##" and "#,##0.00". I have a lot of those fields so I need a kind of generic solution...

## Answer

**Dimo** answered on 22 Dec 2022

Hello Hendrik, The Blazor binding mechanism expects a component parameter to be linked to a specific variable and will reflect the current variable value. If zero is not a valid value at all, then use a nullable variable and set it to null to render an empty NumericTextBox. If you need more complex logic, you may need two variables and additional code that uses the NumericTextBox events (e.g. ValueChanged ) to map values from one variable to the other and change values on the fly. Regards, Dimo Progress Telerik
