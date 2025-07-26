# Grid differeneces between 3.6.1 and 4.0.1?

## Question

**Dea** asked on 13 Feb 2023

After upgrading the grids tag=<GridToolBar> seems to have disappeared from the control. Was it replaced by <GridToolBarTemplate>? If so why doe I get a red error line under the tag when I rename the tag from the old to the new? Tis at 4.0.1 now:

## Answer

**Torben** answered on 13 Feb 2023

try to use the : Icon="@FontIcon.FileExcel"

### Response

**Svetoslav Dimitrov** answered on 15 Feb 2023

Hello Deasun, Indeed, as Tobren said, the issue is with the Icon. You can see a list of all breaking changes from the 4.0 documentation article. Regards, Svetoslav Dimitrov
