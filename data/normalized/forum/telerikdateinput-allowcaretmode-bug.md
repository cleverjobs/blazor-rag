# TelerikDateInput AllowCaretMode Bug

## Question

**Ind** asked on 31 Aug 2023

Cannot type in date into TelerikDateInput if AllowCaretMode is true and the DateInput focus is in the whole input, how to reproduce: move focus to DateInput from previous input ( whole dateInput is in focus) Type in 01 into the DateInput, the caret will move to end, but no value filled. This is the REPL page: [https://blazorrepl.telerik.com/GnYsHlcv54uXw7hd34](https://blazorrepl.telerik.com/GnYsHlcv54uXw7hd34) this is the form and how to reproduce:

## Answer

**Svetoslav Dimitrov** answered on 05 Sep 2023

Hello Indra, Thank you for the detailed explanation and runnable REPL snippet. This is indeed a valid bug report. As a small token of our appreciation, I have awarded your account with Telerik Points. Here is the Bug Report I have logged on your behalf: When the whole DatePicker receives focus, and the AllowCaretMode parameter is set to true, you cannot input a value. I have added your Vote for it and you are automatically subscribed to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Indra** commented on 07 Sep 2023

Another issue for DateInput Blazor Server version go to the demo page [https://demos.telerik.com/blazor-ui/dateinput/overview](https://demos.telerik.com/blazor-ui/dateinput/overview) focus on the DateInput, press CTRL A to focus on Whole input. try input 01 01 2001, it wont fill the input. This is not happening in the REPL provided for the demo (Web Assembly version).

### Response

**Indra** commented on 08 Sep 2023

yes so the bug happens for DatePicker Blazor Server version too (default setting without AllowCaretMode ). Not happening in the Web Assembly version (the corresponding REPL page of Telerik Demo page) In the demo page, select all DatePicker (CTRL + A) so the whole DatePicker is in focus. Then try type in 01 01 2001 This is sample output: [https://demos.telerik.com/blazor-ui/datepicker/overview](https://demos.telerik.com/blazor-ui/datepicker/overview) This is the REPL page for that demo page (Web Assembly version) [https://blazorrepl.telerik.com/QxEMGMFR22V3lOy053](https://blazorrepl.telerik.com/QxEMGMFR22V3lOy053)

### Response

**Svetoslav Dimitrov** commented on 12 Sep 2023

Hello Indra, I did some testing and I would like to share my findings and confirm if you experience the same behavior. On my side, the issue that you have reported to us is only happening if I type on the fast side, so quickly type 01, slash or tab 01, slash or tab, and 2001. This happens because the demos are hosted as a server-side application and the physical distance between the user and server causes latency issues. Latency in server-side projects is documented by Microsoft in their hosting models article. Here is also a YouTube video where Steve Sanderson, the creator of Blazor goes into some details on latency. If you try and run the same code on a local server-side Blazor application you should not see the issue. So why does it work in REPL? WebAssembly is the client-side hosting model for Blazor and everything happens on your local device. So there is no latency. I hope this clarifies the situation you are facing. Let me know your thoughts on this.

### Response

**Indra** commented on 12 Sep 2023

Hi Svetoslav, The original issue cannot insert date properly with AllowCaretMode enabled happens in both local and deployed machine (our application is blazor server). But after deploying with AllowCaretMode removed, it still happened in deployed machine, not in local, so I tried to reproduce with your REPL demo(Web Assembly) and the main demo page (Blazor Server). Yes my guess is it is latency issue same like [https://www.telerik.com/forums/menu-problems.](https://www.telerik.com/forums/menu-problems.) I tried with normal pace of DOB input, even slow, try it with your demo page 01011982 without tab or slash. Even without the whole input selected. You cannot input 01011982 ( even without the whole input selected this time ). So it is broken. Changing architecture to Web Assembly is not my decision and it is too late at this stage. If it is the problem with blazor server latency, I believe Telerik can use the same approach used to fix this [https://www.telerik.com/forums/menu-problems](https://www.telerik.com/forums/menu-problems) Thanks

### Response

**Svetoslav Dimitrov** commented on 15 Sep 2023

Hello, Indra and everyone who might find this forum, We have logged another bug report regarding the issues with the latency. Here is a link to the public feedback item - [Blazor Server] When having higher latency, the value of the date inputs is incorrect
