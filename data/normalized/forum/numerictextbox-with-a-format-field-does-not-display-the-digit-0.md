# NumericTextBox with a format field does not display the digit '0'

## Question

**Chr** asked on 08 Nov 2023

When I make a format of $AUD#, or #,#, or even # it works for anything that is not 0. This also occurs in the demo formats in Blazor Numeric Textbox Overview - Telerik UI for Blazor I assume it's as designed, but is there any way to force the display of 0?

## Answer

**Chris** answered on 09 Nov 2023

Actually i think i figured it out, it needs to be $0,0 guessed it from here objective c - What does a hash/pound (#) represent in a format string? - Stack Overflow
