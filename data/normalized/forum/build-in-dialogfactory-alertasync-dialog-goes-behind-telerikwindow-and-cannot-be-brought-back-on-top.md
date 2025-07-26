# Build in DialogFactory.AlertAsync dialog goes behind TelerikWindow and cannot be brought back on top

## Question

**ianian** asked on 20 Apr 2022

REPL Built in dialog from DialogFactory.AlertAsync Goes behind TelerikWindow if the window is clicked. Then it cannot be brought back on top or otherwise closed. Shouldn't the built in dialog be modal and forced on top of the TelerikWindow until it is acknowledged? Please, let me know. Thanks.

## Answer

**Dimo** answered on 21 Apr 2022

Hi Ian, The REPL works correctly and we fixed such an issue recently. Can you still reproduce it with the latest version? Regards, Dimo Progress Telerik

### Response

**ian** commented on 21 Apr 2022

Hello. Thanks for your reply. The REPL in the link you provided has the exact same issue that I am talking about. If I have a TelerikWindow which brings up a dialog, then I click on the TelerikWindow while the dialog is displayed, the dialog goes behind the window and I cannot interact with it anymore. Click the open button, click the Open the SECOND window button, and then click back on the original window 'The Title'. Now the Confirm dialog has gone behind it and I cannot interact with it anymore. Does that make sense?

### Response

**Dimo** commented on 21 Apr 2022

I confirm I am not able to reproduce the problem any more in either of the two REPLs (they always use the latest UI for Blazor version). What browser are you using? Can you try in incognito mode and/or clear the browser cache?

### Response

**ian** commented on 21 Apr 2022

Microsoft Edge Version 100.0.1185.44 (Official build) (64-bit) I tried it in a private window and got the same result. We are on version 2.29 here at the moment but I expected the REPL to execute the newest version. Maybe I will try this locally with the latest version and record a video of what I am seeing.

### Response

**Dimo** commented on 21 Apr 2022

Yup, my Edge version is the same. Here is a video. Try the scenario locally. In the meantime, I will check with my colleagues if it's possible for this to be a REPL caching issue.

### Response

**ian** commented on 21 Apr 2022

Thanks for your help so far. The issue I am describing is that after the second window opens correctly and is on top as expected, clicking on the original window will cause it to go behind that window and not be able to come back on top or otherwise be usable from that point onward. I will post a video soon but you should be able to reproduce by clicking on the original window after the second window has opened.

### Response

**Joana** commented on 25 Apr 2022

Hi Ian, Thank you for the additional information. I believe that the issue you are encountering is due to the body/app styling. In the REPL case there is `display: block` style to the app element that causes the issue with the overlay position. We have this logged in our
