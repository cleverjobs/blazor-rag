# Telerik theme builder adding more colors to the color series

## Question

**Chr** asked on 13 Aug 2024

I need to add more colors to my charts. The theme builder only has 7 colors. I can see in the exported file that they are in the root under --kendo-color-series a though g. I have tried adding --kendo-color-series-h but my charts won't use that 8th color. I know this is the right place cause i can change the first 7 colors and see that change. So how do I add more colors to the kendo color series?

## Answer

**Dimo** answered on 13 Aug 2024

Hi Christian, The predefined series colors in the CSS theme are a fixed number and cannot be increased without changes in our Chart source code. To apply an infinite number of colors, please use the ColorField feature of the series. Regards, Dimo

### Response

**Christian** commented on 13 Aug 2024

This doesn't work for dynamic data, I would have to hard code it all. Not really infinite and not at all what you claim the theme builder does and is for
