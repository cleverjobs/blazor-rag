# Open PoPup in Grid without using a <GridCommandColumn> edit

## Question

**Adh** asked on 31 May 2021

Hello I'm working on the view and I wanted to check if in the grid / editing there is the possibility of creating the PopUp event without the <GridCommandColumn> <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> I don't want that edit button to appear in my view, what I'm looking for is that clicking anywhere in the row opens that PoPup and when the PoPup appears there is a delete, update, calcel button. It is possible to modify the Grid view in this way I looked a lot and I can't find the way. Thank you.

### Response

**Matthias** commented on 31 May 2021

For this scenario, I use a Window and show this modal after clicking on a Button Just use the selected row and edit the values in a separate Window. As long as you use an observable collection you see the changes immediately in the grid If you want to open the window after a (double)click - there is also an event for

## Answer

**Svetoslav Dimitrov** answered on 03 Jun 2021

Hello Adhemar, We have created a Knowledge-Based article that showcases how to put the Grid in Edit mode both by using a Popup form and in Inline mode. I hope it helps you move forward with your application. Regards, Svetoslav Dimitrov
