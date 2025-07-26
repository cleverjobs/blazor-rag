# Column fix width

## Question

**Cip** asked on 19 Oct 2020

Hello, Is it possible to set a fix pixel width to the columns of the grid and when the grid is displayed the columns not to appear stretched with the entire width of the table? What I mean is the following: 1. For example I have a grid with 4 columns. Each column has 100px width. The width of the container where the grid is present is 600px. In this case having 4 columns we have a total of 400px and it remains an empty space of 200 pixels to the end of the grid. 2. In the second exemple I have 8 columns in the grid. Each column heaving 100px width. The width of the container where the grid is present is 600px. In this case the sum of the widths of the columns is 800px which is bigger then 600px by 200px and in this case I would like on the bottom to appear a horizontal scroll that will give the user the possibility to see the contents of of the other 2 columns. I have tried to give a fix width to all the columns, to set the Resizable property to true but I could not achieve what I explained in the 2 cases that I mentioned above. Can you help me please? Can those cases be achieved somehow or not? Best regards, Ciprian

## Answer

**Svetoslav Dimitrov** answered on 19 Oct 2020

Hello Ciprian, I would refer to the scenarios in their turn: First scenario: When all column widths are explicitly set and the cumulative column width is less than the available Grid width, the remaining width is distributed evenly between all columns. Second scenario: This is the expected behavior. When the accumulative width of all columns exceeds the width of the Grid a horizontal scrollbar will appear. More information about the Width of the columns of the Grid can be found from this link. Regards, Svetoslav Dimitrov
