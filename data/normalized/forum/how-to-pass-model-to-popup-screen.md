# How to pass model to popup screen

## Question

**Lak** asked on 14 Apr 2021

Hi, I have to bind dropdown list in popup from Telerik grid when you click on edit. Now i wanted to get the selected value from grid. Please help me out on this issue. Thank you.

## Answer

**Svetoslav Dimitrov** answered on 14 Apr 2021

Hello Lakshmipathi, You can use the Editor Template for the Grid. It allows you to control what is rendered when the Grid enters the Edit mode. It provides a context object that needs to be cast to the type of your data and contains the information for the currently edited Grid row. You can use the context to bind the respective value to the DropDownList. Regards, Svetoslav Dimitrov Progress Telerik
