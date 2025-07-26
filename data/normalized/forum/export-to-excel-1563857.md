# Export to Excel

## Question

**Pet** asked on 04 May 2022

Hi, I'd like to export data to Excel, but I need to export about 100 000 rows and 20 columns. How can I do this? It's possible it takes several minutes, but with possibility in new thread. Maybe I will also have to set something on IIS for timeout or Oracle DB. Thanks Peter

### Response

**Timothy J** commented on 04 May 2022

If I was faced with this problem, I would export this on the backend and asynchronously provide a link to the file when the file was ready.

### Response

**Marin Bratanov** commented on 07 May 2022

Indeed, that's what I would suggest as well. The last bullet in this section about file generation can give you a couple of ideas and a starting point for an implementation.

### Response

**Deasun** commented on 31 Aug 2023

I do this like so: private List<rtpRptsResults> grdYourGrid { get; set; } bool YourGrid_ExportAllPages { get; set; } public bool YourGrid_CancelExport { get; set; } public List<string> YourGrid_ExportColumns { get; set; }=new List<string>(); async Task YourGridsName_OnBeforeExcelExport(GridBeforeExcelExportEventArgs args) { ldrVisible=true; await Task.Delay(1); if (grdYourGrid.Count> 100000) { Task.Run(()=> doCallRptExportMgr(strWhoIAm)); strAppMsg="Export will be emailed to you when done!"; ldrVisible=false; args.IsCancelled=true; } else { if (YourGrid_ExportColumns.Any()) { args.Columns=args.Columns.Where(col=> YourGrid_ExportColumns.Contains(col.Field)).ToList(); } args.IsCancelled=YourGrid_CancelExport; }; } doCallRptExportMgr Builds your file with headers on server. { in my case a csv } Email user with link to file on server in email. Hope thats enough to pint u in right direction. Works fine for me with 100K+ results.
