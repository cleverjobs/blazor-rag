# Preserve grid state on refresh.

## Question

**Sar** asked on 21 Dec 2022

I'm displaying "live" data in a telerik blazor grid that is refreshed every 30 seconds by a timer from a database. I've tried following the examples to preserve the grid state, but all rows collapse after StateHasChanged(). I do not want to store the state in the local browser. The reason I would like this feature, is that I will be displaying a large amount of nested data, and would like to only allow the user to look at one record at a time (to simplify the interface). I'm not able to successfully preserve the expanded state. I have also tried var state=Grid.GetState(); state.ExpandedItems=new List<MainModel> { mod }; await InvokeAsync(()=> StateHasChanged()); await Grid.SetState(state) But the state results in collapsed.

### Response

**Yanislav** commented on 23 Dec 2022

Hello Sara, Based on the description, I understand the Grid is rebound over time and you want to persist the expanded rows after rebinding. I've prepared an example where a similar scenario is implemented and the rows are not collapsing. [https://blazorrepl.telerik.com/QclmmduM06PElYBv41](https://blazorrepl.telerik.com/QclmmduM06PElYBv41) Is the scenario similar to the one at your end? If the sample is not useful, may I ask you to reproduce the problem you are facing in it and send it back to us for further review? Thus, I will be able to investigate it and try to find a possible solution.

### Response

**Sara** commented on 30 Dec 2022

**Edit - I'm querying the data every 30 seconds to refresh the grid using SourceData=GenerateData(); as per the example, but the page never refreshes when new data is found - and calling RebindGrid() in the timer event causes three dots and nothing happens. How can I refresh via a timer function and not just through user interaction? Perfect, that's exactly what I needed. Thank you!
