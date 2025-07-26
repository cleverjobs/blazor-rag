# Zero Records Message

## Question

**Kel** asked on 15 Mar 2020

I would like to display a message where rows would be displayed in grid, when there are no records returned from the data source. Basically, a message with graphics and hyperlink that direct the user to a page to enter a new record. Is there any feature of the grid that would support this thy of workflow? Row Template maybe?

## Answer

**Svetoslav Dimitrov** answered on 16 Mar 2020

Hello Kelly, I have created a new Feature Request for creating a NoDataTemplate. You can Follow the implementation from this link: [https://feedback.telerik.com/blazor/1457874-zero-records-message-nodatatemplate](https://feedback.telerik.com/blazor/1457874-zero-records-message-nodatatemplate) and i have given a Vote on your behalf. As a workaround, in the meantime, I would suggest you use if / else statement where you render the grid only if there is information to be displayed like shown in the code snippet below: @if(MyGridData==null) {
//Loading animation or any custom component (e.g. CreateNewItem)
} else
{ <TelerikGrid /> } You can also see these Feature Requests on our Feedback Portal. They are not directly connected to what you have encountered, but will further enrich the functionality you described: [https://feedback.telerik.com/blazor/1446689-animation-during-grid-load](https://feedback.telerik.com/blazor/1446689-animation-during-grid-load) [https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly](https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly) I have given your Vote for both of them, as well, and you can Follow the status updates on their implementation. Regards, Svetoslav Dimitrov
