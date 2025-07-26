# Grid Selection

## Question

**Ger** asked on 06 May 2019

Dear Telerik, Is it possible to select a row ? Visually and logically ? I need a modal choose-dialog -> Window with a grid where I can select an item and pass the selected object to the main Page. Is it already possible ? Regards, Gert

## Answer

**Marin Bratanov** answered on 06 May 2019

Hi Gert, I made the following page for tracking this feature: [https://feedback.telerik.com/blazor/1407775-grid-row-selection.](https://feedback.telerik.com/blazor/1407775-grid-row-selection.) I expect you already know the drill - but just in case - use the Follow button to get notifications. On implementing this right now - I can see a way of implementing it at the moment like this: Add a command column to the dialog grid: [https://docs.telerik.com/blazor-ui/components/grid/columns/command.](https://docs.telerik.com/blazor-ui/components/grid/columns/command.) In the click handler of the custom command, get the item the user chose and store it somewhere (for example, in a List that you have prepared for the purpose). You can consume this list on the main page (for example, bind another grid to it, or whatever else you need). You can also use it to populate a second grid (or a simpler list) in the dialog to show the selection to the user. At the moment, selection of rows is not available in the grid, so you couldn't easily make the appearance change. Perhaps you could use a row/cell template and use a flag inside the model to add/remove a class that changes the appearance of all cells or a certain cell in the template. The issue with this approach is that the data model would need to learn about the presentation. Consider closing the dialog when the user selects and item (of course, suitable only if you want single row selection). Regards, Marin Bratanov
