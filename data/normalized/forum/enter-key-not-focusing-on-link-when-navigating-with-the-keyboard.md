# Enter key not focusing on link when navigating with the keyboard

## Question

**Mik** asked on 20 Jul 2022

I have added a templated column to my grid that contains hyperlinks. However, I'm not able to navigate to it within the same context as navigating the grid with the arrow keys. So, if I set focus in the grid, and then use the arrow keys to navigate to the cell with the link in it, I would expect that pressing the Enter Key will put the focus on the link so that I can press enter again to navigate to the link's destination. This is functionality similar to how the GridCommandColumn works where pressing enter on the cell that has the focus, navigates into the cell and puts the focus on the first button in that cell. Then you can hit enter to activate the button or escape to exit back out to focus back on the cell. Your documentation in the keyboard navigation demo even says that it should do this here: Enter activates editing for the data cell when the grid is in InCell EditMode. In EditMode – saves changes and closes the editor. When a header cell is focused applies sorting. When a hierarchy cell is focused expands/collapses the detail template. When a template cell or a command cell is focused, focuses the first focusable element inside. Is this a bug, or is there something that I need to do to make it work for a template column? Here's a repl copied from your keyboard navigation demo that illustrates the issue: [https://blazorrepl.telerik.com/cQELQuvs25Rykh2B47](https://blazorrepl.telerik.com/cQELQuvs25Rykh2B47)

## Answer

**Svetoslav Dimitrov** answered on 25 Jul 2022

Hello Mike, This is indeed a valid bug and I logged it on your behalf - Cannot navigate in or out of an element defined within a Template via keyboard. I have added your vote for it and you are automatically subscribed to receive email notifications on status updates. Regards, Svetoslav Dimitrov
