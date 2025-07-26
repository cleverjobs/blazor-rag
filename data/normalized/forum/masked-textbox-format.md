# Masked Textbox format

## Question

**Ter** asked on 18 Feb 2023

Hello, How do I force user input to uppercase? I have this mask: Mask="00-LLLA00000000" I want the LLL to always be uppercase. When A is an alpha character, I want it to be uppercase as well. Thanks, TFISHER

## Answer

**Dimo** answered on 22 Feb 2023

Hello Terry, I can suggest two options. You can use one of them or BOTH of them at the same time. 1. Use CSS to transform how the value looks. <TelerikMaskedTextBox @bind -Value="@Value" Mask="LLL" Class="uppercase">
</TelerikMaskedTextBox> <style>.uppercase input { text-transform: uppercase;
} </style> @code { string Value { get; set; }="foo";
} 2. Modify the value while the user is typing. Note that the initial value may still not meet the requirement, unless you have tweaked it in advance. <TelerikMaskedTextBox Value="@Value" ValueChanged="@ValueChanged" Mask="LLL">
</TelerikMaskedTextBox> @code { string Value { get; set; }="foo"; void ValueChanged ( string newValue ) {
Value=newValue.ToUpper();
}
} Regards, Dimo

### Response

**Brett** answered on 02 May 2023

I've been looking for a way to convert a TelerikTextBox to uppercase as the user types and the CSS is so elegant but unfortunately, that is not how the data is stored to the underlying property that the TextBox is bound to. I really wish this would work because it is so much easier that wiring up an OnChange event for all of the fields I want upper case.

### Response

**Dimo** commented on 02 May 2023

@Brett - if ValueChanged / OnChange is not an option, then use CSS for the user and then override the value before storing it. This will probably require fewer changes in the app. On a side note, why not make the app support string values regardless of the letter casing? Perhaps you prefer a built-in property for value capitalization, but such a feature must depend on the language (culture) and the resulting complexity doesn't justify the rare usage and low customer demand.

### Response

**Brett** commented on 02 May 2023

Hi Dimo, I ended up using the CSS solution and then convert it before I write it back to the database. It's just an extra step but not a huge deal. I just wish the component had the capability to write the data back this way itself. I looked at the MaskEditBox and it looks like you can't do all caps with that either. Thanks for the help!
