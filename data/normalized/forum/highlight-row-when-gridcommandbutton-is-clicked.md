# Highlight Row when GridCommandButton is clicked.

## Question

**Dus** asked on 07 Jun 2023

Is this possible? I have seen the documentation on highlighting rows, but I haven't seen anything around getting a row to highlight outside of row selection and checkbox selection.

## Answer

**Radko** answered on 12 Jun 2023

Hi Dustin, You can achieve what you are after by utilizing the GridState. You can define an OnClick event handler within the GridCommandButton to which you can pass the reference/any data related to the item that has been clicked. Once you have this, through the Grid State, you can control the selection. I have prepared a rather simple example that demonstrates this: [https://blazorrepl.telerik.com/mxaUvQaz41xLrERU50](https://blazorrepl.telerik.com/mxaUvQaz41xLrERU50) Regards, Radko

### Response

**Dustin** commented on 13 Jun 2023

This is exactly what I was needing!!! Thanks a ton!!!!
