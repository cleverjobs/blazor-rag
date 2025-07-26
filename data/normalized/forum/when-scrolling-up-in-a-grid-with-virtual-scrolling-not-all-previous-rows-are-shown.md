# When scrolling up in a Grid with virtual scrolling not all previous rows are shown

## Question

**Lar** asked on 14 Nov 2023

I have implemented virtual scrolling in a grid. Scrolling down goes smoothly. It does not matter if you scroll fast or slowly. And it also shows all rows. When scrolling up slow or click by click using the scrollbar and waiting till the grid is refreshed completely each time. The up scrolling gets disabled before you get to the first record. In this case only the first row is not shown. When scrolling up fast, so not waiting for the grid to refresh each time, the up scrolling gets disabled very quick and you are then not able to view the first records. This can be up to 20 records (of the 34 in my test set) I can see that in this case the GridReadEvent args.Request.Skip is the amount of records not shown (obviously). I logged the calls to the onread method when scrolling fast down and fast up. When scrolling down all requests get through. When scrolling up they don't. It looks like the some onread requests get bounced. Does anyone bumped into this problem before? Or know what I could do wrong?

### Response

**Larissa** commented on 14 Nov 2023

Sorry ignore this question. No bouncing or not getting to the first record when scrolling up. I introduced a bug my selves causing the search query not to be run when skip was 0 ...
