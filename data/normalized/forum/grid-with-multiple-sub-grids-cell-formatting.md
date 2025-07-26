# Grid with multiple sub grids, cell formatting ?

## Question

**Dea** asked on 16 Oct 2023

I have a main grid that has 4 rows. The top 3 rows have numeric data and formatted as: $0,00.00 etc. The 4th row has percentage data in the cells. should be formatted as 0.00% or just 0.00. Currently the data is showing up as $0.00 I am not sure how one would do that. Any pointers?

## Answer

**Georgi** answered on 19 Oct 2023

Hello, Deasun, It is possible to format the different rows with the Column Template. This way, you can format depending on different conditions like this: <GridColumn Field="Number"> <Template> @{
var item=context as MainModel;
if (item.Id !=4)
{
@(string.Format("{0:C}", item.Number))
}
else
{
@(string.Format("{0:P2}", (item.Number/100)))
}
} </Template> </GridColumn> In this case, all cells in this column will be formatted as currency except the fourth one(id 4), which will be a percentage. Note that the percentage format in .NET has a range of [0%, 100%] for values between [0, 1]. Therefore, the value 1 is 100%, and the value 80 is 8000%. I have prepared a REPL example to show the result. Let me know if additional questions arise. Regards, Georgi Progress Telerik

### Response

**Deasun** commented on 24 Oct 2023

Thanks I will try that out. Just a note! I have tried your repl link in all 3 major browsers, latest versions, and none work. I just get a blank screen in all 3. Link: [https://blazorrepl.telerik.com/wHFavjvF51ZFnRSL54](https://blazorrepl.telerik.com/wHFavjvF51ZFnRSL54) Result { this is chrome }

### Response

**Georgi** commented on 27 Oct 2023

Hi, Daesun, There might have been an error with REPL, as the link you have shared works for me. This can usually be solved by refreshing the page or clearing the browser's cache. In case this doesn't fix it, I sent an attached file with the code snippet that you can copy and paste into the REPL to test.
