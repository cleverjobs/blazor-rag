# BulitInNumberFormats with three decimal places.

## Question

**Umi** asked on 10 Nov 2022

I need to format one of the columns with three decimal places. In [https://docs.telerik.com/devtools/winforms/api/telerik.documents.spreadsheetstreaming.builtinnumberformats,](https://docs.telerik.com/devtools/winforms/api/telerik.documents.spreadsheetstreaming.builtinnumberformats,) I could not find any option for the above-mentioned purpose. I am formatting a column before the data is exported in grid. Here is a code: I would really appreciate if you could tell me if there is such a BuiltInNumberFormat. If not, is there Telerik class that allows me to do so? I tried incell formatting, but without success.

## Answer

**Umidjon** answered on 10 Nov 2022

Thank you, I resolved it. It seems to be as simple as : args.Columns[1].NumberFormat="0.000";
