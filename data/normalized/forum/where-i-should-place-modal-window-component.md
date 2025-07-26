# where I should place Modal Window component?

## Question

**Ale** asked on 07 Nov 2022

I have TelerikGrid and when I click on the item of this grid, I should open Telerik Window Modal component. <StatusUpdateModalComponent WindowVisible="@ModalVisible"> </StatusUpdateModalComponent> In grid: <GridCommandButton OnClick="ShowUpdateWindow"> Update </GridCommandButton> In event handler: protected void ShowUpdateWindow(GridCommandEventArgs args)
{
ModalVisible=true;
} When it's inside grid it opens many modal windows (for each row). But if outside it shows only one time and doesn't show again if I click again. Should I put it inside grid or outside?

## Answer

**Svetoslav Dimitrov** answered on 10 Nov 2022

Hello Alexandre, We have a sample application that showcases how to create a custom popup form for the Grid. Can you check the approach from there and get back to me if it helped you move forward with your application? Regards, Svetoslav Dimitrov
