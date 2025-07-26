# Row Drag and Drop Indicator Not Visible for a Grid within a Window

## Question

**Lel** asked on 12 Sep 2023

Here's a code snippet demonstrating the issue: [https://blazorrepl.telerik.com/cRODPclB17lz8CCi20](https://blazorrepl.telerik.com/cRODPclB17lz8CCi20) Row drag and drop works like in the documentation example, except the indicator to show where the row will be dropped is missing. If you press escape this both cancels the drag and drop and closes the window. It also shows the indicator where it would have been, and there is no way to remove the indicator without refreshing the page. How can this issue be resolved?

### Response

**Georgi** commented on 15 Sep 2023

Hi, Leland, The issue of the missing drop hint stems from its z-index property. By design, a high enough z-index is set to the Window and Dialog components to ensure their contents are visible. When two or more such components are present, the z-index is incremented to make sure the currently focused component is shown. However, as of now, this hasn't been done with the rest of the popups, drop hints included. That said, you can override the z-index property of all drop hints, ensuring they will always show on top of other content. This can be done with the following CSS rule: <style>.k-drop-hint { z-index: 99999!important;
} </style> As for the second issue, it occurs because currently ESC does not cancel the drag and drop but closes the Window if it is focused. The hints can be removed from the DOM after the window is closed with the following JavaScript expression: document.querySelector( "body> div.k-drop-hint.k-drop-hint-h" ).remove(); Regards, Georgi Progress Telerik
