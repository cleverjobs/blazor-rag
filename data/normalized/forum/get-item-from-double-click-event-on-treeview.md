# Get Item from Double Click Event on TreeView

## Question

**Jam** asked on 18 Jul 2019

Hey all, I've been playing with your Blazor components and I need some help with your new TreeView. My objective is to choose an item in the treeview (i.e. double click the item or drag and drop) and then populate a grid with the chosen item. This is probably easy but I'm stuck. You have an OnExpand event on the tree but nothing else. Does anyone have an example or idea on how I could do this please? Thanks, Jimmy

## Answer

**James** answered on 18 Jul 2019

Hi All, Well, I answered my own question. With a little more digging I ran across a thread caller "Row click and double click events". Andriy post on his solution for click is awesome. So with a little adjustment I got it working for double click. [https://www.telerik.com/forums/row-click-and-double-click-events#PQpO8DcbzkCArF3UqoLcWA](https://www.telerik.com/forums/row-click-and-double-click-events#PQpO8DcbzkCArF3UqoLcWA) Cheers, Jimmy

### Response

**Marin Bratanov** answered on 18 Jul 2019

Hello Jimmy, Indeed, this is the approach for now. We are still not certain if such DOM events are to be exposed by the component or through a template, yet you may want to Follow the feature request page to get notifications on any updates: [https://feedback.telerik.com/blazor/1418731-node-click-event.](https://feedback.telerik.com/blazor/1418731-node-click-event.) I've already added your vote for the feature. Regards, Marin Bratanov
