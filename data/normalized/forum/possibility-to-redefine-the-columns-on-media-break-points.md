# Possibility to redefine the columns on media break points

## Question

**Den** asked on 24 Sep 2020

Hi, The TileLayout is great. I'm searching a way to dynamically switch the definition according to media breakpoints like width of the screen. Say, on a wide screen I want to present my data in 4 columns, but on a small screen the tiles a very compressed so I would like to have them reordered in 2 or even only 1 column. Is that possible?

## Answer

**Marin Bratanov** answered on 24 Sep 2020

Hi Denis, You could use the desired way to get the event to the C# (Blazor) side (for example, tools like this ), and then change the parameter value of the Telerik component. Here's a basic example that does it on a click of a button to illustrate the concept (two key things - I there is no column width because it is easier to get even distribution that way, since the width will vary, and the columns don't go below 2 because then there is a tile in this sample that spans two columns so you should keep an eye out for that too - I also added that information to the docs - commit ): <TelerikButton OnClick="@ChangeColumns">Change columns</TelerikButton> @ColumnsCount

<TelerikTileLayout Columns="@ColumnsCount" Width="100%" RowHeight="150px" Resizable="true" Reorderable="true">
<TileLayoutItems>
<TileLayoutItem HeaderText="Panel 1">
<Content>Regular sized first panel.</Content>
</TileLayoutItem>
<TileLayoutItem HeaderText="Panel 2">
<Content>You can put components in the tiles too.</Content>
</TileLayoutItem>
<TileLayoutItem HeaderText="Panel 3" RowSpan="3">
<Content>This tile is three rows tall.</Content>
</TileLayoutItem>
<TileLayoutItem HeaderText="Panel 4" RowSpan="2" ColSpan="2">
<Content>This tile is two rows tall and two columns wide</Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>

@code{ int ColumnsCount { get; set; }=4; void ChangeColumns ( ) { if (ColumnsCount> 2 )
{
ColumnsCount=2;
} else {
ColumnsCount=4;
}
}
} Regards, Marin Bratanov

### Response

**Brian** answered on 24 Sep 2020

Denis, If you want to stick with stylesheets, the tilelayout uses css grids so you could define your own media queries or take advantage of other grid-* properties. Brian
