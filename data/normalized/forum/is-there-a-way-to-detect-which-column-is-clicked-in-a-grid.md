# Is there a way to detect which column is clicked in a grid?

## Question

**Jef** asked on 30 Jun 2021

Is there any plans to implement an OnColumnContextMenu event in the grid? Or maybe an OnCellContextMenu event that identifies both the row and column? And to go a step further, what about exposing events when the Grid header is clicked.

## Answer

**Svetoslav Dimitrov** answered on 02 Jul 2021

Hello Jeffrey, We have a knowledge-based article that showcases how to get the row, column, and cell value with the OnRowContextMenu event. Could you try the approach from this article and get back to me if it helps you move forward with your application? Regards, Svetoslav Dimitrov

### Response

**Jeffrey** commented on 02 Jul 2021

My grid has 37 columns. If i'm interpreting the code correctly, I would have to have to put an event handler on all 37 columns. It's doable but feels awfully heavy-handed. I'm not sure if it's a workable solution.

### Response

**Svetoslav Dimitrov** commented on 07 Jul 2021

Hello Jeffrey, I agree that placing an event handler to all 37 columns might be some additional work. In order for us to better assess the feature request could you provide a business scenario where a context menu should be assigned to an entire column?

### Response

**Jeffrey** commented on 07 Jul 2021

I'm developing a complex sales quotation application (hence the 37 columns). This is a rewrite of an older thick-client windows application. One feature that I am trying to replicate is the ability for the user to select a column and then invoke a menu to give them options relevant to the column. Having an event at the grid header level would work.

### Response

**Svetoslav Dimitrov** commented on 12 Jul 2021

Hello Jeffrey, The scenario you described is indeed a valid one. The business case seems more suitable for the Spreadsheet component. We have an open feature request for the addition of this component and I have added your Vote for it, this increases the popularity of the item. You can follow the public thread to receive email notifications on status updates. In the public item, you can see a workaround until the component is released for the Telerik UI for Blazor product suite. Let me know if this is a suitable approach for you. Regards, Svetoslav
