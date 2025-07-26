# TabStripTab Initializes every time its activated?

## Question

**Dou** asked on 25 Feb 2021

It appears that every time a TabStripTab which is not currently active is clicked on, its contained components are recreated and initialize. I was expecting that after the first time the TabStripTab is activated and the components are initialized, subsequent events that make a TabStripTab active would not Initialize the components again. Can I configure the TabStripTab so that it doesn't Initialize every time?

## Answer

**Marin Bratanov** answered on 25 Feb 2021

Hello Douglas, This is the expected and blazor-y way to do this. Nevertheless, you can Follow this feature request for when the tabstrip will initialize all content and switch it out with CSS: [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) Regards, Marin Bratanov

### Response

**Daniel** answered on 24 Mar 2021

Marin, I'm posting as a reply since I have a related question. In this code you can see that I'm starting a while(true) loop. When I switch to another tab in TelerikTabStrip, it does not clean up this async task. From the Debug statements I can tell that it continues to run. Can you recommend a way to handle this? Or perhaps a better pattern for having this while loop for each tab? Thanks! protected override void OnInitialized() { RealTimeUpdate(); Debug.WriteLine("LEAVING OnInitialized"); } private async Task RealTimeUpdate() { while (true) { gridData=GetData() StateHasChanged(); await Task.Delay(10000); Debug.WriteLine("STILL GOING"); } }

### Response

**Marin Bratanov** answered on 24 Mar 2021

Hello Daniel, You can consider using a cancellation token to cancel such tasks when the component is disposing. You can find a similar approach used in this page from our Dashboard sample app - the "endless" loop activates when you select the "Generate random data at interval" option from the dropdown at the top right hand side. Regards, Marin Bratanov

### Response

**Daniel** answered on 24 Mar 2021

Too many concepts I can't grasp on that page. I will see if I can apply just the cancellation token portion to my example.
