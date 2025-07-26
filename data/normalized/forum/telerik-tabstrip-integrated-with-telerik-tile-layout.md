# Telerik Tabstrip integrated with Telerik Tile Layout

## Question

**LeoLeo** asked on 20 May 2024

I'm currently trying to integrate telerik tilelayout inside telerik tabstrip dynamically? for example <TabStripTab Class="@(filteredRows.Any() ? GetTabWidth() : "auto")" Title="@tabtitle1["tabtitle"].ToString()"> <TelerikTileLayout Columns="12" RowHeight="auto" Resizable="true" Reorderable="true"> <TileLayoutItems> @foreach (DataRow row in filteredRows) { <_Data columnspan='Convert.ToInt32(row["columnspan"])' rowspan='Convert.ToInt32(row["rowspan"])' pageId="@pageId" oDt="row" encryptQueryString="@data"></_Data> } </TileLayoutItems> </TelerikTileLayout> </TabStripTab> } @if (filteredRows2.Any()) { <TabStripTab Title="@tabtitle2["tabtitle"].ToString()"> <TelerikTileLayout Columns="12" RowHeight="auto" Resizable="true" Reorderable="true"> <TileLayoutItems> @foreach (DataRow row in filteredRows2) { <_Data columnspan='Convert.ToInt32(row["columnspan"])' rowspan='Convert.ToInt32(row["rowspan"])' oDt="row" data="@data"></_Data> } </TileLayoutItems> </TelerikTileLayout> </TabStripTab> when i set persist content to true it reloads the components which invoke the database calling ?I s there any way to do without component being refreshed?

## Answer

**Sean** answered on 06 Aug 2024

Hello, When using Telerik components like TelerikTileLayout inside a TelerikTabStrip and setting PersistContent="true", the behavior you are observing where the components are being refreshed, causing additional database calls, is due to the nature of how the PersistContent feature works. The PersistContent="true" attribute in Telerik components typically preserves the content of the tab when switching between tabs. However, this also means that the content remains in the DOM and doesn't get destroyed when switching between tabs, which can lead to the component being re-rendered and potentially re-fetching data from the server when the tab is shown again. To prevent the component from being refreshed and avoid unnecessary database calls when using PersistContent="true", you can cache the data that is fetched from the database either on the server-side or client-side. This way, when the component is re-rendered, it can first check the cache for the data before making a new database call.
