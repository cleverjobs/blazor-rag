# DataGrid OnRead does not work - Loading indicator stays busy

## Question

**Ger** asked on 04 Jul 2023

Hello everybody, I am facing an issue with the DataGrid. Using Rebind on the Grid it calls the OnRead Method I supplied and inside I get async Data (awaited) set args.Data and args.Total (paged) and the initial call works, showing 3 rows. With the next call (filtered) I can see only 1 row getting retured which is what I want, but the grid still shows all 3 and a loading indicator which never goes away. No Exceptions, the code runs through inside my ReadItems method. No idea what is wrong here: <TelerikGrid @ref="@vm.GridRef" TItem="ListenElementReltestsElternViewModel" OnRead="@vm.ReadItems">... public async Task ReadItems ( GridReadEventArgs args ) {
args.Data=await GetData(currentFilter, CurrentFilterAusdruck);
args.Total=3; // correct for the testcase }

## Answer

**Yanislav** answered on 07 Jul 2023

Hello Gerrit, In general, if the GetData method returns a DataSourceResult.Data object, the Grid should be working correctly. However, in order for me to provide more accurate assistance, I kindly request that you share further details about the GetData method and its functionality. Based on your mention of a loading indicator being displayed, it seems that the issue might be related to the data loading process. Could you please provide more information about how the Grid data is received? Specifically, I would like to know if the Grid data is sourced from a remote data provider. If that's the case, I suggest checking the network tab of the browser's developer tools for any network errors. Please conduct the necessary checks on your end and inform me of your findings. If further assistance is required, could you please attempt to provide an example where the problem can be reproduced? This will allow me to investigate the issue more effectively and explore potential solutions. Regards, Yanislav
