# How to set datepicker init value in C# code

## Question

**Dea** asked on 02 Jun 2023

I have a datepicker on my page and on load I want to set its initial value to a date I get from a DB table. I also want the user to be able to pick a date to set it to and it auto updates the page objects base don that new picked date. I have the auto refresh working on the OnChange event but for some reason I cant set the objects first initial date! REPL: <h1> Hello, Telerik REPL for Blazor! </h1> <TelerikDatePicker @ref="@DTR11" Min="@Min" Max="@Max" ValueChanged="@( (DateTime d)=> DTR1Filter_OnChangeHandler(d) )"> </TelerikDatePicker> @code { public TelerikDatePicker <DateTime> DTR11 { get; set; } private DateTime? DTR11_selectedDate; public DateTime Max=new DateTime(2050, 12, 31); public DateTime Min=new DateTime(1950, 1, 1); protected override async Task OnInitializedAsync() { DTR11_selectedDate=DateTime.Now; //want to do something like: DTR11.value=DTR11_selectedDate; } async Task DTR1Filter_OnChangeHandler(DateTime theUserInput) { DTR11_selectedDate=theUserInput;; } }

## Answer

**Deasun** answered on 02 Jun 2023

It appears I just needed: DTR11.Value=(DateTime)DTR11_selectedDate; Friday! Duh.
