# TelerikLoaderContainer not resolving

## Question

**Chr** asked on 22 Jan 2021

I upgraded to 2.21.0 ... however when trying to add a TelerikLoaderContainer to a page it is not being recognized. Other controls are like TelerikGrid on the same page. Any ideas?

## Answer

**Chris** answered on 22 Jan 2021

I solved this by cleaning my nuget packages as instructed by: [https://docs.microsoft.com/en-us/nuget/consume-packages/managing-the-global-packages-and-cache-folders#clearing-local-folders](https://docs.microsoft.com/en-us/nuget/consume-packages/managing-the-global-packages-and-cache-folders#clearing-local-folders)
