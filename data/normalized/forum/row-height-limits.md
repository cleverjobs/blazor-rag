# Row Height Limits

## Question

**Ste** asked on 03 Jul 2020

I've used your example code to adjust the font size on a grid and been using rowheight to adjust the row height but there appears to be some limit as too how small you can make the row height. I've attached a screen shot which shows there is a lot of space in the row above and below the small text, can this be reduced? Cheers Steve

## Answer

**Marin Bratanov** answered on 04 Jul 2020

Hi Steve, The rows have some padding by default, so you may want to add a CSS rule that removes or decreases it. If we take the example from the docs, here's an additional rule to do that (screenshot of the result is attached): div.smallerFont.k-grid td { padding: 0;
} Regards, Marin Bratanov

### Response

**Steve** answered on 04 Jul 2020

Terrific, Thank You...
