# How to implement a blocking div for longer running method?

## Question

**Bit** asked on 14 Oct 2019

There are various "blocking ui" solutions and examples on the inter-web that allow you to block part or all of the UI while some longer-than-normal process takes place. Eg. a user clicks a button that has to load and process some data. One example done with Angular is this [https://embed.plnkr.co/plunk/bNfRvD](https://embed.plnkr.co/plunk/bNfRvD) How can we implement something similar with Blazor AND not resort to javascript interop?

## Answer

**Marin Bratanov** answered on 14 Oct 2019

Hello, The following features request offers a workaround for the time being: [https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly.](https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly.) I have added your vote and you may want to Follow the item as well. Regards, Marin Bratanov

### Response

**BitShift** answered on 14 Oct 2019

Here is maybe another option? [https://github.com/BlazorExtensions/SignalR](https://github.com/BlazorExtensions/SignalR)

### Response

**Marin Bratanov** answered on 14 Oct 2019

Hi, Could you elaborate a little on this link? From what I gather, it is a wrapper for easier configuration of SignalR hubs and not a loading sign for long-running operations that plugs into the Blazor rendering. Am I missing something? Regards, Marin Bratanov

### Response

**BitShift** answered on 14 Oct 2019

No, you are correct. However, I shared the link to the Extensions after seeing this thread [https://www.telerik.com/forums/build-app-with-mvc-core-signalr-vs-blazor-signalr](https://www.telerik.com/forums/build-app-with-mvc-core-signalr-vs-blazor-signalr) Here is an example I found using this extension [https://dotnetthoughts.net/building-blazor-apps-with-signalr/](https://dotnetthoughts.net/building-blazor-apps-with-signalr/) However, maybe a simpler approach might be something like this: [https://blog.jonblankenship.com/2018/10/19/adding-a-loading-spinner-to-a-button-with-blazor/](https://blog.jonblankenship.com/2018/10/19/adding-a-loading-spinner-to-a-button-with-blazor/) After all, the original intent was to block the user from the entire UI (while showing a spinner) while the long process completed. While the use of SignalR in the above cases offers up some interesting scenarios, for what Im trying to do, I think simply showing/hiding a div overlay would suffice. Most of these solutions utilize setting the z-order of the element and/or setting opacity etc. Just something to keep the users from clicking on anything until the process is "done".

### Response

**BitShift** answered on 14 Oct 2019

So the use of SignalR could very likely enable a "progress" indicator to be built, as well as more complex client-server interactions, or so it would seem?

### Response

**Marin Bratanov** answered on 14 Oct 2019

Indeed, a <div> with a sufficiently high z-index is usually the thing that gets rendered. This is why I suggested the TelerikWindow approach from the public page, as it is easier to show from C#: showing and size. <TelerikButton OnClick="@DoLongWork">Do long work</TelerikButton>

<TelerikWindow @bind-Visible="@LoadingSignVisible" Modal="true">
<WindowTitle>
<strong>Please Wait</strong>
</WindowTitle>
<WindowContent>
@*Add animated gif and styling to taste*@Please wait...we are processing your request.
</WindowContent>
</TelerikWindow>

@code { bool LoadingSignVisible { get; set; } //this method must be async so the UI can be updated while waiting for the remote service async Task DoLongWork ( ) {
LoadingSignVisible=true; await Task.Delay( 3000 ); //simulate long running operation LoadingSignVisible=false;
}
} Regards, Marin Bratanov
