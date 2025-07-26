# RowNumber in ExpandoObject Dynamic Grid

## Question

**Moh** asked on 14 Jan 2025

Hello I need RowNumber in <GridColumns> in Dynamic Grid which is set with ExpandoObject. Please help. Thank you

## Answer

**Dimo** answered on 16 Jan 2025

Hi Mohamad Javad, Here is a KB article that shows one way to implement row numbers as part of the Grid model. It doesn't use ExpandoObject, but the idea is the same. Regards, Dimo Progress Telerik

### Response

**Johan** commented on 27 May 2025

Doesn't work with virtual tables! Amazing that the grid doesn't support something as simple as row numbers. And adding a field or property to the items in the list doesn't work, because that gets messed up as soon as you sort a column. That field becomes an "index" field instead of a row number.

### Response

**Johan** answered on 27 May 2025

The suggested solution is for non-virtual tables only. Amazing that the grid doesn't support something as simple as row numbers. And adding a field or property to the items in the list doesn't work, because that gets messed up as soon as you sort a column. That field becomes an "index" field instead of a row number.

### Response

**Nadezhda Tacheva** commented on 30 May 2025

Hi Johan, At this stage, it is not clear to me what is the exact problem that you are facing with virtual tables. Regardless of the type of data that you have on your data source, you can still reshape it before passing it to the Grid to use a model with an added field for the row numbers. As for the sorting, I tested the example here and I confirm the row numbers remain static - they do not change upon sorting the other columns which is the expected behavior. If you need further assistance with setting up the row numbers, please share an isolated runnable sample demonstrating your current configuration and the exact problem you are hitting.
