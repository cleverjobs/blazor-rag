# TileLayout improvements:

## Question

**Víc** asked on 29 Mar 2023

I'm working on a landing page builder, I need to be able to do a couple of extra things with TileLayout. I would like this behaviour to be added optionally by configuration. I would like to Drag & Drop elements between two TelerikTileLayout collections. In my dahsboard I want to have groups of tiles, like the ones in SAP launchpad, here are some images. I want to move tiles from one section to another. [https://experience.sap.com/wp-content/uploads/sites/56/2021/06/SAP-Fiori-Launchpad-Spaces_MyHome_1.96.png](https://experience.sap.com/wp-content/uploads/sites/56/2021/06/SAP-Fiori-Launchpad-Spaces_MyHome_1.96.png) I would like to specify the actual position of a element with the Row & Column index. I want to build a launchpad like the one in Azure. Here are some images of what I want to build. As you can see, you are free to chose any row/col you want in the grid. [https://media.licdn.com/dms/image/C5112AQGroL99SJPhag/article-cover_image-shrink_720_1280/0/1559712744601?e=2147483647&v=beta&t=0_c13EnPEq_pxXxf8SNuH1jzC4_N8hUYR_uf2kUKmSA](https://media.licdn.com/dms/image/C5112AQGroL99SJPhag/article-cover_image-shrink_720_1280/0/1559712744601?e=2147483647&v=beta&t=0_c13EnPEq_pxXxf8SNuH1jzC4_N8hUYR_uf2kUKmSA) [https://adamtheautomator.com/wp-content/uploads/2022/09/image-93.png](https://adamtheautomator.com/wp-content/uploads/2022/09/image-93.png)

## Answer

**Nadezhda Tacheva** answered on 03 Apr 2023

Hi, Please see my comments on the relevant points as follows: Drag & Drop elements between two TelerikTileLayout collections By design, dragging items between two TileLayout instances is not possible. For such functionality, I would recommend the Kanban Board component that we will release in a future version of UI for Blazor. For the time being, you may explore its appearance and behavior in the Kendo UI for jQuery version. If you still want to use the TileLayout, you may achieve the desired functionality with a custom approach - use a single TileLayout instance that contains all tiles and add dummy TileLayoutItem instances to serve as group names. Here is an example approach: [https://blazorrepl.telerik.com/wHYIaRlS01zYwLKE34.](https://blazorrepl.telerik.com/wHYIaRlS01zYwLKE34.) Note: the group header tile must occupy the maximum columns specified for the component, so it is not reordered while dragging the rest of the tiles. Specify the actual position of an element with the Row & Column index. This functionality is currently not available but I opened a feature request on your behalf: [https://feedback.telerik.com/blazor/1603940-ability-to-specify-initial-position-of-a-tile-row-and-column-parameters](https://feedback.telerik.com/blazor/1603940-ability-to-specify-initial-position-of-a-tile-row-and-column-parameters) I also added your vote there to bump its popularity. We prioritize the enhancements based on the community demand. As the creator, you are automatically subscribed to get status updates. I hope you will find the above information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva

### Response

**Víctor** commented on 06 Apr 2023

Thanks for your response. Yor REPL It's pretty close. But this some disadvantages, All the items are in the same grid so I can't change the tile sizes. And I won't be able to DnD between groups in diferent layouts. Which is something we where planning to add. For example DnD between the sidebar and the body. For the X / Y coordinates I was thinking of using css clases. BTW why is it that there are no CssStyles atributes in the components? This would be a clear usecase for a Style not a Class. I miss them :/ Thanks!

### Response

**Nadezhda Tacheva** commented on 10 Apr 2023

Hi, Thank you for the follow-up! I am glad I was able to propose a solution that is close to the one you are looking for. Please see details on the relevant points below: Tiles moving and resizing In terms of changing the size of the tiles, I am not sure why you are left with the impression that in this case the tiles cannot be resized. Changing their size does not depend on the fact that they are placed in a single TileLayout instance - you may test resizing a tile in the sample I shared and then move the tile to another group. The suggested solution focuses on allowing you to move tiles between different groups while keeping them in the same TileLayout instance as drag and drop between two TileLayout components is currently not supported. I've raised a discussion with the team about the possibility to allow such functionality and I'd like to gather some more feedback from you in this regard. Let's say you place a component in the tile (for example, a Grid) - you allow the users to interact with this component and after that, you save its state. What should happen if you move the tile with the Grid to another TileLayout instance? Shall it keep its state or shall it start anew? Another option we could consider is not handling the tiles moving from one TileLayout instance to another but exposing a drag/drop event which the developer may handle to have full control over the tile moving and what will happen with its content (similar to how the drag and drop functionality works in other components ). Please consider and let me know your thoughts. Components styling Having the ability to add a Class parameter instead of Style attribute is a design decision that allows more flexibility. One may need to add styles just to the root item of a component but others may need to access this specific component instance and style some of its child elements. While the child elements are not always accessible through the markup, adding a custom class to the component allows one to access its children in the CSS.

### Response

**Víctor** commented on 18 Apr 2023

I agree having a Drag & Drop event would give the biggest flexibility! Let's say you place a component in the tile (for example, a Grid) - you allow the users to interact with this component and after that, you save its state. What should happen if you move the tile with the Grid to another TileLayout instance? Shall it keep its state or shall it start anew? Well, I want the user to be able drag & drop the tiles of the Launchpad / Dashboard at design time. So I'm not sure the state of a grid inside of the tile is important to me. If we have the event I could just add & render the new tile to the new group, also remove it from the old one. Easy peasy Regarding the moving of a tile I think allowing the dev to specify a Rol Col is not enough, I would like to drag and drop a tile to a certain X Y row col and let it sick there. This could be done by setting a new property in the TileLayout called: AutoFlow: Dense (current behabiour, simiar to the css grid-auto-flow property) AutoFlow: Unset (the new behaviour where the itles can float freely in the TileLayout)

### Response

**Svetoslav Dimitrov** commented on 21 Apr 2023

Hello Victor, I am stepping up in this thread as my colleague Nadezhda is out of the office. I can see how the Drag and Drop events can be very beneficial for the TileLayout, thus I am opening a new feature request on your behalf - Allow Drag and Drop between different TileLayouts. I have added your Vote for it and you, as a creator, are automatically subscribed to receive email notifications on status updates. Regarding the AutoFlow parameter, thank you for the suggestion, this is also a very valid request - Add a parameter similar to the autoFlow one in Kendo React. Your vote is already in and you will receive email updates on status changes. Regards, Svetoslav Dimitrov

### Response

**Víctor** commented on 25 Apr 2023

Thanks yes that's sounds about right :)
