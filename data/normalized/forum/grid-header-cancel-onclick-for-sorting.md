# Grid Header cancel OnClick for sorting

## Question

**Pin** asked on 11 Jun 2022

Hi If I have a column header ina grid which is sortable, and in the header template I place a button, then clicking said button will perform whatever the button's onclick is as well as changing the sort of the column. I don't see a way to mark the click as handled, prevent it bubbling up and being handled a second time by the grid header. Is there a way to achieve this currently?

## Answer

**Hristian Stefanov** answered on 15 Jun 2022

Hi Matthew, I confirm there is an easy way to achieve the desired result. You can wrap the button in another element that stops the propagation of the said event. Here is an example prepared for you in this REPL link to show the two behaviors and the difference. Regards, Hristian Stefanov

### Response

**Pingu** commented on 18 Jun 2022

Just what I needed, thanks. :)
