# Tree Drag & Drop broke in version 3.3.0

## Question

**And** asked on 16 May 2022

Hello, I'm still trying to produce a reproducible scenario in Repl to share, but upgrading to 3.3.0 broke our treeview drop code. If I revert back to 3.2.0 it begins to work properly again. I have a typical tree with several "folders" & "files" which I can drag and drop to re-organize. The only time telerik shows the circle with a slash drag hint is when you drag the source node over top itself. In 3.3.0 it seems that the circle with the slash is showing up over most but not all of the nodes in the tree. I can't explain why it thinks some areas are valid drop targets and others are not. One node is fine to drop on and the next and previous ones show the No Drop icon. I'll continue to try and make a Repl example but wanted to raise awareness of this sooner than later. Thanks, -Andy

## Answer

**Andrew** answered on 16 May 2022

Turns out we had hardcoded our Telerik main js file instead of using the one in the nuget package. For those of you who see mysterious behavior after upgrading and using the nuget package, make sure you're referencing your js file like this: <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script> Thanks, -Andy
