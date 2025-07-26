# Missing Grid OnCellClick Event?

## Question

**Dav** asked on 23 Jul 2022

Is there a workaround for being able to execute code before rendering the edit template on a Grid when edit mode is Incell? I need to execute code just before editing starts.

## Answer

**Svetoslav Dimitrov** answered on 27 Jul 2022

Hello David, The OnEdit event will fire just before the cell is opened for editing and before the editor template. You can use that event to cancel the editing or to execute any custom code before the Grid is rendered in Edit mode. You can read more about the sequence in which the events are firing for the Incell edit mode from the Event sequence section of our InCell editing documentation article. Regards, Svetoslav Dimitrov
