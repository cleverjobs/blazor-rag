# "Select All" breaks Column Virtualization

## Question

**Ray** asked on 14 Jan 2025

Hi, in a Blazor Grid with Column Virtualization and multiple ow selection enabled, when I use the "Select all" option the column virtualization doesn't load any further values on scrolling. I took an example from the Telerik docs and added a checkbox column: [https://blazorrepl.telerik.com/QzOPbePP34Fw94E733](https://blazorrepl.telerik.com/QzOPbePP34Fw94E733) Is there any solution for this? Best regards, Rayko

## Answer

**Tsvetomir** answered on 16 Jan 2025

Hello Rayko, Thank you for the provided REPL example. I tested it on my end, and it appears to work as expected. After selecting all rows, the values load correctly upon scrolling. I have attached a screen recording of the result. With that in mind, I recommend sharing more detailed steps on how to reproduce the described behavior. This will help me to observe it on my side and troubleshoot further. I look forward to your reply. Regards, Tsvetomir Progress Telerik

### Response

**Rayko** commented on 17 Jan 2025

Hi Tsvetomir, Did you scroll horizontally and did you use the "Select all" checkbox? I found out that the issue occurs once the checkbox is used, for checking all AND even for unchecking all. Normal behavior: With "Select all" checked: Best regards, Rayko

### Response

**Tsvetomir** commented on 17 Jan 2025

Hi Rayko, I can confirm that, I've tried to reproduce the described behavior by selecting all rows through the "Select All" checkbox and scrolling horizontally. In my first reply, it looks like the screen recording didn't attach successfully. I'm attaching it now. I apologize for that. As you can see, the data is loaded successfully with a small delay, which is expected for the Column Virtualization feature. Refer to the Virtualized Columns Notes section in our documentation for more information about the specific if this feature. Regards, Tsvetomir

### Response

**Rayko** commented on 17 Jan 2025

Hi Tsvetomir, I think I found a difference... if the (Windows) display scale is set to 100% the issue occurs, with any other setting it works normally. Best regards, Rayko

### Response

**Tsvetomir** commented on 21 Jan 2025

Hi Rayko, I've managed to reproduce the described behavior only on a IOS device. Is that your case, are you using an IOS device? Regards, Tsvetomir

### Response

**Rayko** commented on 21 Jan 2025

Hi Tsvetomir, I use Chrome on a Win10 machine. A colleague uses different browsers on his Win11 machine. We both were able to reproduce the issue. For me it seems to be related to the screen scale. Best regards, Rayko

### Response

**Tsvetomir** commented on 21 Jan 2025

Hi Rayko, I've tested the provided REPL example in Chrome with latest version on a Windows11 machine. My screen scale is 100%. Can you share what Chrome version do you use? If it not the latest, you can try upgrading the browser version to latest. Regards, Tsvetomir

### Response

**Rayko** commented on 21 Jan 2025

Hi Tsvetomir, It's: Version 132.0.6834.84 (Offizieller Build) (64-Bit)

### Response

**Tsvetomir** commented on 24 Jan 2025

Hi Rayko, Thank you for the provided information once again. It seems that you are using the latest browser version. In term of screen scale, as a mentioned, my screen scale is 100% and still can't reproduce the behavior. This leads me think that has no relation with it, and probably have something in common with the screen resolution. As a next step could you provide following information: What Product version do you use? What type of the hosting model do you use, WASM or Server? Have you tried to test the behavior on different type of browser? What screen resolution do you use? Have you tried to zoom in/out the browser? Additionally, If possible, provide a detailed list of steps to reproduce the issue and a sample project. This will allow me to see the behavior on my side and troubleshoot further. I look forward to your reply. Regard, Tsvetomir

### Response

**Rayko** commented on 24 Jan 2025

Hi Tsvetomir, several colleagues have same issue. Different machines, Win 10 and 11, Chrome, Firefox and Edge. Screen resolution is 1920x1080. Furthermore I testet it with 1600x900. The scale is the only factor which makes it reproducable. Regarding your points: Product version: latest --> it's the Repl linked above Hosting model: I guess it's Server --> it's the Repl linked above Tried on different browsers: Yes Screen resolution: native 1920x1080 (also tested on 1600x900) Brower zoom: Hey... here we have a difference... with zoom>100% it works, everything less the columns are not loaded Steps to reproduce: - Just load the sample above - Click the Select all check box - Scroll vertical Best regards, Rayko

### Response

**Tsvetomir** commented on 29 Jan 2025

Hello Rayko, Thank you for the provided information. After further observation of the behavior, I successfully reproduced it by zooming out my browser to 80%. I can confirm that the behavior is a bug in the Grid component. With that bein said, I have created a public item on your behalf to address this: Selecting all rows and zooming out my browser to 80% or less, breaks the column virtualization. You are automatically subscribed as a creator, which means you will receive email notifications regarding the status updates of this item. Also, as a token of appreciation, I have credited your account with Telerik points for reporting this bug first. Thank you for bringing that to our attention. Please excuse us for any trouble caused. Regard, Tsvetomir

### Response

**Rayko** commented on 29 Jan 2025

Hi Tsvetomir, glad to read that. And thank you for creating the item! Best regards, Rayko
