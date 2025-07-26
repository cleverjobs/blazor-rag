# Grid: only toggle between asc/desc in a single column sort

## Question

**Cra** asked on 18 Apr 2022

Hi, apologies if this has been asked but I didn't find it via search. We are implementing the grid in our projects and one feature I'd like to implement is to prevent the default or 'no sort' state on a column when toggling sort on the same column. Our users should always be sorting by one column. If the user clicks repeatedly on the column currently sorted, we want it to only toggle between asc and desc. What happens right now is with single sort mode, say we have col1 that is sort asc by default. - If the user clicks col1 header once, it sorts to desc. - If they click col1 header again it goes to 'empty'.* * What I want to do is have it flip to desc instead. Obviously if they then sort by a different column it will clear the sort on this column. I understand why there is such a default/empty state but was curious if there is a way to prevent this in our scenario. I saw the OnStateChanged example in the docs but it doesn't seem to provide info on what was previously selected so I could even cancel what was going on. Unless I missed something there. Thanks!

## Answer

**Svetoslav Dimitrov** answered on 21 Apr 2022

Hello Craig, We have an open feature request regarding the AllowUnsorted setting of the Grid. Once this is implemented, you will be able to disable the unsorted state for the Grid. I have added your Vote for it, and you can click the Follow button to receive email notifications on status updates. In the public thread, you can see a workaround for the time being. Regards, Svetoslav Dimitrov Progress Telerik
