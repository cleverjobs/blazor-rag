# Dynamically create tileLayoutItem from collection.

## Question

**JayJay** asked on 28 Sep 2020

I'm trying to use the TileLayout to create a photo list viewer similar to your example on the TileLayout overview page. My list of photos is coming from a collection so the number of TileLayoutItem is variable. How would I do this? Here is the code I've tried. Should i use your pager component? <TelerikTileLayout Columns="5" ColumnWidth="300px" RowHeight="235px" Reorderable="true"> <TileLayoutItems> @foreach (var item in photoIdList) { <TileLayoutItem> <content> <div class="card"> <img card-img-top alt="Card image cap" src="[https://myphotoapi/image/api/photo?pid=@item&w=167&h=125"](https://myphotoapi/image/api/photo?pid=@item&w=167&h=125") /> </div> </content> </TileLayoutItem> } </TileLayoutItems> </TelerikTileLayout> I keep getting this error: crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.TileLayoutItem' does not have a property matching the name 'ChildContent'. System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.TileLayoutItem' does not have a property matching the name 'ChildContent'.

## Answer

**Marin Bratanov** answered on 28 Sep 2020

Hi Jay, The <Content> tag has an uppercase "C" and tags are case-sensitive so they compile properly. Regards, Marin Bratanov

### Response

**Jay** answered on 28 Sep 2020

Thanks for the quick reply. Yes that fixed it. I need to remember components should be capitalized by convention as compared to html tags.
