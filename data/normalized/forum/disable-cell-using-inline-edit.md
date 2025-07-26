# Disable cell using inline edit

## Question

**Pau** asked on 25 May 2022

Hi I have a grid using Inline edit, but in some circimstances some cells must be disabled. How can i do this? Eric

## Answer

**Nadezhda Tacheva** answered on 02 Jun 2022

Hi Eric, I am stepping in the discussion as my colleague, Marin, is currently out of office. In general, the idea for setting the Editable parameter to false is to actually perform that dynamically based on the specific cells you want to disable the editing for. You can handle the OnEdit event which provides details for the item the user initiated editing for. In the handler, include your business logic, depending on which the desired cells for this certain item will be disabled. In other words, with the suggested approach, you will be setting the Editable parameter to false for specific item and not for the whole column. To better illustrate how it can be achieved, I prepared this runnable sample: [https://blazorrepl.telerik.com/mmuAOGOL57C4UM5H10.](https://blazorrepl.telerik.com/mmuAOGOL57C4UM5H10.) It showcases disabling the edit of the Name cell for the items with ID less than 4. I hope this will help you move forward with your application. Please let us know if any further questions are raised. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Paul** commented on 02 Jun 2022

Love it! Thanks Eric

### Response

**Werdna** commented on 17 Apr 2023

Hi Nadezhda, Your sample doesn't seem to work when changing the GridEditMode to Incell. It works initially, but after I click in a cell that is not editable like "Name 3" and then click on a cell that SHOULD be editable like "Name 5", the "Name 5" cell does not become editable. Is there any way to get this to work in Incell mode? Thanks.

### Response

**Nadezhda Tacheva** commented on 19 Apr 2023

Hi Werdna, The design and behavior of the Incell are different and the suggested solution is indeed not applicable to Incell editing. The approach relies on toggling the Editable parameter of the column in the OnEdit handler. In Inline editing, the OnEdit event is raised per row, as soon as the user clicks the Edit command button. By design of the Incell editing mode, to open a cell for editing, the user should click on it. Thus, the OnEdit event is raised upon cell click. However, if a column is initially marked as Editable="false", the OnEdit event will expectedly not be raised for it and thus the Editable parameter cannot be toggled. For Incell editing, you may use a different approach. Let the column be editable by default, so the OnEdit event will be raised. Through the event arguments of its handler, you may cancel the event for the cells that you want to prevent the editing for. I've modified the sample to illustrate the approach: [https://blazorrepl.telerik.com/cROoljFt10FvkKY006.](https://blazorrepl.telerik.com/cROoljFt10FvkKY006.) I hope this helps you move forward with your application.

### Response

**Werdna** commented on 19 Apr 2023

Hi Nadezhda, That works! Thank you very much for your response.

### Response

**Marin Bratanov** answered on 26 May 2022

Hello Eric, You can set the Editable parameter of their column to false. Alternatively, you can use the OnEdit event and cancel it dynamically based on runtime conditions. Regards, Marin Bratanov Progress Telerik

### Response

**Paul** commented on 30 May 2022

Hi Both is not what i need, not the whole column should not be editable just for some records. The cell should not be editable, shown to user in disabled color. So also using the OnEdit is not the solution See example here, first column Eric
