# Grid attached to a report dataset whose column names may change?

## Question

**Dea** asked on 08 Nov 2022

Say I have a report with 13 month column names. Depending on the date range given to report the columns names could be different. How do I build the resulting class to hold the data for the gird in this case? public class MgtRtp2Result { public string? TN { get; set; } public string? BAN { get; set; } public string? Platform { get; set; } [DisplayFormat(DataFormatString="{0:C}")] public decimal Col1Amt { get; set; } [DisplayFormat(DataFormatString="{0:C}")] public decimal Col2Amt { get; set; } } Col1Amt name in the SQL result coming back could be May2022 for first run but Jun2022 for next run. Same thing can happen Col2Amt. Thanks for the help.

### Response

**Deasun** commented on 08 Nov 2022

would it be something like: public class MgtRtp2Result { public string? TN { get; set; } public string? BAN { get; set; } public string? Platform { get; set; } [DisplayFormat(DataFormatString="{0:C}")] public Col1Amt (string Title, decimal ValueAmt ) { get; set; } [DisplayFormat(DataFormatString="{0:C}")] public Col2Amt (string Title, decimal ValueAmt ) { get; set; } } If so hows the grid know which to use for the tile of the column and the value of the cell?

### Response

**Hristian Stefanov** commented on 11 Nov 2022

Hi Deasun, Every property of the model is the " Field " of each column in the Grid. The " Field " parameter accepts values of type string, boolean, DateTime, and number. If the " Title " parameter is not set explicitly, the column will display the " Field " parameter name as its title automatically. I confirm that the " Title " parameter can get changed dynamically. As far as I understand, the idea here is to change the title dynamically based on given decimal numbers in the column. The decimal numbers are coming from a database. Can you please confirm if that is the case? If it's convenient, please provide the other parts of your configuration so I can get a better understanding of the scenario. You can use dummy data just for the purpose of the sample. I look forward to your reply.

## Answer

**Deasun** answered on 13 Jan 2023

I fixed it by: defining the columns in the .razor page; <GridColumn Field="@nameof(MgtServiceTypeRevSummaryNoTaxes.Mnth1Amt)" Title="@Mnth1Amt_Title" /> And in the .CS code I set that Mnth1Amt_Title to what I want the column name to be. In this rpts case I am calculating it from a hidden field with the starting date. example: Mnth1Amt_Title=String.Format("{0:MMM-yyyy}", dtStartDT) + "_Amt"; Mnth2Amt_Title=String.Format("{0:MMM-yyyy}", dtStartDT.AddMonths(-1)) + "_Amt";
