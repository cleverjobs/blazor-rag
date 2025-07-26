# sing OnStateInit with paged data

## Question

**Pet** asked on 10 Jan 2023

I have a TelerikGrid with OnRead set with code that retrieves Paged data via an API. I store the items + page number + total items etc so that when the user returns they see their previous search. I tried using OnStateInit, but it only lets me set the page number - not the data items or total results.

## Answer

**Dimo** answered on 13 Jan 2023

Hi Peter, The Grid data and total count don't belong to the GridState for 2 reasons: The Grid data is not part of the Grid configuration. It is the result of the Grid configuration ( which includes sorting, filtering, paging, etc. ) The GridState preserves the Grid configuration across user sessions. The Grid data may change between two user sessions. If we are talking about search results here, then this is either filtering or SearchBox search. The built-in way to achieve the desired behavior is to save the FilterDescriptors or SearchFilter from the GridState. You can restore those in OnStateInit. Then, the Grid will request the up-to-date data for these criteria. If you prefer to really cache and show old data, then implement custom logic in OnRead, which will set the old serialized data and count to args.Data and args.Total on initial page load (you will need to detect initial page load with custom logic as well). Regards, Dimo
