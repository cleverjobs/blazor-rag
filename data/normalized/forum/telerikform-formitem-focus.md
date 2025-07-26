# TelerikForm FormItem focus

## Question

**Lou** asked on 31 Oct 2022

Hello, How I can put the focus via the code to FormItem in a TelerikForm ?

## Answer

**Nadezhda Tacheva** answered on 03 Nov 2022

Hi Louis, The editors that the Form uses are essentially integrated UI for Blazor input components (TextBox, NumericTextBox, DatePicker, and more). They all expose FocusAsync method that lets you focus them programmatically. To focus the desired FormItem with code, use a FormItem Template, render the desired editor component and invoke its FocusAsync() when needed. For example: [https://blazorrepl.telerik.com/ccbbuHPn20wid3BZ06.](https://blazorrepl.telerik.com/ccbbuHPn20wid3BZ06.) I hope you will find the above information and sample useful to move forward with your application. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva

### Response

**Louis** commented on 03 Nov 2022

Thanks a LOT

### Response

**Louis** commented on 04 Nov 2022

Someone maybe interested. I have to call the focus in this event protected override async Task OnAfterRenderAsync(bool firstRender) { await InterneIdRef.FocusAsync(); }
