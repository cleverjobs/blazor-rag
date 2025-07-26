# Set row height (style) for Gantt control

## Question

**Mat** asked on 11 Oct 2023

I have a user requesting to change the row height (style) for a Gantt control. The user made a similar request for a TreeList and a Grid and I was able to identify the properties in css and override them with padding-block and padding-line. I tried the same for the Gantt control but those properties did not achieve the desired result. Here is the spacing they want that I was able to set for the TreeList and Grid controls: I was able to achieve that with the following css:.k-grid-md td, .k-grid-md .k-table-td, .k-button-md { padding-block: 0; padding-inline: 0; } The k-button-md was needed to reduce the padding if there was a command button on the row. Here is what the Gantt control looks like now: Any suggestions on how to achieve the same on the Gantt control?

## Answer

**Dimo** answered on 12 Oct 2023

Matt - The Gantt table rows have a height style that you also need to override with custom CSS to reduce their height. However, the Gantt layout depends on the row height and reducing it will break the appearance in the TimeLine section. I am afraid that such customization is not supported. Regards, Dimo Progress Telerik

### Response

**Matt** commented on 12 Oct 2023

Unfortunately some of my users don't believe it until they see it... form over function in many cases as well. What are the css classes/properties that need to be overridden?

### Response

**Dimo** commented on 12 Oct 2023

REPL test page On a side note, it is possible to increase the row height, whenever that's needed.

### Response

**Matt** commented on 12 Oct 2023

Thank you for the code sample!
