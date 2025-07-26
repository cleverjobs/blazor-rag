# Blazor Server RadGrid: huge websocket data volume issue

## Question

**Mic** asked on 26 Aug 2021

Hello, First of all, please note i am doing tests with a Trial version of Telerik (2.25.0). I plan to buy licence in a few days but i need to be sure Telerik is appropriated for my project. I have an issue with websocket data volume on RadGrid. Here is what i've done: - I have create an empty Blazor Server project (.Net 5 dotnet framework) - I have create an Entity with 2 properties: Id (Int32) and Name (String, 10 chars max) - I have create a database with about 500 records of the previous Entity. - I have put a RadGrid component with pagination (10 items per page). This Grid is displaying the 500 records. I have checked something on Entity Framework and SQL Server: RadGrid sends a new SQL request on each page change and only fetchs 10 items on each page. - Telerik paging is very slow for me (my customers will run my application with a very poor connexion) - I have sniffed packets on network and i have seen a very huge amount of data in websocket traffic when i click on another Radgrid page on my browser: 377ko per page (for only 10 items of { Int32, String[10] } !). Here is what i've done: I have cleared my sniffer. Then i have changed page one time in my browser and i have stopped sniffer. Everything was done on a virtual machine. There were no other traffic (Internet or local) In wireshark, i see a huge amount of data on the websocket stream. Here is a very short extract: !.......!.......!.......!...............................!.......!.......!.......!.......!.......!.......!.......!.......!.......!.......!.......!...............................!.......!.......!...... !......!!......"!......#!......$!......%!......&!......'!......(!..............................)!......*!......+!......,!......-!.......!....../!......0!......1!......2!......3!......4!..............................5!......6!......7!......8!......9!......:!......;!......<!......=!......>!......?!......@!..............................A!......B!......C!......D!......E!......F!......G!......H!......I!......J!......K!......L!..............................M!......N!......O!......P!......Q!......R!......S!......T!......U!......V!......W!......X!..............................Y!......Z!......[!......\!......]!......^!......_!......`!......a!......b!......c!......d!..............................e!......f!......g!......h!......i!......j!......k!......l!......m!......n!......o!......p!..............................q!......r!......s!......t!......u!......v!......w!......x!......y!......z!...... And on the bottom of the stream, i can see the datas displayed on my grid: ...

HelloWorld.gridcell.1.0. .1.false.256.gridcell.1.1. .2.false

... This grid datas are packed and they are not heavy (about 2kbytes). But what are the 375k previous bytes ? Is there a way to avoid them ? Please not i am running this project in a Developpment environnement. Do you think the 375kbytes datas can be debug informations and if so, how can i remove them ? I can't run in Production mode, maybe due to trial version but i need to know before buying licence why websocket data is so heavy. Thanks a lot.

## Answer

**Marin Bratanov** answered on 28 Aug 2021

Hi Mickael, To begin with the issue that I see as crucial for this: my customers will run my application with a very poor connexion This means that using the server-side Blazor model is unlikely to work out for this app very well in the first place. It requires a very good (stable and low-latency) connection between all clients and the server. For it packet loss and latency are extremely detrimental, and poor connections are better suited to the WebAssembly model where the initial load is a tad heavier, but then requests are made over HTTP(S) for data only, and not for rendering. Thus, I strongly suggest you consider a PoC with that model for such a user base. Nevertheless, 370kb of traffic for a page change is not expected. A lot of packets are, and there should be at least one that is a bit larger (that contains the rendering batch for the DOM operation of the framework), but the rest should be tiny ones - several bytes. I am attaching here a short video that demonstrates this. This traffic can grow as the page grows, though, there are many rules that define what re-renders, and there may be adjacent components that also render, depending on how the app is designed and operates, and that can also increase the size of the traffic. Thus, there is probably something else going on in that test (e.g., for some reason the frames on the network have too much overhead, or the app behavior causes more re-rendering than expected). This should not be caused by the trial version though, the only time it can cause more traffic is when it randomly adds the trial message, but that would be random rather than on every request. Regards, Marin Bratanov

### Response

**Mickael** commented on 28 Aug 2021

Thanks a lot for your answer. I understand for the server-side Blazor model. When i say my customers will have a poor Internet connexion i mean i have to optimize my webapp for all my customers and some of them will have a poor internet connexion. I can't accept 370kbytes of volume each time they change page. I have made a mistake in my initial post. The problem comes when i put 250 items per page. I have made other tests: I have inspected websocket messages and i tried to locate grid datas when i change page. There is something strange: When i configure 10 items per pages I got a "JS.RenderBatch" message of 16.7kbytes. I can see my grid datas in hex viewer: My Grid data is stored between 0x035e and 0x03ab. (Like in your video, an address represents a 16 bytes block). Last address line of message is: 0x418 So I have a 13.8kbytes "header" (0x035e * 16 /1000), then 1.2kb for my grid datas (0x03ab - 0x035e) * 16/1000 and a "footer" of 1.7kbytes (0x0418-0x03ab) * 16 / 1000 When i put 250 items per pages (same project, same datas, i just changed PageSize property): I got a "JS.RenderBatch" message of 385kb: My Grid data is stored between 0x5296 and 0x58f8. Message ends at 0x5da3. So: I have a 338kbytes header (0x5296 * 16 /1000), then 26kbytes of grid data ((0x58f8-0x5296) * 16 /1000) and a 19kbytes footer (0x5da3 - 0x58f8) * 16 /1000 Conclusion: I understand grid datas is heavier in second cases because i have 250 rows instead of 10 (26kb instead of 1.2kb). But i do not understand why "message header" grows from 13.8kb to 338kb. What contains this header exactly ? Is there a simple way to decode this binary messages ? It looks like msgpack but i did not managed to decode them in order to understand what they contain. Is there a way for me to optimize your grid ? I would like to only download data each time a user change page. Thanks

### Response

**Marin Bratanov** commented on 28 Aug 2021

The blunt answer is "I don't know", Mickael. These messages are entirely generated and controlled by the framework. We use absolutely standard Blazor rendering methods (things like foreach loops, conditional markup, etc.) and so we let the framework do the rendering - this is how a native Blazor component should work. My gut tells me that the framework adds metadata in the header of the signalr message - things like which DOM elements to modify, maybe when, maybe some event sequence or health checks (like checksums or even some logic). This is one of the reasons why the fewer markup you have to render at one time - the better. The way to optimize this is to optimize the grid rendering - basically, to reduce the batches of content that needs to be updated - the fewer DOM elements, the better Blazor works. Ways to do that are: reducing the page size if users prefer to scroll rather than page, use Virtual Scrolling: [https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling](https://docs.telerik.com/blazor-ui/components/grid/virtual-scrolling) if you have many columns, enable Column Virtualization (with paging or virtual scrolling): [https://docs.telerik.com/blazor-ui/components/grid/columns/virtual](https://docs.telerik.com/blazor-ui/components/grid/columns/virtual) reduce the markup you render in things like cell templates (for example, consider showing additional content in tooltips or a dedicated details window ) You can find some more general tips in the following documentation section: [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#slow-performance](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#slow-performance)

### Response

**Mickael** commented on 28 Aug 2021

Thanks for your answer. Are you sure this messages are not generated by RadGrid source code ? Do you know a way to decode this messages ? What happens when i change page in RadGrid source code ? Do you send only data ? Or do you also send formatting parameters or stuff like that ? Thanks

### Response

**Marin Bratanov** commented on 28 Aug 2021

I am absolutely sure, Mickael. We do not do our own rendering, we let the framework do that, because we make truly native components. When you change the page there are changes standard to blazor rendering in our code - e.g., a collection changes over which a foreach loop is made to render rows. Tracking the DOM elements and updating them in the browser is something the framework does, not we. I suppose that reading the framework source code may provide some insights, but I have not tried to delve into that, nor have I tried to disassemble what they contain.

### Response

**Mickael** commented on 28 Aug 2021

Thanks. There is no way to compress messages ?

### Response

**Marin Bratanov** commented on 28 Aug 2021

I am not aware of one. If it exists, it should be in the hub options builder (AddHubOptions() of AddServerSideBlazor()) but I think that the default is the most efficient that's available in SignalR (websockets with content as compressed as the framework can easily read on the client). I don't think that it can be affected by the dynamic compression module of IIS either - it should go to the asp.net core pipeline directly, not to the IIS handlers. Even if that were possible, I am not sure it would not break the framework.

### Response

**Mickael** commented on 28 Aug 2021

I am trying to put a hook or a middleware on signalr circuit in order to see human readable format for every send message on websocket. But it is not easy. If someone read this message and have an idea: Please let me know; Thanks

### Response

**Mickael** commented on 28 Aug 2021

One more thing: I am working in Developpement Environment. (I can't switch to Production env because i am working with Trial version of Telerik). Do you think this big headers can be debug informations ? Are they present in production env ? Thanks

### Response

**Marin Bratanov** commented on 28 Aug 2021

The difference between the trial and dev versions of our tools are: You are not allowed to use a trial version in production legally. The trial version will randomly render trial messages on the components. Otherwise the functionality and builds are the same, they are both built in Release mode. To the best of my knowledge, the signalr traffic contains only events and dom updates, it should not contain debug info, bug you can easily verify that by switching your app to release mode and inspecting the traffic again.

### Response

**Mickael** commented on 29 Aug 2021

I have changed Properties/launchSettings.json: "environmentVariables": {
"ASPNETCORE_ENVIRONMENT": "Production"
} And i get this error at runtime: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor.getLocationHost' ('TelerikBlazor' was undefined). I was thinking Telerik is not allowed in Production env. Do you have an idea about this error ? Everything works fine in Development env Thanks

### Response

**Marin Bratanov** commented on 29 Aug 2021

Try the steps here, it is likely cache: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors)

### Response

**Mickael** commented on 30 Aug 2021

Can you confirm me TelerikGrid's internals works with Blazor Virtualize component: [https://docs.microsoft.com/en-us/aspnet/core/blazor/components/virtualization?view=aspnetcore-5.0.](https://docs.microsoft.com/en-us/aspnet/core/blazor/components/virtualization?view=aspnetcore-5.0.) Thanks

### Response

**Marin Bratanov** commented on 30 Aug 2021

The Telerik Grid does not use the Virtualize component that comes with the framework and there is no logical place to use it in the context of a grid. Perhaps somewhere in a template if you wish to show a ton of extra data, but I'd say that such a scenario is better suited as some form of detail template or detail tooltip or detail dialog rather than a nested virtualized list. Moreover, our grid works in .NET Core 3.1 where the Virtualize component is not available. In fact, to some extent our virtualization implementation was the inspiration for this component.
