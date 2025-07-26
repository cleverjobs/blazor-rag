# DropdownList initial item empty on UI

## Question

**Bai** asked on 11 May 2022

Hello, I seem to be having an issue regarding the Telerik DropdownLists. Any dropdown list that has its values loaded from the database, displays empty, regardless of whether the property bound to the value has anything it or not. It's specially confusing, when the bound property has a correct value, yet it still displays empty. This issue seems to be exclusive to the loaded from database values, as anything locally added, seem to work in the same manner. We are currently using version 2.3.X, but we are unable to update due to styling breaking.

### Response

**Marin Bratanov** commented on 11 May 2022

A couple similar issues have been fixed recently ( here and here ) and I recall another issue about async data loading that was fixed too, so it is likely that an upgrade will solve this.
