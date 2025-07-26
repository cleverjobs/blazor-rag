# how to set the telerikgrid height relative to the browser

## Question

**Afr** asked on 18 Apr 2023

Hi, I am using the telerikgrid in my web application. I want the height of the grid should adjust by itself when user resizes the browser. The user should not get the scroll bar for the browser. As of now I am using the following: Size="Telerik.Blazor.ThemeConstants.Grid.Size.Medium" Resizable="true" Pageable="false" Height="50vh" ScrollMode="GridScrollMode.Scrollable" Using this setting when the user is resizing the browser the scroll bar coming up for browser which we dont want. Can you please help on this? Thanks & regards, Afreen

## Answer

**Radko** answered on 21 Apr 2023

Hi Afreen, The Grid's Height parameter accepts any supported CSS values, as mentioned here: Grid Parameters. Having said this, setting Height to 50vh should work as expected, as this is directly applied as an inline style to the wrapping element of the Grid. I have prepared a simple REPL example that demonstrates this: [https://blazorrepl.telerik.com/wnkIcPEJ14OsMRw554.](https://blazorrepl.telerik.com/wnkIcPEJ14OsMRw554.) Could you please have a look and let me know if the behavior is satisfactory? As for the fact you observe a scroll bar - could this be something to do with another element constraining the height of the container the Grid is positioned in? Regards, Radko Stanev Progress Telerik

### Response

**Johan** answered on 23 Nov 2023

It's also possible to use the css style "calc()" for the height of the grid. Like: Height="calc(100vh - 100px)" This is when you have content above or below the grid that is 100px in height. Rezising works great.
