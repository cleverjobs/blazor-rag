# 2.1 upgrade error

## Question

**Ric** asked on 27 Sep 2019

If I upgrade to 2.1 I get the following error when trying to run my project in the latest VS. System.IO.FileNotFoundException: Could not load file or assembly 'Telerik.DataSource, Version=1.2.0.0, Culture=neutral, PublicKeyToken=20b4b0547069c4f8'. The system cannot find the file specified. Downgrading back to 2.0 makes this go away. Maybe I am missing an upgrade step?

## Answer

**Marin Bratanov** answered on 30 Sep 2019

Hi Rick, Generally, a Clean and the Rebuild of the solution should help. If not, try clearing the nuget cache. You can read more about this in the following thread: [https://feedback.telerik.com/blazor/1431387-telerik-datasource-version-1-2-0-0-does-not-load.](https://feedback.telerik.com/blazor/1431387-telerik-datasource-version-1-2-0-0-does-not-load.) Regards, Marin Bratanov

### Response

**Rick** answered on 30 Sep 2019

Clean/rebuild worked, thanks.

### Response

**Marin Bratanov** answered on 30 Sep 2019

Thanks for confirming this, Rick. I marked your post as an answer to the thread for anyone else having a similar problem. Regards, Marin Bratanov
