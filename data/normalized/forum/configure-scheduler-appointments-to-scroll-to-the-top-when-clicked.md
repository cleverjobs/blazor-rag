# Configure scheduler appointments to scroll to the top when clicked?

## Question

**Kyl** asked on 06 May 2025

When I click on scheduler appointments where the top isn't visible, the scheduler often (but not always) scrolls up but doesn't scroll up enough to make the top of the appointment visible. I did a video showing what I mean. When you click the bottom part of the longer appointments, the top isn't immediately scrolled to and you have to scroll a little further to make it visible. Is it possible to configure the scheduler (without custom JS) so that the top of the appointment is visible when clicked? I haven't fully figured out what triggers it to scroll up either. The shorter appointments don't scroll at all when clicked, even if they are barely visible. The nearest I can tell, any appointment longer than an hour will scroll when clicked but it will only scroll up enough so that the first hour is still hidden. I do see that if the bottom isn't visible, it will always scroll down enough so that the bottom is in view but I'm not sure why the same doesn't happen for the top.

## Answer

**Nadezhda Tacheva** answered on 08 May 2025

Hi Kyle, Thank you for reaching out! The scrolling behavior is actually not correct - the page should not scroll when the user clicks on an appointment. After some testing on my end, it appears this behavior occurs only in the Material and Bootstrap themes. I logged a bug report on your behalf and added your vote there: [Material and Bootrstrap Themes] Clicking on a not fully visible appointment scrolls the page. As a creator, you are automatically subscribed to get status updates. Last but not least, I rewarded your account with some Telerik points as a small gesture of appreciation for your report. Regards, Nadezhda Tacheva Progress Telerik
