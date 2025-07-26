# Get and Set the Column width

## Question

**Pet** asked on 03 Feb 2021

Hi, I can set the Grid property Resizable="true" to allow the user to adjust the column width. I want save all column width in the Localstorage to restore it after a page refresh. How can I read the width of all columns and set at first load? I use Blazor Server. Exists an event "OnColumnWidthResized"? Best regards, Peter

## Answer

**Marin Bratanov** answered on 03 Feb 2021

Hello Peter, You can do this through the grid state - both saving the column size, order, as well as filter, sorting, grouping, paging, and so on. You can find an example in the Persist State online demo - it's nearly codeless (two event handlers, a few lines of code, a serialize and deserialize call in the service). As for an event - the StateChanged event fires when the columns change, you can read more about this in the documentation about the grid state - I recommend you skim through all the intro too, as this feature opens up a lot of possibilities. Regards, Marin Bratanov

### Response

**Peter** answered on 03 Feb 2021

Hello Marin, Perfect. Thank you for the complete example. Best Regards, Peter
