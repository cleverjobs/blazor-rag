# Extra whitespace in TileLayoutItem

## Question

**Der** asked on 23 Mar 2021

I have 3 sections A, B and C. Each is a tilelayoutitem. I have to calculate the rowspan for each with a C# function. for example section A has 47 rows, B has 17 and C has 9. below is the snippet. when it renders there is a bunch of whitespace after the 47 rows in section A, a moderate about for the 17 rows in B and C shows up fine with only a little bit of whitespace. I don't know how to make each tilelayoutitem fit its content properly. thanks @foreach (var item in Groups) { <TileLayoutItem HeaderText="@item" ColSpan="6" Class="tile-with-overflow" RowSpan="@CalculateRowSpan(@item)"> <Content> <SaleDetail Group="@item" FormatDetails="@SalesFormatDetails"></SaleDetail> </Content> </TileLayoutItem> }

## Answer

**Marin Bratanov** answered on 24 Mar 2021

Hi Derek, The tiles are not designed to fit their content, but the other way around - they create layout that the content should fit. If you are looking for containers that can take the size of their content, the Window component might be a good fit. If you don't set Height to it, the content will determine the height, like with any other HTML element. I'm also attaching here a screenshot of the sample size calculation from the sample I made for you below. You will note that I have dramatically decreased not only the row/column size, but also the spacing which also counts towards the final size. The default spacings (gaps in the CSS terminology) are 16px in each direction so 47 rows will give you 46 gaps times 16px=736px height from the gaps alone, and then also the size of the row too. <TelerikTileLayout Columns="15" ColumnWidth="10px" RowHeight="5px" RowSpacing="5px" ColumnSpacing="5px" Resizable="true" Reorderable="true"> <TileLayoutItems> <TileLayoutItem HeaderText="A" RowSpan="47" ColSpan="6"> <Content> 47 tall, 6 wide. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="B" RowSpan="17" ColSpan="6"> <Content> 17 tall, 6 wide. </Content> </TileLayoutItem> <TileLayoutItem HeaderText="C" RowSpan="9" ColSpan="6"> <Content> 9 tall, 6 wide. </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Regards, Marin Bratanov Progress Telerik

### Response

**Bill** answered on 25 Mar 2021

How do I put an image in a TileLayouItem? My ChartComponent is 925x480px. I will load the saved .png file into the TileLayoutItem and try different layouts. Essentially, we need 2x2 with minimal whitespace gaps.

### Response

**Marin Bratanov** answered on 25 Mar 2021

Hi Bill, If you want the tile to fit an image with those dimensions, you need to set the appropriate ColSpan and RowSpan, according to the dimensions of the columns, rows and gaps you've provided to the component. To reduce gaps, reduce the RowSpacing and ColumnSpacing parameters like in my example. If you want the tile to be 2 columns wide and two rows tall, but accommodate content that is 925px this means that the ColSpan should be 2, RowSpan should be 2, and the ColumnWidth should be something like 460px, with RowHeight at least 240px (or equal to ColumnWidth if you want squares). Regards, Marin Bratanov
