# Always sorted

## Question

**Rob** asked on 30 Nov 2021

When clicking the header of a sortable column, it toggles between ascending, descending and no sort order. How to make it always have a sort order, i.e. only toggle between ascending and descending?

## Answer

**Hristian Stefanov** answered on 03 Dec 2021

Hi Robert, You can achieve that kind of custom sorting by using the Grid state. Use the OnStateChanged and choose to always have the desired sort descriptor. You will have to cache the old state and compare which column lost their sort state. One thing to mention is - if there is always a sort parameter, the underlying SQL query will become very heavy. Every column will always have an OrderBy statement. That can make performance worse on the backend. I hope this helps. Let me know if you need further information. Regards, Hristian Stefanov
