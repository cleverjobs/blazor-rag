# When showing a modal-dialog, how do I show just the TreeList's scroll bar?

## Question

**Joe** asked on 03 Jan 2024

I have the following TreeList definition inside a model-dialog box. The modal-dialog:overflow-y options (auto, hidden, scroll, visible) let me turn the dialog's scroll bar on and off. However, none of them seem to work like I would expect. How do I freeze the height of the modal-dialog so that the scroll bar on the TreeList becomes active? It seems the dialog stretches off-screen. @if (ShowDialog)
{ <div class="modal fade show d-block" id="exampleModal" tabindex="-1" role="dialog"> <div class="modal-dialog" role="document"> <div class="modal-content"> <div class="modal-header"> <h5 class="modal-title" id="titleLabel"> @Title </h5> <button type="button" class="close" data-dismiss="modal" aria-label="Close" @onclick="Close"> <span aria-hidden="true"> &times; </span> </button> </div> <div class="modal-body"> <TelerikTreeList Data="@Groups" IdField="@nameof(SelectedGroup.Id)" ParentIdField="@nameof(SelectedGroup.ParentId)" SelectedItems="@SelectedGroups" FilterMode="@TreeListFilterMode.None"> <TreeListColumns> <TreeListColumn Expandable="true" Field="Name" Title="Name" /> </TreeListColumns> </TelerikTreeList> </div> </div> </div> </div> } <style>.modal-dialog,.modal-dialog img { /*same value to avoid overwidth*/ width: 70%; height: 90%; margin: 15px auto; overflow-y: visible;
} </style>

## Answer

**Dimo** answered on 08 Jan 2024

Hello Joe, 1) Scrollability requires a height for the element that should be scrollable. The height can be set in px, em, %, vh or any other CSS unit. If you wish the modal container to be scrollable, set a height to it. Keep in mind that a percentage height requires an explicit height for the parent element and the rule applies recursively. 2) If you wish the TreeList to be scrollable, then set the Height parameter of the TreeList. It may be also possible to set a height to the modal container and 100% Height to the TreeList. In this case, the TreeList will be scrollable. The above rule for percentage heights applies here too. Regards, Dimo Progress Telerik

### Response

**Joel** commented on 08 Jan 2024

While your answer may be correct... it was not helpful.

### Response

**Dimo** commented on 09 Jan 2024

Joe - most probably, the application is not applying percentage heights, according to web standards. Every percentage height requires an explicit height for the parent element. On a side note, if you need something to be 50% of the browser window, then it's a lot easier to use viewport units - 50vh. Here is a REPL example that uses our Window and a TreeList inside.

### Response

**Joel** commented on 09 Jan 2024

! Dude ! You rocked my world. I've never used the TelerikWindow. My modal-dialog was greatly lacking and this took care of that. High-fives all around.

### Response

**Joel** commented on 09 Jan 2024

The REPL got me there.

### Response

**Joel** answered on 08 Jan 2024

Overflow-y: Hidden with Height of 50% gives me this: Chops the dialog and doesn't let me use the scroll bar. I expected this one to work because the dialog height seems to be forced.

### Response

**Joel** answered on 08 Jan 2024

Overflow-y: Visible with Height of 50% gives me this: The scrollbar of the page shows up which means the treelist just extends the entire page down... still not using the TreeList scrollbar.

### Response

**Joel** answered on 08 Jan 2024

Overflow-y: Scroll with Height of 50% gives me this: Overflow-y of Auto looks the same way. This one may work if I turn off the TreeList scrolling. But, this scrollbar is for moving down the Dialog... not the TreeList

### Response

**Joel** answered on 08 Jan 2024

As a side note... when I get rid of the TreeList scrollbar then my title and button to close the dialog become unavailable. So, I'd really like the TreeList scroll option to work here.
