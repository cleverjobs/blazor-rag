# Grid Drag&Drop

## Question

**Mat** asked on 22 May 2021

After playing around with the new Drag&Drop functionality - I found a possible issue After Drag and Drop a lot (about 20 to 30 times) the Grid does not refresh anymore. Also the demo (Blazor Telerik Demo) does not work correct anymore - have a look at the attachment Best regards Matthias

### Response

**Marin Bratanov** commented on 23 May 2021

Can you reproduce this if you run the demos locally? The way the UI behaves makes me think there is some error and perhaps there is some issue in the demo code itself that throws an exception, or the SignalR connection drops in your case for some reason. On my end 40-50 drag operations still worked OK on the demo, but I might be much closer to the server than you and have much smaller latency.

### Response

**Matthias** commented on 24 May 2021

Thank you for your fast reply! I will test the demo locally- it’s pretty difficult to reproduce, sometimes it works perfect, sometimes after a few operations it breaks. In my application it also breaks locally without any exceptions. I will observe it a few days and send a a report. Have a nice day!

### Response

**Marin Bratanov** commented on 24 May 2021

Sure, Matthias, if you can reproduce a problem reliably, please do edit the opener post and post the example so we can have a look. When we can reproduce a bug reliably we have the chance to fix it, otherwise there is too much guesswork involved.

## Answer

**Matthias** answered on 27 May 2021

Maybe it was something with the cache- but I don’t have any issues anymore.

### Response

**Marin Bratanov** commented on 27 May 2021

Thank you for getting back to me! I am happy to see things working well for you!
