# DatePicker Min Validation

## Question

**cwcw** asked on 09 Dec 2022

In my opinion there is an error in the date picker component. When I enter manually a date below the min value then the binded value is set to null but in the input field the wrong date is not cleared (See Screenshot). You can reproduce it by the DatePicker - Overview Demo: 1. Enter 01.01.1950 2. Click on the year and use the arrow down button to set 1949. The value is set to null and the input field is cleared. 3. Click on dd and set day to 01. Value 01.01.1949 is shown. 4. Click outside the date picker. Value is null but input shows 01.01.1949. Please let me know whether this is a known issue and you intend to fix it.

### Response

**Chad** commented on 13 Jan 2025

Has this been addressed properly?

### Response

**Dimo** commented on 14 Jan 2025

@Chad - the invalid user input stays in the DateInput textbox by design and doesn't disappear. The mentioned behavior "the input field is cleared" from the original post doesn't occur anymore. The idea is to allow the user to edit and adjust the value more easily. Let me know if I am missing something and provide exact testing steps if necessary.

## Answer

**Dimo** answered on 13 Dec 2022

Hello, Hm, there is an inconsistent behavior indeed. I have pinged the developers about it, but we may also need to consult the UX team before deciding whether to always remove the value or always to keep it. The component shows a red border for an invalid value, so leaving it may actually be better for the user, so that they correct it more easily. In the meantime, you can use the DatePicker OnBlur event and a couple of JS lines to remove the undesired invalid value from the DatePicker textbox. @inject IJSRuntime js

<TelerikDatePicker @bind -Value="@DateValue" Id="dp1" Min="@( new DateTime(1950, 1, 1) )" Max="@( new DateTime(2030, 1, 1) )" OnBlur="@( ()=> ClearDateInput("dp1" ) )" DebounceDelay="0" /> <script suppress-error="BL9992"> // function clearDateInput ( id ) { setTimeout ( function ( ) { var input=document.getElementById(id); if (input) {
input.value="dd.mm.yyyy";
}
});
} // </script> @code {
DateTime? DateValue { get; set; } async Task ClearDateInput ( string id ) { if (!DateValue.HasValue)
{ await js.InvokeVoidAsync( "clearDateInput", id); }
}
} Regards, Dimo Progress Telerik
