# Insert new row and position cursor in the first editable field when TAB key is pressed

## Question

**Vas** asked on 31 Mar 2021

Hi, I have the next task to solve. For Incell editing if the cursor is on the last row in the last editable field and the TAB key is pressed, a new row must be added as the last row and the cursor must be positioned in the first editable field of this row. The data source for the grid is of the ObservableCollection<> type. I tried to write code on the OnUpdate and OnStateChanged events but without reaching the desired result. Any help is welcome. Vasile Lacatus Advanced Software Solutions

## Answer

**Vasile** answered on 31 Mar 2021

Note: I do not need paging or grouping in the grid.

### Response

**Marin Bratanov** answered on 01 Apr 2021

Hello Vasile, The general approach would be to add a new item to the grid data source and after that put it in edit mode through the grid state (see the Initiate Editing or Inserting of an Item section). Perhaps you can try this in OnUpdate, but keep in mind that after it, the grid will re-render, so you may need to use Task.Run() to add a delay to change the grid state until after the re-render has happened (usually 50-100ms should suffice). If you do make such a sample, feel free to open a pull request in this repo to share it with the community, we award such contributions with Telerik points. Regards, Marin Bratanov Progress Telerik
