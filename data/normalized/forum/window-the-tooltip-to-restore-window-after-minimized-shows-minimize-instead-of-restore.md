# Window: the tooltip to restore window after minimized shows "Minimize" instead of "Restore"

## Question

**NiV** asked on 20 Aug 2023

If I minimize a TelerikWindow, the tooltip that appears on the "Restore window" button shows "Minimize" instead of (say) "Restore". Please see attached file. Version is 4.4.0. Thank you.

## Answer

**Georgi** answered on 23 Aug 2023

Hi, Fabio, I can confirm this is a defect on our side, and have logged a bug in our feedback portal on your behalf. As a temporary workaround, you can use the StateChanged event and update the Title of the action button when the Window is resized. The StateChanged event fires when the user attempts to minimize, maximize, or restore the Window. I have prepared a REPL example with the suggestion from above applied. Let me know if additional questions arise. Regards, Georgi Progress Telerik
