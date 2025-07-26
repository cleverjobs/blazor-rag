# Fixed Size Tile by Position

## Question

**Wal** asked on 30 Oct 2020

Is there a way to fix the size of the tile based on it's position in the tilelayout component?

## Answer

**Marin Bratanov** answered on 31 Oct 2020

Hello Walter, How would you expect such a feature to be exposed? For example, if in OnResized, you could: use .GetState() to see what tile is in what position (at the moment you can get the state already, identifiers for tiles will likely be implemented here, feel free to join the discussion) find the tile at the position you want to change and set its ColSpan and RowSpan in the state object you got with the desried values and business logic you have use .SetState() to set that new state to the tile layout - that's the thing that can't work right now, the tile layout does not re-render in that event, it's purely informational for the developer so you can save the state (see the notes here ) So, if you could perform step 3, would that suffice for you? Regards, Marin Bratanov
