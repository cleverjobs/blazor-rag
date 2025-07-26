# Grid: Sticking a column to the right even if other columns do not take up all the space

## Question

**Cha** asked on 19 May 2023

Hi, I am currently evaluating the Telerik Grid and I need to have, in my grid, a command column that stays sticked to the right of the grid no matter the width of the other elements. Note that I also allow resize of all columns (except the command column itself). In other words, I would like for the white space in the attached picture to move from after the command column to between the rating and command columns. Is that at all possible? Thanks.

## Answer

**Tsvetomir** answered on 24 May 2023

Hi, Charles, The frozen/locked columns are still part of the main table of the grid. Therefore, when resizing, the table has new width and the white space is actually the difference between the wrapper width and the actual table content. What I can suggest is that you add the MinResizableWidth to your columns so that their cumulative width is always at least as wide as the actual wrapper. Regards, Tsvetomir Progress Telerik

### Response

**Charles** commented on 12 Jun 2023

Hi, setting a MinResizableWidth is not ideal for us, since this property has to be set in pixels and I want my grid to adapt to the screen size of the user (i.e. have all columns visible on initial load). Can you think of another work around?

### Response

**Tsvetomir** commented on 13 Jun 2023

Having the width specified in exact pixels is a prerequisite in order to achieve the scenario at hand. What you could do is make the calculations of the width dynamically based on the screen size and apply them conditionally. This way, you would not hardcode a single value for the MinResizableWidth.
