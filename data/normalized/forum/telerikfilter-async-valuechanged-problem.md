# TelerikFilter async ValueChanged problem

## Question

**Lic** asked on 21 Oct 2022

Hello I'm using Telerik.UI.for.Blazor 3.6.0 I would like to make async query on TelerikFilter ValueChanged EventCallback ( change found items count ) but when i change my implementation from private void OnFilterValueChanged ( CompositeFilterDescriptor filter ) { //code here } to private async Task OnFilterValueChanged ( CompositeFilterDescriptor filter ) { //code here validation and get filteringRules int count=await dispatcher.QueryAsync( new CountItemsQuery(filteringRules)); //code here } TelerikFilter stop working properly When i add second filter condition and then i would like remove it nothing hapens (GUI do not reload) Second try remove filter condition throws Exception: Index was out of range. Am i doing something wrong or it's error? Best regards

## Answer

**Svetoslav Dimitrov** answered on 26 Oct 2022

Hello Licencje, I have prepared a small REPL where I made the event handler for the ValueChanged asynchronous and it seems to work as expected. Can you modify the snippet so that we can reproduce the issue? This will greatly help us when investigating the problematic behavior that you are reporting to us. An additional question, did the same code work prior to 3.6.0? Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Licencje** commented on 26 Oct 2022

Thanks for quick response In your example code missing await in handler. Simplest change which break the program private async Task OnValueChanged ( CompositeFilterDescriptor filter ) {
Value=filter;
TriggeredValueChangedCount++; await Task.Delay( 1 ); //equivalent of async method } With this code try add 2 expressions and then remove it one by one. Changed REPL In 3.4.0 same situation.

### Response

**Svetoslav Dimitrov** commented on 28 Oct 2022

Hello Licencje, I am sorry I missed such a simple reproduction of my first message. This is indeed a valid bug and I have logged it on your behalf - Async code in the ValueChanged event handler prevents the re-render of the component. I have added your Vote for it and you are automatically subscribed to receive email notifications on status updates. That being said, as a small token of appreciation I have awarded Telerik Points to your account.
