# Display the number of records matching the current filter

## Question

**Sco** asked on 22 Sep 2023

I have a Blazor Server app using TelerikGrid. The grid has lots of columns and I have FilterMode set to FilterRow and the default filtering works great. However, since the grid is also set to ScrollMode Virtual, there is no immediate indication of how well the filter is defined. To fix this I want to display the number of records that are actually "filtered in" in comparison to the total number of records possible so that the user can tell if they've (for example) selected nearly all the records. I've looked everywhere and I cannot find a way to ask the grid how many records are currently filtered in. It seems like I could take the FilterDescriptors, convert them to SQL for a where clause, and run the query every time they change the filter, but that seems like such a waste to essentially run the filter twice every time it reloads. Even though my dataset is currently small enough that I cache the whole thing on the server, I'm still doing twice the work to get to a number the grid must know. Here is a snippet from my Razor file: @code { private int _filteredCount=0; // How to set this? }
<TelerikGrid Data="@_applications" Pageable="false" Sortable="true" Resizable="true" FilterMode="@GridFilterMode.FilterRow" Width="100%" ScrollMode="@GridScrollMode.Virtual" OnStateInit="(GridStateEventArgs<ApplicationListDTO> args)=> StateInitHandler(args)" OnStateChanged="(GridStateEventArgs<ApplicationListDTO> args)=> StateChangedHandler(args)" Height="540px" RowHeight="60">
<GridColumns>
Column definitions left out for brevity
</GridColumns> </TelerikGrid>
<div class="applicationCount">@(_applications.Count()) applications found, @_filteredCount listed</div> Suggestions?
