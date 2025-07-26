# general blazor/telerik ?

## Question

**Dea** asked on 17 Nov 2022

I have a SP I call that takes 1 or 2 minutes to run. I am running into the error: system threading taskcanceledexception a task was canceled atm the SP takes 1:08 to run. At 35 seconds, using filters to get less data back, it runs fine! We have many reports that take a bit to run. How to I get this task thing to stop killing my app.

### Response

**Timothy J** commented on 17 Nov 2022

The task is cancelled from where? The browser?

### Response

**Deasun** commented on 17 Nov 2022

Browser. It says something has happened, reload. Doing the Inspection thing I see a System.Threading.Tasks.TaskCanceledException as the first error. Appears to be timing out somewhere. I know the data from the SQL server is back from stepping thru the code.

### Response

**Timothy J** commented on 17 Nov 2022

I would check the timeout on the httpclient, the browser, etc. Have you verified using Fiddler?

### Response

**Deasun** commented on 17 Nov 2022

It appears I was calling the routine incorrectly! What I had: await getData_ProdResultRtp3(strWhoIAm); What now seems to work: await Task.Run(()=> DoLongSyncOperation()); Not sure what the difference is between those two? I assume, I know! :(, the 2nd one force it to wait till that routine is done?

### Response

**Deasun** commented on 17 Nov 2022

sorry: await Task.Run(()=> getData_ProdResultRtp3(strWhoIAm)); for the 2nd cmd.

## Answer

**Deasun** answered on 13 Jan 2023

This fixed it: await Task.Run(()=> getData_ProdResultRtp3(strWhoIAm));
