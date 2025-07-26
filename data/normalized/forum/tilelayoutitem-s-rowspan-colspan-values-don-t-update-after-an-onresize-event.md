# TileLayoutItem's RowSpan, ColSpan values don't update after an OnResize Event?

## Question

**Bri** asked on 09 Jul 2022

When user resizes a TileLayoutItem in a TileLayout, I am trying to detect the new RowSpan and ColSpan values using the OnResize Event. However, it appears as if the RowSpan and ColSpan values don't update? Simple Example, resize a tiled item and look at the console output (it never changes regardless of the new user-set spans): @using Telerik.Blazor.Components

<TelerikTileLayout Reorderable="true" Resizable="true" Columns="4" ColumnWidth="200px" RowHeight="200px" OnResize="@OnResize">
<TileLayoutItems>
<TileLayoutItem @ref="@_tileItem1" Id="tile1" HeaderText="Tile 1" ColSpan="1" RowSpan="1">
<Content>Tile 1 </Content>
</TileLayoutItem>
<TileLayoutItem @ref="@_tileItem2" Id="tile2" HeaderText="Tile 2" ColSpan="1" RowSpan="1">
<Content>Tile 2 </Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>

@code { private TileLayoutItem _tileItem1=null; private TileLayoutItem _tileItem2=null; private void OnResize ( TileLayoutResizeEventArgs args ) { if (args.Id=="tile1" ) { Console.WriteLine( $"rows: {_tileItem1.RowSpan}, cols: {_tileItem1.ColSpan} " ); } else if (args.Id=="tile2" ) { Console.WriteLine( $"rows: {_tileItem2.RowSpan}, cols: {_tileItem2.ColSpan} " ); }
}

}

### Response

**Brian** commented on 09 Jul 2022

After a little more investigation, I see that the state *is* getting updated with the new spans, but the instance ref is not. So if you query one vs. the other, you get 2 different answers. Here is example code showing how the TileLayoutItem and state of the TelerikTileLayout are out-of-sync: @using Telerik.Blazor.Components <TelerikTileLayout @ref="@_tileLayout" Reorderable="true" Resizable="true" Columns="4" ColumnWidth="200px" RowHeight="200px" OnResize="@onResize">
<TileLayoutItems>
<TileLayoutItem @ref="@_tileItem1" Id="tile1" HeaderText="Tile 1" ColSpan="@_item1ColSpan" RowSpan="@_item2RowSpan">
<Content>Tile 1 </Content>
</TileLayoutItem>
<TileLayoutItem @ref="@_tileItem2" Id="tile2" HeaderText="Tile 2" ColSpan="@_item2ColSpan" RowSpan="@_item2RowSpan">
<Content>Tile 2 </Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>

@code { private TelerikTileLayout _tileLayout=null; private TileLayoutItem _tileItem1=null; private TileLayoutItem _tileItem2=null; private int _item1ColSpan=1; private int _item1RowSpan=1; private int _item2ColSpan=1; private int _item2RowSpan=1; private void onResize ( TileLayoutResizeEventArgs args ) {
TileLayoutState state=_tileLayout.GetState(); if (args.Id=="tile1" ) {
Console.WriteLine( $"object1 rows: {_tileItem1.RowSpan}, cols: {_tileItem1.ColSpan} " );
Console.WriteLine( $"state1 rows: {state.ItemStates[ 0 ].RowSpan}, cols: {state.ItemStates[ 0 ].ColSpan} " );
} else if (args.Id=="tile2" ) {
Console.WriteLine( $"object2 rows: {_tileItem2.RowSpan}, cols: {_tileItem2.ColSpan} " );
Console.WriteLine( $"state2 rows: {state.ItemStates[ 1 ].RowSpan}, cols: {state.ItemStates[ 1 ].ColSpan} " );
}
}

} I can keep going in my own code and use the state values... but perhaps (?) this is a bug?

### Response

**Dimo** commented on 13 Jul 2022

Hi Brian, The TileLayout state is the correct place to check for the current TileLayout settings. The Blazor framework does not update parameter values, unless you use two-way binding, and this is currently not supported for the RowSpan and ColSpan parameters. However, we have it as a feature request for future implementation. Consider voting and following it.
