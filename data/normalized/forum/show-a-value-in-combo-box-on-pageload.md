# Show a value in combo box on pageload

## Question

**Uth** asked on 27 Jan 2022

I am using telerikcombobox inside telerikgridn as column. I need to show a value from db in the empty combobox on pageload. Can anyone please help me. Thank you

## Answer

**Marin Bratanov** answered on 30 Jan 2022

Hello Uthaya, If the combobox is to depend on the row data, you need to use the template of the column to get the current model and show a corresponding value from it in the combobox. You can use any desired business logic to set that value. The following thread I just answered a few minutes ago shows a very similar scenario that you may fid useful, together with my explanations in the answer: [https://www.telerik.com/forums/unable-to-set-initial-value-of-the-combobox-in-a-grid](https://www.telerik.com/forums/unable-to-set-initial-value-of-the-combobox-in-a-grid) Regards, Marin Bratanov
