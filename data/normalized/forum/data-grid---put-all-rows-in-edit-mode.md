# Data Grid - Put all rows in edit mode

## Question

**Jas** asked on 30 Apr 2021

I am trying to use the data grid for mapping a source to a destination. I would like to have a grid toolbar command that puts all rows in edit mode and then while in edit mode either disable or hide the button. Is this feasible if so, any guidance on how to do this?

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hi Jason, Such a scenarios where something is editable from top to bottom feels more like a case for a spreadsheet component, the grid is designed to work per-row rather than be a huge editable spreadsheet. You can Follow the implementation of a native one here: [https://feedback.telerik.com/blazor/1442151-spreadsheet-component](https://feedback.telerik.com/blazor/1442151-spreadsheet-component) and in the meantime you can consider the Kendo widget. With the grid you could do that by using the row template or cell template and having conditional markup that puts editors in place of the texts. Note that this would not rely on the built-in editing of the grid and you would need to take care of all data operations yourself (such as updating the concrete row model, the main data collection in the view-model and the database). You would also need to make sure to use the appropriate editor for each field according to its type, which is something the grid does for you otherwise. Regards, Marin Bratanov Progress Telerik

### Response

**Jason** commented on 30 Apr 2021

Thank you, I completely forgot about the row and cell templates.

### Response

**Ryan** commented on 12 Dec 2022

Jason, how did you end up setting this up?

### Response

**Dimo** commented on 13 Dec 2022

This Grid batch editing example may also be relevant.
