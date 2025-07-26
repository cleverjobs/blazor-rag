# TelerikGrid Sortable does not work when the DataSource is ObervableCollection

## Question

**Ale** asked on 21 Feb 2022

Repro Steps: Pick any example, even the default one in the documentation, and make its data type ObervableCollection, and all of a sudden the values of Sortable=@true on the Grid and rows get ignored. This seems to be specific only to ObservableCollection. Even IReadOnlyList supports sorting just fine. There is nothing in the documentation mentioned about why ObservableCollection shouldn't support sorting. If this is by design, please amend the documentation, otherwise please let us know if you're planning to fix it. Thanks.

### Response

**Marin Bratanov** commented on 22 Feb 2022

This REPL seems to sort fine for me, and it is based on this demo with Sortable enabled. If you see an issue with the latest version please modify it and add it to your post so it can be reviewed.
