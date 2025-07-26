# How to know if a particular item in DataGrid is not being shown due to applied filter? (without implementing OnRead)

## Question

**Ale** asked on 21 Apr 2022

Implementing OnRead is very intrusive and can very easily lead to bugs now or in the future. I have a feature that would operate on all visible rows in the Grid (in all pages, not just the current one), and I need to know if a certain item/row is visible or not. Is this possible, or can it be a future feature? Thanks.

## Answer

**Marin Bratanov** answered on 23 Apr 2022

Hi Alex, This would not be possible as a built-in feature. You will need to use OnRead to get the currently shown data so you can cache it and compare against the full data source. This example can be a basis for you, but you may also need to store a version of the filtered data without paging too, that will also complicate things. The purpose of the OnRead event is exactly to allow you to implement such complex and highly specific business logic. You can also keep using the Telerik DataSource methods (like .ToDataSourceResult()) to fetch the data for the grid and this will get you results identical to the ones the grid gets out-of-the-box (it uses the same code internally). You can even have a copy of the request so you can disable paging and fetch that full filtered data in case you need that. Granted, that is yet another request to the data source, and may have a memory (or general performance) footprint, but there is no way for the grid to know and accommodate such highly specific use cases otherwise. Regards, Marin Bratanov Progress Telerik
