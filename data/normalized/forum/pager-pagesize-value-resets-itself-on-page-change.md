# Pager PageSize value resets itself on page change

## Question

**Ken** asked on 21 Jun 2022

Trying to wire up a pager for a grid. If I set the pagesize options as 5, 10, and 20 with 100 records available and choose a pagesize of 20, I get 5 available pages. If I choose page 4, the pagesize resets to 5 and I get 20 pages. How can I keep the pagesize of 20 when changing pages?

## Answer

**Kenn.** answered on 23 Jun 2022

So as it turns out not only is there a PageChanged event, but also a PageSizeChanged event. In that event, the backer field containing the pagesize value can be updated, allowing it to be sent with further page changed events.
