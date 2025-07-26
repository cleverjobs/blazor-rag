# Grid selection performance

## Question

**Nic** asked on 06 Jan 2020

Hi Marin and happy new year! I don't know if you can advise, but we've noticed that when selecting multiple rows of the grid (not using the checkbox), the selection seems to be noticeably slow. There seems to be quite a delay when clicking one or more rows (using shift in the latter case) and the highlight colour changing to show the selection. Our grid is quite complex as we use RowTemplate and a manual datasource, but I notice that there is a similar albeit less pronounced delay in your demo. Any idea what might be causing this? Kind Regards, Nick. <TelerikGrid Data=@Items TItem="Item" Sortable="true" Height="100%" Pageable=true OnRead="@ReadItems" PageSize=50 TotalCount=@Total class="viewgrid" SelectionMode=Telerik.Blazor.GridSelectionMode.Multiple @bind-SelectedItems="@SelectedItems"> <RowTemplate Context="item"> @foreach (var viewColumn in ViewDefinition.Columns) { <ViewGridColumn ViewColumn="@viewColumn" Item="@item" OnDoubleClick="@RowClicked" /> } </RowTemplate> <GridColumns> @foreach (var viewColumn in ViewDefinition.Columns) { <GridColumn Title="@viewColumn.Label" Field="@viewColumn.FieldName" Width="@(viewColumn.Width + " px")"></GridColumn> } </GridColumns> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 06 Jan 2020

Happy New Year, Nick, We have had a couple of reports about selection being a bit slow and we have it on our radar to investigate it (even though I can't commit to a timeframe right now). I suspect that the issue is mainly that the rows re-render when selection happens so they get the appropriate class, and the more content there is in a row, the slower the re-rendering. Hopefully, there will be something we can do about this, but it looks like a tough one at the moment. What we've also seen is that WASM projects are considerably slower in general, and this issue is more pronounced there. Considering that, and that WASM is still in preview, you may consider using a server-side type of project for the time being. Regards, Marin Bratanov

### Response

**Nick** answered on 07 Jan 2020

Thank Marin, it's not the end of the world and I totally appreciate it may be a Blazor thing, I just wanted to mention it as it makes our application feel a bit "sticky"! :)

### Response

**Marin Bratanov** answered on 07 Jan 2020

Hi Nick, At this point, the WASM flavor is considerably slower than the server-side flavor. We're really seeing the difference in a new sample PWA application we're working on right now - things that we're used to being instantaneous in a server project now take>1 second. The grid selection is one of them. Regards, Marin Bratanov

### Response

**Nick** answered on 23 Jan 2020

Hi Marin, I've been doing some testing around this. I created a sample program which has 300 rows of data in a grid. The data is generated, and some of it is quite long. As well as using the Telerik Grid I also wrote a quick component which just draws and HTML table and handles the single line selection in a similar way to the Telerik grid, by setting a background colour on all of the td elements in the selected row. My aim was to try and figure out if the problem is with the Blazor rendering being slow whor whether it is elsewhere. In my test app - which I can supply. Just selecting a single row in the Telerik grid is taking 9 seconds. As you will appreciate this just isn't usable. The time taken seems related to the number of rows in the grid which was what made me wonder whether it was the rendering. However my simple HTML table which also has to remove the background colour from any already selected row and add it to the selected one it is relatively fast, roughly 300-500ms. I appreciate that the grid control is much more complicated and is doing things with javascript and selected items etc. but I can't really use it in the state it is in, so unless we can get a speed up I will have to replace it. I've attached some performance tracing from Firefox. Let me know if you want the test application. Kind Regards, Nick.

### Response

**Nick** answered on 23 Jan 2020

P.S I forgot to say that in the main application I'm writing, where I do paging, I've noticed similar problems going to another page. The time taken is very similar.

### Response

**Marin Bratanov** answered on 24 Jan 2020

Hello Nick, We'd welcome a sample, please open a ticket and send it, and I will add it in the issue for investigating the selection performance. At this stage, it seems like the renders of the rows take time inside the framework, and each row has to be re-rendered in order for its class to change, which is likely what causes the slowdown - in the grid there is a lot more going on in a row than there is in a simple table so that we can allow all the other features it has. This is also likely what causes the onclick handler to appear it is taking time - the handler fires, we wait for the rendering to happen, and all that time counts towards the handler time. In fact, it is possible that exactly that native logic is causing the performance issue and we may have to move towards toggling the selection class with JS only. Of course, this is subject to detailed investigation and I may be completely wrong. Regards, Marin Bratanov

### Response

**Nick** answered on 24 Jan 2020

Thanks Marin! I've raised a ticket here with the project attached: [https://feedback.telerik.com/blazor/1450716-grid-selection-and-paging-slow](https://feedback.telerik.com/blazor/1450716-grid-selection-and-paging-slow) I think what the test project proves is that in a simple scenario it isn't a problem with blazor re-rendering the grid to change the background colour of one row. If the whole grid is being re-rendered or something then it must be related to the way Telerik Grid works. As you say the Telerik grid is obviously way more complicated and probably has to do extra work because of the way it is implemented, and of course Blazor is new and quite complex. I hope there is a resolution because we won't be able to use the grid if not! I would have to test a different grid or just write my own component for our needs - which will be a lot dumber :) Thanks again, Nick.

### Response

**Marin Bratanov** answered on 24 Jan 2020

Thank you for the sample, Nick, I will show it to the dev team. We will work on this, so for anyone else stumbling on this thread - click the Follow button on page Nick linked to get status notifications. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 31 Mar 2020

To post an update to this as this thread is rather popular - we have made significant improvements in the grid performance (not just in the selection) in our newer releases (mostly in 2.8.0 from the end of February), and it will work much faster than before. It is important to note that the WASM flavor of Blazor is still slower than the server-side Blazor approach, and that's something Microsoft need to address. We have shared with them our findings on where bottlenecks come up, and hopefully they will be able to improve things for everyone. As a general rule - the standard performance optimization tips apply - using reasonable page sizes for the grid being the topmost suggestion (say, 10, 20 or 30 is usually about as much as a screen can fit anyway, so there is no point in rendering 200 rows all the time). If your users don't want paging, you can use row virtualization. Then, the fewer columns you have, the fewer DOM elements there will be and the faster the app will be. In many cases a lot of the columns can be moved to a Details view/window/pane in the page so they are only shown when needed per item, as they are rarely used. The next thing is complex templates - the more complex a template is, the more work the framework does when rendering it, and repeating that for many rows can also slow things down. Regards, Marin Bratanov

### Response

**SBSDEV** answered on 28 Jan 2021

I'd like to post on this and let you know this issue is pretty bad. If there is a more recent issue or post I am happy to discuss further there. If you enable Debug logging on a Server-side project, you get massive SignalR and Blazor traffic on every click on the grid - it is re-rendering every single row on every single click (and re-render is a full dispose/re-create of each row which are themselves components, ouch) We are using the grid virtualization so it is at least limiting to what is visible, but wow. Is there a technical reason why this is happening? Can ShouldRender be used in a more targeted way?

### Response

**Marin Bratanov** answered on 28 Jan 2021

Hi, This is how it is supposed to work - to have native components means they go to the framework to render things, and that comes up as signalr traffic for a server-side blazor app. There is no unnecessary re-rendering, however, I am attaching here a short video that shows how only the attributes that changed re-render - you can see how the things that change highlight for a bit in the browser and that's only the class of the entire row, and the checked attribute of the checkbox. The cell contents and the adjacent rows do not get changes. The diff on the backend will run on the entire grid, of course, because that's the component raising the EventCallback, and this is how the framework operates in this regard. So the extent of changes that go to the UI will depend on any other changes that the application logic may have (e.g., checks inside templates whether the current item is selected might cause more changes in the DOM, depending on the application logic). We already use ShouldRender to optimize the rendering as much as possible - tightening it further will mean the grid will barely re-render, and that will start causing appearance and functionality issues. We do monitor this and take it into account when implementing features. Regards, Marin Bratanov

### Response

**SBSDEV** answered on 29 Jan 2021

Hi Marin, First of all, thank you for the reply and for the video. Overall the -performance- on the actual client (when running Blazor server) is good and the virtualization works very well. Performance, however, on WebAssembly is not good. I guess my main question is related to the number of object allocations due to ALL gridrow components being destroyed and re-rendered by the framework on every change in row selection. Even though the diff sent to the client may be very small, there is just this enormous amount of churn even when a single row is selected. In our case, we have grids with row templates using a static renderfragment to minimize component churn - otherwise there would be a double penalty (one for the internal gridrow and one for our component within the row template). Imagine a virtualized grid showing 30 rows and the user is just holding down the Down key to scroll down the list. In that case the object allocation churn is very high even though the diffs may be small. I imagine that puts a lot of pressure on the GC which I wonder is part of the reason the WebAssembly side is so much slower (that and other factors we already know about that are out of your control). This churn also puts a lot of server GC pressure if we're running hundreds of clients, for instance. So I'm curious if there is a way to avoid those allocations for those gridrows that haven't changed and to just skip re-rendering those gridrow components? Also not sure if the internal gridrow needs to be a component or if you can accomplish that by renderfragments which at least would reduce the allocation pressure. Just a brainstorm. Merely ideas and you guys will figure out the implementation side, but just raising the concern since that's a ton of GC allocations just for simple navigation of the grid. Thanks

### Response

**Marin Bratanov** answered on 29 Jan 2021

Hi, The WebAssembly performance does still have catching up to do, and there are three big rocks in that regard that the framework has to solve: moving from interpreted code to native web assembly code (that is something the build of the app must do) allowing multithreading on the wasm side (right now it runs on the single UI thread of the browser, like JS does) ahead-of-time compilation (also closely related to interpreted vs native mode) Once the framework does that, our components will get those benefits immediately because they are native blazor components and not wrappers over js widgets. For the time being, performance in webaseembly needs special care, and perhaps this section of our docs can help you with some ideas: [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#slow-performance.](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#slow-performance.) As for our grid - we use @key to tie rows to models, and we have things as optimized as is possible. There need to be some components in the grid and its rows that will allow all the rich functionality you see, in a maintainable manner. Thus, the diff the framework does is as optimized as possible - it must be allowed to run for each new row because we can't know what data is in it when scrolling happens. Re-rendering the grid during an EventCallback is also inevitable if you want the grid to actually react. Regards, Marin Bratanov

### Response

**SBSDEV** answered on 29 Jan 2021

Thanks Marin. Regarding WASM, I'm aware of those limitations and know that is out of your control - AOT will be beautiful! Regarding the grid, here is a simpler scenario boiled down: - Grid contains 30 rows - No scrolling happens - User clicks row 1 - User clicks row 2 - User clicks row 3 That generates 90 new gridrow component allocations - with each click, it destroys 30 gridrows and re-renders 30 new gridrows. I would expect there to be no allocations and 3 separate small diffs to the client. Maybe you are forced to re-render because you cannot determine whether our logic would make it safe to skip rendering. In that case it would be *great* to specify in a callback or something like a "ShouldRenderRow(rowKey)" which I can override and then I can say "nope - nothing has changed, retain this row!" In the case above, I would return false to you. If I did have logic that might change another row based on selection or de-selection, then I would just return true. The default method would just return true so business as usual. This would work well in a virtualized mode too since it may just be keeping an existing component but just moving it into a different place. Just trying to avoid unnecessary GC :)

### Response

**Marin Bratanov** answered on 01 Feb 2021

Hello, We have already done a lot of work on optimizing things. For example, navigating the focused cell with the keyboard only re-renders the two cells, not all elements. The situation with the rows is different, however - selection can change all rows and toggle their selection, and the grid can't know that, and so can clicks - that's why all rows need to re-render. With virtualization every time a new page of data is fetched that a brand new data set, even if just one row was scrolled down, so all rows need to update. On the GC and allocation - in our tests that is by far not the most significant issue in Blazor WASM, the overall number of components, DOM elements, and parameters is more important. It is also important to note that when the Blazor app is a WebAssembly app, the server does not do any of the diffing and allocation - it all happens only within the client's browser, so that does not put strain on your server. Thus, more allocs can seem like a bigger issue than they are. Regards, Marin Bratanov

### Response

**SBSDEV** answered on 06 Feb 2021

Marin, here's a small portion of the debug log after clicking on 1 row. I still think additional optimizations would be possible, especially if I can explicitly return back to you on a per-row basis whether or not any data has changed and you can then leave that row alone. Also, there are elements like GroupCellSpacers that might be able to be RenderFragments instead. With the amount of churn that happens and the large number of components, all the optimizations add up.

### Response

**Marin Bratanov** answered on 08 Feb 2021

Thank you for reaching out. There is a delicate balance between having a plethora of features and also managing performance, and it is inevitable the one will always require a small sacrifice from the other. Usually to have some rich functionality you have to sacrifice application size and a little bit of performance. This is also the case here, with the grid having hundreds of features (I'd go as far as to say that I consider it fully featured for the majority of use cases, just 2 years after the first line of code). What I can assure you is that we are constantly keeping an eye on performance, including features enabled by the MS team, that enable us to improve it where we previously were unable to. Regards, Marin Bratanov

### Response

**Stefano** answered on 12 May 2022

Hello, 15 months later I have met the same problem. I'm sorry. I already lamented the slowness of your treeview component and now I meet a worst problem with your datagrid. A grid, paginated, 20 rows per page, with many columns hidden and 30 visible, with expando objects as data source. In debug mode, with developer tools open, when I click on a row I have to wait 5 seconds and over 1600 log lines to see the row selected, with the grid, obviously, remaining unresponsive for all this time. Why the "on mouse over" row higlighting is istantaneous and the selection requires the full rendering of the entire grid? I think I cannot explain my state in a better way than saying that I feel bad. What are going to say my customers? I don't know what to think about it. If it is not possible to do better because of the current state of Blazor (which I think will not change in the next future), than Blazor is broken. If is not possible because of the declarative UI pattern, than it is broken. Otherwise, it's your component to be broken. I think it is a combination of this things. Please, give me some hope, because right now I'm thinking that I have to throw away everything and start from scratch with another technology.

### Response

**Dimo** commented on 17 May 2022

@Stefano - I agree that 5 seconds for item selection is a lot. However, here is a Grid test page with 10,000 items, 30 visible columns and 30 non-visible columns. The performance looks OK to me for such amount of data. A delay may occur if the Grid is using column templates with nested components or lots of HTML inside. In this case, consider virtual columns. If the problem appears to be different and points to the Grid, please prepare an isolated runnable test page for us to check. I recommend sending it in a separate private ticket, as this forum thread is relevant to a very old version, which didn't have the optimizations it has now. We also have some performance optimization tips, which you may have already seen, but I am mentioning that just in case.

### Response

**Hao** answered on 24 Oct 2022

Hi, Please summary how is it going with this bad performance on WASM. So code is simple with 5000 rows but it is too slow when I click "Select ALL" somehow. is it related? How can I select my all products? <TelerikGrid Data="ViewModel.Products" TItem="Item" FilterMode="@GridFilterMode.FilterMenu" Height="750px" RowHeight="50" ScrollMode="GridScrollMode.Virtual" EnableLoaderContainer="true" Sortable="true" Reorderable="true" SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedProducts"> <GridColumns> <GridCheckboxColumn SelectAll=true Width="50px" SelectAllMode="GridSelectAllMode.All"></GridCheckboxColumn> </GridColumns> </TelerikGrid>

### Response

**Dimo** commented on 25 Oct 2022

@Hao - you are right, the select-all performance is not good in WebAssembly. I have logged a public item for research on your behalf. In the meantime, you can use a HeaderTemplate for the CheckBoxColumn for better performance.

### Response

**Hao** commented on 25 Oct 2022

Thank Dima so much. Yeah. I will go with header template. Regards,
