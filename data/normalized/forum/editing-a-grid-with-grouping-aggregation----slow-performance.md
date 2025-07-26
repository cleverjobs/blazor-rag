# Editing a grid with grouping/aggregation -- slow performance?

## Question

**Ada** asked on 14 Mar 2025

I have a grid with in-cell editing. Only some of the columns are editable. The grid is grouped by two columns, which I default in OnGridStateInit. The two aggregate columns are NOT editable. Everything works just fine, but as I click around through the editable columns, the page gets slower and slower and slower over time. Specifically, clicking away from an editable column causes a refresh (or something) that takes increasing longer and longer. A spinny loader appears. This behavior immediately goes away when the grouped columns are removed by ungrouping at the top of the grid (no code update). Is this a bug or am I doing something wrong? I tried changing from in-cell editing to in-row editing and have the same problem. A workaround is to ungroup for editing, and then regroup for display purposes, but I'm new and want to verify I'm not doing something wrong.

## Answer

**Anislav** answered on 16 Mar 2025

Hi Adam, I assume you're using the OnRead event handler to load data from an API and the OnUpdate event handler to update data on the server. Since these operations are asynchronous, the grid displays a loading indicator duting data operations that take more than 600ms to complete. I've prepared an example with this setup here: [https://blazorrepl.telerik.com/wfkxFgvK17ILV46V03.](https://blazorrepl.telerik.com/wfkxFgvK17ILV46V03.) Is this setup similar to yours? Are you able to reproduce the issue using this example? I haven’t been able to. How much data are you retrieving and displaying in the grid? Could you share some code that reproduces the issue? Regards, Anislav Atanasov

### Response

**Adam** commented on 17 Mar 2025

Hi, thanks so much for your response! Your posted example actually shows the issue I described, but it takes a few modifications to really notice it: 1) Remove the artificial 1000ms delay. (line 83) 2) You create a sample dataset of 30 items. Please change that to 90. (line 92) 3) Set the Page Size of the grid to 90 as well. (line 9) 4) Run the code. 5) Click up and down the far right column, as if you were editing each value. You'll note the page gets slower and slower with every click.

### Response

**Anislav** commented on 17 Mar 2025

I was able to reproduce the issue by following the instructions you provided. However, I am not sure what is causing this behavior. It seems that when the Grid is set to edit records in a popup using the EditMode parameter with GridEditMode.Popup, the issue either does not occur or is less noticeable. Here is an example: [https://blazorrepl.telerik.com/wzYxFVYC23JPEHSA23](https://blazorrepl.telerik.com/wzYxFVYC23JPEHSA23) Regards, Anislav Atanasov

### Response

**Adam** commented on 17 Mar 2025

Removing grid aggregates resolves the issue. I'm glad you were able to reproduce the problem. Please let me know if there is an actual internal bug that can be fixed.

### Response

**Adam** commented on 17 Mar 2025

I concur that Popup editing seems to resolve the issues as well. It must have something to do with how aggregates are calculated after an update, maybe? I don't know. Hopefully you/your engineers can figure it out. Thanks again for your attention!

### Response

**Adam** commented on 17 Mar 2025

Sorry, one more comment. Popup editing does NOT resolve the issue. As more and more edits are made, the page gets slower and slower over time. It takes 20-30 edits on your example page. It's much more noticeable on my app. The workaround I have found is to remove grouping while editing, then regroup.

### Response

**Dimo** answered on 19 Mar 2025

Hi Adam, Anislav, Indeed, I observed the degradation in performance. I created a public item that you can track: Improve performance when editing a grouped Grid Regards, Dimo
