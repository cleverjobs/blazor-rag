# Javascript error with scheduler in a dialog

## Question

**Kyl** asked on 07 Mar 2025

I'm getting a JavaScript error when I open a TelerikDialog that has a TelerikScheduler in it. The error is: telerik-blazor.js:1 Uncaught TypeError: Cannot read properties of undefined (reading 'filter') at m.handleOverflowingItems (telerik-blazor.js:1:2451674) at e.ResizeService.onResize [as resizeCallback] (telerik-blazor.js:1:2446927) at ResizeObserver.onResize (telerik-blazor.js:1:2228100) at telerik-blazor.js:1:2239508 I have a reproduction here, specifically in this page. The error appears when you click the button and the dialog opens. If I remove the Scheduler, the error goes away. The configuration for the Scheduler was taken from the overview page. This is happening with Telerik Blazor 8.0. I checked with version 6.2 and it didn't show an error in that case.

### Response

**Anislav** commented on 08 Mar 2025

I copied the code from this GitHub repository: [https://github.com/kbaley/TelerikBlazor/blob/dialog-scheduler/TelerikBlazor/TelerikBlazor.Client/Pages/GridDialogScheduler.razor.](https://github.com/kbaley/TelerikBlazor/blob/dialog-scheduler/TelerikBlazor/TelerikBlazor.Client/Pages/GridDialogScheduler.razor.) I then tested it in this Blazor REPL: [https://blazorrepl.telerik.com/mTaduibK14u6y4Ya01](https://blazorrepl.telerik.com/mTaduibK14u6y4Ya01) and I did not see any errors in the console. By default, the Telerik REPL uses Telerik UI for Blazor version 8.0.0, which matches the version used in your project. This suggests that the issue might be related to how the project is set up or how components are arranged within the layout. Since setting up and debugging your specific project would take additional time, I recommend creating a minimal reproducible example, such as a REPL, where the issue occurs. That would help identify the root cause more efficiently. Regards, Anislav Atanasov

## Answer

**Dimo** answered on 10 Mar 2025

Hi Kyle, I was only able to reproduce the error if I first ran the app from the wrong repo branch and then checked out to the correct branch. This implies the problem is related to cache. The same conclusion can be made from the fact that the same Scheduler example works in any other app. Please delete all bin and obj folders in the app and the error should disappear. Regards, Dimo

### Response

**Kyle** commented on 10 Mar 2025

I saw the same behavior with the different branches in my sample as well. Running it clean from the "problem" branch doesn't give an error but I still get one in my main app after clearing bin and obj for both the server and client projects. Note that it's not quite the same as the Scheduler sample on the Telerik site. It works fine for me as well when I embed a Scheduler on a regular page. I only see the error when I open a dialog that has a scheduler in it. It happens even when I copy and paste the working component from my sample. I've traced it to the component not being initialized with an overflowMode in telerik-blazor.js but I'm pretty sure it's a Blazor thing. In any case, I have a working sample locally and a failing one so I'll continue stripping down my main app until I narrow it down. Thank you for putting me on the right track.
