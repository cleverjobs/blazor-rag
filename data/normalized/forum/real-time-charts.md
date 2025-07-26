# Real-time charts

## Question

**Bla** asked on 30 Mar 2021

Hi. I'm just wondering if there is a way to get a real-time chart like this. (or any other of the style) I'm already made something "similar" with Telerik's charts. It is working but the component refresh does not look good. It redraws the series every time I add a new value. In my approach I tried using StateHasChanged () and Chart.Refresh () getting the same results. Can you give me an idea of how to achieve that the series are not redrawn completely and only the last value is added in such a way we would obtain a smoother behavior? Regards. Ludwig.

## Answer

**Marin Bratanov** answered on 30 Mar 2021

Hi Ludwig, The link seems to be missing, yet I doubt there is a charting engine that does not need to redraw the entire chart, at least at one point. What I can suggest is disabling the animations for the chart by setting its Transitions parameter to false, so that there is less visible change for the user. Regards, Marin Bratanov Progress Telerik

### Response

**Blazorist** answered on 30 Mar 2021

Hi Marin. Yes, you are right. I had not seen your answer and coincidentally doing tests I found the property Transitions. All I need to do is set it to false and I get the behaviour that I need. Also change the rendering mode to canvas in order to consume less resources. <TelerikChart Height="100%" Width="100%" @ref="@CPUChart" RenderAs="RenderingMode.Canvas" Transitions="false"> By the way, I have a window of about 30 items that are the ones I show in the graph. I handle the list binded with the series as a FIFO queue. Adding and removing a value every x seconds. In your experience, do you think it is the correct way to operate on the list associated to the chart? Thank you very much! Ludwig.

### Response

**Marin Bratanov** answered on 31 Mar 2021

Hi Ludwig, What you are doing is the typical approach people take. What I'd keep an eye out for is a couple things: how often you do data updates - especially in a WASM scenario - re-rendering the chart far too often can consume resources and the app can become a little unresponsive for the user (say, if they want to do something else besides look at graphs that update all the time) how much data you pass - especially in a WASM scenario - every new piece of data usually goes over the wire, so you should consider sending only what you need, as that is a relatively slow process how much the chart re-renders - I would suggest building a new collection with the new data (e.g., remove one or more items if needed, add the new item or items coming from the server) and pass that to the chart once, so it re-renders only one how many elements the chart renders- reducing them will improve its performance, you can read more here, here and here. Regards, Marin Bratanov

### Response

**Blazorist** answered on 31 Mar 2021

Thank you very much Marin. Very kind for the detailed answer you have given me. Regards. Ludwig.

### Response

**Marin Bratanov** answered on 31 Mar 2021

Glad to help :) --Marin
