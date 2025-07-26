# NoDataTemplate shows for TelerikChart when there's data

## Question

**Kyl** asked on 17 Dec 2024

I'm working from this demo to use NoDataTemplate with a TelerikChart. The demo works for me in the link but locally, the NoDataTemplate is always visible regardless of whether there's data in the chart. I copied the files from that demo to a test project and still can't get the NoDataTemplate to disappear. I have the test project here and the chart is in the Test.razor page.

### Response

**Hristian Stefanov** commented on 18 Dec 2024

Hi Kyle, I’ve copied and tested the Test.razor page in a local project, and the NoDataTemplate appears to show and hide correctly depending on whether there is data. Testing in this REPL link seems to work as well. If the example works as expected in the REPL, it suggests that the issue is related to your project’s specific configuration. As a next step, I recommend starting an investigation by gradually removing parts of your project to pinpoint the source of the issue. Begin with features like authentication, and ensure that our JavaScript file is correctly linked and loaded. Please keep me updated on your progress—I’m ready to help. Kind Regards, Hristian

### Response

**Kyle** commented on 18 Dec 2024

Hi Hristian, I kind of assumed it was an issue with my project configuration because I've seen it working in the REPL link I posted in my original post. Are you able to send a working project with the test page included so I can narrow it down? Or point me to a place where I can download a working project that uses NoDataTemplate? -- Kyle

### Response

**Kyle** commented on 18 Dec 2024

Hristian, I may have discovered the issue. I downloaded this sample app and injected my component into it and it worked. But when I downgraded the nuget from 7.1.0 to 6.2.0, I was able to duplicate the error. So it seems like version 6.2.0 doesn't play well with the NoDataTemplate. Thanks for looking into this. I should be good to go now. -- Kyle

### Response

**Kyle** commented on 18 Dec 2024

...and if I had read the opening paragraph on the documentation instead of skimming over it, I would have saved all of us a whole bunch of time.

### Response

**Hristian Stefanov** commented on 18 Dec 2024

Hi Kyle, Thank you for keeping me updated on the situation and sharing that the version was the key here. I'm glad to hear that the matter is resolved now. Kind Regards, Hristian
