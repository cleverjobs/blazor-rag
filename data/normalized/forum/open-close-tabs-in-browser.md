# Open & Close Tabs in browser

## Question

**Pet** asked on 14 Apr 2022

Hi, I'd like to close all tabs, which were opened by user. I have problem, it still closes only one opened tab. I use this methods: <TelerikButton OnClick="@OpenTabC" Primary="true">Open Tab C</TelerikButton> <TelerikButton OnClick="@OpenTabF" Primary="true">Open Tab F</TelerikButton> <TelerikButton OnClick="@CloseTabs" Primary="true">Close Tab</TelerikButton> async Task OpenTabC() { await JS.InvokeVoidAsync("open", $"counter", "_blank"); } async Task OpenTabF() { await JS.InvokeVoidAsync("open", $"fetchdata", "_blank"); } async Task CloseTabs() { var loadDataTasks=new Task[] { Task.Run(async ()=> await JS.InvokeVoidAsync("close", $"counter")), Task.Run(async ()=> await JS.InvokeVoidAsync("close", $"fetchdata")) }; try { Task.WaitAll(loadDataTasks); } catch (Exception ex) { // handle exception } } What is wrong in CloseTabs method, please, why does it close only one tab? It is possible to do without JS.InvokeVoidAsync? Thank you Peter

### Response

**Dimo** commented on 19 Apr 2022

Peter - check this StackOverflow thread and experiment with a similar approach. You will need JavaScript by all means. This question is related to general programming, so I am removing our component-related tags.
