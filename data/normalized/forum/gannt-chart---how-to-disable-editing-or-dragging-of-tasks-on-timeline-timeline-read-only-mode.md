# Gannt chart - How to disable editing or dragging of tasks on timeline? (Timeline read-only mode?)

## Question

**Len** asked on 15 Jul 2022

Hi, I'm trying to display the Gantt component as read-only. While it's easy to disable editing for the TreeList that's part of the Gantt component, I can't seem to disable editing of tasks through the timeline. There are 3 things that I'm trying to resolve. 1. How to disable the popup editor when double clicking a task in the timeline? Only thing I can come up with is hide the popup editor through a css class with 'display: none': <GanttSettings> <GanttPopupEditSettings Class="d-none" /> </GanttSettings> 2. How to disable dragging of the tasks on the timeline? I can't seem to find a way to lock the tasks in place. I can always drag them. I'm aware I can set the start and end values of the task back to the original value after dragging (through OnUpdate), but I don't want to be able to drag them in the first place. 3. How to hide specific editing buttons on the task in the timeline? When hovering over a task in the timeline it always shows a number of handles or buttons for the following actions (circled in red in the below screenshot): - change the completion percentage. - specify new dependencies - delete the task How can the handles and buttons for these actions be disabled/hidden? Kind Regards

## Answer

**Dimo** answered on 18 Jul 2022

Hi Lennert, Here is how to disable editing in the Gantt TimeLine and altogether: 1. Disable popup editing on double-click Cancel the OnEdit event. async Task OnEdit ( GanttEditEventArgs args ) {
args.IsCancelled=true;
} 2. How to disable dragging of the tasks on the timeline? AND 3. How to hide specific editing buttons on the task in the timeline? Dragging cannot be disabled, but it's possible to make the user unaware of it. It is possible to use CSS and hide all UI hints, which are related to dragging and resizing. Razor <TelerikGantt Class="no-timeline-edit" TreeListEditMode="@GanttTreeListEditMode.None" OnEdit="@OnEdit" /> CSS /* delete button */.no-timeline-edit.k-task:hover.k-task-actions, /* resize handles */.no-timeline-edit.k-task:hover.k-resize-handle, /* progress drag handle */.no-timeline-edit.k-task-wrap:hover.k-task-draghandle, /* dependency handles */.no-timeline-edit.k-task-wrap:hover.k-task-dot, /* drag overlay */.no-timeline-edit.k-gantt-marquee, /* drag tooltip */.no-timeline-edit.k-gantt-resize-hint { visibility: hidden;
} Last but not least, remove the OnUpdate and OnDelete handlers. Here is a feature request about built-in read-only Gantt TimeLine that I opened on your behalf. Regards, Dimo
