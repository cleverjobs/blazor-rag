# Datepicker format doesn't work

## Question

**Bru** asked on 07 Feb 2024

I have this code: <TelerikDatePicker @bind-Value="@Value" Width="400px" Format="dd/MM/yyyy"> </TelerikDatePicker> this results in this: Why is it not the format dd/MM/yyyy as I specified?

## Answer

**Twain** answered on 08 Feb 2024

I tested the code and it works as expected: Demo It would be helpful if you could provide more information to analyze the issue.

### Response

**Svetoslav Dimitrov** answered on 12 Feb 2024

Hello Bruno, Can you confirm if you are using Globalization in your application? I am asking this because the culture of the application can override the Format of the DatePicker - thus a different format is rendered. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Bruno** answered on 12 Feb 2024

I added @{ CultureInfo cultureInfo=new CultureInfo("nl-BE"); cultureInfo.DateTimeFormat.ShortDatePattern="dd/MM/yyyy"; CultureInfo.CurrentCulture=cultureInfo; } but this has no effect... it still displays the "dd-MM-yyyy" format Also, when I specify the format explicitly as attribute, then why should the globalization override this?

### Response

**Bruno** answered on 12 Feb 2024

I just started a clean new telerik blazor project (v5.0.1). I still have the issue (see code below) (Also if use backslashes like '\' then he takes it, but '/' gets changed into '-') @page "/" <TelerikButton OnClick="@SayHelloHandler" ThemeColor="primary">Say Hello</TelerikButton> <TelerikDatePicker @bind-Value="@SelectedDate" Width="400px" Format="dd/mm/yyyy"> </TelerikDatePicker> <br /> @helloString @code { private DateTime? SelectedDate { get; set; } MarkupString helloString; void SayHelloHandler() { string msg=string.Format("Hello from <strong>Telerik Blazor</strong> at {0}.<br /> Now you can use C# to write front-end!", DateTime.Now); helloString=new MarkupString(msg); } }

### Response

**Dimo** answered on 15 Feb 2024

Hi Bruno, Please provide the following information: What is the locale in the regional settings on your dev machine? Is your app Blazor Server or WebAssembly? Does the attached app behave as expected? It's a Blazor Server app with hard-coded nl-BE culture. Regards, Dimo Progress Telerik

### Response

**Bruno** commented on 19 Feb 2024

This is the result... i can use every separator except '/', it gets replaced by '-'

### Response

**Dimo** commented on 22 Feb 2024

Hi Bruno, I tested the attached app from my previous reply with Dutch (Belgium) regional settings and the date separator was correct and according to the component configuration. See the screenshot. (I restarted my computer to make sure the regional settings are applied.) Frankly, I am not sure what is happening. Do you have any other pointers how to reproduce the problem?
