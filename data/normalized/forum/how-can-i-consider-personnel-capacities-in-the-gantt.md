# How can I consider personnel capacities in the Gantt?

## Question

**duk** asked on 05 Dec 2022

Good day, I would like to use the Gantt chart for industrial production planning. Independently of the bars, a color highlighting of individual columns (see picture) is to be inserted based on the personnel situation in available employee hours (e.g. workstation 2: 7h/...) and the workload according to the work plan ( workstation 2: .../7h). In addition, a mouse-over on the capacity situation is to be shown per day. Can this be implemented by the current functions in the Gantt? So far I have not been able to find any configurable elements for the columns. This is actually enormously important for our project and something like this (or similar) was confirmed in the initiation interview, which among other things prompted the purchase of the license. Alternatively (even better) would be a dynamic capacity historygram under the Gantt, which is synchronously movable in vertical axe. Here, only a bar (required employee hours per day) would have to be displayed as a total and a constant line (available employee hours) would have to be inserted additionally. Would a connection with a column chart be feasible from your point of view? (Kind a like: [https://demos.telerik.com/blazor-financial-portfolio)](https://demos.telerik.com/blazor-financial-portfolio)) Many thanks in advance.

## Answer

**Svetoslav Dimitrov** answered on 08 Dec 2022

Hello Paul, Let me summarize what I understood from your request: In the Gantt chart, you are displaying the actual/total work hours per workstation. In the Tooltip, I can see that Workstation 2, and Workstation 3 are fully loaded (Workstation 2) and Workstation 3 is beyond the limit (14/10h). I believe that the problematic case is for Workstation 2 and Workstation 3. I did not understand what you would like to happen if this is the case. What should the Gantt chart do to react to those facts? Regarding your question about the Column Chart, yes, a connection should be possible. You can pass Gantt's data to the Chart and the Chart component should render accordingly. I am kindly waiting for your feedback. Regards, Svetoslav Dimitrov

### Response

**duktionsplanungIGP** commented on 09 Dec 2022

Thanks for your response. Ich will try the second solution first. Can I dynamically synchronize the vertical scollbar of the gantt and the chart? Do you have any examples for that scenario? Thank you very much. Regards, Paul

### Response

**Svetoslav Dimitrov** commented on 13 Dec 2022

Hello Paul, Can you please follow up on the desired scenario? I was trying to sum up your request, but I did not understand the exact scenario. On the topic of dynamically synchronizing the vertical scrollbar, can you follow up with a bit of information on this topic too?

### Response

**duktionsplanungIGP** answered on 20 Dec 2022

Good morning, I can try to describe the scenario in more detail. The Gantt chart visualizes the production orders that will be processed in the specified time period (defined by start and end time). This production order contains a work plan, which activities (assembling, welding, joining) have to be performed to get the desired part at the end. However, in the Gantt I can see only at macro level when all the work will be done - in which time period. However, since I need to know how many people have to work on each task list or activity (stored in the task list data), I need to show how many people (and thus employee hours (7-8h)) are required depending on the position of the event in the Gantt (time period). For this purpose, a histogram should show the available capacity (how many employees are present according to plan) and the required capacity (how many employees I need according to the work plan in the period). If I move the event (production order) in time, the required capacities also change dynamically, because they are needed at a certain time within this event (fixed times in work plan). However, the histogram should run dynamically synchronously, so that, for example, for the 20th of December in the Gantt also below for the 20th of December in the histogram, quasi on a height, the capacities are displayed and these are not shifted in time. Therefore it must run horizontally dynamically synchronously, if possible via a scroll bar. Thank you very much and relaxing christmas holidays! Best Regards Paul

### Response

**Svetoslav Dimitrov** commented on 22 Dec 2022

Hello Paul, I really appreciate your feedback on the topic. I think I understand your business needs. To be sure that we are on the same page, let me provide a quick summary: Each production order is a summary task that contains three sub-tasks - Assembling, Welding, and Joining. For each sub-task, you have some people working on it. You would like to display the employees currently working on the tasks to be displayed in the UI, let's say in a Column Chart (that is the other name of the Histogram). The first two points can be achieved with the current toolset of the Gantt Chart. You can add a separate column in the Gantt Tree to show how many people work on each sub-task. The Column Chart supports the DateAxis feature. Commonly, most Gantt Chart tasks have start and end dates across some timespan (let us say 35 days). Each column in the Column Chart can represent a single date, but it would not be able to render a single column for a time span of 35 days. How would you like to approach that? Based on the information you have provided I believe that you will receive the most complete service from our Professional Services team (a paid service, not included in the license). You can send your exact business needs to them and they will handle the implementation. Let me know if you would like to get in touch with our Professional Services team. Have a great holidays yourself.
