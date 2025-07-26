# Window Stacking Modal Problem

## Question

**Ger** asked on 06 May 2019

Dear Telerik; The Window-Component is really awesome. I have a small issue opening a new Window from within a opened Window. Both Windows are marked as Modal . The second Window displays on top of the first Window, which is perfect, but is not modal. I still can changes Controls in the first Window. Is it possible to correct this ? Regards, Gert

## Answer

**Marin Bratanov** answered on 06 May 2019

Hello Gert, Usually, only one modal dialog is used. This is an accessibility guideline - or, at least, this is how I interpret the fact that all documents I've seen describe only one modal dialog and never mention anything about the desired behavior when a second one opens. So, I'd suggest making the first dialog non-modal, which will denote that action in the second is mandatory. I have also logged an enhancement idea on your behalf about this, you can track it (and leave any other suggestions you may have) in the following page: [https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.](https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.) Regards, Marin Bratanov
