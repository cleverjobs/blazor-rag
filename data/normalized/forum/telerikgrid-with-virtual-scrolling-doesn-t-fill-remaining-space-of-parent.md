# TelerikGrid with virtual scrolling doesn't fill remaining space of parent

## Question

**KaiKai** asked on 24 Mar 2023

Hello, we use the TelerikGrid with virtual scrolling. Now we want, that the grid fills the remaining space regardless the number of rows. The parent div already has the size of the window but the grid doesn't fill it up. I set the height of the grid to 100% but this didn't work. Does anybody have an idea what we have to do? Best regards Kai

## Answer

**Svetoslav Dimitrov** answered on 29 Mar 2023

Hello Kai, When you take advantage of the Virtual scrolling feature in the Grid you must set the Height of the Grid and the RowHeight parameter in pixels. If the Grid is virtually scrollable, setting dynamic height is not possible. Regards, Svetoslav Dimitrov Progress Telerik
