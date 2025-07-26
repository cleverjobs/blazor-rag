# Cancel Event when characters exceed maxlength or maxvalue

## Question

**Lar** asked on 17 Oct 2022

Is there a way to cancel the keydown/keypress/keyup events to prevent non-digit characters from getting typed when characters in a TelerikTextBox? Also, I need a MaxLength set to 9 which the TelerikTextBox has but the TelerikNumericTextBox does not have. I want to prevent non-digit characters, and I also want to disallow typing more than a specified number of characters. The TelerikNumericTextBox only turns its border control red when exceeding a specified max value. I want to prevent typing more than 'x' number of digits.

## Answer

**Dimo** answered on 20 Oct 2022

Hi Larry, The described scenario calls for a MaskedTextBox - it has built-in configuration settings for value length and allowed characters. On a side note, the NumericTextBox has a Max parameter. Regards, Dimo

### Response

**Larry** commented on 20 Oct 2022

Does the MaskedTextBox allow a variable number of characters or does it force a set number of characters? I need max length to be 9 digits but I also need it to allow fewer digits

### Response

**Dimo** commented on 21 Oct 2022

Yes, it does. Check the MaskedTextBox Mask and Prompt documentation.
