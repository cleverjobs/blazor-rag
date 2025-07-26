# Grid InCell edit mode - avoid click on cell for edit

## Question

**Mak** asked on 14 Apr 2021

Hi, When I set grid in InCell edit mode, I have to click on grid cell, so the textbox control for edit becomes available. Can I set it active/available for edit once grid is loaded and avoid clicking on the cell? Current scenario: 1. Grid is loaded 2. Click on the cell I want to edit 3. Text box is shown with the value for edit 4. On focus lost the updated value is shown in the cell and text box is gone Desired scenario: 1. Grid is loaded 2. No need to click on any cell, all available cells for edit are showing text boxes with the value for update 3. Update desired values in the grid cells text box 4. On focus lost the updated value is shown in the cell and text box is gone Thanks, Max

## Answer

**Marin Bratanov** answered on 15 Apr 2021

Hi Maksym, You can put a grid row in edit mode by using the grid state (see the "Initiate Editing or Inserting of an Item" example). For incell editing mode, you can also set the EditField to point to the field name you want to edit. What is important is that editing in the grid works per-row, so you can have one row in edit mode. With incell editing users can quickly edit all rows and columns with the keyboard, much like they would in Excel, so putting all rows in edit mode should not be necessary. Regards, Marin Bratanov Progress Telerik

### Response

**Maksym** answered on 15 Apr 2021

Hi Marin, Thanks for your replay. Much appreciated. You mentioned the following: "With incell editing users can quickly edit all rows and columns with the keyboard, much like they would in Excel". That is exactly what I need. Perhaps you could send an example of how to achieve that? Thanks, Maksym

### Response

**Marin Bratanov** answered on 15 Apr 2021

Hello, You can see how to do that and how it works here: [https://demos.telerik.com/blazor-ui/grid/editing-incell](https://demos.telerik.com/blazor-ui/grid/editing-incell) and here is more documentation: [https://docs.telerik.com/blazor-ui/components/grid/editing/incell](https://docs.telerik.com/blazor-ui/components/grid/editing/incell) Regards, Marin Bratanov Progress Telerik

### Response

**Maksym** answered on 15 Apr 2021

From what I see, you can always set only one row to be editable. So, for example, let's say I have 10 rows in the "InCell " grid. I would not be able to have all 10 in edit mode at the same time, correct?

### Response

**Marin Bratanov** answered on 15 Apr 2021

Correct. A grid is row-based. It is not designed for editing all rows at the same time. If you want such experience, perhaps a spreadhseet component is more suited to such needs, you can Follow the implementation of one here: [https://feedback.telerik.com/blazor/1442151-spreadsheet-component.](https://feedback.telerik.com/blazor/1442151-spreadsheet-component.) You can also consider putting textboxes in the template of all your columns so effectively all fields are editable all the time in all rows. Note that in such a case you should not use the built-in grid data source operations (such as the OnUpdate event) but handle saving to the data source entirely with the code from the templates around the custom inputs you would have. I must also note that so many inputs will re-render the grid very often and you can see a performance deterioration. Also, this is not a scenario that the grid supports because it is not its built-in editing and it can't help with it. Regards, Marin Bratanov

### Response

**Maksym** answered on 15 Apr 2021

Thanks Marin, it is clear now...
