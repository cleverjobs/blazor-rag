# Binding a Date Input to a nullable DateTime?

## Question

**TomTom** asked on 07 May 2019

I'm trying to bind a TelerikDatePicker component to a nullable DateTime property, but I'm getting a compile time warning of "cannot convert from System.DateTime? to System.DateTime". Does the TelerikDatePicker support binding to nullable values and if not, could it be changed to do so?

## Answer

**Bozhidar** answered on 07 May 2019

Hello, Currently only DateTime is supported, but we'll add support for nullable DateTime as soon as we can - in a few weeks at the most. Regards, Bozhidar

### Response

**Tom** answered on 07 May 2019

Perfect, thanks Bohzidar. We've taken the plunge and committed to doing our next production project in Blazor/Core 3, so this is a must for us
