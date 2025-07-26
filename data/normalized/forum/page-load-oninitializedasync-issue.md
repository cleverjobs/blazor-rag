# Page Load OnInitializedAsync Issue

## Question

**Ric** asked on 13 Sep 2019

I think this is a blazor issue maybe, not Telerik. Has anyone had an issue with OnInitializedAsync firing twice? My event fires, loads the data in my grid, then fires again and reloads grid. preview9-19423-09

## Answer

**Rick** answered on 13 Sep 2019

Looks like I found it. If anyone else has the issue, the setting in the hosts file, @(await Html.RenderComponentAsync<App>(RenderMode.ServerPrerendered)) is what causes it. Change it to @(await Html.RenderComponentAsync<App>(RenderMode.Server))

### Response

**Marin Bratanov** answered on 16 Sep 2019

Hello Rick, I have marked your post as an answer to the question, because that is, indeed, the source of this behavior. Prerendering fires the component lifecycle once on the initial request, and then again after the signalR connection is established. According to MSDN ( link on prerendering and reconnection ), this may not always happen, but it depends on the availability of the same circuit on the server, and I don't think there is a way for you to guarantee that. Here's the relevant extract: The client reconnects to the server with the same state that was used to prerender the app. If the app's state is still in memory, the component state isn't rerendered after the SignalR connection is established. Depending on what you need to happen, you may also find useful the OnAfterRender event as it does not fire during pre-rendering, or the ShouldRender overrides ( link ), or the IsConnected flag in the component context (available near the end of the article linked above). Regards, Marin Bratanov
