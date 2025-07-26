# TelerikChart in div with class flex-fill not confined to div

## Question

**CJCJ** asked on 11 Nov 2021

I have a div with bootstrap class of d-flex and inside that div I have two additional divs with class of flex-fill. The idea is to have a section on the blazor page I'm developing that contains two TelerikChart objects side by side. My problem is the Charts get generated to be wider then the div. How can I use TelerikChart and contain the chart within the div. <div class="card-body d-flex flex-fill"> <div class="flex-fill" id="Savings"> <TelerikChart> <ChartSeriesItems> <ChartTitle Visible="false"> </ChartTitle> <ChartSeries Type="ChartSeriesType.Pie" Data="@i" Field="@nameof(extras.ISG.Savings)" CategoryField="@nameof(extras.ISG.Part)" ExplodeField="false"> <ChartSeriesTooltip Visible="true" Context="item"> <Template> @((item.DataItem as extras.ISG).Part) <br /> @((item.DataItem as extras.ISG).TotalTransactions) <br /> @((item.DataItem as extras.ISG).Savings) </Template> </ChartSeriesTooltip> <ChartLegend Visible="true" Position="ChartLegendPosition.Bottom"> </ChartLegend> </ChartSeries> </ChartSeriesItems> </TelerikChart> </div> <div class="flex-fill" id="defferedSummary"> <TelerikChart> <ChartSeriesItems> <ChartTitle Visible="false"> </ChartTitle> <ChartSeries Type="ChartSeriesType.Pie" Data="@CdefferedGrouped" Field="@nameof(extras.dGrouped.Earned)" CategoryField="@nameof(extras.dGrouped.Partner)" ExplodeField="false"> <ChartSeriesTooltip Visible="true" Context="item"> <Template> @((item.DataItem as extras.dGrouped).Part) <br /> @((item.DataItem as extras.dGrouped).TotalTransactions) <br /> @((item.DataItem as extras.dGrouped).Earned) <br /> @((item.DataItem as extras.dGrouped).Spent) </Template> </ChartSeriesTooltip> <ChartSeriesLabels Visible="true" Position="ChartSeriesLabelsPosition.Right"> </ChartSeriesLabels> <ChartLegend Visible="true" Position="ChartLegendPosition.Bottom"> </ChartLegend> </ChartSeries> </ChartSeriesItems> </TelerikChart> </div> </div>

### Response

**Marin Bratanov** commented on 11 Nov 2021

Does calling its Resize() method when the containers change size help: [https://docs.telerik.com/blazor-ui/components/chart/overview#chart-size?](https://docs.telerik.com/blazor-ui/components/chart/overview#chart-size?)

### Response

**CJ** commented on 11 Nov 2021

The problem is on load it does not size properly. If you look at the attached image which is a snip of the running site containing the code above with some labels etc removed for confidentiality reasons. The pie chart on the left for some reason expands outside the boundry of it's containing div. When I inspect the code in chrome dev tools the containing div is exactly half the area but the contents of the pie chart expands way past it. The chart on the right appears to stay in its container which adds to my confusion.

### Response

**Marin Bratanov** commented on 15 Nov 2021

Try adding a button to call its .Refresh() method. If that gives it the right size, then it is a timing issue and the chart would likely initialize while the div is having too large a size. If it does not fix the issue, then for some reason the chart would be calculating the size of the element wrongly, or there would be some CSS trickery it does not support. In such a case I suggest opening a ticket with a full project that shows the issue (some dummy data in the chart will suffice) so we can take a look.
