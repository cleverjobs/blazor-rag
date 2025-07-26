# Control Horizontal vs Vertical Layout

## Question

**Mar** asked on 12 Mar 2021

If I place the DateRangePicker inside a TelerikForm, the start and end input fields are stacked vertically. If I were to place the control just inside a div, they are arranged horizontally. How can I get the control to arrange itself horizontally when inside a form? Thanks

## Answer

**Marin Bratanov** answered on 12 Mar 2021

Hello Marc, We're aware of this and I made this page where you can Follow it: [https://feedback.telerik.com/themes/1510936-daterangepicker-in-a-form-drops-on-two-lines.](https://feedback.telerik.com/themes/1510936-daterangepicker-in-a-form-drops-on-two-lines.) I've also added a workaround and a reproducible in that page, I am also pasting it here: <style>.k-form.k-daterangepicker-wrap.k-floating-label-container { display: inline-block; width: auto;
} </style> <div class="demo-section k-form k-form-vertical"> <div class="k-form-field"> <label for="outbound-date" class="k-label k-form-label"> Travel Date </label> <div class="k-form-field-wrap"> <TelerikDateRangePicker @bind-StartValue="@StartValue" @bind-EndValue="@EndValue" StartId="outbound-date"> </TelerikDateRangePicker> </div> </div> <div class="k-form-field"> <p> The selected travel date is: <strong> @StartValue.Value.ToLongDateString() </strong> and <strong> @EndValue.Value.ToLongDateString() </strong> </p> </div> </div> <div class="demo-section"> <h4> <label for="outbound-date"> Book your flight tickets </label> </h4> <TelerikDateRangePicker @bind-StartValue="@StartValue" @bind-EndValue="@EndValue" StartId="outbound-date"> </TelerikDateRangePicker> <div class="mt-lg"> <h6 class="kd-demo-heading mt-sm"> Selected Dates </h6> <div> <strong> Departure: </strong> @StartValue?.ToString("dd MMM yyyy") </div> <div> <strong> Return: </strong> @EndValue?.ToString("dd MMM yyyy") </div> </div> </div> @code {
public DateTime? StartValue { get; set; }=new DateTime(2020, 4, 3);
public DateTime? EndValue { get; set; }=new DateTime(2020, 4, 10);
} If you prefer GitHub issues, you can subscribe here too, it's the same item: [https://github.com/telerik/kendo-themes/issues/1956.](https://github.com/telerik/kendo-themes/issues/1956.) Regards, Marin Bratanov

### Response

**Marc Simkin** answered on 12 Mar 2021

Great. Thanks.
