# spreadsheet component download tool exports xlsx.zip

## Question

**JKa** asked on 27 Apr 2025

The xlsx.zip contains some strange files, but why is there no normal .xlsx file.. In the past it did produce a normal .xlsx file in the download tool of the spreasheet. Is there a setting/option for this?

### Response

**JKattestaart** commented on 27 Apr 2025

Setting thefilename in the OnDownLoad Event solves the issue. I guess there's no default file anymore

## Answer

**Anislav** answered on 27 Apr 2025

I tested the spreadsheet component, and for me it works as expected — it produces a normal.xlsx file. In short, an XLSX file is actually a zipped archive containing a set of XML files. If you're seeing it as an archive, it may indicate that you don't have a program like Microsoft Excel, LibreOffice Calc, or Numbers (on macOS) installed to open it properly. If that's not the case, could you please extract a sample from your code that reproduces the issue and share it via [https://blazorrepl.telerik.com/?](https://blazorrepl.telerik.com/?) Regards, Anislav Atanasov
