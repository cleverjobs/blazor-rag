# StockChartCategoryAxis

## Question

**HYO** asked on 13 Dec 2021

Hello, I apologize for my poor English. I'm trying to develop the stock chart. The categories of all stock charts in the demo are date format, but what I want is int format. I'd like to make the weekly count a chart. Therefore, my category data is a number from 1 to 53. The current page is as follow. Data represented as 09:00:00.fff is actually a number between 1 and 53. Also, I would like to express the valueaxis expressed in {$0.0} as an integer. How can I use the int type in category data?

### Response

**Nadezhda Tacheva** commented on 15 Dec 2021

Hi Hyokyeong, Generally speaking, the Stock Chart serves to visualize the deviation of a financial unit over a period of time and it is designed to work with data types to allow the user select specific time frame. That said, I will additionally discuss your use case with our development team and get back to you with more details. Thank you for your patience in the meantime!

## Answer

**Nadezhda Tacheva** answered on 17 Dec 2021

Hi Hyokyeong, Thank you for your patience once again! We were able to discuss the case with our development team and while the Stock Chart is designed to work with DateTime types, we do consider having control over the Stock Chart Navigator Labels a valid scenario that will allow one to render the desired content/format there. That said, I opened the following feature request in our public
