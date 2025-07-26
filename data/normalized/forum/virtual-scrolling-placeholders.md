# Virtual Scrolling placeholders

## Question

**Mar** asked on 15 Jul 2020

I've a weird issue with grid and virtual scrolling. It seems that if you scroll with the scrollbar all goes fine, but if you use flywheel to scroll to the top, some of the first items are not loaded and the placeholders are shown instead, the scrollbar has cursor in top position. I can see from the debug that the last onread is made with skip value equal to the number of missing items.

## Answer

**Svetoslav Dimitrov** answered on 16 Jul 2020

Hello Marco, One of the most common problems that might cause this issue is that the RowHeight is not set to a number high enough to accommodate the content of the row. You can find more information and possible solution in this Knowledge Base article. Regards, Svetoslav Dimitrov
