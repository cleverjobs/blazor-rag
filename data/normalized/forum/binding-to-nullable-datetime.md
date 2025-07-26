# Binding to nullable DateTime

## Question

**Nic** asked on 10 Jun 2019

Hi, Is there any way of binding to a nullable DateTime or is there a recommended approach for handling null/empty values. I think this question could apply to any of the controls that bind to a struct or an in-built type like Int/Decimal. Thanks, Nick.

### Response

**Neil N** commented on 30 May 2024

Is there a reason why nullable DatePickers return null when an invalid date is entered? We have: public DateTime MinDate { get; set; }=DateTime.Now.AddDays(30); public DateTime? AutopayDuesEndDate { get; set; } <p><TelerikDatePicker Width="200px" @bind-Value="@AutopayDuesEndDate" Min="@MinDate"></TelerikDatePicker></p> <label hidden="@ValidEnrollDate">Please enter a date on or after @MinDate.ToString("MMMM d yyyy").</label> if (AutopayDuesEndDate==null || (AutopayDuesEndDate !=null && AutopayDuesEndDate>=MinDate)) { ValidEnrollDate=true; } else { ValidEnrollDate=false; return; } If the user uses the picker to choose a date then an invalid date can't be chosen so that's ok. But they can manually enter an invalid date by typing it in and the if check doesn't work because AutopayDuesEndDate is set to null. I know I can use an EditForm and a model with data annotation but that seems like overkill for one field. Is that the only way to get the validation we need (i.e., no date or date at least 30 days in future)?

### Response

**Svetoslav Dimitrov** commented on 04 Jun 2024

Hello Niel, You can use the ValueChanged or OnChange event (depending on your business logic) to validate if the date that the user input is correct in your scenario.

### Response

**Neil N** commented on 04 Jun 2024

Hi Svetoslav, Neither of the suggestions seem to work. <TelerikDatePicker Width="200px" Value="@AutopayDuesEndDate" Min="@MinDate" ValueChanged="@( (DateTime? inputDate)=> EndDateOnChangeHandler(inputDate) )"> </TelerikDatePicker> private void EndDateOnChangeHandler(DateTime? userInput) EndDateOnChangeHandler only fires if a valid date is entered. For example, if @MinDate is 2024-07-06 and 2024-06-06 is entered then the event doesn't fire. Same thing with ValueChanged.

### Response

**Svetoslav Dimitrov** commented on 07 Jun 2024

Hello Neil, Let me start by explaining why the DatePicker returns null if the Date is incorrect. When the value of the DatePicker is incorrect the component defaults its value to the default value of the bound DateTime object - when the DateTime object is nullable it goes to null. In general, the behavior you are after is done by validation, including a form and data annotation attributes. It is expected that the events will not fire when you have set the Min parameter. What you can do is the knowledge that if a date is invalid, the value will be null and display a message to your users: <TelerikDatePicker @bind-Value="datePickerValue" Format="dd MMMM yyyy" Min="@Min" Max="@Max"> </TelerikDatePicker> @if(datePickerValue==null)
{ <span> Enter a date between the 1st of January 2024 and the 1st of January 2025 </span> }

@code {
DateTime? datePickerValue { get; set; }=DateTime.Now;
public DateTime Min=new DateTime(2024, 1, 1, 8, 15, 0);
public DateTime Max=new DateTime(2025, 1, 1, 19, 30, 45);
} The Telerik UI for Blazor DatePicker component does not provide an alternative to the built-in validation.

### Response

**Neil N** commented on 07 Jun 2024

I guess I wasn't clear (but the code I provided the validation requirements). The user can leave the date blank (null) - that's valid. What they can't do is enter a date like 2023-10-01 today and have it treated as valid. We cannot treat invalid dates as null because the user has indicated they do in fact want an end date (they might have mistyped the year).

### Response

**Svetoslav Dimitrov** commented on 12 Jun 2024

Hello Niel, I can suggest that you remove the Min parameter, and use the value changed event where you can handle the values. When you do not have the Min parameter the ValueChanged event will always fire. The best possible option is to use the TelerikForm (or EditForm) as the behavior you are after is validation.

## Answer

**Nick** answered on 11 Jun 2019

I'm not sure if it helps, but there's a discussion in the Asp.Net core issues page about binding to nullable types: [https://github.com/aspnet/AspNetCore/issues/5541](https://github.com/aspnet/AspNetCore/issues/5541)

### Response

**Marin Bratanov** answered on 11 Jun 2019

Hi Nick, Nullable DateTime is still not supported and you can track this feature in the following page: [https://feedback.telerik.com/blazor/1410422-binding-to-nullable-value.](https://feedback.telerik.com/blazor/1410422-binding-to-nullable-value.) Regards, Marin Bratanov

### Response

**Nick** answered on 11 Jun 2019

Thanks Marin, sorry I should have looked first.

### Response

**Marin Bratanov** answered on 11 Jun 2019

No worries, Nick, that's why I'm here :) I would personally have expected that to work too, in your place. We simply haven't gotten around to clearing up all of those things, with all the changes and new things that are happening. It's early days for Blazor, and even more so for component suites on it. --Marin

### Response

**Sean** answered on 28 Aug 2019

Hi. This shows as completed in the top left, but it doesn't work yet. Any further progress?

### Response

**Marin Bratanov** answered on 29 Aug 2019

Hello Sean, What version of Telerik UI for Blazor are you running? Can you confirm you are on 1.6.0 and that you have .NET Core 3 Preview 8 installed? I just tested the following code and it seems to work fine for me (I am also attaching a video of my test at the end of this post): @using Telerik.Blazor.Components.DatePicker
@using Telerik.Blazor.Components.DateInput

<TelerikDatePicker @bind-Value="theDate"></TelerikDatePicker>
<br />
The selected date is: @theDate
<br />
<TelerikDateInput @bind-Value="@StartDate" Format="MM/dd/yyyy HH:mm:ss"></TelerikDateInput>
<br />
The date input date is: @StartDate

@code {
DateTime? theDate;
DateTime? StartDate { get; set; }=new DateTime( 2020, 1, 1 );
} Regards, Marin Bratanov

### Response

**Nic** answered on 09 Dec 2020

Hello... Is the DatePicker having issues with nullable date values ? when a value is null we get the default value of 1/1/0001 how do we get around this issue .. we still want to preserve the null value.. have you guys fixed this yet? This post is dated from Jun 2019.. so.. i hope there is an alternative solution a year and a half later.. Please advice.. Thanks !!!

### Response

**Svetoslav Dimitrov** answered on 11 Dec 2020

Hello, The DatePicker should not have an issue with the nullable DateTime type. Below, I have prepared two examples of the DatPicker using both nullable and non-nullable DateTime objects. <h3>Nullable DateTimePicker</h3>
<TelerikDatePicker @bind-Value="@HireDate"></TelerikDatePicker>

<h3>Non-nullable DateTimePicker</h3>
<TelerikDatePicker @bind-Value="@VacationDate"></TelerikDatePicker>

@code { public DateTime? HireDate { get; set; } //nullable DateTime - default value null public DateTime VacationDate { get; set; } //non-nullable - default value 1/1/0001 } Regards, Svetoslav Dimitrov

### Response

**Kristjan** answered on 15 May 2024

Wondering, why our loved TelerikCalendar does not enjoy the same benefits of nullable datetime as the TelerikDateInput does.

### Response

**Hristian Stefanov** commented on 20 May 2024

Hi Kristjan, Thank you for bringing to our attention the nullable DateTime problem within the Calendar. To address it, I created a public item on your behalf on our public
