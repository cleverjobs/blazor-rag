# Drag and Drop

## Question

**kha** asked on 27 Sep 2020

Hello, i was wondering if you are currently working on drag and drop ability or you have it in mind

## Answer

**Marin Bratanov** answered on 27 Sep 2020

Hi Khashayar, In general, drag-and-drop in Blazor is a bit limited at the moment due to limitations of the framework, and such features are, therefore, a bit limited in our components because we have to see what the framework does before we invest a sizeable chunk of time into building a JS solution to only have to scrap it and re-integrate something from the framework - that would prevent us from shipping a ton of other useful features. We are keeping an eye on the situation and there are various features that can be implemented, such as a draggable window, drag-and-drop for treeview nodes, files in the upload and so on. So, at the moment, drag-and-drop can be used to reorder columns and to group by a field in the grid, and in the TileLayout. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 06 Oct 2020

Hi again, I am writing with an update - there is a feature request for the grid rows now: [https://feedback.telerik.com/blazor/1488666-row-drag-and-drop-in-the-grid.](https://feedback.telerik.com/blazor/1488666-row-drag-and-drop-in-the-grid.) The idea right now is that there will be an event when you drop a row that will give you the dropped row, the row over which it was dropped, and maybe whether it was above, below or on top of the row. This would let you alter the data as needed for the custom sorting logic. If this is something you're interested in, click the Vote and Follow buttons on the page to, respectively, raise its priority and get status updates via email. Regards, Marin Bratanov
