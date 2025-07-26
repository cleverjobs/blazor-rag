# Telerik Grid OnRead Event endless loading

## Question

**KatKat** asked on 12 May 2023

I have a grid that loads big data. We used to use the ObservableCollection but opted to use the OnRead for better performance (loading takes time when using ObservableData). We have EventAggregators and PropertyChanged events running async OnInitialised().. Does this affect the OnRead event? We manually track the Add, Edit/Update, Delete and Duplicate actions on the grid. So upon running our blazor app, the grid won't load the data on the grid and has the loading animation on endless loop. (Tried waiting for it to load for about 2 hours). Also tried debugging line per line from which I saw that upon executing the OnRead, the args,Data and args,Total were popullated properly.

### Response

**Kat** commented on 04 Jul 2024

args.Data=result.Data It returns data but still keeps loading

### Response

**Rob** commented on 03 Jul 2025

I'm having this exact same problem. Were you able to find a solution? I see no one from Telerik support responded to your question. :(

### Response

**Hristian Stefanov** commented on 08 Jul 2025

Hello, A similar scenario with an endless loader is covered in the following forum post: [https://www.telerik.com/forums/set-selected-grid-row-item-after-a-filter-event-is-triggered?](https://www.telerik.com/forums/set-selected-grid-row-item-after-a-filter-event-is-triggered?) Best, Hris
