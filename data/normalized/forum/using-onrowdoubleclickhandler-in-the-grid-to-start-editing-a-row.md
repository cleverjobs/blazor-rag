# Using OnRowDoubleClickHandler in the Grid to start editing a row

## Question

**Rus** asked on 28 Jan 2022

I have a grid setup, and would like to double click to open the pop up to edit the row. I set the Grid and add the OnRowDoubleClickHandler to my code. I tested that this works, from the debugger when I double click a row the Handler gets called correctly. I then add code to get the current state from the grid, I setup the EditItem and the OriginalEditItem then I Set the State. My problem is I need todo Three clicks to get this to work. I have to double click the row, then wait and click once more in the same row, then the pop up editor comes up. I can do fast three clicks and it works as well. If I double click on the row to edit, then even click once time on any other row, the original row comes up for edit. From the examples I am setting the state like this: var currState=GridRef. GetState (); // reset any current insertion and any old edited items. Not mandatory. currState. InsertedItem=null; // add item you want to edit to the state, then set it to the grid SampleData originalItem=MyData. Where ( itm=> itm. ID==4 ). FirstOrDefault (); SampleData itemToEdit=SampleData. GetClonedInstance ( originalItem ); // you can alter values here as well (not mandatory) //itemToEdit.Name="Changed from code"; currState. EditItem=itemToEdit; currState. OriginalEditItem=originalItem; // for InCell editing, you can use the EditField property instead await GridRef. SetState ( currState );

## Answer

**Russ** answered on 28 Jan 2022

Found the issue. I was calling OnRowDoubleClickHandler as a async task. As soon as I removed it, the double click was working correctly
