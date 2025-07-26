# TelerikDatePicker Format (Client-side)

## Question

**Hen** asked on 14 May 2019

Dear Telerik, I have a question regarding the TelerikDatePicker's Format property. I have set the format to "dd/MM/yyyy" <TelerikDatePicker Format="dd/MM/yyyy" bind-Value="@DatePickerValue" ValueChanged="@OnDateChanged"></TelerikDatePicker> But the Picker still displays the date as yyyy-MM-dd. I have tried various ways, including setting the CultureInfo in different ways, but nothing seams to help. Do you have a solution for this ? Regads, Gert

## Answer

**Marin Bratanov** answered on 14 May 2019

Hello Gert, Can you confirm you have the JS interop file registered, with the correct version, as explained here: [https://docs.telerik.com/blazor-ui/components/dateinput/overview?](https://docs.telerik.com/blazor-ui/components/dateinput/overview?) Here's some code I used to test this, and at the end of this post you will find a screenshot of what I see in the browser: @using Telerik.Blazor.Components.DateInput Format="dd/MM/yyyy" <TelerikDateInput Format="dd/MM/yyyy" bind-Value="@DatePickerValue"></TelerikDateInput> <br /> No explicit format <TelerikDateInput Format="dd/MM/yyyy" bind-Value="@DatePickerValue"></TelerikDateInput> <br /> Format="yyyy MMM dd" <TelerikDateInput Format="yyyy MMM dd" bind-Value="@DatePickerValue"></TelerikDateInput> <br /> @DatePickerValue @functions { DateTime DatePickerValue { get; set; }=DateTime.Now; } Also, version 1.1.0 is planned for tomorrow, so you could give that a try as well. That said, we rely on the framework to provide the formatting and Blazor still has issues with date formatting and localization: [https://github.com/aspnet/Blazor/issues/1166](https://github.com/aspnet/Blazor/issues/1166) and [https://github.com/mono/mono/issues/6368.](https://github.com/mono/mono/issues/6368.) Also, at the moment, the ValueChanged handler is also blocked by this: [https://github.com/aspnet/AspNetCore/issues/8385.](https://github.com/aspnet/AspNetCore/issues/8385.) The framework is still young and is bound to have some hiccups yet and date formatting and handling still seems to be one of them. Regards, Marin Bratanov
