# Javascript to highlight a row (Blazor server/Datagrid)

## Question

**mik** asked on 15 Jan 2023

I'm attempting to emulate the typical desktop grid user experience with using up/down/pgup/pgdn keys to move the selected row (single) in a grid. I have it all working perfectly when running locally in development. But when deployed to production server, it's too slow due to latency over the wire. It's about a 1 second delay for each row change if there are more than say 5 rows. The more rows that are displayed, the slower it gets. I tried the navigable setting but it's just not quite what our users would expect. So, I'm thinking of a JavaScript function that will simply highlight a row. I'm already handling tracking the selected row programmatically, so if I can just highlight the specified row at the front end and remove the 2-way binding on the SelectedItems, I think that will solve the latency issue. 2 questions: (1) Is this how you'd suggest handling this to speed up the rendering? (2) do you have any JavaScript that would highlight a row in a grid where a specific cell value is equal to a specific value? I've spent a couple of days trying to find/come up with some JS that would highlight a row. But I'm not having any luck. await _js.InvokeVoidAsync("App.highlightRow", "." + "myGridClassName", IDValueToHighlight); Thank you for your consideration, Mike

## Answer

**Nadezhda Tacheva** answered on 18 Jan 2023

Hi Mike, Generally speaking, we have received reports for slow performance of the select all functionality in WASM apps and we will be revising that. However, the issue occurs when multiple items are selected simultaneously. I would say that such a delay is not expected when selecting only one item. I was testing the built-selection but I am not hitting such an issue. As far as I can understand the use case, you are performing a custom selection as the user navigates up and down. My suggestion will be to focus on the selection business logic and see if it can be optimized to avoid this lag. I would generally not recommend using JavaScript to handle the scenario. However, if you'd still like to take this road, what you may try is to add a "k-selected" class to the row when you want to highlight it. This is the class that we internally use for the selection. When you want to omit the highlight after the user navigates out of the row, you will need to remove this class from the row element. I hope you will find this information useful. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva Progress Telerik

### Response

**mike** commented on 19 Jan 2023

Thank you, that was very helpful. Here's the JavaScript that we ended up with. FYI, the class name is "k-state-selected". We'll do some experimenting to see if it improves performance. App.highlightRow=function (gridClassName, idValueToSearch, column) { var tables=document.getElementsByClassName(gridClassName); var rows=tables[0].getElementsByTagName('tr'); for (var i=1; i <rows.length; i +=1) { var cols=rows[i].getElementsByTagName('td'); /*console.log(cols[column].innerText);*/ if (cols[column].innerText==idValueToSearch) { (rows[i]).classList.add("k-state-selected"); } else { (rows[i]).classList.remove("k-state-selected"); } } }

### Response

**Nadezhda Tacheva** commented on 23 Jan 2023

Hi Mike, Thank you for the follow-up! I am glad you have found a solution that fits your scenario. I'd like to add a note on the class name, so you don't run across some issues when you upgrade. Up to version 3.3.0(inclusively) of UI for Blazor, this class was indeed called "k-state-selected". However, as of 3.4.0 release, it was renamed to "k-selected". Having that in mind, if you upgrade and continue using the old class name, you may not get the expected selection styling. I hope you will find this information useful. Please let us know if any other questions appear.
