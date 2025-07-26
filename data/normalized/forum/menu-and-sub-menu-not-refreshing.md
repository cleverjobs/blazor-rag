# menu and sub-menu not refreshing

## Question

**Kon** asked on 14 Dec 2020

Hi, I have a problem with menu and sub-menu. The problem does not always occur, but quite often. SignalR latency is low (local server). See attachment - after I move the mouse pointer outside the menu area, the items are still expanded. Best regards Konrad

## Answer

**Marin Bratanov** answered on 14 Dec 2020

Hi Konrad, You can Follow the fix for that here: [https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time](https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time) We had made some fixes in this regard that could cater for some signlalr issues but there is work to be done so this item is now open again. Regards, Marin Bratanov

### Response

**Todd** answered on 18 Dec 2020

Same issue. (I posted on the General Discussion thread, too, but wanted to make sure I'm in the loop no matter where updates happen!)

### Response

**Konrad** answered on 07 Jan 2021

OK, thanks, waiting for fix/investigation. The issue in on local server / intranet (the server and network is not under load), so it doesn't seem to be a latency problem, but not sure. Best regards

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hi Konrad, Tools such as VPN or other networking setup (even using wireless connection on a laptop/pc/tablet/phone) can potentially interfere with the latency. You can see this section of the MS article to measure it so we can rule that out: Measure network latency, here's the sample component itself @inject IJSRuntime JS

@if (latency is null )
{
<span>Calculating...</span>
} else {
<span>@(latency.Value.TotalMilliseconds)ms</span>
}

@code { private DateTime startTime; private TimeSpan? latency; protected override async Task OnAfterRenderAsync ( bool firstRender ) { if (firstRender)
{
startTime=DateTime.UtcNow; var _=await JS.InvokeAsync<string>( "toString" );
latency=DateTime.UtcNow - startTime;
StateHasChanged();
}
}
} Regards, Marin Bratanov

### Response

**Konrad** answered on 29 Jan 2021

Hi Marin, is there any chance to move on with the topic in the coming weeks/months? Best regards Konrad

### Response

**Marin Bratanov** answered on 29 Jan 2021

Hello Konrad, This issue is high on our priority list, but there is a major problem with handling it - there is no tooling that can simulate delays and jitter for signalr connections. This makes reproducing this reliably hard, and that, in turn, makes it very hard to know if you actually fixed it. We do intend to work on it, yet I am not in a position to promise time frames at the moment. The best way to know when it gets done is to click the Follow button on its portal page. Regards, Marin Bratanov
