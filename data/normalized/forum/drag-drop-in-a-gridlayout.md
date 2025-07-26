# Drag & Drop in a GridLayout

## Question

**Hen** asked on 23 Feb 2024

I need a solution where I can rearrange "Boxes" in a GridLayout with Drag & Drop. Before I start to solve it badly on my own I want to make sure if there is not a good solution out there already !? Has anyone an example or a headstart for me ?

### Response

**Dimo** commented on 23 Feb 2024

The TileLayout uses a CSS grid under the hood and supports tile reordering. The configuration is not through rows and columns, but you can achieve a similar result with RowSpan and ColSpan.

### Response

**Hendrik** commented on 24 Feb 2024

Thank you very much for your answer, but I guess, your approach is not working for me because I need a fixed position for each box. All other boxes have to stay in their position after one has changed its position.

### Response

**Hendrik** commented on 25 Feb 2024

I helped myself and got to a very nice solution using the GridLayout and some CSS. I wasn ́t aware that Drag & Drop can be that easy...
