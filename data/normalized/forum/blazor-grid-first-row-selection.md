# Blazor Grid: first row selection

## Question

**Dea** asked on 27 Nov 2023

How to set in code the first row of the grid selected? grdRptCallDetails_SelectedItems=RptResults[0].ToList(); Wont work. So How do I set that to the first row in the grid?

### Response

**Deasun** commented on 27 Nov 2023

ok, just incase anyone else needs this: lgRecID=gdCallDetails[0].RecordNbr; grdRptCallDetails_SelectedItems=gdCallDetails.Where(item=> item.RecordNbr==lgRecID).ToList(); Only issue with this is you have to have a unique ID value in that RecordNbr field. for each row.
