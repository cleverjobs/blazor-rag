# CSS for the grid footer

## Question

**Eri** asked on 28 Jul 2022

Is there a way to remove the left, right, and bottom grid lines from the footer? I want the grid to show for the header and data cells, just not the foot row. Thanks

### Response

**Blazorist** commented on 28 Jul 2022

Hi Eric. It is not very clear what you want to achieve. Can you elaborate a little more?

### Response

**Eric** commented on 28 Jul 2022

I want the grid to look like the below example. There the header row and the data rows should have gridlines around the cells, but the footer doesn't have gridlines. Hope that helps.

## Answer

**Dimo** answered on 02 Aug 2022

Hello Eric, Generally, such customizations are implemented by inspecting the Grid HTML markup and CSS styles. Then, add CSS rules that override the existing theme styles. Here is a REPL example. If you want to adjust the Grid borders, so that the footer row appears "outside" the Grid, then you need some more CSS code. Regards, Dimo Progress Telerik
