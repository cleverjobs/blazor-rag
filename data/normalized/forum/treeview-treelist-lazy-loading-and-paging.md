# Treeview/Treelist lazy loading and paging

## Question

**Han** asked on 24 Nov 2023

I am using treelist to display an hierarchical dataset that is read from an API using web calls. I have encounbtered a problem where my source data contained many root items (which was an actual programming error), but by this surfaced a problem that you have to read ALL roots (or all children of an item) in order to make paging work correctly. As in some cases I may have up to 10K "child" items (whichs unfortunately landed in my root due to the error), I would expect treeview and treelist to handle this without actually having to transfer 10K objects from my API call. For this, a similar solution like the one used for the grid "OnRead" event would be a good solution as this could tell the treeview how many (root or direct child) objects there actually are and provide the offset to start reading with and how many objects to return. You could even throw in filtering and sorting for all I care and recycle the DataRequest class for this. This in turn should help getting the "paging" right for the treelist/treeview. Regards - Hans

## Answer

**Dimo** answered on 27 Nov 2023

Hi Hans, (Only) OnRead may not help here, because it will still load all sibling items at a given level. What you need is virtualization and we have feature requests that you can follow - TreeView Item Virtualization TreeList Row Virtualization I already voted on your behalf. Regards, Dimo Progress Telerik
