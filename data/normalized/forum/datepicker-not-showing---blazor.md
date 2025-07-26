# DatePicker not showing - Blazor

## Question

**Enr** asked on 28 Nov 2022

Hi, A have a very simple code in order to test the DatePicker control: @page "/datepicker/overview" @page "/datepicker/index" @layout EmptyLayout <div> <div> <label for="travel-date" class="k-label k-form-label">Travel Date</label> <div class="k-form-field-wrap"> <TelerikDatePicker Min="@Min" Max="@Max" @bind-Value="@selectedDate" Id="travel-date" DebounceDelay="@DebounceDelay"> </TelerikDatePicker> </div> </div> <div class="k-form-field"> <p>The selected travel date is: <strong>@selectedDate?.ToLongDateString()</strong></p> </div> </div> @code { public DateTime Max=new DateTime(2050, 12, 31); public DateTime Min=new DateTime(1950, 1, 1); private DateTime? selectedDate; public int DebounceDelay { get; set; }=200; } This is the result I get: Looks like some styling is missing. Developing in VisualStudio 2022 (Preview). Any ideas? Thank you...

### Response

**Dimo** commented on 29 Nov 2022

Enrique - have you registered our theme CSS file? Is the URL correct? See Point 3 in section Step 4: Enable the Blazor UI Components General Themes documentation with other ways to register the theme CSS file

### Response

**Enrique** commented on 30 Nov 2022

Thank you Dimo... Regards.
