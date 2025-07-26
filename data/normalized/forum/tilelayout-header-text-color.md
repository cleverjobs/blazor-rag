# TileLayout header text color

## Question

**Dav** asked on 28 Sep 2020

I am using the Sass Themebuilder and trying to change the color of the TileLayout header text. It doesn't seem to be affected by the "Header text" property but instead by the "Component text". Is that by design? It seems wrong.

## Answer

**Svetoslav Dimitrov** answered on 29 Sep 2020

Hello David, You can Subscribe for status updates about this issue here: [https://github.com/telerik/kendo-themes/issues/1885.](https://github.com/telerik/kendo-themes/issues/1885.) As a workaround, you can add the Class parameter of the TileLayout and pass a custom CSS class to make the cascading of styles easier. As a quick reference, I have made a small sample, where I have changed the color of the headers to green: <style>.myTileLayout.k-tilelayout.k-tilelayout-item-header.k-card-title { color: green;
} </style> <TelerikTileLayout Columns="3" ColumnWidth="200px" RowHeight="150px" Resizable="true" Reorderable="true" Class="myTileLayout"> <TileLayoutItems> <TileLayoutItem HeaderText="Panel 1"> <Content> Regular sized first panel. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 2"> <Content> You can put components in the tiles too. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 3" RowSpan="3"> <Content> This tile is three rows tall. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 4" RowSpan="2" ColSpan="2"> <Content> This tile is two rows tall and two columns wide </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Regards, Svetoslav Dimitrov

### Response

**DoomerDGR8** commented on 02 Jun 2021

I needed background color as well: <style> .myTileLayout.k-tilelayout .k-tilelayout-item-header { background-color: blue; color: white; } </style>
