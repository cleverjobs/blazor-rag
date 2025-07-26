# Shrink Controls & grid

## Question

**Eri** asked on 29 Apr 2022

I am using your controls in a Blazor application and I am finding that they naturally take up a lot of space. Is it possible to make a change to in the site.css or via another method to use a more compact style? Or maybe use the small versions by default? This is especially true of the grid. Even grids with <6 rows are not big enough to avoid datetime values from wrapping. Thanks in advance.

## Answer

**Svetoslav Dimitrov** answered on 04 May 2022

Hello Eric, There are multiple ways to control the dimensions of the Grid component (and others too). Let me first provide some Grid-specific information, and afterward follow up with some general guidance on other components. Grid-specific The Grid provides multiple parameters to control the dimensions of the component as a whole, its rows, and columns. You can use the Height and Width parameters of the Grid to shrink the "general" size of the component. To further tweak the size, you can use the RowHeight (which controls the height of each row in the Grid), and the Width parameter exposed to each column in the Grid. Further than that, you can use the OnCellRender event to provide custom CSS classes (that provide some CSS rules) for the cells. General guidance Most of our Telerik UI for Blazor components expose Width and Height parameters to control the dimensions. I hope this helps you move forward with your application. Regards, Svetoslav Dimitrov
