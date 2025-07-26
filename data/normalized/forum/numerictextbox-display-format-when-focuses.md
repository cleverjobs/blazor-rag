# NumericTextBox display format when focuses

## Question

**Chr** asked on 08 Nov 2023

I'd like to check if its possible to have the format of a NumericTextBox display when the user has focus (i.e. they are typing something in). Currently it just shows a blank input (which makes sense), but if we could prepend it with a format or something that would be useful. For example, adding the $ sign at the start. It's not a huge issue but keen to see if it's possible.

## Answer

**Dimo** answered on 13 Nov 2023

Hi Chris, The desired behavior will require the component to parse strings all the time, instead of working with a true numeric value. If you wish to be more transparent with the users about the expected input, I recommend you the following NumericTextBox parameters and other options: Format - when the component has a value and is not focused Placeholder - when the component doesn't have a value Define (form) labels with additional text instructions for the users Render the $ sign over the textbox with CSS: <TelerikNumericTextBox @bind-Value="@NumValue" Format="C2" Width="160px" Class="dollar" /> <style>.dollar:focus -within::before { content: "$"; position: relative; top: 4px; left: 7px;
} </style> @code {
decimal? NumValue { get; set; }=2. 5m;
} Regards, Dimo Progress Telerik
