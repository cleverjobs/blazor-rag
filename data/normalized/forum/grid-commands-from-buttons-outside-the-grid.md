# Grid Commands from buttons outside the Grid

## Question

**Cip** asked on 07 Oct 2020

Hello, I don't want to add any GridCommandButton into the Grid's Layout. For example I have implemented a ribbon on my page and there I have a button "Add Entry". Is it possible to achieve the same functionality from that button I have mentioned as when the Add GridCommandButton with the attribute Command="Add" is added to the grid layout in the toolbar? Best regards, Cipri

### Response

**Nathan** commented on 01 Feb 2024

Hi, I have the same question, is this solved?

### Response

**Leland** commented on 29 Feb 2024

I also have this same question. Marin never answered it here.

### Response

**Dimo** commented on 01 Mar 2024

>> Marin never answered it here. That's not true. The answer has always been to use the Grid state and programmatic editing and inserting through the Grid state. I just added one more link to Marin's old reply to make it more clear. (Edit): The linked example uses Buttons inside the Grid Toolbar, but you can move them anywhere outside the Grid too.

### Response

**Leland** commented on 13 Mar 2024

I was referring to the fact that Marvin continued the conversation in private ticket 525612. I did finally figure it out. The "some predefined value" threw me and probably the others off. You can just leave that out and use a blank new item if you don't want to auto-populate the inserted item with a default value.

## Answer

**Marin Bratanov** answered on 07 Oct 2020

Hi Cipri, Yes, you can do that with the Grid State feature. See an example here: Add or edit Grid rows programmatically. I'd also recommend you review the entire Grid State article for more details on what this feature can do for you, because it can do much more. Regards, Marin Bratanov

### Response

**chesk345** commented on 18 Jun 2021

I'd like to do something simpler; that is, to simply open the Add New Record dialog via a button outside the Grid. Is there an example of such you can refer me to, please?

### Response

**Marin Bratanov** commented on 19 Jun 2021

You can do this with the grid state feature, see the section titled "Initiate Editing or Inserting of an Item". It looks like this async Task StartInsert() { var currState=GridRef.GetState(); // reset any current editing. Not mandatory. currState.EditItem=null; currState.OriginalEditItem=null; // add new inserted item to the state, then set it to the grid // you can predefine values here as well (not mandatory) currState.InsertedItem=new SampleData() { Name="some predefined value" }; await GridRef.SetState(currState); // note: possible only for Inline and Popup edit modes, with InCell there is never an inserted item, only edited items }

### Response

**chesk345** commented on 21 Jun 2021

Thanks for your reply. Please bear with me, as I did look at this code before posting my question, and I don't understand how it applies to what I want to do. I was expecting to be able to open the "Add New Item" popup and let the user provide the new item through the UI. The sample code shows an instance of the class with hard-coded values: currState.InsertedItem=new SampleData() { Name="some predefined value" }; How do I get those vales from the popup instead? Thanks again for your assistance.

### Response

**Svetoslav Dimitrov** commented on 24 Jun 2021

Hello Francis, The line of code you refer to showcases how-to predefined some values for your user and this is not mandatory. If you provide such values and the user edits them you will get the values that the user input, not the predefined. Let me know if you need any further assistance.

### Response

**chesk345** commented on 24 Jun 2021

I understand. I am asking how to open the Telerik "Add New Item" popup from my own button on the page, rather than from the Telerik Command Button in the Grid's toolbar. Thanks...

### Response

**Marin Bratanov** commented on 27 Jun 2021

I made a private ticket for you so we can discuss this in a more comfortable environment than these short comments, its ID is 1525612. By the time you are reading this, you should have my reply there.
