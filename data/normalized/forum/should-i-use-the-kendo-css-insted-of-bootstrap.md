# Should I use the Kendo css insted of bootstrap?

## Question

**Mar** asked on 02 Sep 2021

I am a little confused about where kendo css stops and where bootstrap starts. I can see that all Blazor Controls are created using kendo css classes. Are there utilities for margin, padding and grid layout in the kendo library, can I skip bootstrap?

## Answer

**Dimo** answered on 03 Sep 2021

Hi Martin, The UI for Blazor's Bootstrap theme makes our components look consistent with the Bootstrap CSS framework, so that the two can be used together. However, we do not provide CSS classes for constructing layouts - we have components for that (e.g. Form, GridLayout, TileLayout, Splitter, etc.). The Splitter is useful for organizing the whole page in areas, for example - header, left content, right content, footer. Splitter panes can be collapsed and resized. The GridLayout displays items in rows and columns, similar to the CSS grid layout. The StackLayout displays cards in a single row or column with some spacing options. The TileLayout displays tiles that are resizable and reorderable. So depending on your scenario and needs, you can indeed skip the Bootstrap CSS library. Please refer to our Bootstrap theme documentation for more details. Regards, Dimo Progress Telerik
