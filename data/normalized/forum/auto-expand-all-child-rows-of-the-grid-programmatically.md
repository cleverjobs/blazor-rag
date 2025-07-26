# Auto-Expand all Child rows of the grid programmatically

## Question

**Mik** asked on 18 Jan 2023

I'm trying to expand all child rows of the grid whenever a user has a flag to auto-expand. I'm using the ExpandedItems collection in the GridState to add all items from my datasource to the collection. This works when I initially click the switch to turn auto-expand on. However, whenever I move to a new page, filter, change the page size, etc. all of the child rows end up collapsed. I have tried re-setting the ExpandedItems collection using some of the grid's events like PageChanged or StateChanged but nothing happens. My guess is that the mechanism that resets the Expanded Items is being called after I am expanding them, so the rows are being set back to collapsed. Is there a way to do this so that whenever a page change or filter occurs, all items are expanded?

## Answer

**Hristian Stefanov** answered on 23 Jan 2023

Hi Mike, Based on the provided information, I understand that the scenario is about a hierarchical Grid in which the desired result is to keep its rows expanded during different operations. Let me know if I'm missing something from the scenario. Indeed, the hierarchical grid behavior is that when leaving the current editing cell (which fires OnUpdate and updates the cell) or performing an operation (filter, paging, etc.), the Grid items are getting collapsed/refreshed. That is how the mechanism reacts to such changes in the state. To change the above-described behavior and keep the items expanded state (upon updating a cell, and performing an operation), we have an open feature request that will allow it: Persist Hierarchy Expanded Items State. I voted there on your behalf and raised the priority. You can also subscribe to the item to receive email notifications for status updates. In the meantime, if an alternative approach appears, I will post it as a comment at the above link. If we can assist with anything else, I'm at your disposal. Regards, Hristian Stefanov Progress Telerik

### Response

**Mike** commented on 23 Jan 2023

Hi Hristian, Thanks for your response. Yes ultimately, at the heart of it, I would like to be able to persist the hierarchical data. Although in my case, I'm using the DetailTemplate to display a large text field in the parent record, so that it spans all of the columns and doesn't stretch the rest of the fields out. So there is currently no workaround to set the expanded items back after a state change event? Thanks, Mike

### Response

**Hristian Stefanov** commented on 26 Jan 2023

Hi Mike, Currently, I'm sorry to confirm that there is no workaround. If such appears, I will immediately post it in the public item. Kind Regards, Hristian
