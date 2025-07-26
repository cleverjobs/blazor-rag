# Blazor telerik hierarchy grid collapses on incell editing

## Question

**Sre** asked on 12 Apr 2023

Hello, We have a Blazor Telerik Grid with DetailTemplate. One of the columns in Master/Parent is an editable column. The grid is set with "Incell" for property 'EditMode'. Issue:- When the editable column is clicked for editing, the entire grid row(with detail) is collapsed if the row is in expanded mode. Once editing is completed, the grid goes back to its previous state(expanded). Editing parent column in collapsed mode, works without any issues. Would like to know if I can keep the grid row in expanded mode while editing(ie. keep the original state) if its in expanded state. If not, is it the default behavior of hierarchy grid and how can it be overridden? Note - Tried with OnEdit and OnRowClick events, but the collapse happens before the respective event handler call. Thanks in advance ! Sreeni

## Answer

**Radko** answered on 17 Apr 2023

Hello Sreeni, First of all - thanks for bringing this issue to our attention. I have examined the case and can confirm there indeed appears to be room for improvement. I have logged a public item on your behalf where I have added your vote already: Blazor telerik hierarchy grid collapses on incell editing. The goal of this item should be to either not close the detail template at all, or to at least raise the correct state change event which one could act upon. As for a potential workaround, I am afraid there are not too many options here, as triggering edit does not raise an OnStateChanged event with ExpandedItems as a changed property, which seems rather unexpected. Regards, Radko Stanev Progress Telerik
