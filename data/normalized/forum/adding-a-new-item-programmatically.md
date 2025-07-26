# Adding a new item programmatically

## Question

**Ric** asked on 28 Feb 2020

Hi there, I need the same fuctionality of the "Add" command of the grid's toolbar but using a button located anywhere in the page. Is this possible? <GridToolBar> <GridCommandButton Command="Add" Icon="add">Add Item</GridCommandButton> </GridToolBar> Thank you.

## Answer

**Svetoslav Dimitrov** answered on 02 Mar 2020

Hello Richard, There are a few ways to approach that: There is a thread in our Feedback Portal (link here ) for a feature request that might suit your needs. If public methods for controlling the grid are implemented you will be able to invoke them from buttons anywhere on the page. I have given your Vote for it. You could also Follow it in order to receive email notifications for future status updates. Another way of doing it is to use a custom form for editing or adding (for examples click here and here ). A third way could be by relocating the GridCommandButton "Add" by surrounding it in a div and use the position CSS property to put it anywhere on the page where you require. Here is a short sample: <GridToolBar> <div style="position:*position options*>
<GridCommandButton Command=" Add " Icon="add"> Add Item </GridCommandButton> </div> </GridToolBar> If neither of these work for you or require any further assistance, please do not hesitate to contact us. Regards, Svetoslav Dimitrov
