# TileLayout nested tiles

## Question

**Dav** asked on 22 May 2025

Is it possible to have nested tiles in a TileLayout. For example. The main page could have 2 tiles which the user could reorder or resize and within each of these tiles there would be some components that could be reordered or resized just within the inner tile. In the image below I was able to create 2 tiles but they cannot be reordered. I tried placing these 2 tiles inside another TelerikTileLayout but had issues when attempting to reorder or resize the inner components. In my actual application I may end up with multiple levels of nesting and the structure is generated from a definition read in by the page. I create an example here [https://blazorrepl.telerik.com/QTapQGvU54CO5Pjw05](https://blazorrepl.telerik.com/QTapQGvU54CO5Pjw05) Regards

## Answer

**Hristian Stefanov** answered on 27 May 2025

Hi David, Nesting TileLayouts is uncommon, but possible if tile resizing and reordering are enabled only for the innermost component instance. The opposite use case can appear complex and confusing for end users, as they may expect to drag tiles across component instances, which is not possible. Here are some guidelines and steps you can follow: Guidelines for Nested TileLayouts Enable Resizing and Reordering for One Level at a Time: To prevent conflicts between nested TileLayouts, enable resizing and reordering only for one level at a time. Typically, this would be the innermost TileLayout instance, to avoid unexpected behavior where resizing or reordering affects both parent and child components. Toggle Resizable and Reorderable Properties: Bind the Resizable and Reorderable properties of each TileLayout instance to different variables. You can toggle these properties at runtime to control which level of tiles can be resized or reordered. User Interface for Level Selection: Implement a user interface element, such as toggle buttons, to allow users to choose which level of tiles they want to resize or reorder. Example Here's an example of how you might set up nested TileLayouts with resizing and reordering only on one level. Feel free to adjust it following the above guidelines. <TelerikTileLayout Reorderable="false" Resizable="false" Columns="4" ColumnWidth="200px" RowHeight="200px"> <TileLayoutItems> <TileLayoutItem HeaderText="Outer Tile 1"> <Content> <TelerikTileLayout Reorderable="true" Resizable="true" Columns="2" ColumnWidth="100px" RowHeight="100px"> <TileLayoutItems> <TileLayoutItem HeaderText="Inner Tile 1"> <Content> Inner Content 1 </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Inner Tile 2"> <Content> Inner Content 2 </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Outer Tile 2"> <Content> <TelerikTileLayout Reorderable="true" Resizable="true" Columns="2" ColumnWidth="100px" RowHeight="100px"> <TileLayoutItems> <TileLayoutItem HeaderText="Inner Tile 3"> <Content> Inner Content 3 </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Inner Tile 4"> <Content> Inner Content 4 </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Regards, Hristian Stefanov Progress Telerik

### Response

**David** commented on 27 May 2025

Thanks. Regards.
