# Edit the text of a Treeview item node

## Question

**Mic** asked on 25 Oct 2021

I have a requirement where the user needs to be able to add a node to the treeview, which I have working. The requirement however is to NOT use a popup to prompt for the text for the node, but rather add the node - and have it editable straight away. The users can then enter the text, and either hit enter, or press/click somewhere else on the screen to commit the text change - and in turn - call the relevant API endpoint to persist the text. Any ideas? Was hoping for an <EditItemTemplate> of sorts, but only <ItemTemplate> seems to be available. Any assist appreciated :)

### Response

**Michael** commented on 25 Oct 2021

I have stumbled across the TelerikTreeList component. Is this the only way to do it?

## Answer

**Svetoslav Dimitrov** answered on 27 Oct 2021

Hello Michael, Indeed, you are correct that the TreeList would be a good replacement for the TreeView in cases you need built-in CRUD operations. Another alternative would be to use the Rename node demo application as a basis. This application showcases how to edit the text for a node in a TreeView without the need for a popup window. Regards, Svetoslav Dimitrov
