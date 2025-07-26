# Height on grid with scroll bar causes headers to misalign

## Question

**Ric** asked on 31 Mar 2025

I have several grids in my app, but I've noticed that when I set a height on a grid (to show the scroll bar and make the grid vertically fill its container), the header row seems offset. Here's a grid with no height; And with Height="70vh" set on the same grid; The headers are slightly offset - on other grids, it also appears that the more rows, the more offset the headers become. Anyone have any ideas what might be causing this? Ive not found anything that even plausibly could be causing it in my code.

## Answer

**Anislav** answered on 31 Mar 2025

Hi Richard, I reviewed the screenshots you provided, and there is a slight misalignment between the borders of the table header cells and the body cells in the first example as well. This issue becomes more noticeable when the grid's height is fixed, and a scrollbar appears in the second example. I created similar samples here: [https://blazorrepl.telerik.com/GJkHHbbZ07ivxlDy45.](https://blazorrepl.telerik.com/GJkHHbbZ07ivxlDy45.) As you can see, there’s no discrepancy between the borders of the header and body cells in grids with both fixed and non-fixed heights. Based on this, it seems like some custom CSS on your pages is affecting the grid's rendering. I recommend testing the grid on a blank page without any additional layout or styles. Alternatively, you can create a fresh test project using Telerik grids to confirm whether the issue persists. Regards, Anislav Atanasov

### Response

**Richard** answered on 01 Apr 2025

Hi Anislav, The problem was down to this in my app,css (Blazor) .k-grid-header, .k-grid-footer { padding-right: 0; /* version 2.26 and older requires !important here */ } Which was copied out of one of the Telerik Demos / how to guides (IIRC one about changing the font size in the grid since the rest of the CSS in the block sets the font size)
