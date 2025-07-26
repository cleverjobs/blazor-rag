# Is there a way to control the browser level auto complete on a numeric textbox?

## Question

**Wil** asked on 25 Aug 2023

I'm using custom formatting in my numeric text boxes for units (in, kg, cm, etc.). The issue is that we want the browser auto complete to function within the numeric textbox, but the options that come from the history of the input all include the formatting string, so when selected, the value disappears before the onchange event since it technically contains a string. Is there a workaround for this, or something else I may be missing? Thanks for any insight!

## Answer

**Nadezhda Tacheva** answered on 30 Aug 2023

Hi Will, The only possible scenario I could think of in which you may be hitting such an issue is if you are using a standard HTML form that submits the whole value, including the format string. For example: [https://blazorrepl.telerik.com/wxEixavm02t6zTyy47.](https://blazorrepl.telerik.com/wxEixavm02t6zTyy47.) Is that the case or I am missing something? With this configuration, the form will send the whole input content. As you've mentioned, it will be treated as invalid when one tries to autocomplete the NumericTextBox afterwards. This is expected as the NumericTexBox allows numeric values only. Unfortunately, I am not aware of a way to change that browser behavior, so I can suggest two other options: Use our Form component - it works with a model or EditContext created from it and it will save only the proper numeric value without the string representation. Disable the autocomplete of the NumericTextBox - you can do that by not setting its AutoComplete property (or setting it to "off"). I hope you will find the above information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Will** commented on 30 Aug 2023

Hi Nadezhda, I think, for now at least, we'll just turn off the autocomplete. I think you're right in that there is no way to get the behavior we want (which is to allow the browser auto complete to be selected but only "take" the numerical value and leave out the string). Thanks for the help!

### Response

**Nadezhda Tacheva** commented on 31 Aug 2023

Hi Will, Thanks for getting back to me! I am glad to find out that tuning off the autocomplete is an option in your scenario. Should you face any other difficulties, please do not hesitate to contact us.
