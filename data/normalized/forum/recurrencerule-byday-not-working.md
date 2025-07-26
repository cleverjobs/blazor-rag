# RecurrenceRule BYDAY not working

## Question

**Hol** asked on 09 Aug 2022

Hello, I have a CalDav-Server as data storage for caldav-clients. One client frontend is the Telerik Scheduler. I have created an event series with end date like this: RecurrenceRule="FREQ=DAILY;UNTIL=2022-08-13T23:59:59" which works fine. But a RecurrenceRule like this: RecurrenceRule="FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR" works on other clients (like Thunderbird), but in the Scheduler it produces the same result like: RecurrenceRule="FREQ=DAILY" Did I something wrong with the rule or is there a problem with the Scheduler?

## Answer

**Nadezhda Tacheva** answered on 12 Aug 2022

Hi Holger, You have not done anything wrong. You have actually hit a bug with the Scheduler. Currently, when the RecurrenceRule uses DAILY frequency, the collection of days that is set through the BYDAY rule is not taken into consideration and thus events are rendered for every day. I opened a bug report on your behalf: RecurrenceRule BYDAY does not work with DAILY frequency I added your vote to increase the popularity as we prioritize the fixes based on the community demand. You are automatically subscribed and will receive email notifications on status updates, so you can easily track the progress of the fix. A possible workaround for the time being is to use "FREQ=WEEKLY" and extend the occurrence to the desired days of the week. For example, targeting the "Morning run" appointment: [https://blazorrepl.telerik.com/cQuiFGOK01nSotIT28.](https://blazorrepl.telerik.com/cQuiFGOK01nSotIT28.) Last but not least, I'd like to thank you for reporting this behavior! As a small token of appreciation, I've rewarded your account with some Telerik points. Regards, Nadezhda Tacheva
