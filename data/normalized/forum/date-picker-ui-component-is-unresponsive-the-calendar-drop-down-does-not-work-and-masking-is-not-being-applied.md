# Date Picker UI component is unresponsive. The calendar drop down does not work and masking is not being applied

## Question

**IanIan** asked on 11 Mar 2024

DatePicker UI component is unresponsive. The calendar drop down does not work and masking is not being applied. I followed the instructions on First Steps with UI for Blazor in a Web App - Telerik UI for Blazor I have the nuget package set up, I have the scripts in, I followed the instructions and double checked that I followed all of them. I can't figure out why this ui component is not working. @page "/datePicker" @attribute [StreamRendering] <PageTitle>Telerik DatePicker</PageTitle> The selected date is: @datePickerValue.ToShortDateString() <br /> <TelerikDatePicker @bind-Value="datePickerValue" Format="dd MMMM yyyy" Min="@Min" Max="@Max"> </TelerikDatePicker> @code { DateTime datePickerValue { get; set; }=DateTime.Now; public DateTime Min=new DateTime(1990, 1, 1, 8, 15, 0); public DateTime Max=new DateTime(2025, 1, 1, 19, 30, 45); }

## Answer

**Dimo** answered on 13 Mar 2024

Hello Ian, Most likely, the app's interactivity location is " Per page / component " and the . razor file lacks interactive render mode. If I am wrong, please send the app for inspection. Regards, Dimo Progress Telerik

### Response

**Ian** commented on 13 Mar 2024

Ok awesome, I got that in and telerik buttons are working. However, the DatePicker component is now throwing a weird error that does not make sense. It only occurs with the DatePicker component. I have a little proof of concept app with the same thing happening and I'll include that

### Response

**Dimo** commented on 14 Mar 2024

@Ian - the TelerikRootComponent setup in your app assumes that the application has Global interactivity, which is not the case. Please do one of the following: Use an app with Global interactivity location. Follow the documentation page about using TelerikRootComponent with Per Page/Component interactivity I also recommend the following documentation sections for better understanding of the TelerikRootComponent role: Purpose of TelerikRootComponent TelerikRootComponent and app interactivity

### Response

**Ian** commented on 14 Mar 2024

Awesome! Thank you for your help
