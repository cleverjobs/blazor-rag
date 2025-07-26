
## Environment
<table>
<tbody>
<tr>
<td>Product</td>
<td>Scheduler for Blazor</td>
</tr>
</tbody>
</table>

## Description
How do I "page" the scheduler data? I want to load on demand only the currently visible appointments in the view from the backend to improve performance.

## Solution
You can use the events the component provides to pass the current view and date to the data service so it can implement a high performant query to return only the necessary items, instead of returning all available appointments.

You can find an example in the following sample project: [Scheduler - Load Appointments On Demand](https://github.com/telerik/blazor-ui/tree/master/scheduler/load-appointments-on-demand)
