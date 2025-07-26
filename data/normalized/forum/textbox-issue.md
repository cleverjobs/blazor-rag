# TextBox Issue

## Question

**Dea** asked on 14 Oct 2022

When the user types in a character or copies and pastes into text box the valuechanged event on that first character is null, Why? Any way around this? What am I doing wrong on it. Type 1 character in first box and nothing happens. Type more and the typed character appears in second, one off what should be there. ANd same happens if you paste a value in. Code example: <h1> Hello, Telerik REPL for Blazor! </h1> <div style="border: 1px gray solid;"> <span @onkeypress="@onSearchValueChange" @onkeydown="@onSearchValueChange"> <TelerikTextBox @bind -Value="@stringValue" @ref="@txtBxRefSearchValue" Id="SearchValue" /> </span> <TelerikTextBox @bind -Value="@stringValue2" @ref="@txtBxRefSearchValue2" Id="SearchValue2" /> </div> @code { string stringValue { get; set; } TelerikTextBox txtBxRefSearchValue { get; set; } string stringValue2 { get; set; } TelerikTextBox txtBxRefSearchValue2 { get; set; } public void onSearchValueChange( KeyboardEventArgs e) { // Note! it has no value on the first character, NULL, but once 2nd one typed in tis good to go. if (txtBxRefSearchValue.Value is not null) { if (txtBxRefSearchValue.Value.Length> 0) { stringValue2="Work on value"; } else { stringValue2="Do nothing"; }; }; } }

## Answer

**Dimo** answered on 18 Oct 2022

Hi Deasun, There are several things to change in the code to make it work: Set DebounceDelay of the TextBox to 0, otherwise the textbox value will update with a delay of 150ms, which is after the event handlers. Retrieve the textbox value the Blazor way, which is via the parameter ( stringValue ). Do not use the component reference for such operations. Use async keydown / keypress handlers with some delay to prevent race condition with the textbox value update. <span @onkeypress="@onSearchValueChange" @onkeydown="@onSearchValueChange"> <TelerikTextBox @bind-Value="@stringValue" DebounceDelay="0" /> </span> <br /> <br /> <TelerikTextBox @bind-Value="@stringValue2" /> @code { string stringValue { get; set; }
TelerikTextBox txtBxRefSearchValue { get; set; } string stringValue2 { get; set; }
TelerikTextBox txtBxRefSearchValue2 { get; set; } public async Task onSearchValueChange ( KeyboardEventArgs e ) { await Task.Delay( 1 ); if ( stringValue is not null )
{ if ( stringValue.Length> 0 )
{
stringValue2="Work on value";
} else {
stringValue2="Do nothing";
};
};
}
} Regards, Dimo Progress Telerik

### Response

**Deasun** commented on 18 Oct 2022

Thank you.
