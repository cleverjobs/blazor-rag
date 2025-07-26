# How to update a grid cell's contents from the code block in a razor file?

## Question

**Tho** asked on 21 Jul 2023

For a specific column, whenever one of its cells are clicked, the value in that clicked cell needs to update to a newly calculated value. Ideally, I'd like to be able to fire off an event containing information about the cell just clicked and use that information to update the cell's displayed value from the code block. I've tried the column event OnRowClick, but that doesn't allow me to specify which cell was clicked. I've also tried adding an onclick event inside the GridColumn's Template, but this only delivers MouseEventArgs. Is there anyway to do this without resorting to Javascript?

## Answer

**Nadezhda Tacheva** answered on 26 Jul 2023

Hi Thomas, Indeed the OnRowClick provides the whole item and not the specific cell the user clicked on. We are considering exposing a CellClick event or adding the information about the column Field in the arguments of the RowClick event. You may check the details in this request: [https://feedback.telerik.com/blazor/1556697-cell-click-event.](https://feedback.telerik.com/blazor/1556697-cell-click-event.) I added your vote there and you can follow it to get timely status updates. As for a custom approach, you are in the right direction by using a column Template. The portion you may be missing is that you also need to pass the context to the onclick handler of the container that holds the cell value, so you can get the item details in the code block. I've prepared a basic example to showcase the approach: [https://blazorrepl.telerik.com/mnkBcglR18e3ItV931.](https://blazorrepl.telerik.com/mnkBcglR18e3ItV931.) I have also included some styling suggestions that may be useful for the scenario. The code shows how to expand the custom container to fill the whole cell - thus, you can catch the click on the whole cell and not only on the text. I hope this will help you move forward with your application. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik
