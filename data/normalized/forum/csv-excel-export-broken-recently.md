# CSV/Excel export broken recently?

## Question

**Pin** asked on 06 Jun 2022

Hi, Have been focusing on some backend stuff and missed a couple released of Telerik Blazor. Have gone through docs for the missed releases but can't see anything to assist me - After updating to latest, it seems to have broken my ability to export properly. I am using OnRead and returning the data via the args myself from the database. When I export a CSV or Excel file for a grid which has data in it, I get the headers for each column but I get no data. Another method I am using elsewhere, though I haven't taken much time to look at it just yet, is using GridRef.Data, where GridRef is an @ref to my Grid, and this also appears to be broken and not be getting any data, yet the grid is showing data clearly in it returned via the OnRead. Is there something I need to have changed with one of the recent updates?

### Response

**Dimo** commented on 08 Jun 2022

@Pingu - we are not aware of anything broken recently. It's unclear what version you have used so far and what is the implementation, so please review these articles. All of them are either new or recently updated - Breaking changes in version 3.0.0 - the most important change is related to OnRead. Common Data Binding documentation - that's a new and structured overview of our data binding mechanism. It contains the changes related to version 3.0 CSV export documentation - recently updated Excel export documentation - recently updated Grid export events - recently updated Grid Excel export demo Grid CSV export demo

### Response

**Pingu** commented on 09 Jun 2022

Hey. Sorry I should have mentioned - I was upgrading from 3.0.0 to latest. Had already transformed my OnReads to meat the new OnRead stuff in the top link listed. I recently managed to figure out one half of the issue. I use Dapper and so I can't use the ToDataSourceResult() (or at least this gives me no benefit, because it will first return the entire table from the database), so I have a pretty custom thing. Anyway, they custom thing I have builds a SQL query based on the args, but it wasn't handling being asked for a page size of 0 correctly, so when page size was 0 it was returning 0 results - The query I was building was asking for row numbers between a start and finish I calculated using pagesize, but with pagesize set to 0, finish would be 1 less than start, and so no results returned. I've fixed this now. What I still have an issue with, is accessing GridRef.Data. This is always null now, even though my Grid has content in it. I could solve this by storing the results of the last OnRead request in a variable within the component and using that rather than GridRef.Data, but was wondering why GridRef.Data was null now?

### Response

**Dimo** commented on 09 Jun 2022

GridRef.Data is null, because the Data parameter is no longer used (and should not be used) when there is an OnRead handler. Storing the current data in a helper variable in OnRead is a valid approach, if you need this.
