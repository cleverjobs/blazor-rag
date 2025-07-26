# GridEditMode.Incell - GridColumn with TelerikGridCheckBox

## Question

**Lar** asked on 19 Oct 2022

I have a grid where I click on a row that makes sense for a text box or drop down list - I click on a cell with either of these controls, and then I can edit text or select as expected. I want to change that behavior for a cell with a checkbox. I want the value of the checkbox to change on the first click instead of it putting the checkbox cell in focus and then clicking it again to change its value. Is this possible?

### Response

**Hristian Stefanov** commented on 24 Oct 2022

Hi Larry, As far as I understand, the desired result is to enable/disable the editing for specific rows based on a checkbox. I confirm that it is possible by using a bool column with a template. I have prepared an example for you - REPL link. You can run and test it by trying to edit the description cell and then changing the checkbox state. I hope I understand the case correctly. If not, please share a little more information about the scenario here. You can also modify the above REPL sample to show me the configuration from the actual project. I look forward to hearing from you with feedback. Kind regards, Hristian

### Response

**Larry** commented on 24 Oct 2022

That's what I was looking for, thank you.
