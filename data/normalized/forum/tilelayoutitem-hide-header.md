# TileLayoutItem, hide header

## Question

**Han** asked on 31 May 2023

Hello all, In my app I use tile layout to let the user manage a bunch of charts and other things. when in "edit mode" I want the headers of the tiles to be displayed, but in "browse" mode I want the headers of the tiles to be invisible as the title of the tile et all is already in the chart displayed in the tiles content. Using an empty <HeaderTemplate> I still get an empty one line header for each tile. Is there a way around this,? Otherwise, please see this as a FR. Regards, Hans

## Answer

**Hristian Stefanov** answered on 05 Jun 2023

Hi Hans, As far as I understand, the desired result is to selectively hide the tile headers based on certain conditions. I confirm that achieving this is indeed possible. To accomplish it, you can utilize an " if " block to dynamically apply a CSS style of " display: none; " to the HTML element representing the tile header. Consequently, the header will only be visible when you are in " edit mode ". I have prepared an example for you that demonstrates the above approach: @if (!EditMode)
{ <style>.my-tilelayout.k-tilelayout-item-header { display: none;
} </style> } <TelerikButton OnClick="@( ()=> EditMode=!EditMode )"> Enter "Edit Mode" </TelerikButton> <br /> <br /> <TelerikTileLayout Class=" my-tilelayout " Columns="3" RowHeight="150px" Resizable="true" Reorderable="true"> <TileLayoutItems> <TileLayoutItem HeaderText="Tile 1"> <Content> Regular-sized first tile. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Tile 2"> <Content> You can put components in the tiles too. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Tile 3" RowSpan="3"> <Content> This tile is three rows tall. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="Tile 4" RowSpan="2" ColSpan="2"> <Content> This tile is two rows tall and two columns wide </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> @code {
bool EditMode;
} Please run and test it to see the result. I remain at your disposal if you encounter any challenges during the testing phase. Regards, Hristian Stefanov

### Response

**Hans** commented on 05 Jun 2023

Works like a charm. I could even put the class on <TileLayoutItem> and have individual tiles show ther header or no. Thanks!

### Response

**Louise** commented on 12 Jun 2023

I have nearly lost my mind trying to figure out headers and footers and even when I get it right it's usually hit and miss and I can't repeat it. I am very grateful. threes
