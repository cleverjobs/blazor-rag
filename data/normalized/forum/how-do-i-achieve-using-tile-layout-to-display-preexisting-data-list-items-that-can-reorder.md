# How do I achieve using Tile Layout to display preexisting data/ list items that can reorder?

## Question

**Kez** asked on 14 Dec 2022

Right now, each tile can be created in each Content and TilelLayoutItem tag. The way my current list works is to use the TileLayout inside of a TelerikListView component using my list as the data. Like this: <TelerikListView Data=@Data Pageable="true" PageSize="int.MaxValue"> <Template> <TelerikTileLayout Columns="1" Reorderable="true" Resizable="false" RowHeight="180px"> <TileLayoutItems> <TileLayoutItem HeaderText="Descriptors"> <Content>@context.Description</Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> </Template> </TelerikListView> It shows each item from the list in a new tile as expected, but the problem with this is that since I put it in just one Content/TileLayout tag, each tile somehow counts as one tile, so the Reorderable feature doesn't work. You can test this by adding a another Content tag. The contents of the second tag will only be able to swap with the contents of the first tag, but the contents of the first tag still won't be able to swap with each other. Does the same thing if you use a foreach loop to display the list data as well. How do I achieve using TileLayout to display preexisting data/ list items that can reorder? Or how can I reorder the tiles while using a foreach loop?

### Response

**Yanislav** commented on 19 Dec 2022

Hello Kezi, I've reviewed the code snippet and actually, the behavior is expected. The TileLayout component generally allows reordering the items. However, in your scenario, the TileLayout declaration is inside the Template of the ListView. Since the Template configuration generates content for each item of the ListView, this means a new instance of TileLayout component is rendered for each item. The different TileLayout instances are not related and that's the reason why the tiles cannot be reordered. To use the reorderable feature, all the elements have to be rendered inside only one TileLayout. This is achievable, but it means you have to pass a collection of objects to the ListView, and those objects should have a property that is also a collection. Then you can iterate through it to generate TileLayoutItems for each entity. Here is an example: [https://blazorrepl.telerik.com/mQPQvKve53mhrzEp31](https://blazorrepl.telerik.com/mQPQvKve53mhrzEp31) However, this approach is confusing if you do not have hierarchical data - in this case, the ListView will actually have only one item, like in the example above. Based on the code snippet you've shared, I assume that's not the case. With that being said, may I ask you to share more information on what you are trying to achieve and if is there a reason to use the TileLayout component inside the ListView? Thus, it will be clearer to me what you are aiming for and if the desired result is achievable, I can try to find a possible solution. Thank you in advance!

### Response

**Kezi** commented on 19 Dec 2022

Hi Yanislav! I actually wanted the tiles to be displayed like a pageable list that could also be reordered, but then I realized that there was a pageable component that I could just add to the TileLayout by itself, so I figured it out.
