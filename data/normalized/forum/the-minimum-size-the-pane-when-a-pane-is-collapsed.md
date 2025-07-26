# The minimum size the pane when a pane is collapsed.

## Question

**Val** asked on 20 Mar 2023

Hello, How to collapse the pane using their collapse/expand buttons or double-clicking the split bars, so that the minimum size the pane is taken into account. Currently the whole panel is closed. Thank you very much

## Answer

**Dimo** answered on 22 Mar 2023

Hi Valeriy, If I understand correctly, you want the three buttons in the left column to remain visible when you collapse the "Home" pane. This is possible only if you split the content into two separate panes. Users will collapse the "Home" pane and the new one on the left will remain visible. Regards, Dimo

### Response

**Valeriy** commented on 22 Mar 2023

Hi Dimo, I'm using the Telerik TabStrip inside the left SplitterPane with the minimum size. The TabStrip tab titles display on left side of the component content. I want the TabStrip tab titles in the left to remain visible when user collapse the SplitterPane Why the minimum size the pane is not accepted, when user collapse the SplitterPane? I made a small example: [https://blazorrepl.telerik.com/wdaxmGFA03rrrm4F28](https://blazorrepl.telerik.com/wdaxmGFA03rrrm4F28) Thank you for the help.

### Response

**Dimo** commented on 23 Mar 2023

The Min pane size applies during resizing and when the pane is visible. When you collapse it, it is no longer visible. This is how the Splitter works.
