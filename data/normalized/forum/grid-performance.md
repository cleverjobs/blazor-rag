# Grid Performance

## Question

**Jam** asked on 21 Oct 2021

We are looking to implement the grid to replace agGrid in a situation where the users are accustomed to some patterns. We are using server-side Blazor and have reports that may have 60k rows. Our preference is not to use paging, and since we have grouping, it seems that virtual scrolling is not an option. Right now we struggle to load as many as 10k rows, even without grouping. I get an error: WebSocket closed with error 1006. We are not doing any updates in the grid, so it would seem that if we could turn off anything to make it read only (we do filter and sort it, but don't update any cells) then that might lighten the load. Any ideas about grid or column attributes we could set? Or any other ideas?

## Answer

**Marin Bratanov** answered on 23 Oct 2021

Hi James, The original issue (web socked closed) is likely due to the sheer size of data that needs to go through the SignalR connection - our Blazor grid is a truly native Blazor component and so it goes through the framework rendering, it is not a JS component. Thus, the Blazor grid is subject to the rules and limitations of the Blazor framework - of which the most relevant here is that too large DOM operations don't work too well and you need to optimize that (e.g., with paging or virtualization). You can read some more ideas on optimizing Blazor components performance here, and if grouping is vital, the options you have are either paging, or loading groups on demand. Regards, Marin Bratanov Progress Telerik
