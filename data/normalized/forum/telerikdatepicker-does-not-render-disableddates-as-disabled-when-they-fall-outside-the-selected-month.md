# TelerikDatePicker does not render DisabledDates as disabled when they fall outside the selected month

## Question

**Rol** asked on 01 Feb 2022

Calendar days that fall outside the selected month never have the class k-state-disabled, even when those days are part of DisabledDates. That means the user sees a normal (enabled) rendering, the pointer cursor, and can even click on the day, but nothing will happen. It becomes more obvious, and annoying, when I want to color each disabled day red, and/or each allowed day green. I cannot do this because the k-other-month days now cannot be colored red, and will be colored green, or not colored at all.

## Answer

**Svetoslav Dimitrov** answered on 04 Feb 2022

Hello Roland, I would like to provide a quick overview of the scenario that I understood. When you are on the February 2022 month view and you disable the 31 of January 2022, or the 1st - 13th of March 2022 and the respective cells, aforementioned, do not render as disabled (the styles are not rendered). If you go to the March month view (or the view for January) they are rendered as disabled. However, if you try to click on any of the aforementioned cells, they would not be bound to the DatePicker. If this is indeed the case, the behavior you are facing is expected and by design. When we delivered the date picker with the respective views we detached from each other and are not expected to render styles for another view. That being said, I will forward your feedback to our development team and see if there would be possibility to change the current behavior. Regards, Svetoslav Dimitrov

### Response

**Roland** commented on 04 Feb 2022

" the styles are not rendered " and therefore seem to suggest enabled dates, which may not be correct.

### Response

**Hristian Stefanov** commented on 09 Feb 2022

Hi Roland, In the meantime, I'm jumping into the discussion as my colleague Svetoslav is out of the office currently. The reported behavior here seems related to one bug report we have: If the Min parameter excludes a whole month of the current year and you navigate to next year, you cannot navigate back to the current year from the Decade view Please take a look to confirm if it covers the scenario. There is a workaround provided as well.

### Response

**Roland** commented on 09 Feb 2022

That supposed workaround does not work, because the DatePicker does not expose the Calendar's render event

### Response

**Hristian Stefanov** commented on 11 Feb 2022

Hi Roland, You are right in the case here. I'm very sorry for the misleading. The workaround is indeed for the Calendar component only. Still, the fix of this bug will cover the same problem in the DatePicker as well. Please let me know if we can help with anything else.
