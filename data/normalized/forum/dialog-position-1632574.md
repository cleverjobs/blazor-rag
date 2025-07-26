# Dialog position

## Question

**Ila** asked on 28 Nov 2023

Is there a way to open a dialog/window next to the button that opened it?

## Answer

**Dimo** answered on 29 Nov 2023

Hi Ilan, Use a modal Window instead of a Dialog. Set the Window position parameters to values from the MouseEventArgs of the Button's OnClick handler. Note that MouseEventArgs provides numeric position values, while the Window expects string values with "px". Regards, Dimo Progress Telerik
