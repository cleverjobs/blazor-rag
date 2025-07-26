# Add OnBeforeActiveTabIndexChange

## Question

**Igo** asked on 05 Aug 2024

Hi all, Could you please add the OnBeforeActiveTabIndexChange event and allow to cancel ActiveTabIndexChange in the handler? I saw an example in the doc about how to prevent tab (index) change, but it is not sufficient because of: - event if you won't change the tab index, the active tab is still being destroyed and recreated; - we don't want to keep the tab in memory by using the Persist flag; We need to prevent tab switching by showing the user a confirmation and reacting to the user's choice.

## Answer

**Hristian Stefanov** answered on 07 Aug 2024

Hi Igor, I noticed that you have already submitted a request for this: TabStrip - Add OnBeforeActiveTabIndexChange event. An update on that item is now available at the provided link. Regards, Hristian Stefanov
