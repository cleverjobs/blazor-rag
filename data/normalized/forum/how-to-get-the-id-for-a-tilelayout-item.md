# How to get the Id for a TileLayout Item?

## Question

**Kez** asked on 19 Dec 2022

The example for the OnReorder feature returns a null result. The Id (args.Id) is never shown in the console log message. @* Handle the OnResized event *@<TelerikTileLayout Columns="3" Reorderable="true" OnReorder="@OnReorderHandler"> <TileLayoutItems> <TileLayoutItem HeaderText="Panel 1"> <Content> Regular sized first panel.</Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 2"> <Content> You can put components in the tiles too.</Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 3" RowSpan="3"> <Content> This tile is three rows tall.</Content> </TileLayoutItem> <TileLayoutItem HeaderText="Panel 4" RowSpan="2" ColSpan="2"> <Content> This tile is two rows tall and two columns wide </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> @code { async Task OnReorderHandler ( TileLayoutReorderEventArgs args ) { Console. WriteLine ( $ "tile {args.Id} reordered, might be a good time to save the state." ); } }

## Answer

**Yanislav** answered on 21 Dec 2022

Hello Kezi, The "Id" property of the received arguments is "null" since, as I see in the snippet, the Id parameter of the TileLayoutItems is not declared. In order to receive an Id in the OnReorder event handler, declare an Id for the tile items. <TileLayoutItem Id="second" HeaderText="Panel 2"> I realize that this specifics is not listed in the documentation, so please accept my apologies if this has caused some inconvenience on your end. We will update the article as soon as possible. I've modified the example and set IDs for the TileLayoutItems. Here is how the component behaves now: [https://blazorrepl.telerik.com/QmPQcYOi47N0QaMt14](https://blazorrepl.telerik.com/QmPQcYOi47N0QaMt14) With this configuration, the value of the received Id equals the declared Id instead of null. I hope the above information will help you move forward with your application. Regards, Yanislav

### Response

**Kezi** commented on 28 Dec 2022

Thank you. Do you know if there's a way to change the ID based on the tile reorder position? For example, if reorderable was enabled, and the tile item data was being pulled from a list, and I moved the last item in the list to the top, the ID should now be "first." Is that possible?

### Response

**Tsvetomir** commented on 02 Jan 2023

Hi, Kezi, The Id is passed as a reference with its public getter and setter. Therefore, you can update the Id directly in the handler: args.Id="my new id"; Note that this Id is used for internal identification of the items. It is not rendered as an id attribute to any HTML element. It is designed to be used actually for identifying the content of the respective tile (e.g. "sales chart" id will hint that the tile contains a chart component that shows sales). Having said that, it is best to keep key-value pairs of the tile in their order. This way, you can persist the state without the risk of unintentionally introducing a duplicate id. [https://docs.telerik.com/blazor-ui/components/tilelayout/state](https://docs.telerik.com/blazor-ui/components/tilelayout/state)
