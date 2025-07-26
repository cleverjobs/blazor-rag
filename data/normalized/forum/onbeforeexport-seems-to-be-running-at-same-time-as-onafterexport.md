# OnBeforeExport seems to be running at same time as OnAfterExport

## Question

**Dea** asked on 28 Jan 2025

I have a grid with an Excel export. It can take some time so I want to show a Notification at the start and end of the process using OnBeforeExport and OnAfterExport. However both Notifications show at the same time. I have reproduced the issue, attached. Despite the 5 second delay being in OnAfterExport, neither Notification shows until after the delay and the Excel download. Any ideas? Relevant part of code:

### Response

**Nadezhda Tacheva** commented on 31 Jan 2025

Hi Dean, The behavior is most likely a matter of timing and configuration. The OnBeforeExport and OnAfterExport do not fire simultaneously but there is a very short time frame between them. In the general case, the export happens pretty quickly. So, even if you manage to show different notifications when the export starts and when it ends, chances are these notifications will flash really quickly which may not be the best user experience. Can you please share more details on the scenario and why you need to show notifications when the export starts? Is it because you want to notify the user that there is an ongoing process, so they do not start any other action? If yes, would this approach be suitable for you - show a loader upon export start? To be honest, I find this option a safer one as it blocks the Grid and thus guarantees the user won't perform any other action while the Grid is being exported. Take your time to consider my suggestion and let me know your thoughts.

### Response

**Dean** commented on 03 Feb 2025

Thanks for your reply, although it's left me a little confused. I haven't suggested that OnBeforeExport and OnAfterExport run simultaneously, but I am questioning whether OnBeforeExport runs before the actual export of the spreadsheet, as it's name suggests? My example appears to prove it does not? It suggests to me that the sequence is: The Excel spreadsheet is exported OnBeforeExport runs OnAfterExport runs I don't see how any other explanation is possible from the example I supplied. My use case is simply that as my export takes some time (10 seconds or more), I want the user to know that it is happening, as there is no visual clue that anything is happening and they may think they missed the button or something like that. I am not concerned with them interacting with the grid or anything else whilst they wait, I just want to reassure them their spreadsheet is on the way.

### Response

**Dean** commented on 05 Feb 2025

Apologies, the title of the issue does suggest I think they are running simultaneously, I could have picked a better title. The issue is that OnBeforeExport doesn't seem to be running before the export but after.

### Response

**Nadezhda Tacheva** commented on 06 Feb 2025

Hi Dean, Thank you for the clarification! By design, the OnBeforeExport event fires right after the user clicks the ExcelExport button and before the export process starts. I checked the behavior with the source code and I don't see issues with the flow. I also checked the app you provided again and I do think the behavior is related to the configuration and more specifically the Thread.Sleep(5000) added in the OnExcelAfterExport. I updated the solution adding an await Task.Delay(5000) to simulate an ongoing task that will actually delay the export process. The notifications now appear properly at the start and the end of the export process. You can find the updated app attached.
